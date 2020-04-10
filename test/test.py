# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-08-21 15:09:30
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 12:33:00
import unittest
import uuid

from basic import BasicTest

LOTTERY_PATH = "lottery"


class PandoraTest(BasicTest):


    def test_lottery(self):
        data = {"username":"中文"}
        _, json_data, status_code = self.post(LOTTERY_PATH, data=data)
        self.assertEqual(status_code, 200)
        self.assertEqual(json_data.get("status_code"), 1000)


if __name__ == "__main__":
    unittest.main()