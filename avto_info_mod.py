def avto_info(kompaniya,model,rangi,korobka,yili,narhi = None):
	avto = {'kompaniya':kompaniya,
			'model':model,
			'rangi':rangi,
			'korobka':korobka,
			'yili':yili,
			'narhi':narhi}
	return avto

def avto_kirit():
	"""Foydalanuvchiga avto_info yordamida bir nechta avtolar haqida malumotlarni bitta ruyxatga joylash ,
	imkonini beruvchi funksiya"""
	avtolar  = []
	while True:
		print("\n Quidagi malumotlarni kiriting: end = '' ")
		kompaniya = input('ishlab chiqaruvchi>>>')
		model = input('Modeli>>>')
		rangi = input('Rangi>>>')
		yili = int(input('ishlab chiqarilgan yili>>>'))
		narhi = int(input('salondagi narhi>>>'))
		avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi = None))
		javob = input('yana avto qo`shasizmi? (yes/no):')
		if javob=='no':
			break
		return avtolar

def avto_print(avto_info):
	print(f"{avto_info['rangi'].title()} {avto_info['model'].upper()},"
		  f"{avto_info['kompaniya'].upper()} da ishlab chiqarilgan,  "
		  f"{avto_info['korobka']} korobka, {avto_info['yili']} - yil ishlab chiqarilgan,"
		  f"{avto_info['narhi']}$")

