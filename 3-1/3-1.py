from pprint import pprint

mass = [x for x in range(10)]
a = [n ** 2 for n in mass if (n % 3 and n % 4)]
pprint(a)