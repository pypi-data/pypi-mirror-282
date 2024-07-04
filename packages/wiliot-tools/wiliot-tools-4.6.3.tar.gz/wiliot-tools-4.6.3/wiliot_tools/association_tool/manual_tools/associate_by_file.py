#  """
#    Copyright (c) 2016- 2023, Wiliot Ltd. All rights reserved.
#
#    Redistribution and use of the Software in source and binary forms, with or without modification,
#     are permitted provided that the following conditions are met:
#
#       1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#       2. Redistributions in binary form, except as used in conjunction with
#       Wiliot's Pixel in a product or a Software update for such product, must reproduce
#       the above copyright notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the distribution.
#
#       3. Neither the name nor logo of Wiliot, nor the names of the Software's contributors,
#       may be used to endorse or promote products or services derived from this Software,
#       without specific prior written permission.
#
#       4. This Software, with or without modification, must only be used in conjunction
#       with Wiliot's Pixel or with Wiliot's cloud service.
#
#       5. If any Software is provided in binary form under this license, you must not
#       do any of the following:
#       (a) modify, adapt, translate, or create a derivative work of the Software; or
#       (b) reverse engineer, decompile, disassemble, decrypt, or otherwise attempt to
#       discover the source code or non-literal aspects (such as the underlying structure,
#       sequence, organization, ideas, or algorithms) of the Software.
#
#       6. If you create a derivative work and/or improvement of any Software, you hereby
#       irrevocably grant each of Wiliot and its corporate affiliates a worldwide, non-exclusive,
#       royalty-free, fully paid-up, perpetual, irrevocable, assignable, sublicensable
#       right and license to reproduce, use, make, have made, import, distribute, sell,
#       offer for sale, create derivative works of, modify, translate, publicly perform
#       and display, and otherwise commercially exploit such derivative works and improvements
#       (as applicable) in conjunction with Wiliot's products and services.
#
#       7. You represent and warrant that you are not a resident of (and will not use the
#       Software in) a country that the U.S. government has embargoed for use of the Software,
#       nor are you named on the U.S. Treasury Department’s list of Specially Designated
#       Nationals or any other applicable trade sanctioning regulations of any jurisdiction.
#       You must not transfer, export, re-export, import, re-import or divert the Software
#       in violation of any export or re-export control laws and regulations (such as the
#       United States' ITAR, EAR, and OFAC regulations), as well as any applicable import
#       and use restrictions, all as then in effect
#
#     THIS SOFTWARE IS PROVIDED BY WILIOT "AS IS" AND "AS AVAILABLE", AND ANY EXPRESS
#     OR IMPLIED WARRANTIES OR CONDITIONS, INCLUDING, BUT NOT LIMITED TO, ANY IMPLIED
#     WARRANTIES OR CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, NONINFRINGEMENT,
#     QUIET POSSESSION, FITNESS FOR A PARTICULAR PURPOSE, AND TITLE, ARE DISCLAIMED.
#     IN NO EVENT SHALL WILIOT, ANY OF ITS CORPORATE AFFILIATES OR LICENSORS, AND/OR
#     ANY CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
#     OR CONSEQUENTIAL DAMAGES, FOR THE COST OF PROCURING SUBSTITUTE GOODS OR SERVICES,
#     FOR ANY LOSS OF USE OR DATA OR BUSINESS INTERRUPTION, AND/OR FOR ANY ECONOMIC LOSS
#     (SUCH AS LOST PROFITS, REVENUE, ANTICIPATED SAVINGS). THE FOREGOING SHALL APPLY:
#     (A) HOWEVER CAUSED AND REGARDLESS OF THE THEORY OR BASIS LIABILITY, WHETHER IN
#     CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE);
#     (B) EVEN IF ANYONE IS ADVISED OF THE POSSIBILITY OF ANY DAMAGES, LOSSES, OR COSTS; AND
#     (C) EVEN IF ANY REMEDY FAILS OF ITS ESSENTIAL PURPOSE.
#  """

import pandas as pd

from wiliot_api import PlatformClient, TagRole
from wiliot_core import set_logger, check_user_config_is_ok

CATEGORY_ID = 'Default'


