import base64
# url = "https://www.cnblogs.com/songzhixue/"
# bytes_url = url.encode("utf-8")
# str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
# print(str_url)
from pprint import pprint
import json
url="eyJzY2hlbWEiOiJpZ2x1OmNvbS5zbm93cGxvd2FuYWx5dGljcy5zbm93cGxvd1wvY29udGV4dHNcL2pzb25zY2hlbWFcLzEtMC0xIiwiZGF0YSI6W3sic2NoZW1hIjoiaWdsdTpjb20uYXJ0ZW1pc1wvY29tbW9uXC9qc29uc2NoZW1hXC8xLTAtMSIsImRhdGEiOnsiZ2VuZGVyIjoibWFsZSIsImNvdW50cnkiOiJGUiIsInVzZXJfdW5pcXVlX2lkIjoiMTY4MDQwMjYiLCJsYW5ndWFnZSI6ImVuIiwiYWNjb3VudF9jbGFzcyI6ImZvcm1hbCIsImN1cnJlbmN5IjoiRVVSIiwicGFnZV9jb2RlIjoiY2FydCJ9fSx7InNjaGVtYSI6ImlnbHU6Y29tLmFydGVtaXNcL2FwcF9jb21tb25cL2pzb25zY2hlbWFcLzEtMC0xIiwiZGF0YSI6eyJtZWRpYV9zb3VyY2UiOiIiLCJpbXNpIjoiIiwibGFuZGluZ19wYWdlIjoiIiwiYXBwX3ZlcnNpb24iOiIxLjEwLjAiLCJkZXZpY2VfaWQiOiIxMUE5QjVCNS1CQTJGLTQxNkItQTk1My01Mjc0QUI1QjMwQzEiLCJ2cG4iOiIwIiwic3lzY291bnRyeSI6IlVTIiwidGltZXpvbmVkaXNwbGF5IjoiR01UKzgiLCJ1cmkiOiJcL2NhcnRcLz9nb29kc19udW1iZXI9MSZzaG93VHlwZT1zaG93JnNrdV9udW1iZXI9MSZza3VfYW1vdW50PTQuMzMiLCJpc190YWJsZXQiOiIiLCJzeXNsYW5nIjoiZW4iLCJhbmRyb2lkX2lkIjoiIiwicmVmZXJyZXIiOiJcL3Byb2R1Y3RfZGV0YWlsXC8_Z29vZHNfaWQ9MjM3NjYyOCZwcmVwYWdlPTAmZnJlZWJpZV9kZXRhaWw9MSZ2ZXJzaW9uPW5ldyIsImVtYWlsIjoiMjJAdGV0eC5jb20iLCJyb290IjoiMCIsImlkZnYiOiIxMUE5QjVCNS1CQTJGLTQxNkItQTk1My01Mjc0QUI1QjMwQzEiLCJhZHZlcnRpc2luZ19pZCI6IiIsInN0YXJ0dXBfaWQiOiIxNTc5MjMwOTY2ODA5IiwidGVzdF9pbmZvIjoiIiwibGF0bG5nIjoiIiwib3JnYW5pY19pZGZ2IjoiQTM5NDc4RjItMUY5QS00MzZDLUJBMDgtRUZBQjk2QzY1OTU3IiwiaWRmYSI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCJ9fSx7InNjaGVtYSI6ImlnbHU6Y29tLnNub3dwbG93YW5hbHl0aWNzLnNub3dwbG93XC9tb2JpbGVfY29udGV4dFwvanNvbnNjaGVtYVwvMS0wLTEiLCJkYXRhIjp7Im9zVHlwZSI6ImlvcyIsImFwcGxlSWRmYSI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCIsIm9zVmVyc2lvbiI6IjEzLjMiLCJhcHBsZUlkZnYiOiJBMzk0NzhGMi0xRjlBLTQzNkMtQkEwOC1FRkFCOTZDNjU5NTciLCJkZXZpY2VNYW51ZmFjdHVyZXIiOiJBcHBsZSBJbmMuIiwibmV0d29ya1R5cGUiOiJ3aWZpIiwiZGV2aWNlTW9kZWwiOiJpUGhvbmUifX0seyJzY2hlbWEiOiJpZ2x1OmNvbS5zbm93cGxvd2FuYWx5dGljcy5zbm93cGxvd1wvY2xpZW50X3Nlc3Npb25cL2pzb25zY2hlbWFcLzEtMC0xIiwiZGF0YSI6eyJwcmV2aW91c1Nlc3Npb25JZCI6IjhkMmFjMTlmLTgzZjYtNGE2OS1iMTI3LTE2NDQ0ZDA3NmU3ZCIsImZpcnN0RXZlbnRJZCI6IjcxNmE0ZjkyLTNjN2EtNDFhMi05MTMxLTEwZjEzZmU4ZThjNSIsInNlc3Npb25JZCI6ImFmOWMzZGYzLWMxNjktNGNiNy1iNzdmLTBjZjE0NTY4Nzk3MCIsInVzZXJJZCI6IjVkNGM0ZjJkLWQ4ZjktNGU5Yi04ZWNhLWJiNWFiN2Y1MDRhYiIsInNlc3Npb25JbmRleCI6MjQ2LCJzdG9yYWdlTWVjaGFuaXNtIjoiU1FMSVRFIn19XX0="
url=url.replace('_',"/").replace('.','+')
str_url = base64.b64decode(url).decode("utf-8")
str_url = str_url.replace("\\","")
str_url_dic=json.loads(str_url)#将字符串转换成字典
js = json.dumps(str_url_dic, sort_keys=True, indent=4, separators=(',', ':'))#将字典
print(js)
print("=================================================")

str = '{"key": "wwww", "word": "qqqq"}'
j = json.loads(str)
print(type(j))
pprint(j)
print("=================================================")

dic = {"a": "1", 'b': 2, 'c': 3}
print(type(dic))
js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
a=json.loads(js)
print(type(a))
print(type(js))
print(js)