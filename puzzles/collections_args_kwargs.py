#https://www.youtube.com/watch?v=D6-d5yWOBd0

#упаковка

# a, b = (1, 2)
# print(f'{a=}')
# print(f'{b=}')

##########################

# c, *d = (1, 'a', True, 4)
# print(f'{c=}')
# print(f'{d=}')

##########################

# *e, f = 'Hello'
# print(f'{e=}')
# print(f'{f=}')

#распаковка

# a = [1, 2, 3]
# b = (a,)
# c = (*a,)
# print(f'{b=}')
# print(f'{c=}')

##########################

# e = -5, 5
# # range(e) вызовет ошибку
# f = range(*e)
# g = list(f)
# print(f'{f=}')
# print(f'{g=}')
# h = [*range(*e)]
# print(f'{h=}')
# hh = [range(*e)]
# print(f'{hh=}')

##########################

# a = {1: 'a', 2: 'b', 3: 'c'}
# b = {4: 'd', 5: 'e'}
# print({*a})
# print({*a.values()})
# print({*a.items()})
# print({**a})
# print({**a, **b})