# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  selenium-python-helper
# FileName:     http_client.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/06/29
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import urllib3
import typing as t
from selenium_helper.log import logger
from requests import get, post, Response
from selenium_helper.utils import covert_dict_key_to_lower, get_html_title

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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


def get_proxy() -> dict:
    proxy_address = get_proxy_address()
    return {
        "http": "http://{}".format(proxy_address),
        "https": "http://{}".format(proxy_address)
    }


class HttpService(object):
    __time_out = 60
    __domain = None
    __url = None
    __protocol = None
    __headers: dict = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " +
                      "Chrome/123.0.0.0 Safari/537.36"
    }

    def __init__(self, domain: str, protocol: str) -> None:
        self.__domain = domain
        self.__protocol = protocol

    def send_request(self, method: str, path: str, params: dict = None, data: dict or str = None, json: dict = None,
                     headers: dict = None, proxies: dict = None) -> t.Any:
        if isinstance(headers, dict):
            self.__headers = headers
        self.__url = "{}://{}{}".format(self.__protocol, self.__domain, path)
        # 发送HTTP请求
        logger.info(
            "尝试发起http请求，url: {}, 方法：{}，请求params参数：{}，请求headers参数：{}，请求data参数：{}，请求json参数：{}".format(
                self.__url,
                method,
                params or "{}",
                self.__headers,
                data or "{}",
                json or "{}",
            )
        )
        return self.__send_http_request(method=method, proxies=proxies, params=params, data=data, json=json)

    def __send_http_request(self, method: str, params: dict = None, data: dict = None, proxies: dict = None,
                            json: dict = None) -> dict:
        # 实际发送HTTP请求的内部方法
        # 使用 requests 库发送请求
        method = method.lower().strip()
        if method in ("get", "post"):
            try:
                if method == "get":
                    response = get(self.__url, params=params, verify=False, timeout=self.__time_out,
                                   headers=self.__headers, proxies=proxies)
                else:
                    response = post(
                        self.__url, params=params, json=json, data=data, verify=False, timeout=self.__time_out,
                        headers=self.__headers, proxies=proxies
                    )
                result = self.__parse_data_response(response=response)
            except Exception as e:
                logger.error("调用url<{}>异常，原因：{}".format(self.__url, str(e)))
                result = dict(code=500, message=str(e), data=dict())
        else:
            result = dict(code=400, message="Unsupported HTTP method: {}".format(method), data=dict())
        return result

    def __parse_data_response(self, response: Response) -> dict:
        # 获取 Content-Type 头信息
        content_type = response.headers.get('Content-Type') or ""
        # 判断返回的内容类型
        if 'application/json' in content_type or 'text/json' in content_type:
            # JSON 类型
            data = covert_dict_key_to_lower(d=response.json())
        elif 'text/plain' in content_type or 'text/html' in content_type:
            # 纯文本类型
            data = dict(code=response.status_code, message=get_html_title(
                html=response.text), data=response.text)
        else:
            if response.json():
                # JSON 类型
                data = covert_dict_key_to_lower(d=response.json())
            else:
                # 其他类型，默认视为二进制内容
                content = response.content.decode('utf-8')
                data = dict(code=response.status_code,
                            message=get_html_title(html=content), data=content)
        logger.info("调用url: {}的正常返回值为：{}".format(self.__url, data))
        return data


if __name__ == '__main__':
    print(get_proxy_address())
