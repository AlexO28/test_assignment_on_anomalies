# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:55:57 2023

@author: Семья
"""
import api
from fastapi import FastAPI


app = FastAPI()


@app.post("/predict")
def separate_the_flees(http_requests):
    return api.separate_the_flees(http_requests)
