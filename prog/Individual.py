#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def posl(a = []):
    n = int(input())
    if n == 0:
         a.append(n)
         return a
    posl()
    a.append(n)
    return a

if __name__ == '__main__':
    print(posl())