class AssociateFile(object):
    def __init__(self, config):
        _, self.logger = set_logger(app_name='AssociateFile')
        self.config = config
        try:
            _, api_key, _ = check_user_config_is_ok(env=config['env'],
                                                    owner_id=config['owner_id'],
                                                    client_type=config['client_type'])
            if config['is_gcp'].lower() == 'yes':
                self.client = PlatformClient(api_key=api_key, owner_id=config['owner_id'],
                                             env=config['env'], logger_=self.logger.name,
                                             cloud='GCP', region='us-central1')
            else:
                self.client = PlatformClient(api_key=api_key, owner_id=config['owner_id'],
                                             env=config['env'], logger_=self.logger.name)
        except Exception as e:
            self.logger.warning(f' Could not create a client due to {e}')
            raise Exception(f' Could not create a client due to {e}')

        try:
            df = pd.read_csv(config['log_path'])
            if 'wiliot_code' not in df or 'asset_code' not in df:
                raise Exception('file must contain the following columns: wiliot_code,  asset_code')

            pairs = df[['wiliot_code', 'asset_code']][(df['wiliot_code'].notnull() & df['asset_code'].notnull())]
            action_str = config['action_type'].lower()
            bad_request = 0

            for i, p in pairs.iterrows():
                self.logger.info(f'{i}: try to do {action_str} the following: {p["asset_code"]}, {p["wiliot_code"]}')
                try:
                    if config['action_type'].lower() == 'association':
                        status = self.client.create_asset(name=p['asset_code'], asset_id=p['asset_code'],
                                                          category_id=CATEGORY_ID,
                                                          pixels=[{'tagId': p['wiliot_code'], 'role': TagRole.DEFAULT}])
                    elif 'dis-association' in config['action_type'].lower():
                        status = self.client.disassociate_pixel_from_asset(asset_id=p['asset_code'],
                                                                           pixel_id=p['wiliot_code'])
                        if 'delete' in config['action_type'].lower():
                            status_d = self.client.delete_asset(asset_id=p['asset_code'])
                            status = status and status_d
                    else:
                        raise Exception(f'unsupported action type: {config["action_type"]}')
                    if status:
                        self.logger.info(
                            f'{action_str} for {p["asset_code"]}, {p["wiliot_code"]} was done successfully')
                    else:
                        self.logger.warning(f'{action_str} for {p["asset_code"]}, {p["wiliot_code"]} Failed')
                except Exception as e:
                    self.logger.warning(f'could not do {action_str} due to {e}')
                    bad_request += 1
            if bad_request > 0:
                self.logger.warning(f'could not complete the task for {bad_request} requests')
            else:
                self.logger.info('all requests were successfully done!')

        except Exception as e:
            self.logger.warning(f'Could not read data from file due to {e}')
            raise Exception(f'Could not read data from file due to {e}')


if __name__ == '__main__':
    import PySimpleGUI as Sg

    def get_user_inputs():
        layout = [[Sg.Text('Please select file to associate/disassociate'),
                   Sg.Input('', key='log_path_str', size=(80, 1)),
                   Sg.FileBrowse(key='log_path')],
                  [Sg.Text('Action Type?'),
                   Sg.Combo(('Association', 'Dis-association', 'Dis-association & Delete'), default_value='Association',
                            key='action_type', size=(40, 1))],
                  [Sg.Text('environment'), Sg.Combo(('prod', 'test', 'dev'), default_value='prod', key='env')],
                  [Sg.Text('owner id'), Sg.Input('', key='owner_id')],
                  [Sg.Text('for GCP?'), Sg.Combo(('yes', 'no'), default_value='no', key='is_gcp')],
                  [Sg.Text('Client type'),
                   Sg.Input('', key='client_type')],
                  [Sg.Button('Run')]
                  ]

        # Create the window
        window = Sg.Window('Upload Sensor Data to Cloud', layout)
        while True:
            event, values = window.read()
            # See if user wants to quit or window was closed
            if event == 'Run' and (values['log_path'] != '' or values['log_path_str']):
                values['log_path'] = values['log_path_str'] if values['log_path_str'] is not None else values['log_path']
                window.close()
                return values
            elif event == 'Run':
                print('must include log file')
            else:
                window.close()
                print('exit by user')
                exit(-1)

    user_config = get_user_inputs()
    a = AssociateFile(user_config)
    print('done')
