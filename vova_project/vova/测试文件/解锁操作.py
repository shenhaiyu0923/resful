import uiautomator2 as u2
d = u2.connect('feeec6d8')

#  c14ec51e
self.d.screen_on()
self.d.swipe(0.5,0.7,0.5,0.2,0.3)#滑动
#self.d.drag(0.5,0.7,0.5,0.2,2)#拖动

#self.d.session('com.vova.android')
#print(self.d.device_info)
self.d(resourceId="com.vova.android:id/com.androiself.d.systemui:id/vivo_digit_text", text="9").click()
self.d(resourceId="com.vova.android:id/com.androiself.d.systemui:id/vivo_digit_text", text="2").click()
self.d(resourceId="com.vova.android:id/com.androiself.d.systemui:id/vivo_digit_text", text="3").click()
self.d(resourceId="com.vova.android:id/com.androiself.d.systemui:id/vivo_digit_text", text="9").click()
self.d(resourceId="com.vova.android:id/com.androiself.d.systemui:id/vivo_digit_text", text="2").click()
self.d(resourceId="com.vova.android:id/com.androiself.d.systemui:id/vivo_digit_text", text="3").click()
'''

	'udid': 'feeec6d8-3c:a5:81:a7:3c:e5-vivo_X21A',
	'version': '9',
	'serial': 'feeec6d8',
	'brand': 'vivo',
	'model': 'vivo X21A',
	'hwaddr': '3c:a5:81:a7:3c:e5',
	'port': 7912,
	'sdk': 28,
	'agentVersion': '0.8.0',
	'display': {
		'width': 1080,
		'height': 2280
	},
	'battery': {
		'acPowered': False,
		'usbPowered': True,
		'wirelessPowered': False,
		'status': 2,
		'health': 2,
		'present': True,
		'level': 96,
		'scale': 100,
		'voltage': 4379,
		'temperature': 310,
		'technology': 'Li-ion'
	},
	'memory': {
		'total': 5839880,
		'around': '6 GB'
	},
	'cpu': {
		'cores': 8,
		'hardware': 'Qualcomm Technologies, Inc SDM660'
	},
	'arch': '',
	'owner': None,
	'presenceChangedAt': '0001-01-01T00:00:00Z',
	'usingBeganAt': '0001-01-01T00:00:00Z',
	'product': None,
	'provider': None

'''