dic = {'Alan': 8, 'George': 2, 'Akshay': 5, 'Bilahari':  3}
l = list(dic.items())
l.sort()
print('Ascending order is',  l)
l = list(dic.items())
l.sort(reverse=True)
print('Descending order is',  l)
