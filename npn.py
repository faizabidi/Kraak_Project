inp = raw_input ('Enter a file')
try:
	if len (inp) < 1 : inp = 'Database/ALLDATA_08202016.csv'
	file = open (inp)
except:
	print 'File not found'
	exit()

plst = list()
nlst = list()
lst = list()

for items in file:
	items = items.rstrip().split (',')
	#print items[4]
	items[4] = items[4].strip()
	lst.append (items[4])
	#if items[5] not in lsit:
	#	print items[5]
#print lst
myset = set(lst)

for items in myset:
	print items

#print("\n"myset
"""	if items[9] == 'p':
		plst.append (items[4])
	elif items[9] == 'n':
		nlst.append (items[4])

uniquePList = list (set (plst))
uniqueNList = list (set (nlst))
print uniquePList
print uniqueNList"""
