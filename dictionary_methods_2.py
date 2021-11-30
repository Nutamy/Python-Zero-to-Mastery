dic = {
  'a': [1,2,3],
  'b': 'hello',
  'c': 12
}

for i in dic:
  print(i)

print(dic.get('a'))
print(dic.get('z'))

return_get_dic_a = dic.get('a', 'True')
return_get_dic_z= dic.get('z', 'True')
keys = dic.keys()
print(keys)

for i in keys:
  print(i)

values = dic.values()

print(values)

for i in values:
  print(i)

items = dic.items()

print(items)

for i in items:
  print(i)

#dic.clear()
#print(dic.popitem())

dic.update({'name':'Carl'})
dic.update({'b':'Simona'})
print(dic)
