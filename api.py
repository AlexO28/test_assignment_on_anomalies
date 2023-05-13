# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:34:16 2023

@author: Семья
"""
from processing_for_rest import parse_http_requests, prepare_the_results
from processing_in_prod import prepare_the_data
from model import apply_the_model
import json


def separate_the_flees(http_requests):
    http_requests = json.loads(http_requests)
    tab = parse_http_requests(http_requests)
    ids = tab["EVENT_ID"].tolist()
    tab = prepare_the_data(tab)
    tab = apply_the_model(tab)
    res = prepare_the_results(tab, ids)
    return res
