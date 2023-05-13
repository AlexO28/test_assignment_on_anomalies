# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:36:54 2023

@author: Семья
"""
import pandas as pd
import numpy as np
from processing import (
    convertation_to_int,
    process_client_ip,
    add_length_column,
    detection_of_nan_in_strings,
)


def prepare_the_data(tab):
    tab = detection_of_nan_in_strings(tab, "CLIENT_IP", False)
    tab = detection_of_nan_in_strings(tab, "CLIENT_USERAGENT", False)
    tab = detection_of_nan_in_strings(tab, "MATCHED_VARIABLE_VALUE", False)
    tab = detection_of_nan_in_strings(tab, "EVENT_ID", False)
    tab = detection_of_nan_in_strings(tab, "MATCHED_VARIABLE_SRC", False)
    tab = detection_of_nan_in_strings(tab, "MATCHED_VARIABLE_NAME", False)
    tab = convertation_to_int(tab, "REQUEST_SIZE", "anomaly_request_size")
    tab = convertation_to_int(tab, "RESPONSE_CODE", "anomaly_response_code")
    del tab["anomaly_response_code"]
    tab = process_client_ip(tab)
    tab = fill_popularity_column(tab, "CLIENT_USERAGENT")
    tab = add_length_column(tab, "CLIENT_USERAGENT", True)
    tab = fill_popularity_column(tab, "MATCHED_VARIABLE_SRC")
    tab["MATCHED_VARIABLE_SRC_HAS_SEMICOLUMN"] = tab[
        "MATCHED_VARIABLE_SRC"
    ].str.contains(";")
    tab = add_length_column(tab, "MATCHED_VARIABLE_NAME", True)
    tab = fill_popularity_column(tab, "MATCHED_VARIABLE_NAME")
    tab = fill_popularity_column(tab, "MATCHED_VARIABLE_VALUE", safe=True)
    tab = add_length_column(tab, "MATCHED_VARIABLE_VALUE", True)
    tab = fill_popularity_column(tab, "EVENT_ID", safe=True)
    tab = tab[
        [
            "REQUEST_SIZE_INT",
            "anomaly_request_size",
            "RESPONSE_CODE_INT",
            "CLIENT_IP_1",
            "CLIENT_IP_2",
            "CLIENT_IP_3",
            "CLIENT_IP_4",
            "anomaly_client_ip",
            "CLIENT_USERAGENT_POPULARITY",
            "CLIENT_USERAGENT_LENGTH",
            "MATCHED_VARIABLE_SRC_POPULARITY",
            "MATCHED_VARIABLE_SRC_HAS_SEMICOLUMN",
            "MATCHED_VARIABLE_NAME_LENGTH",
            "MATCHED_VARIABLE_NAME_POPULARITY",
            "MATCHED_VARIABLE_VALUE_LENGTH",
            "MATCHED_VARIABLE_VALUE_POPULARITY",
            "EVENT_ID_POPULARITY",
            "anomaly_CLIENT_IP",
            "anomaly_CLIENT_USERAGENT",
            "anomaly_MATCHED_VARIABLE_VALUE",
            "anomaly_EVENT_ID",
            "anomaly_MATCHED_VARIABLE_SRC",
            "anomaly_MATCHED_VARIABLE_NAME",
        ]
    ]
    return tab


def fill_popularity_column(tab, column_name, safe=False):
    popularity_stats = pd.read_csv("popularity_stats_" + column_name + ".csv")
    if safe:
        tab[column_name + "_POPULARITY"] = 1
        for j in range(len(tab)):
            temptab = popularity_stats[
                popularity_stats["index"] == tab.loc[j, column_name]
            ]
            if len(temptab) > 0:
                tab.loc[j, column_name + "_POPULARITY"] = temptab[
                    column_name + "_POPULARITY"
                ].tolist()[0]
    else:
        tab = pd.merge(
            tab, popularity_stats, how="left", left_on=[column_name], right_on=["index"]
        )
    tab.loc[np.isnan(tab[column_name + "_POPULARITY"]), column_name + "_POPULARITY"] = 1
    return tab
