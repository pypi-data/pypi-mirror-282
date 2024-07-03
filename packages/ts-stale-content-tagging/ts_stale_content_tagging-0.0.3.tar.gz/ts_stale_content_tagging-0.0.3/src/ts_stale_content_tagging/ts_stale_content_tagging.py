#!/usr/bin/python
'''Tableau Server tag content, Authors Jose Ramirez, Marcus Mitchell (mailto: mmitchell@healthfirst.org, josramirez@healthfirst.org)
Requirements:
  - tableauserverclient
  - pandas
  - yaml
  - logging
Python:
  - 3.7.3
Usage:
  - script to programatically tag content on tableau server
'''

import tableauserverclient as TSC
import pandas as pd
import yaml
import logging

def load_conf_file(config_file):
    # open yaml file in safe read
   with open(config_file, "r") as f:
       config = yaml.safe_load(f)
       con_conf = config[0]["connection"]
   return con_conf

def main():
    #Configuring logger
    logging.basicConfig(filename='ts_stale_content_tagging_logs.log', level=logging.DEBUG, format = '%(asctime)s - %(message)s', datefmt='%Y-%m-%d,%H:%M:%S %p', filemode="w")
    connection_conf = load_conf_file("ts_stale_content_tagging.yaml")
    ts_url = connection_conf["server"]
    ts_pat_name = connection_conf["personal_access_token_name"]
    ts_pat_secret = connection_conf["personal_access_token_secret"]    
    authorization = TSC.PersonalAccessTokenAuth(ts_pat_name, ts_pat_secret)
    connection = TSC.Server(ts_url, use_server_version=True)
    connection.auth.sign_in(authorization)

    #read data from excel files
    datasources_file = pd.read_excel(io=r'\\sv-hfi-014\is\Tableau\Datasources\File\Excel\Tableau\test_ts_datasources_stale_ea.xlsx')
    workbooks_file = pd.read_excel(io=r'\\sv-hfi-014\is\Tableau\Datasources\File\Excel\Tableau\test_ts_workbooks_stale_ea.xlsx')
    wb_ids = workbooks_file['luid']
    ds_ids = datasources_file['luid']

    #add stale content tag to workbooks
    for wb_id in wb_ids:
        try:
            workbook = connection.workbooks.get_by_id(wb_id)
            print("\nWorkbook ID {} retrieved from list...".format(wb_id))
            workbook.tags.add('"Stale Content"')
            connection.workbooks.update(workbook)
        except Exception as e:
            logging.error('An error occurred: %s', str(e))
            print(f"There was an error adding the stale content tag to the workbooks. {e}")
        else:
            print("\Workbook ID {} has been tagged as stale content...".format(wb_id))

    #add stale content tag to datasources
    for ds_id in ds_ids:
        try:
            datasource = connection.datasources.get_by_id(ds_id)
            print("\nDatasource ID {} retrieved from list...".format(ds_id))
            datasource.tags.add('"Stale Content"')
            connection.datasources.update(datasource)
        except Exception as e:
            logging.error('An error occurred: %s', str(e))
            print(f"There was an error adding the stale content tag to the datasource. {e}")
        else:
            print("\Datasource ID {} has been tagged as stale content...".format(ds_id))             

    connection.auth.sign_out()
    logging.info(main)

if __name__ == "__main__":
    main()