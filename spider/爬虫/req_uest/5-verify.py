import logging
import requests

logging.captureWarnings(True)# 忽略警告

url = "https://sam.huat.edu.cn:8443/"


response = requests.get(url,verify=False)

print(response.text)

