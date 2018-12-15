#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:20:17 2018

@author: Anastasia
"""

#%% ex. 1


class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

def recalculate_quality(product):
    if product.name == "potato":
       product.quality = product.quality - 0.5
    elif product.name == "cheese":
         product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
    return product 
potato = Product("potato", 8)
tomato = Product("tomato", 4)
cheese = Product("cheese", 6)
milk = Product ("milk", 2)


#%% ex. 2 

import requests


def take_all_repository(user):

    url = "https://api.github.com/users/{}/repos".format(user)
    response = requests.get(url).json()

    return response

take_all_repository("AnastasiaLasunina")


#%%
import requests


def description_repository(user):

    url = "https://api.github.com/users/{}/repos".format(user)
    response = requests.get(url).json()

    description_lst ={}


    for i in response:

        description_lst.update({"Name":i["name"]})
        description_lst.update({"Number of stars":i["stargazers_count"]})
        description_lst.update({"Language":i["language"]})
        description_lst.update({"Url":i["url"]})

        print ([description_lst])

 
description_repository("AnastasiaLasunina")


#%% ex. 3 

#%%

from flask import Flask, jsonify


server = Flask("Phonebook")

phonebook = {"Natalie": "5739201",
             "Lukas": "20393472",
             "Agata": "48290489",
             "David": "38931380"}


@server.route("/phonebook")
def get_phonebook():
    return jsonify(phonebook)

    
@server.route("/add-contact/<phone>/<name>", methods=["POST"])
def add_contact_post(phone, name): 
    

    if name not in phonebook: 
        
        phonebook.update({name:phone})
        return jsonify("you have added " + name + " with the phone number: " + phone)
    
    else: 
        return jsonify("you have already added " + name)


@server.route("/get-phone/<name>")
def get_phone_by_name(name): 
    
    if name in phonebook: 
        return jsonify(name + "'s  phone number is " + phonebook[name])
    
    else: 
        return jsonify("there is no " + name + " in your phonebook")


@server.route("/delete-contact/<name>", methods=["DELETE"])
def delete_contact_by_name(name):   
    if name not in phonebook: 
        
        return jsonify("there is no " + name + " in your phonebook")
    else:
        del phonebook[name]
        
        return jsonify(name + " has been deleted from your phonebook :( ")         


                  
@server.route("/update-contact/<name>/<phone>", methods=["PUT"])
def update_contact(name, phone): 
    
    if name not in phonebook: 
        return jsonify("There is no one in you phonebook with that name")
    
    else: 
        phonebook[name] = phone
        return jsonify(name + " has been updated to: " + phone)
    
        
    
server.run()

















