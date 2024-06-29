# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  selenium-python-helper
# FileName:     http.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/06/29
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from requests import get
from selenium_helper.libs import logger

url = "http://api.ip.data5u.com/dynamic/get.html?order=a2e80005b59944e04a8d78347ed1c726&json=1&ttl=1&random=2&sep=6"


def get_proxy_address() -> str:
    data = ""
    try:
        response = get(url, verify=False, timeout=10)
        if response.status_code == 200:
            """"
            {
                "data": [
                    {
                        "ip": "223.215.177.193",
                        "port": 48004,
                        "ttl": 33778
                    }
                ],
                "msg": "ok",
                "success": true
            }
            """
            result: dict = response.json() or dict()
            if result.get("success") is True:
                proxy_ip_info = result.get("data")[0] if len(result.get("data")) > 0 else dict()
                if proxy_ip_info:
                    data = "{}:{}".format(proxy_ip_info.get("ip"), proxy_ip_info.get("port"))
        else:
            logger.error(response.raise_for_status())
    except Exception as e:
        logger.error(e)
    return data


if __name__ == '__main__':
    print(get_proxy_address())
