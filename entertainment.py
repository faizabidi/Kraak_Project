import csv
from collections import defaultdict

#delete the last two columns - links and notes
d_category = dict ()
d_company = dict ()
d_fnb = dict ()
d_prod_line = dict ()
d_ethnicity = dict ()

inp = open ("Entertainment.csv","rb")
rdr = csv.reader (inp)

ofile = open ("result.csv","wb")
wtr = csv.writer (ofile)
################################################
lst_category = ['Actress/TV Personality ', 'Actress/Dancer', 'Actress/Model', 'Actor/Comedian', 'Actor/Musician', 'Actor/TV personality', 
'Model/TV personality', 'Actor/Director', 'Musician/Entrepreneur', 'Actress/Musician', 'Actress/Entrepreneur', 'Model/TV Personality', 'Actor', 'Actor ', 'TV personality', 
'Illusionist ', 'TV Personality', 'Musician', 'Fashion Designer', 'Actress ', 'Actress', 'TV Personality ', 'Model ', 'Model']

lst_category_replace = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '13', '15', '16', '17', '18', '19',
 '20', '20', '22', '23', '23']
################################################
lst_company = ['Sauza Tequila Import Company', 'Pabst Brewing Company', 'Absinthe Maninthe', 'Vita Coco', 'Roberto Cavalli', 'Wrigley Company', 
'Skinny Girl Cocktails LLC', 'Coors Brewing Company', "D'usse", 'Dreaming Tree Wines', 'Hershey Foods', 'Milk PEP', 'Bacardi Limited', 'Kraft Foods Group Inc', 
'Ahneuser-Busch InBev', 'Hanson Brothers Beer Company', 'Casamigos Spirits Company', 'PepsiCo', "McDonald's", 'Dr Pepper Snapple Group', 'The Dannon Company', 
'Chateau Miraval', 'Vanilla Puddin Chardonnay', '3G Capital', 'The Wonderful Company', 'Urban Remedy', 'Sunny Delight Beverage Company', 'Agavera Camichines ', 'Pepsico', 
'Danny Devito', 'Borden Milk', 'Popchips, inc.', 'Willlie Nelson ', 'Wat-AAH!', 'Conjure Cognac LLC', 'Danone', 'Post Foods', 'Blue Chair Bay Rum', 'Diageo ', 
'Genesee Pure Food Company', 'Globefill Inc', 'Nestle', 'Dunkin Brands', 'PHA', 'Chicken and Rice Company', 'Sammy Hagar', 'Unilever', 'Mars Inc.', 'American Egg Board', 
'CKE Restaurants', 'Jas Hennessy & Co. ', 'TCCC', 'Davide Campari-Milano ']

lst_company_replace = list ()

for x in range (1, len (lst_company) + 1):
        lst_company_replace.append (str (x))
################################################
lst_fnb = ['Alcohol', 'Sweet', 'Alcohol ', 'Cereal', 'Water', 'QSR', 'Other', 'Dairy', 'Candy', 'Dairy ', 'Fruit and Vegetables', 'LCB', 
'NCB', 'Fruit and Vegetables ', 'Salty', 'SSB']
lst_fnb_replace = list ()
for x in range (1, len (lst_fnb) + 1):
        lst_fnb_replace.append (str (x))
