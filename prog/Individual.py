#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def posl(a=[]):
    n = int(input())
    while n != 0:
        posl()
        a.append(n)
        return a
    a.append(n)
    return a

if __name__ == '__main__':
    print(posl())
