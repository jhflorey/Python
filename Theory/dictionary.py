dic = {}
dic_1 = {
    "name": 'huy',
    'age':14,
    'location': 'vietnam',
    'second': [1,2,3,4]
}

dic_1['gender'] ='male'
print(dic_1)
dic_1['location'] = 'usa'
print(dic_1)
print(dic_1.keys())
print(dic_1.values())
for  a in dic_1.items():
    print(a)

print(dic_1.get('second_1','ahihi'))