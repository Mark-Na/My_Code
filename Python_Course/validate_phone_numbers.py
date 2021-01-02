import re
def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None
print(extract_phone("my number is 432 214-9230"))
print(extract_phone("my number is 432 214-923044"))

def extract_all_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(input)
    return match

print(extract_all_phone("call me at 310 445-9876 or 310 446-9876 "))

def is_valid_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False
print(is_valid_phone("436 483-94732"))
print(is_valid_phone("436 483-9473"))
# check time validity
# import re
# def is_valid_time(input):
#     pattern = re.compile(r'^\d\d?:\d\d$')
#     match = pattern.search(input)
#     if match:
#         return True
#     return False
import re
url_regex = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("http://www.youtube.com/videos/asd/das/asd")
print(match.group())#can put a number ingroup to get a certain portion of the group
print(match.groups())