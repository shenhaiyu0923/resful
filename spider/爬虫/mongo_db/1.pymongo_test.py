#coding:utf-8
from pymongo import MongoClient


# 创建数据库链接对象
client = MongoClient('192.168.153.137', 27017)

# 选择一个数据库
#db = client['admin']
# 用户密码
#db.authenticate('python','python')

# 选择一个集合
col = client['pydata']['test']


col.insert({"class":"python37"})
col.insert([{"class":"python38"},{"class":"python39"},{"class":"python40"}])
for data in col.find():
    print(data)
# print(col.find_one())
print("*"*50)

# 全文档覆盖更新
# col.update({"class":"python40"},{"message":"helloworld"})
# col.update({},{"$set":{"id":"xxxx-xxxx"}})
# col.update({}, {"$set": {"id": "xxxx-xxxx"}}, multi=True)
# col.update({"message":"hello world"}, {"$set": {"id": "xxxx-xxx2"}}, upsert=True)

# col.delete_one({"message":"helloworld"})
#col.delete_many({"id": "xxxx-xxxx"})

# for data in col.find():
#     print(data)