################################################
lst_product_line = ['Skinnygirl', 'FNV', 'Smirnoff', 'Quaker Oats Chewy Granola Bars', 'Roberto Cavalli Vodka', 'Vita Coco', 'Blast Colt 45', 'Milk ', 
'Hennessy', 'Sunny D', 'QREAM', "McDonald's", 'Gatorade', 'Snickers', "D'usse", 'Dreaming Tree Wines', 'Nestle Pure Life', 'Wonderful Pistachios', 
'Activia Yogurt', 'MmmHop', 'Dasani', 'Sprite', 'Popchips', 'Colt 45', 'Eggs', 'Campari', 'Burger King', "Reese's", 'Crystal Head Vodka', 
'Pepsi', 'Diet Coke', '1800 Tequila Silver', "Glaceau's Vitaminwater", 'Urban Remedy', 'Jell-o', 'Smartwater', 'Juicy Fruit ', 'Absinthe Maninthe', 'Doritos', 
'Beach Bar Rum', 'ZICO', 'Danny DeVito Limoncello', 'Sauza 901', 'Dark Roast Coffee', 'Wat-AAH!', "Lay's Potato Chips", 'Conjure Cognac ', 'Blue Chair Bay Rum', 
'Dr Pepper', 'Coca-Cola', 'Whiskey River Bourbon', 'Cabo Wabo Tequila', 'Cocoa Pebbles', 'Drink UP Campaign', "Carl's Jr", 'MiO Energy ', 'Casamigos Tequila', 
'Budweiser', 'Danimals ', 'Aquafina', 'Ciroc', 'Vitaminwater ZERO', 'Miraval Rose', 'Bacardi', 'Diet Pepsi', 'Chicken & Rice', 'Lipton ', 'Vanilla Puddin Chardonnay', 
'NCB', 'Coors Light', 'Milk', 'Mountain Dew']

lst_product_line_replace = list ()
for x in range (1, len (lst_product_line) + 1):
        lst_product_line_replace.append (str (x))
################################################
lst_ethnicity = ['LFE', 'MFE', 'BFE', 'BME', 'AFE', 'AME', 'WFE', 'LME', 'WME']
lst_ethnicity_replace = list ()
for x in range (1, len (lst_ethnicity) + 1):
        lst_ethnicity_replace.append (str (x))
################################################

read_file = inp.read ()

#replace stuff in the CSV file
for items, replacement in zip (lst_category, lst_category_replace):
	read_file = read_file.replace (items, replacement)

for items, replacement in zip (lst_company, lst_company_replace):
	read_file = read_file.replace (items, replacement)

for items, replacement in zip (lst_fnb, lst_fnb_replace):
        read_file = read_file.replace (items, replacement) 

for items, replacement in zip (lst_product_line, lst_product_line_replace):
        read_file = read_file.replace (items, replacement)        

for items, replacement in zip (lst_ethnicity, lst_ethnicity_replace):
        read_file = read_file.replace (items, replacement)



ofile.write (read_file)


"""
        for r in rdr:
        	d_category[r[1]] = r[0:7]
        	d_company[r[2]] = r[0:7]
        	d_fnb[r[3]] = r[0:7]
        	d_prod_line[r[4]] = r[0:7]
        	d_ethnicity[r[5]] = r[0:7]

        	#change category to numeric values
        	if (r[5] == 'LFE'):
        		r[5] = 1
        	elif (r[5] == 'MFE'):
        		r[5] = 2
        	elif (r[5] == 'BFE'):
        		r[5] = 3
        	elif (r[5] == 'BME'):
        		r[5] = 4
        	elif (r[5] == 'AFE'):
        		r[5] = 5
        	elif (r[5] == 'AME'):
        		r[5] = 6
        	elif (r[5] == 'WFE'):
        		r[5] = 7
        	elif (r[5] == 'LME'):
        		r[5] = 8




        	#wtr.writerow( (r[0], r[1], r[2], r[3], r[4], r[5], r[6]) )

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
#print lst_prod_line
print lst_ethnicity

'Category', 'Actress/TV Personality ', 'Actor', 'Actress/Dancer', 'TV personality', 'Illusionist ', 'Actress/Model', 'TV Personality', 'Musician', 'Actor/Comedian', 'Actor/Musician', 'Actor/TV personality', 'Fashion Designer', 'Actor ', 'Model/TV personality', 'Actress ', 'TV Personality ', 'Model', 'Actor/Director', 'Musician/Entrepreneur', 'Actress', 'Actress/Musician', 'Model/TV Personality', 'Model ', 'Actress/Entrepreneur'
"""