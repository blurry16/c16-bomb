# This file contains every phone format, that is needed to run the bomber.

# +7(953)-531-58-53
def format_dash(phone_number):
    phone_number = phone_number.replace("+", "").replace(" ", "").replace("-", "")
    if phone_number.startswith("("):
        phone_number = phone_number[1:]
    phone_number = ("+" + phone_number[:1] + "(" + phone_number[1:4] + ")" + "-" + phone_number[4:7] + "-" +
                    phone_number[7:9] + "-" + phone_number[9:11])
    return str(phone_number)


# +7 (953) 531 58 53
def format_spaces(phone_number):
    phone_number = phone_number.replace("+", "").replace(" ", "").replace("-", "")
    if phone_number.startswith("("):
        phone_number = phone_number[1:]
    phone_number = ("+" + phone_number[:1] + " (" + phone_number[1:4] + ")" + " " + phone_number[4:7] + " " +
                    phone_number[7:9] + " " + phone_number[9:11])
    return str(phone_number)


# 79535315853
def format_plus(phone_number):
    return phone_number[1:12]


# 89535315853
def format_plus_8(phone_number):
    phone_number = phone_number[1:12]
    num = list(phone_number)
    num[0] = "8"
    num = "".join(num)
    return str(num)

