import sys
from operator import itemgetter

try:
	num = int(sys.argv[1])
except:
	num = 100

fileName = 'factors.csv'

def get_factors(n):
	numFactors = 0
	for i in range(1, n + 1):
		if n%i == 0:
			numFactors += 1
	return((n, numFactors, round(n/numFactors, 1)))

def get(n):
	l = []
	for i in range(1, n + 1):
		l.append(get_factors(i))
	return l

def run(l):
	l.sort(key=itemgetter(1))
	return l

lst = run(get(num))

with open(fileName, 'w+') as f:
	f.write('\nNum,Factors,Value')
	for num, factors, value in lst:
		f.write('\n' + str(num) + ',' + str(factors) + ',' + str(value))
