import uiautomator2 as u2
import time
#d = u2.connect('feeec6d8')
d = u2.connect('127.0.0.1')
d.session('com.vova.android')


d.set_fastinput_ime(True)
d.click_post_delay = 0.5  # 设置每次单击UI并单击后的延迟0.5s
d.wait_timeout = 30.0  # ＃设置默认元素等待超时（秒）
d(resourceId="com.vova.android:id/search_animation_view").click()
d(resourceId="com.vova.android:id/category_title").click()
d(resourceId="com.vova.android:id/icet_search").send_keys('13121566').send_action('search')#模拟搜索商品
time.sleep(3)
d(resourceId="com.vova.android:id/goodsImg").click()
d(resourceId="com.vova.android:id/layout_goods_detail_bottom").click()#点击加载购物车
d(resourceId="com.vova.android:id/buy_root").click()#点击CHECKOUT

d(resourceId="com.vova.android:id/country_name").click()#点击国家进入搜索国家页
d(resourceId="com.vova.android:id/edit_text").send_keys('china').send_action('search')#搜索中国
d(resourceId="com.vova.android:id/item_country_container").click()#选中中国
d(resourceId="com.vova.android:id/go_back_layout").click()#返回Checkout
d(resourceId="com.vova.android:id/place_order_btn").click()#点击下单

d.xpath('//*[@resource-id="recycler_view"]'
        '/android.view.ViewGroup[1]/android.widget.ImageView[2]').click()#选择信用卡
d(resourceId="com.vova.android:id/normal_buy_btn").click()#点击确认支付
d(resourceId="com.vova.android:id/go_back_layout").click()#点击返回
d(resourceId="com.vova.android:id/tv_dialog_negative").click()#返回按钮确认
d(resourceId="com.vova.android:id/go_back_layout").click()#点击返回
d(resourceId="com.vova.android:id/tv_dialog_negative").click()#返回按钮确认
order1=d(resourceId="com.vova.android:id/order_no_tv").info["text"]

'''
印度支付： UPI----EHFGA5967A      Banking---LCTZP7078E


boleto---CPF：12649239700


'''