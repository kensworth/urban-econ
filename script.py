#Copyright(c) 2016 Kenneth Zhang
import csv

employSum = 0
employTotal = 0
employArray = []
wageArray = []
count = 0

with open('map_economic_2013_emp_20160303030411.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Employment 2013']:	
			employArray.append(float(row['Employment 2013']))
			count += 1

with open('map_economic_2013_private_wage_20160303030504.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                if row['Annual Wage 2013']:
                        wageArray.append(float(row['Annual Wage 2013']))

for i in range (0,179):
	wageArray[i] = wageArray[i] * employArray[i]


employArray.sort(reverse=True)

for value in employArray:
	employTotal += value

for i in range(0,4):
	employSum += employArray[i]

cr4 = employSum / employTotal
print 'CR4: ' + str(cr4)

HHI = 0

for value in employArray:
	share = (value / employTotal) 
	HHI += share ** 2

print 'HHI = ' + str(HHI)

employArray.sort()
fraction = 1 / float(count)

increasingTotal = 0
rectTotal = 0

for value in employArray:
	increasingTotal += value
	rectTotal += fraction * (increasingTotal / employTotal)	

gini = (0.5 - rectTotal) / 0.5

print 'Gini: ' + str(gini)
print '------------------------------------'

wageSum = 0
wageTotal = 0

wageArray.sort(reverse=True)

for value in wageArray:
        wageTotal += value

for i in range(0,4):
        wageSum += wageArray[i]

cr4 = wageSum / wageTotal
print 'CR4: ' + str(cr4)

HHI = 0

for value in wageArray:
        share = (value / wageTotal) 
        HHI += share ** 2

print 'HHI = ' + str(HHI)

wageArray.sort()
fraction = 1 / float(count)

increasingTotal = 0
rectTotal = 0

for value in wageArray:
        increasingTotal += value
        rectTotal += fraction * (increasingTotal / wageTotal) 

gini = (0.5 - rectTotal) / 0.5

print 'Gini: ' + str(gini)
