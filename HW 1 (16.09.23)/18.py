"""За день машина проезжает N километров. Сколько дней нужно, чтобы проехать маршут длиной M километров?"""
n = int(input())
m = int(input())
print((m - 1) // n + 1)
