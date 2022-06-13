dicts = {'kumar': '1', 'yuva': '1', 'sasi': 2}
print(dicts)
print(type(dicts))
temp = dict(dicts)
print(type(temp))
print(temp)
print(dicts.values())
print(dicts.keys())
print(dicts.get('yuva'))
for x in dicts:
    print(x)
for x in dicts.values():
    print(x)
for x, y in dicts.items():
    print(x, y)
