## web接口

请求方式

请求路径

请求参数

返回结果

登录接口

请求方式：GET

请求路径：login/?username=python

请求参数：username

返回结果：{'message':'ok'} json



获取单一图书数据接口

请求方式：GET

请求路径：books/1/

请求参数：id

返回结果：{'btitle':西游记'} json



## 图书数据增删改查

查询单一图书

请求方式：GET

请求路径：books/1/

请求参数：id

返回结果：{ id,'btitle',''bread','pub_date'} json



查询所有图书

请求方式：GET

请求路径：books/

请求参数：

返回结果：json

[{},{},{}]





保存图书

请求方式：POST

请求路径：books/

请求参数：btitle(必须) bpub_date(必须) bread(可选) bcomment(可选)  json

返回结果：{ id,'btitle',''bread','pub_date'} json



更新图书

请求方式：PUT

请求路径：books/1/

请求参数：btitle bpub_date bread bcomment json  id 路径

返回结果：{ id,'btitle',''bread','pub_date'} json





删除图书

请求方式：DELETE

请求路径：books/1/

请求参数：id

返回结果：{} 



### 序列化过程

将获取到的数据对象转化为json返回前端

获取后端数据库中的数据对象 —> json 返回前端

### 反序列化

将前端传的数据转化为数据对象

接受前端—>验证数据—>保存或更新为新的数据对象



.md

Markdown



# asdasd

## asdasd

### asdas

``` python
def a_print(*args):
  print(111)
  return 111
```

``` html
<a href=> </a>
```





* asdasd
* asdasd
* asdadsa
  * asdasda
    * asdasd
      * asdasd





1. asdasd
2. asdasd
   1. asdasd





**asdasd**

















