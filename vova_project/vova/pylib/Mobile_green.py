from cfg import *


class CardGreen():

    def green_first(self,goods_id,country):#用例一;信用卡订单
        d.set_fastinput_ime(True)
        d.click_post_delay = 0.7  #设置每次单击UI并单击后的延迟0.5s
        d.wait_timeout = 10.0     #＃设置默认元素等待超时（秒）
        d(resourceId="com.vova.android:id/search_animation_view").click()
        d(resourceId="com.vova.android:id/category_title").click()
        d(resourceId="com.vova.android:id/icet_search").send_keys(goods_id)
        d.send_action('search')  # 模拟搜索商品
        time.sleep(3)
        d(resourceId="com.vova.android:id/goodsImg").click()
        d(resourceId="com.vova.android:id/layout_goods_detail_bottom").click()  # 点击加载购物车
        d(resourceId="com.vova.android:id/buy_root").click()  # 点击CHECKOUT

        d(resourceId="com.vova.android:id/country_name").click()  # 点击国家进入搜索国家页
        d(resourceId="com.vova.android:id/edit_text").send_keys(country)
        d.send_action('search')  # 搜索中国
        d(resourceId="com.vova.android:id/item_country_container").click()  # 选中中国
        d(resourceId="com.vova.android:id/go_back_layout").click()  # 返回Checkout
        d(resourceId="com.vova.android:id/place_order_btn").click()  # 点击下单
        d.xpath('//*[@resource-id="com.vova.android:id/recycler_view"]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.ImageView[2]').click()# 选择信用卡
        #d.long_click(0.488, 0.895)#点击确认支付
        #d(className="android.widget.Button").click()#点击确认支付
        #d(text="Confirm to Pay").click() # 点击确认支付
        d(resourceId="com.vova.android:id/normal_buy_btn").click()  # 点击确认支付
        d(resourceId="com.vova.android:id/pay_btn").long_click()#长按缓冲
        cardtitle = d(resourceId="com.vova.android:id/title_text").info["text"]
        print(cardtitle)
        if cardtitle=="Add a Card":
            d.press("back") # 点击返回
            d(resourceId="com.vova.android:id/tv_dialog_negative").click()  # 返回按钮确认
            d.press("back") # 点击返回
            d(resourceId="com.vova.android:id/tv_dialog_negative").click()  # 返回按钮确认
            order1 = d(resourceId="com.vova.android:id/order_no_tv").info["text"]
            d.press("back")
            d.press("back")# 点击返回  ,手机按键
            d.press("back")
            d.press("back")
            d.press("back")
            d(resourceId="com.vova.android:id/account_animation_view").click()  # 点击me
            return order1
        else:
            d.session(vova_android)


    def green_second(self,goods_id,country):#用例二;信用卡订单
        d.set_fastinput_ime(True)
        d.click_post_delay = 0.7  #设置每次单击UI并单击后的延迟0.5s
        d.wait_timeout = 10.0     #＃设置默认元素等待超时（秒）
        d(resourceId="com.vova.android:id/search_animation_view").click()#点击底部search
        d(resourceId="com.vova.android:id/category_title").click()
        d(resourceId="com.vova.android:id/icet_search").send_keys(goods_id)
        d.send_action('search')  # 模拟搜索商品
        time.sleep(3)
        d(resourceId="com.vova.android:id/goodsImg").click()#点击商品列表中商品图片
        d(resourceId="com.vova.android:id/layout_goods_detail_bottom").click()  # 点击add to bag
        d(resourceId="com.vova.android:id/element_item_textview", text="EU Plug").click()#选中尺寸
        d(resourceId="com.vova.android:id/add2cart_confirm_btn").click()#点击add to bag跳转到购物车
        d(resourceId="com.vova.android:id/buy_root").click()  # 点击CHECKOUT

        d(resourceId="com.vova.android:id/country_name").click()  # 点击国家进入搜索国家页
        d(resourceId="com.vova.android:id/edit_text").send_keys(country)
        d.send_action('search')  # 搜索中国
        d(resourceId="com.vova.android:id/item_country_container").click()  # 选中中国
        d(resourceId="com.vova.android:id/go_back_layout").click()  # 返回Checkout
        d(resourceId="com.vova.android:id/place_order_btn").click()  # 点击下单

        d.xpath('//*[@resource-id="com.vova.android:id/recycler_view"]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.ImageView[2]').click()# 选择信用卡
        d(resourceId="com.vova.android:id/normal_buy_btn").click()  # 点击确认支付
        d(resourceId="com.vova.android:id/pay_btn").long_click()#长按缓冲
        cardtitle = d(resourceId="com.vova.android:id/title_text").info["text"]
        print(cardtitle)
        if cardtitle=="Add a Card":
            d.press("back") # 点击返回
            d(resourceId="com.vova.android:id/tv_dialog_negative").click()  # 返回按钮确认
            d.press("back") # 点击返回
            d(resourceId="com.vova.android:id/tv_dialog_negative").click()  # 返回按钮确认
            order1 = d(resourceId="com.vova.android:id/order_no_tv").info["text"]
            d.press("back")
            d.press("back")# 点击返回  ,手机按键
            d.press("back")
            d.press("back")
            d.press("back")
            d(resourceId="com.vova.android:id/account_animation_view").click()  # 点击me
            return order1
        else:
            d.session(vova_android)




    def green_third(self,goods_id,country):#用例二;信用卡订单
        d.set_fastinput_ime(True)
        d.click_post_delay = 0.7  #设置每次单击UI并单击后的延迟0.5s
        d.wait_timeout = 10.0     #＃设置默认元素等待超时（秒）
        d(resourceId="com.vova.android:id/search_animation_view").click()#点击底部search
        d(resourceId="com.vova.android:id/category_title").click()
        d(resourceId="com.vova.android:id/icet_search").send_keys(goods_id)
        d.send_action('search')  # 模拟搜索商品
        time.sleep(3)
        d(resourceId="com.vova.android:id/goodsImg").click()#点击商品列表中商品图片
        d(resourceId="com.vova.android:id/layout_goods_detail_bottom").click()  # 点击add to bag

        d(resourceId="com.vova.android:id/element_item_textview", text="Coffee").click()#选择颜色
        d(resourceId="com.vova.android:id/element_item_textview", text="36").click()#选中尺寸
        d(resourceId="com.vova.android:id/add2cart_confirm_btn").click()#点击add to bag跳转到购物车
        d(resourceId="com.vova.android:id/buy_root").click()  # 点击CHECKOUT

        d(resourceId="com.vova.android:id/country_name").click()  # 点击国家进入搜索国家页
        d(resourceId="com.vova.android:id/edit_text").send_keys(country)
        d.send_action('search')  # 搜索中国
        d(resourceId="com.vova.android:id/item_country_container").click()  # 选中中国
        d(resourceId="com.vova.android:id/go_back_layout").click()  # 返回Checkout
        d(resourceId="com.vova.android:id/place_order_btn").click()  # 点击下单

        d.xpath('//*[@resource-id="com.vova.android:id/recycler_view"]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.ImageView[2]').click()# 选择信用卡
        d(resourceId="com.vova.android:id/normal_buy_btn").click()  # 点击确认支付
        d(resourceId="com.vova.android:id/pay_btn").long_click()#长按缓冲
        cardtitle = d(resourceId="com.vova.android:id/title_text").info["text"]
        print(cardtitle)
        if cardtitle=="Add a Card":
            d.press("back") # 点击返回
            d(resourceId="com.vova.android:id/tv_dialog_negative").click()  # 返回按钮确认
            d.press("back") # 点击返回
            d(resourceId="com.vova.android:id/tv_dialog_negative").click()  # 返回按钮确认
            order1 = d(resourceId="com.vova.android:id/order_no_tv").info["text"]
            d.press("back")
            d.press("back")# 点击返回  ,手机按键
            d.press("back")
            d.press("back")
            d.press("back")
            d(resourceId="com.vova.android:id/account_animation_view").click()  # 点击me
            return order1
        else:
            d.session(vova_android)




    def green_third_b(self,goods_id,country,CPF):#用例二;信用卡订单
        d.set_fastinput_ime(True)
        d.click_post_delay = 0.7  #设置每次单击UI并单击后的延迟0.5s
        d.wait_timeout = 10.0     #＃设置默认元素等待超时（秒）
        d(resourceId="com.vova.android:id/search_animation_view").click()#点击底部search
        d(resourceId="com.vova.android:id/category_title").click()
        d(resourceId="com.vova.android:id/icet_search").send_keys(goods_id)
        d.send_action('search')  # 模拟搜索商品
        time.sleep(3)
        d(resourceId="com.vova.android:id/goodsImg").click()#点击商品列表中商品图片
        d(resourceId="com.vova.android:id/layout_goods_detail_bottom").click()  # 点击add to bag

        d(resourceId="com.vova.android:id/element_item_textview", text="Coffee").click()#选择颜色
        d(resourceId="com.vova.android:id/element_item_textview", text="36").click()#选中尺寸
        d(resourceId="com.vova.android:id/add2cart_confirm_btn").click()#点击add to bag跳转到购物车
        d(resourceId="com.vova.android:id/buy_root").click()  # 点击CHECKOUT

        d(resourceId="com.vova.android:id/country_name").click()  # 点击国家进入搜索国家页
        d(resourceId="com.vova.android:id/edit_text").send_keys(country)
        d.send_action('search')  # 搜索巴西
        d(resourceId="com.vova.android:id/item_country_container").click()  # 选中巴西  (默认自动选择巴西货币)
        d(resourceId="com.vova.android:id/go_back_layout").click()  # 返回Checkout
        d(resourceId="com.vova.android:id/place_order_btn").click()  # 点击下单

        d.xpath(
            '//*[@resource-id="com.vova.android:id/recycler_view"]/android.view.ViewGroup[2]/android.widget.ImageView[3]').click()#选择Boleto支付
        CPF_id=d(resourceId="com.vova.android:id/tax_edit_text").info["text"]
        if CPF_id is None:
            d(resourceId="com.vova.android:id/tax_edit_text").send_keys(CPF)
        d(resourceId="com.vova.android:id/normal_buy_btn").click()  # 点击确认支付

        d(resourceId="com.vova.android:id/iv_boleto_success_tip").long_click()#长按缓冲
        suc = d(resourceId="com.vova.android:id/tv_boleto_pay_success_desc").info["text"]
        print(suc)
        d(resourceId="com.vova.android:id/iv_boleto_go_back").long_click()# 点击返回
        d(resourceId="com.vova.android:id/search_animation_view").click()#点击search进行缓冲
        d(resourceId="com.vova.android:id/account_animation_view").long_click()#返回me页面
        return suc



    def green_fourth(self,goods_id,country):#用例二;信用卡订单
        d.set_fastinput_ime(True)
        d.click_post_delay = 0.7  #设置每次单击UI并单击后的延迟0.5s
        d.wait_timeout = 30.0     #＃设置默认元素等待超时（秒）
        d(resourceId="com.vova.android:id/search_animation_view").click()#点击底部search
        d(resourceId="com.vova.android:id/category_title").click()
        d(resourceId="com.vova.android:id/icet_search").send_keys(goods_id)
        d.send_action('search')  # 模拟搜索商品
        time.sleep(3)
        d(resourceId="com.vova.android:id/goodsImg").click()#点击商品列表中商品图片
        d(resourceId="com.vova.android:id/layout_goods_detail_bottom").click()  # 点击add to bag

        d(resourceId="com.vova.android:id/element_item_textview", text="Coffee").click()#选择颜色
        d(resourceId="com.vova.android:id/element_item_textview", text="36").click()#选中尺寸
        d(resourceId="com.vova.android:id/add2cart_confirm_btn").click()#点击add to bag跳转到购物车
        d(resourceId="com.vova.android:id/buy_root").click()  # 点击CHECKOUT

        d(resourceId="com.vova.android:id/country_name").click()  # 点击国家进入搜索国家页
        d(resourceId="com.vova.android:id/edit_text").send_keys(country)
        d.send_action('search')  # 搜索波兰
        d(resourceId="com.vova.android:id/item_country_container").click()  # 选中波兰  (默认自动选择波兰货币)
        d(resourceId="com.vova.android:id/go_back_layout").click()  # 返回Checkout

        d(resourceId="com.vova.android:id/place_order_btn").click()  # 点击下单place order
        d.xpath(
            '//*[@resource-id="com.vova.android:id/recycler_view"]/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.ImageView[2]').click()#选择dotpay支付
        d(resourceId="com.vova.android:id/normal_buy_btn").click()  # 点击确认支付
        title1=d(text="Select payment channel").info["text"]
        print(title1)
        if title1=="Select payment channel":
            d(text="Select payment channel").long_click()#点击title缓冲
            d.press("back")#支付列表返回
            title2=d(resourceId="com.vova.android:id/title_text").info["text"]
            if title2=="Order Details":
                d(resourceId="com.vova.android:id/go_back_layout").click()#order页面返回
        d(resourceId="com.vova.android:id/search_animation_view").click()#点击search进行缓冲
        d(resourceId="com.vova.android:id/account_animation_view").long_click()#返回me页面


CardGreen = CardGreen()


