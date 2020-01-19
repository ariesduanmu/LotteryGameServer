# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-08-21 15:09:30
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-01-19 11:06:32
import unittest
import uuid

from basic import BasicTest

LOGIN_PATH = "login"
LOTTERY_PATH = "lottery"


class PandoraTest(BasicTest):

    def test_login(self):
        data = {"username":"test"}
        _, json_data, status_code = self.post(LOGIN_PATH, data=data)
        self.assertEqual(status_code, 200)
        self.assertEqual(json_data.get("status_code"), 1000)


    def test_lottery(self):
        data = {"username":"test"}
        _, json_data, status_code = self.post(LOTTERY_PATH, data=data)
        self.assertEqual(status_code, 200)
        self.assertEqual(json_data.get("status_code"), 1000)


if __name__ == "__main__":
    unittest.main()