cln={1,2,3,4,4,4,3,2,'hello','world'}
print(cln)
print(len(cln))

collec=set()  # empty set


collec.add(1)
collec.add(2)
collec.add(3)
collec.add(4)
collec.add(1)
print(collec)
collec.remove(1)
print(collec)
collec.pop()
print(collec)
collec.clear()
print(collec)


set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))  # print all Unique Elements from both set 
print(set1.intersection(set2))  # print only common elements from both sets
