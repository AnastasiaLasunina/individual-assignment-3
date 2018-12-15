#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:39:24 2018

@author: Anastasia
"""
#%%
from indiv_assign import recalculate_quality
from indiv_assign import Product,potato, cheese, tomato, milk



def test_recalculate_quality():
    values = [potato]
    for item in values:
        assert recalculate_quality(item).quality == 7.5
        
def test_recalculate_quality1():
    values = [cheese]
    for item in values:
        assert recalculate_quality(item).quality == 4  

def test_recalculate_quality2():
    values = [tomato]
    for item in values:
        assert recalculate_quality(item).quality == 1  
        
def test_recalculate_quality3():
    values = [milk]
    for item in values:
        assert recalculate_quality(item).quality == -1 