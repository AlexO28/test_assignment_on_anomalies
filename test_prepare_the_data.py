# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:56:18 2023

@author: Семья
"""
import pandas as pd
from processing_in_prod import prepare_the_data


def test_prepare_the_data():
    tab = pd.read_csv("part_10.csv")
    tab = tab.head(5)
    tab = prepare_the_data(tab)
    assert len(tab) == 5
    assert tab.columns.tolist() == [
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
    assert tab["REQUEST_SIZE_INT"].tolist() == [166.0, 431.0, 395.0, 387.0, 1733.0]
    assert tab["EVENT_ID_POPULARITY"].tolist() == [1] * 5
