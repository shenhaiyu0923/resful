from selenium import webdriver

driver=webdriver.Chrome()

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

#获取所有城市信息
ele = driver.find_element_by_id('forecastID')

dls=ele.find_elements_by_tag_name('dl')
citys=[]
for dl in dls:

    name=dl.find_element_by_tag_name('dt').text
    ltemp=dl.find_element_by_tag_name('b').text
    ltemp=int(ltemp.replace('℃',''))
    print(name,ltemp)
    citys.append((name,ltemp))

lowest=None
lowestCitys=[]
for one in citys:
    curcity = one[0]
    ltemp = one[1]
    #发现气温更低的城市
    if lowest==None or ltemp<lowest:
        lowest=ltemp
        lowestCitys=[curcity]
        #温度和当前最低相同,加入列表
    elif ltemp == lowest:
        lowestCitys.append(curcity)

print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCitys)))

driver.quit()
















