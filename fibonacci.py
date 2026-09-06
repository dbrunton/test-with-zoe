#!/usr/bin/env python3

def f(n):
 a,b=0,1
 while n:
  yield a
  a,b=b,a+b
  n-=1

if __name__=="__main__":
 print(' '.join(map(str,f(10))))
