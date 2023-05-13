# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:38:03 2023

@author: Семья
"""
import pandas as pd


def parse_http_requests(http_requests):
    res_columns = [
        "CLIENT_IP",
        "CLIENT_USERAGENT",
        "REQUEST_SIZE",
        "RESPONSE_CODE",
        "MATCHED_VARIABLE_SRC",
        "MATCHED_VARIABLE_NAME",
        "MATCHED_VARIABLE_VALUE",
        "EVENT_ID",
    ]
    res_list = []
    for http_request in http_requests:
        request_data = http_request['data']
        res_list.append(
            [
                request_data["CLIENT_IP"],
                request_data["CLIENT_USERAGENT"],
                request_data["REQUEST_SIZE"],
                request_data["RESPONSE_CODE"],
                request_data["MATCHED_VARIABLE_SRC"],
                request_data["MATCHED_VARIABLE_NAME"],
                request_data["MATCHED_VARIABLE_VALUE"],
                request_data["EVENT_ID"],
            ]
        )
    tab = pd.DataFrame(res_list, columns=res_columns)
    return tab


def prepare_the_results(tab, ids):
    res = []
    for j in range(len(tab)):
        res_dict = {
            "EVENT_ID": ids[j],
            "LABEL_PRED": tab.loc[j, "anomality_label"],
        }
        res.append(res_dict)
    return res
