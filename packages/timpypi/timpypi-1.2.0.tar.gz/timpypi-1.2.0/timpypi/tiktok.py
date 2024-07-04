
# -*- coding: utf-8 -*-
# 1 : imports of python lib
import base64
import hashlib
import hmac
import io
import json
import logging
from io import BytesIO
import random
import subprocess
from PIL import Image, ImageDraw, ImageFont
import string
from json import dumps
from datetime import datetime, time, timedelta
from requests import Request, Response, post, put, patch, delete, get, request
from urllib.parse import quote, urlencode
import time
from timpypi.common import exception


_logger = logging.getLogger(__name__)


@exception
def cal_sign(req: Request, secret: str):
    queries = dict(req.params)
    keys = [k for k in queries if k not in ["sign", "access_token"]]
    keys.sort()
    input = "".join(k + str(queries[k]) for k in keys)
    input = req.url + input
    input = secret + input + secret
    return generateSHA256(input, secret)


@exception
def generateSHA256(input: str, secret: str):
    h = hmac.new(secret.encode(), input.encode(), hashlib.sha256)
    return h.hexdigest()


@exception
def get_access_token(
    app_key: str, app_secret: str, auth_code: str, grant_type="authorized_code"
) -> Response:
    path = f"https://auth.tiktok-shops.com/api/v2/token/get?app_key={app_key}&auth_code={auth_code}&app_secret={app_secret}&grant_type={grant_type}"
    return get(url=path, headers={"Content-Type": "application/json"})


@exception
def refresh_token(): ...


@exception
def effect_rainbow(message: str, meme=""):
    if not meme:
        meme = "web/static/img/smile.svg"
    return {
        "effect": {
            "fadeout": "slow",
            "message": message,
            "img_url": meme,
            "type": "rainbow_man",
        }
    }


@exception
def convert_response_value(data: dict, keys: list):
    """
    @Description:
        Convert value to string
        Keys contain value break
    @Return: dict()
    """
    convert_data = data
    for k, v in data.items():
        if k in keys:
            continue
        convert_data[k] = str(v)
    return convert_data


@exception
def generateSign(api: str, params: dict, secret: str):
    timestamp = str(int(datetime.timestamp(datetime.now())))
    if params.get("timestamp", False):
        params.update({"timestamp": timestamp})
    req = Request(url=api, params=params)
    return cal_sign(req, secret)


@exception
def requestGeneral(
    method: Request,
    domain: str,
    api: str,
    params: dict,
    body: dict,
    secret: str,
) -> Response:
    timestamp = str(int(datetime.timestamp(datetime.now())))
    if "timestamp" not in params.keys():
        params["timestamp"] = timestamp
    sinature = generateSign(api=api, params=params, secret=secret)
    params.update({"sign": sinature})
    url = f"{domain}{api}"
    pairs = [f"{key}={value}" for key, value in params.items()]
    url = f"{domain}{api}?" + "&".join(pairs)
    return method(url=url, params=params, data=body)
