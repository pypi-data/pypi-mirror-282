#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright(C) 2023 baidu, Inc. All Rights Reserved

# @Time : 2024/1/25 14:13
# @Author : yangtingyu01
# @Email: yangtingyu01@baidu.com
# @File : internal_usersetting_client.py
# @Software: PyCharm
"""
from typing import List, Optional, Dict, Any
from baidubce.http import http_methods
from baidubce.bce_client_configuration import BceClientConfiguration
from bceinternalsdk.client.bce_internal_client import BceInternalClient


class InternalUsersettingClient(BceInternalClient):
    """
    A client class for interacting with the userstting service. Initializes with default configuration.

    This client provides an interface to interact with the Artifact service using BCE (Baidu Cloud Engine) API.
    It supports operations related to creating and retrieving artifacts within a specified workspace.
    """

    def get_user_setting(self, setting_key: str):
        """
        Get user setting by key.
        :param setting_key:
        :return:
        """
        return self._send_request(http_method=http_methods.GET,
                                  path=bytes("/v1/usersettings/" + setting_key, encoding="utf-8"))