kitoblar = {'matematika':{'hajmi':'123'},'fizika':{'hajmi':'32'},'algebra':{'hajmi':'144'},'kimyo':{'hajmi':'57'}}
book =input('istagan kitob nomini kiriting:')
if book in kitoblar:
	word = kitoblar[book]
	print(f"\n{book.title()}ning hajmi {word['hajmi']} varaq")
else:
	print('kechirasiz bu kitob haqida malumot yoq')	