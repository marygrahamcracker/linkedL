myperson = person()
myperson.name = 'mud'
print(f'my person\'s name is {myperson.name}')
if myperson.needstopee:
    print(f'my person needs to pee')
    myperson.gotobatheroom

if not myperson.needstopee:
    print('my person no longer needs to pee')