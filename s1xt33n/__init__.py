__version__ = "beta1.0.0"

import os
from pathlib import Path

if __name__ == "__main__":
    APIS_PATH = os.path.join(Path(os.getcwd()).parent, "apis.json")
else:
    APIS_PATH = "apis.json"

import json

import requests
from faker import Faker
from bs4 import BeautifulSoup

logo = """ 
  ▄████▄       ██████  ██▓▒██   ██▒▄▄▄█████▓▓█████ ▓█████  ███▄    █ 
 ▒██▀ ▀█     ▒██    ▒ ▓██▒▒▒ █ █ ▒░▓  ██▒ ▓▒▓█   ▀ ▓█   ▀  ██ ▀█   █ 
 ▒▓█    ▄    ░ ▓██▄   ▒██▒░░  █   ░▒ ▓██░ ▒░▒███   ▒███   ▓██  ▀█ ██▒
 ▒▓▓▄ ▄██▒     ▒   ██▒░██░ ░ █ █ ▒ ░ ▓██▓ ░ ▒▓█  ▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
 ▒ ▓███▀ ░   ▒██████▒▒░██░▒██▒ ▒██▒  ▒██▒ ░ ░▒████▒░▒████▒▒██░   ▓██░
 ░ ░▒ ▒  ░   ▒ ▒▓▒ ▒ ░░▓  ▒▒ ░ ░▓ ░  ▒ ░░   ░░ ▒░ ░░░ ▒░ ░░ ▒░   ▒ ▒ 
   ░  ▒      ░ ░▒  ░ ░ ▒ ░░░   ░▒ ░    ░     ░ ░  ░ ░ ░  ░░ ░░   ░ ▒░
 ░           ░  ░  ░   ▒ ░ ░    ░    ░         ░      ░      ░   ░ ░ 
 ░ ░               ░   ░   ░    ░              ░  ░   ░  ░         ░ 
 ░                                                                   
"""


class PhoneNumber:
    """PhoneNumber class generates every phone number format that would be needed.
    **num input format: +79000000000**"""
    replaceable_chars = [" ", "-", "(", ")"]

    def __init__(self, num: str):
        # Protection from stupidity
        for char in self.replaceable_chars:
            num = num.replace(char, "")  # O(len(replaceable_chars))
        # num = num.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        if len(num) != 12:
            raise Exception(
                f"Invalid phone number format! (too {'few' if len(num) < 12 else 'many'} characters, is {len(num)}, must be 12)")
        if num[0] != "+":
            raise Exception(f"Invalid phone number format! (the phone number must start with +)")

        self.a = num  # +79535315853
        self.b = num[1:12]  # 79535315853
        self.c = f"8{num[2:12]}"  # 89535315853
        self.d = f"{num[:2]}({num[2:5]})-{num[5:8]}-{num[8:10]}-{num[10:12]}"  # +7(953)-531-58-53
        self.e = f"{num[:2]} ({num[2:5]}) {num[5:8]} {num[8:10]} {num[10:12]}"  # +7 (953) 531 58 53
        self.f = f"{num[:2]} {num[2:5]} {num[5:8]} {num[8:12]}"  # +7 953 531 5853
        self.g = f"{num[:2]} {num[2:5]} {num[5:8]}-{num[8:10]}-{num[10:12]}"  # +7 953 531-58-53

        self.dict = {
            "default": self.a,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "d": self.d,
            "e": self.e,
            "f": self.f,
            "g": self.g,
        }


class SpamAPI:
    """SpamAPI class contains everything required to post a spam attack request."""

    def __init__(self, phone_num: PhoneNumber, url: str, phone_key: str, format_type: str, data: dict, headers: dict,
                 proxy: dict) -> None:
        self.phone = phone_num
        self.url = url
        self.phone_key = phone_key
        self.format_type = format_type
        self.data = data
        self.data[self.phone_key] = self.phone.dict[self.format_type]
        self.headers = headers
        self.proxy = proxy

    def post(self) -> requests.Response:
        """post the spam attack request."""
        return requests.post(url=self.url, headers=self.headers, data=self.data, proxies=self.proxy)


class JsonFile:
    """JsonFile class contains required methods to work with .json files"""

    def __init__(self, file_path: Path | str) -> None:
        self.file_path: Path = Path(file_path)

    def load(self) -> dict | list:
        """loads data from the file.

        Returns:
            dict | list: _JSONable_
        """
        with open(self.file_path, "r", encoding="UTF-8") as data_file:
            return json.load(data_file)

    def dump(self, data: dict | list, indent: int = 2) -> None:
        """saves (dumps) data into file.

        Args:
            data (dict | list): _JSONable_
            indent (int, optional): _indent for the whole file_. defaults to 2.
        """
        with open(self.file_path, "w", encoding="UTF-8") as data_file:
            json.dump(data, data_file, indent=indent)

    def dumps(self, key: str | int | None = None, indent: int = 2) -> str:
        """loads data from the file and returns it as string.

        Args:
            key (str | int | None, optional): _Simply file[key]; if key is None, the string of the whole file will be returned_. defaults to None.
            indent (int, optional): _indent of the JSON string_. defaults to 2.

        Returns:
            str: _json string_
        """
        _data = self.load()
        return json.dumps(_data, indent=indent) if key is None else json.dumps(_data[key], indent=indent)


PROXIES_URL = "https://free-proxy-list.net/"


def getproxies() -> [str]:
    headers = {"User-Agent": faker.user_agent()}
    response = requests.get(PROXIES_URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select("table tr")

    proxies = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) > 1:
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            # country = cols[3].text.strip()
            countrycode = cols[2].text.strip()
            if countrycode == "RU":
                proxies.append(f"{ip}:{port}")
    return proxies


apisfile = JsonFile(APIS_PATH)

faker = Faker(locale="ru")
