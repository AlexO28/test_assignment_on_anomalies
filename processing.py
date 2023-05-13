# -*- coding: utf-8 -*-
"""
Created on Sun May  7 00:12:10 2023

@author: Семья
"""
import pandas as pd
import numpy as np


def detection_of_nan_in_strings(tab, column_name, in_research=True):
    tab["anomaly_" + column_name] = 0
    for j in range(len(tab)):
        try:
            val = np.isnan(tab.loc[j, column_name])
        except:
            val = False
        if not val:
            try:
                val2 = len(tab.loc[j, column_name])
            except:
                val = True
        if val:
            tab.loc[j, "anomaly_" + column_name] = 1
    if in_research:
        if tab["anomaly_" + column_name].max() == 0:
            del tab["anomaly_" + column_name]
    return tab


def convertation_to_int(tab, old_column, anomaly_column_name):
    new_column = old_column + "_INT"
    tab[anomaly_column_name] = 0
    for j in range(len(tab)):
        try:
            tab.loc[j, new_column] = int(tab.loc[j, old_column])
        except:
            tab.loc[j, new_column] = np.nan
            tab.loc[j, anomaly_column_name] = 1
    return tab


def process_client_ip(tab):
    tab["CLIENT_IP_1"] = 0
    tab["CLIENT_IP_2"] = 0
    tab["CLIENT_IP_3"] = 0
    tab["CLIENT_IP_4"] = 0
    tab["anomaly_client_ip"] = 0
    for j in range(len(tab)):
        try:
            split_ip = str(tab.loc[j, "CLIENT_IP"]).split(".")
            if len(split_ip) != 4:
                raise ("anomaly client ip")
            tab.loc[j, "CLIENT_IP_1"] = int(split_ip[0])
            tab.loc[j, "CLIENT_IP_2"] = int(split_ip[1])
            tab.loc[j, "CLIENT_IP_3"] = int(split_ip[2])
            tab.loc[j, "CLIENT_IP_4"] = int(split_ip[3])
        except:
            tab.loc[j, "anomaly_client_ip"] = 1
    return tab


def add_popularity_column(tab, column_name):
    tab_stats = tab[column_name].value_counts()
    tab_stats = pd.DataFrame(tab_stats)
    tab_stats.reset_index(inplace=True)
    tab_stats.rename(columns={column_name: column_name + "_POPULARITY"}, inplace=True)
    tab_stats.to_csv("popularity_stats_" + column_name + ".csv")
    tab = pd.merge(
        tab, tab_stats, how="left", left_on=[column_name], right_on=["index"]
    )
    return tab


def add_length_column(tab, column_name, with_convertation=False):
    if with_convertation:
        tab[column_name + "_LENGTH"] = tab[column_name].apply(lambda x: len(str(x)))
    else:
        tab[column_name + "_LENGTH"] = tab[column_name].apply(lambda x: len(x))
    return tab
