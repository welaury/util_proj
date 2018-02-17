from functools import reduce


coef_arr = None
while coef_arr == None:
	try:
		coef_arr = input('Input coefficient: ').split(' ')
		coef_arr = [float(coef) for coef in coef_arr]
	except ValueError:
		print('Uncorrect input, try again')
		coef_arr = None

margin = round(sum(1./y for y in coef_arr) - 1, 4)

coef_whithout_margin = [y/(1-margin) for y in coef_arr]

buk_persent = [round(1/y, 3) for y in coef_whithout_margin]

print('margin: '+str(margin))

print('bookmaker prob.:'+str(buk_persent))


'''
type(coef_arr[0]) - возвращает тип объекта

coef_arr = [float(coef) for coef in coef_arr] - изменяет ячейки списка (можно реализвать через enumerate, с прямым обращением к ячкейке по индексу)

for coef in coef_arr: - тут значение изменяется только внутри цикла, ведь coef это лишь ссылка, ее мы и меняем.	
	coef = float(coef)
'''