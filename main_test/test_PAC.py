import logging
from main_test.constants import Cat_Facts_URL ,Dog_Breeds_URL,Pet_Food_Facts_URL
from main_test.Report_Mail import Success_List_Append
import requests
import json
import string
import random
from random import randint
import time
import os


#Fulfillment.....
def test_Cat_Facts():
    print(Cat_Facts_URL)
    payload = {}
    headers = {}
    response = requests.request("GET", Cat_Facts_URL, headers=headers, data=payload)
    print(response.elapsed.total_seconds())
    resp_data = response.json()
    print(resp_data)
    Success_List_Append("test_Cat_Facts", response.elapsed.total_seconds(), response.status_code)

def test_Dog_Breeds():
    print(Dog_Breeds_URL)
    payload = {}
    headers = {}
    response = requests.request("GET", Dog_Breeds_URL, headers=headers, data=payload)
    print(response.elapsed.total_seconds())
    resp_data = response.json()
    print(resp_data)
    Success_List_Append("test_Dog_Breeds", response.elapsed.total_seconds(), response.status_code)

def test_Pet_Food_Facts():
    print(Pet_Food_Facts_URL)
    payload = {}
    headers = {}
    response = requests.request("GET", Pet_Food_Facts_URL, headers=headers, data=payload)
    print(response.elapsed.total_seconds())
    resp_data = response.json()
    print(resp_data)
    Success_List_Append("test_Pet_Food_Facts", response.elapsed.total_seconds(), response.status_code)