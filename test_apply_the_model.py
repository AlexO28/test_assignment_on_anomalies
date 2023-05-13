# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:36:05 2023

@author: Семья
"""
import pandas as pd
import numpy as np
from processing_in_prod import prepare_the_data
from model import apply_the_model


def test_apply_the_model():
    tab = pd.read_csv("part_10.csv")
    tab = tab.sample(n=10, random_state=239)
    tab.reset_index(inplace=True)
    tab = prepare_the_data(tab)
    tab = apply_the_model(tab)
    assert len(tab) == 10
    assert len(tab[np.isnan(tab["anomality_label"])]) == 10


def test_apply_the_model_to_all():
    tab = pd.read_csv("part_10.csv")
    tab.reset_index(inplace=True)
    tab = prepare_the_data(tab)
    res = apply_the_model(tab)
    assert len(res) == len(tab)
    assert len(res[~np.isnan(res["anomality_label"])]) > 0.2 * len(tab)
    assert len(res[~np.isnan(res["anomality_label"])]) < 0.3 * len(tab)
