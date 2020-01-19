# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-08-08 14:21:02
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-01-19 13:08:18
import unittest
import requests
from urllib.parse import urljoin

class BasicTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/"
        
    def post(self, path, data=None, files=None, print_log=True, headers=None, json=None):
        url = self.base_url + path
        if print_log:
            print(f"[*] POST Path: {url}")
            print(f"[*] POST Data: {data}")
            print(f"[*] POST File: {files}")
        response = requests.post(url, data=data, files=files, headers=headers, json=json)
        self.response_output(response)
        try:
            return response.content, response.json(), response.status_code
        except:
            return response.content, {}, response.status_code

    def response_output(self, response):
        if response.status_code != 200:
            print(f"[-] Fail: {response.content.decode('utf-8')}")
        else:
            print(f"[+] GET: {response.content.decode('utf-8')}")
