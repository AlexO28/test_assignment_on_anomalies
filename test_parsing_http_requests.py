# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:27:13 2023

@author: Семья
"""
import numpy as np
from processing_for_rest import parse_http_requests


def test_parsing_http_requests():
    sample_request = [
        {
            "data": {
                "CLIENT_IP": "188.138.92.55",
                "CLIENT_USERAGENT": np.nan,
                "REQUEST_SIZE": 166,
                "RESPONSE_CODE": 404,
                "MATCHED_VARIABLE_SRC": "REQUEST_URI",
                "MATCHED_VARIABLE_NAME": np.nan,
                "MATCHED_VARIABLE_VALUE": "//tmp/20160925122692indo.php.vob",
                "EVENT_ID": "AVdhXFgVq1Ppo9zF5Fxu",
            }
        },
        {
            "data": {
                "CLIENT_IP": "93.158.215.131",
                "CLIENT_USERAGENT": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0\\",
                "REQUEST_SIZE": 431,
                "RESPONSE_CODE": 302,
                "MATCHED_VARIABLE_SRC": "REQUEST_GET_ARGS",
                "MATCHED_VARIABLE_NAME": "url",
                "MATCHED_VARIABLE_VALUE": "[<http://www.galitsios.gr/?option=com_k2\\>](<http://www.galitsios.gr/?option=com_k2%5C%5C>)",
                "EVENT_ID": "AVdcJmIIq1Ppo9zF2YIp",
            }
        },
    ]
    results = parse_http_requests(sample_request)
    assert len(results) == 2
    assert len(results.columns) == 8
    assert results["CLIENT_IP"].tolist() == ["188.138.92.55", "93.158.215.131"]
    assert results["EVENT_ID"].tolist() == [
        "AVdhXFgVq1Ppo9zF5Fxu",
        "AVdcJmIIq1Ppo9zF2YIp",
    ]

