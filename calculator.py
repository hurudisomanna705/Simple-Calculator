# -*- coding: utf-8 -*-
"""calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q73IywMvKB6qtVfCTnt9pzLM-LHvrXVP
"""

a=float(input('number1:'));
b=float(input('number2:'));
operator=input('sign:');
def add(a,b):
  A=a+b;
  print(A)
def sub(a,b):
  B=a-b;
  print(B)
def mult(a,b):
  C=a*b;
  print(C)
def div(a,b):
  D=a/b;
  print(D)
def rem(a,b):
  E=a%b;
  print(E)
def exp(a,b):
  G=a**b;
  print(G)
#= -assign; == - compare
if(operator=='+'):
  add(a,b);
elif(operator=='-'):
  sub(a,b);
elif(operator=='*'):
  mul(a,b);
elif(operator=='/'):
  div(a,b);
elif(operator=='**'):
  exp(a,b);
elif(operator=='%'):
  rem(a,b);
else:
print('invalid')

