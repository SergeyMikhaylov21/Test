#!/usr/bin/python
# -*- coding: UTF-8 -*-

import vk_auth
import json
import urllib2
from urllib import urlencode
import os
import getpass
import sys


email = 'username@domain.ru'
password = 'your_password'
client_id = "5927046" # Vk application ID
token, user_id = vk_auth.auth(email, password, client_id, "photos")
print token
print user_id


# 8033a6903b8ce14889bde9b1a4011ba08456bcb845f35a5865ae7e9a6e6b100aaf93723d853b6d88d8627
# 0c2978f50c2978f50c758ace1e0c73087300c290c2978f554e0113506788798a1f86655
# 18648833

