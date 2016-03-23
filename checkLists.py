import csv

inp = open ("Entertainment.csv","rb")
rdr = csv.reader (inp)

d_category = dict ()
d_company = dict ()
d_fnb = dict ()
d_prod_line = dict ()
d_ethnicity = dict ()


lst_category = list ()
lst_company = list ()
lst_fnb = list ()
lst_prod_line = list ()
lst_ethnicity = list ()

for r in rdr:
	#print r
	d_category[r[1]] = r[0:7]
	d_company[r[2]] = r[0:7]
	d_fnb[r[3]] = r[0:7]
	d_prod_line[r[4]] = r[0:7]
	d_ethnicity[r[5]] = r[0:7]

for keys, values in d_category.items ():
	lst_category.append (keys)

for keys, values in d_company.items ():
	lst_company.append (keys)

for keys, values in d_fnb.items ():
	lst_fnb.append (keys)

for keys, values in d_prod_line.items ():
	lst_prod_line.append (keys)

for keys, values in d_ethnicity.items ():
	lst_ethnicity.append (keys)

#print lst_category
#print lst_company
#print lst_fnb
print lst_prod_line
#print lst_ethnicity