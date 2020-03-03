import time
from appium import webdriver


class DouyinAction():
    """自动滑动，并获取抖音短视频发布者的id"""
    def __init__(self, nums:int=None):
        # 初始化配置，设置Desired Capabilities参数
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'SM-G955F',
            'appPackage': 'com.ss.android.ugc.aweme',
            'appActivity': '.main.MainActivity'
        }
        # 指定Appium Server
        self.server = 'http://localhost:4723/wd/hub'
        # 新建一个driver
        self.driver = webdriver.Remote(self.server, self.desired_caps)
		
        # 获取模拟器/手机的分辨率(px)
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        print(width, height)
        # 设置滑动初始坐标和滑动距离
        self.start_x = width//2 # 屏幕宽度中心点
        self.start_y = height//3*2 # 屏幕高度从上开始到下三分之二处
        self.distance = height//2 # 滑动距离：屏幕高度一半的距离
        # 设置滑动次数
        self.nums = nums

    def comments(self):
        # app开启之后点击一次屏幕，确保页面的展示
        time.sleep(2)
        self.driver.tap([(500, 1200)], 500)

    def scroll(self):
    
        print('滑动ing...')
        self.driver.swipe(self.start_x, self.start_y,
                          self.start_x, self.start_y-self.distance)
        time.sleep(3)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]').click()
        time.sleep(3)
        # 无限滑动
        i = 0
        while True:
            # 模拟滑动
            print('滑动ing...')
            self.driver.swipe(self.start_x, self.start_y,
                              self.start_x, self.start_y-self.distance)
            time.sleep(3)
            self.get_infos() # 获取视频发布者的名字
            # 设置延时等待
            time.sleep(4)
            # 判断是否退出
            if self.nums is not None and self.nums == i:
                break
            i += 1

    def get_infos(self):
        
        # 获取视频的各种信息：使用appium desktop定位元素
        print(self.driver.find_element_by_id('ap').text) # 发布者名字
        print(self.driver.find_element_by_id('xm').text) # 点赞数
        print(self.driver.find_element_by_id('xn').text) # 留言数
        print(self.driver.find_element_by_id('oz').text) # 视频名字，可能不存在，报错

        # # 点击【分享】坐标位置 671,1058
        # self.driver.tap([(671, 1058)])
        # time.sleep(2)
        # # 向左滑动露出 【复制链接】 580，1100 --> 200, 1100
        # self.driver.swipe(580,1100, 20, 200, 1100)
        # # self.driver.get_screenshot_as_file('./a.png') # 截图
        # # 点击【复制链接】 距离右边60 距离底边170 720-60，1280-170
        # self.driver.tap([(660, 1110)])
        # # self.driver.get_screenshot_as_file('./b.png')  # 截图

    def main(self):
        self.comments() # 点击一次屏幕，确保页面的展示
        time.sleep(2)
        self.scroll() # 滑动


if __name__ == '__main__':

    action = DouyinAction(nums=5)
    action.main()