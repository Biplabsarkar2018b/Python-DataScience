import requests
session = requests.Session()

response = requests.get('http://leetcode.com')

# print(session.cookies.get_dict())
print(response.cookies)