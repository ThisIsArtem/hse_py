"""Улитка ползет по вертикальному шесту высотой H метров, поднимаясь за день на A метров, а за ночь спускаясь на B метров. 
На какой день улитка доползет до вершины шеста?"""
h = int(input())
a = int(input())
b = int(input())
print(int((h - b - 1) / (a - b) + 1))