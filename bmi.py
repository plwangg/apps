height = input ('溥請輸入身高(cm)')
weight = input ('請輸入溥體重(kg)')
height = float (height)
weight = float (weight)
h = height / 100
print('身高', height, '體重', weight)
bmi = weight / (h ** 2)
print ('溥的BMI為', bmi)
if bmi < 18.5:
	print('體重太輕囉!!')
elif 18.5 < bmi < 24:
	print('很正常，繼續保持')
else:
	print('妳超肥!減肥吧胖子')