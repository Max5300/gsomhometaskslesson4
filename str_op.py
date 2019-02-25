s = "У лукоморья 123 дуб зеленый 456"
print(s.lower().find('я'))
print(s.lower().count('у'))
if s.isalpha() == False:
    print(s.upper())
if len(s) > 4:
    print(s.lower())
print('О' + s[1:])
