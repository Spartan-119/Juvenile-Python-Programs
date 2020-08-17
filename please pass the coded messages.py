# -*- coding: utf-8 -*-
"""
Please pass the coded messages

Created on Sun Aug 16 23:20:47 2020

@author: Abin
"""

'''
a=[3, 1, 4, 1]
f=[3, 1, 4, 1, 5, 9]
c=[3, 1, 4, 1, 5, 9,1,3,4,6,1,4,3,8,2,4,6,8]
g=[5,4,7,8,1,2,0]
gg=[1,2,3]
d=[5,8,1,2]
b=[3, 1, 4, 1, 5, 9,4,6,4,2]
c1=[1,1,1,1,1,1,1]
k=[1,1]
from collections import deque
def solution(l):
	if len(l) < 100 and not any(n < 0 for n in l):
		if sum(l) % 3 == 0:
			return int(''.join(map(str,sorted(l,reverse=True))))
		elif sum(l) % 3 != 0:
			mul  = sorted([i for i in l if i % 3 == 0])
			nmul = sorted([i for i in l if i % 3 != 0])
			tmp = deque(nmul)
			f=[]
			g=[]
			if nmul:
				for i in nmul:
					tmp.rotate(1)
					g=list(tmp)
					if sum(g[0:len(nmul)-1]) % 3 == 0:
						f.append(sorted(g[0:len(nmul)-1],reverse=True))
				if not mul and not f:
					return 0
				elif not f:
					return int(''.join(map(str,sorted(mul,reverse=True))))
				else:
					return int(''.join(map(str,sorted(max(f)+mul,reverse=True))))
			else: return 0
	else: return 0



print(solution(k))
'''

'''
inputNumbers = [2, 1, 1, 1, 7, 8, 5, 7, 9, 3]

inputNumSorted = sorted(inputNumbers)
sumMax = sum(inputNumbers)
queue = [(sumMax, inputNumSorted)]

found = False
while (len(queue) > 0):
    (sumCurrent, digitList) = queue.pop()
    remainder = sumCurrent%3

    if (remainder == 0):
        found = True
        break
    else :
        for index, aNum in enumerate(digitList):
            if(aNum%3 == remainder):
                sumCurrent -= remainder
                digitList.remove(aNum)
                found = True
                break
            else:
                newList = digitList[:index]+digitList[index+1:]
                if (len(newList) > 0):
                    queue.insert(0, (sumCurrent-aNum, newList))
    if(found):
        break

maxNum = 0
if (found):
    for x,y in enumerate(digitList):
        maxNum += (10**x)*y

print(maxNum)
'''

def solution(l):
	
    inputNumSorted = sorted(l)
    sumMax = sum(l)
    queue = [(sumMax, inputNumSorted)]

    found = False
    while (len(queue) > 0):
        (sumCurrent, digitList) = queue.pop()
        remainder = sumCurrent%3

        if (remainder == 0):
            found = True
            break
        else :
            for index, aNum in enumerate(digitList):
                if(aNum%3 == remainder):
                    sumCurrent -= remainder
                    digitList.remove(aNum)
                    found = True
                    break
                else:
                    newList = digitList[:index]+digitList[index+1:]
                    if (len(newList) > 0):
                        queue.insert(0, (sumCurrent-aNum, newList))
        if(found):
            break

    maxNum = 0
    if (found):
        for x,y in enumerate(digitList):
            maxNum += (10**x)*y

    print(maxNum)
    

l = [2, 1, 1, 1, 7, 8, 5, 7, 9, 3]

solution(l)