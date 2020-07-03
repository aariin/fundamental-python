#scalar data type: simple data type
kid1 = 'Nina'
kid2 = 'Alex'
kid3 = 'Laura'
kid4 = 'Onky'

print(kid1)
print(kid2)
print(kid3)
print(kid4)

#array data type
print('\nlist data type')
kid = ['Nina', 'Alex', 'Laura', 'Onky']
print(kid)
kid.append('Harry')
print(kid)

#greet second kid
print('\ngreet second kid')
print(f'Hai {kid[1]}!')

print('\ngreet all kids')
#special script "for" for list/array data
for k in kid:
    print(f'Hi {k}!')

#or we can use difficult way
print('\ngreet all kids using difficult way')
for k in range(0, len(kid)):
    print(f'Hi {kid[k]}!')