import os
import re
import math
import httpx
import socket
import hashlib
import execjs
import py_mini_racer
import pandas as pd
from urllib.parse import urlparse
from typing import Union, Optional, Literal, List, Tuple, Set, Dict


def get_host(host_type: Literal["local", "public"] = "local") -> str:
    if host_type == "local":
        return socket.gethostbyname(socket.gethostname())
    elif host_type == "public":
        return httpx.get("https://api.ipify.org").text
    else:
        raise ValueError("Unsupported host_type!")


def chunk_data(data: List, chunk_size: int) -> List:
    return [data[i: i + chunk_size] for i in range(0, len(data), chunk_size)]


def split_df(df: pd.DataFrame, n_splits: int) -> List[pd.DataFrame]:
    size_of_each_split = len(df) // n_splits
    remainder = len(df) % n_splits

    dfs = []
    start_idx = 0

    for i in range(n_splits):
        end_idx = start_idx + size_of_each_split + (1 if i < remainder else 0)
        dfs.append(df.iloc[start_idx:end_idx])
        start_idx = end_idx

    return dfs


def ceil_decimal(num: float, decimal_places=2) -> float:
    """
    >>> ceil_decimal(3.14159)
    3.15

    :param num:
    :param decimal_places:
    :return:
    """
    scale = 10.0 ** decimal_places
    return math.ceil(num * scale) / scale


def is_valid_url(url: str) -> bool:
    """
    >>> is_valid_url("https://www.baidu.com/")
    True

    :param url:
    :return:
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def gen_uxid(
        *args,
        keys: List = None, item: Dict = None,
        algo_type: Literal[
            "md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256",
            "sha3_384", "sha3_512", "shake_128", "shake_256"
        ] = "md5"
) -> str:
    """
    >>> gen_uxid("123456")
    'e10adc3949ba59abbe56e057f20f883e'

    :param args:
    :param keys:
    :param item:
    :param algo_type:
    :return:
    """
    m = hashlib.new(algo_type)
    if args:
        values = args
    elif keys is not None and item is not None:
        if isinstance(keys, list) and isinstance(item, dict):
            values = [item[k] for k in keys if k in item]
        else:
            raise ValueError("keys and item must be list and dict!")
    elif item is not None:
        values = [item[k] for k in sorted(item.keys())]
    else:
        raise ValueError("args or keys and item or item must be provided!")

    data = list(map(lambda x: str(x), values))

    for i in data:
        m.update(i.encode())

    return m.hexdigest()


def camel_to_snake(name: str) -> str:
    """
    >>> camel_to_snake('CamelCaseString')
    'camel_case_string'

    :param name:
    :return:
    """
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def get_files_and_dirs(path: str) -> Tuple[List, List]:
    """

    :param path:
    :return:
    """
    files = []
    dirs = []

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.path)
            elif entry.is_dir():
                dirs.append(entry.path)
                sub_files, sub_dirs = get_files_and_dirs(entry.path)
                files.extend(sub_files)
                dirs.extend(sub_dirs)

    return files, dirs


def run_js_by_PyExecJS(js_code: str, *args, function_name: Optional[str] = None, **kwargs):  # noqa
    ctx = execjs.compile(js_code)
    result = ctx.call(function_name, *args, **kwargs)
    return result


def run_js_by_py_mini_racer(js_code: str, *args, function_name: Optional[str] = None, **kwargs):
    ctx = py_mini_racer.MiniRacer()
    ctx.eval(js_code)
    result = ctx.call(function_name, *args, **kwargs)
    return result
