# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:54:25 2023

@author: Семья
"""
import pandas as pd
import pickle
import hdbscan


def apply_the_model(tab):
    tab = tab.fillna(-1)
    with open("hdbscan_model.pickle", "rb") as f:
        model = pickle.load(f)
    labels, strengths = hdbscan.approximate_predict(model, tab)
    tab["cluster_label"] = labels
    anomality_mapping = pd.read_csv("anomaly_mapping.csv")
    anomality_mapping = anomality_mapping[anomality_mapping["anomality_label"] < 54]
    anomality_mapping = anomality_mapping[["cluster_label", "anomality_label"]]
    tab = pd.merge(
        tab,
        anomality_mapping,
        how="left",
        left_on="cluster_label",
        right_on="cluster_label",
    )
    tab.loc[tab["anomaly_client_ip"] == 1, "anomality_label"] = 54
    tab.loc[tab["anomaly_CLIENT_USERAGENT"] == 1, "anomality_label"] = 55
    tab.loc[tab["anomaly_MATCHED_VARIABLE_VALUE"] == 1, "anomality_label"] = 56
    tab.loc[tab["anomaly_EVENT_ID"] == 1, "anomality_label"] = 57
    tab.loc[tab["anomaly_MATCHED_VARIABLE_NAME"] == 1, "anomality_label"] = 58
    return tab
