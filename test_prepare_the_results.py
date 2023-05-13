# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:23:51 2023

@author: Семья
"""
import pandas as pd
from processing_for_rest import prepare_the_results
from processing_in_prod import prepare_the_data
from model import apply_the_model


def test_prepare_the_results():
    tab = pd.read_csv("part_10.csv")
    tab = tab.head(10)
    ids = tab["EVENT_ID"].tolist()
    tab = prepare_the_data(tab)
    tab = apply_the_model(tab)
    results = prepare_the_results(tab, ids)
    assert (
        str(results)
        == "[{'EVENT_ID': 'AVdhXFgVq1Ppo9zF5Fxu', 'LABEL_PRED': 58.0}, {'EVENT_ID': 'AVdcJmIIq1Ppo9zF2YIp', 'LABEL_PRED': nan}, {'EVENT_ID': 'iz7SN2YBrgKk_RFNZW_U', 'LABEL_PRED': 58.0}, {'EVENT_ID': 'AVdjekw4q1Ppo9zF6QT2', 'LABEL_PRED': nan}, {'EVENT_ID': 'SqQGI2QB5cBXmMW1CDbp', 'LABEL_PRED': nan}, {'EVENT_ID': 'nFzwHGQB5cBXmMW1y_TD', 'LABEL_PRED': nan}, {'EVENT_ID': '9KP-ImQB5cBXmMW1yeXY', 'LABEL_PRED': nan}, {'EVENT_ID': '97JpJGQB5cBXmMW1WqBh', 'LABEL_PRED': nan}, {'EVENT_ID': 'irs7_mMBjksgoq1eoQ7a', 'LABEL_PRED': 58.0}, {'EVENT_ID': 'g4RdIGQB5cBXmMW10nGg', 'LABEL_PRED': nan}]"
    )
