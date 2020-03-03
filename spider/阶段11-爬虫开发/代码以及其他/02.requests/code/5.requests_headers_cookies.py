#coding:utf-8
import requests

url = 'https://github.com/exile-morganna'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Cookie': '_ga=GA1.2.1190047373.1543731773; _octo=GH1.1.1199554731.1543731773; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; user_session=IsN0sqpV56zDyNOGBoUWHPRtiIe25zQ0y2cUCmBw0ubT7Zta; __Host-user_session_same_site=IsN0sqpV56zDyNOGBoUWHPRtiIe25zQ0y2cUCmBw0ubT7Zta; logged_in=yes; dotcom_user=exile-morganna; _gh_sess=T0NFUGJlZm5tQmJNQW8rdjhZUUVySm1adnF2TkNNZkpKdW9ZQWlIZFhhZ2QxaEhmWFJNMWZ1enIxWFZOQ2tzbjUxMG1keUtteXoyUWdUVndBRjAyS2cyUGs2RFhnSjJCQk1Ia2ZkNlJIK0ZoRWhQY1VsOG1TcTRQTXJJaVdIQW14OFZid1Ixbnd5NllIMjBMUmpRdndNM0V6VWRKd05vVjNrRXY4blQxNVVsdkE1dlhnMUFWcjhiOVhObGFxZ0lLLS15TzB6Rmg4Q0wxTktOTnVJU1lMdmlBPT0%3D--778a38d546dee1db9e70f8a7f12c7f46ee6878b9'
}

response = requests.get(url, headers=headers)

print(response.url)
with open('github_with_cookies.html', 'wb')as f:
    f.write(response.content)