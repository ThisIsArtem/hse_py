"""Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей и копеек нужно заплатить за N пирожков."""
a = int(input())
b = int(input())
n = int(input())
s = n * (a * 100 + b)
sa = s // 100
sb = s % 100
print(sa, sb)