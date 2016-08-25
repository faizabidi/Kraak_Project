#!/usr/bin/python

inp = raw_input ('Enter a file')
try:
	if len (inp) < 1 : inp = 'ALLDATA_08202016.csv'
	file = open (inp)
except:
	print 'File not found'
	exit()

plst = list()
nlst = list()
lst = list()
count = dict()
meals = list()
ssb = list()

for items in file:
	items = items.rstrip().split (',')
	if items[4] == 'Meals':
		#print items[1]
		meals.append(items[1])
	
	if items[4] == 'SSB':
		ssb.append(items[1])
	#print items[4]
	items[4] = items[4].strip()
	lst.append(items[4])
	#if items[5] not in lsit:
	#	print items[5]
#print lst
mymeals = set(meals)
myssb = set(ssb)

print(len(mymeals))
print(len(myssb))
#Enter a fileKeys Alicia
#for items in myset:
#	print items

for i in lst:
	count[i] = count.get(i, 0) + 1

#for key,value in count:
#	print key,value
print count
#print("\n"myset
"""	if items[9] == 'p':
		plst.append (items[4])
	elif items[9] == 'n':
		nlst.append (items[4])

uniquePList = list (set (plst))
uniqueNList = list (set (nlst))
print uniquePList
print uniqueNList"""
