"""Дано трехзначное число. Найдите сумму его цифр."""
n = int(input())
print(n // 100 + n // 10 % 10 + n % 10)