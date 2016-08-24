inp = raw_input ('Enter file name')
try:
	if len (inp) < 1 : inp = 'AllData_June6.csv'
	file = open (inp)
except:
	print 'File not found'
	exit()

positive = ['Low-cal & no-cal beverage', 'Low cal and no cal beverages', 'Low-cal & no-cal beverages', 'Dairy', 'Dairy ', 'Fruit and Vegetables']
negative = ['Confection or Savory snack or Cereal', 'QSR', 'Confection or Savory Snack or Cereal', 'Cereal', 'SSB', 'Alcohol', 'Alcohol ']
for item in file:
	item = item.strip().split (',')
	#if 
	"""if item[4] in positive:
		item[8] = 'p'
	elif item[4] in negative:
		item[8] = 'n'"""

	print item[8]