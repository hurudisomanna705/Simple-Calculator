
from operators import *
a=float(input('number1:'));
b=float(input('number2:'));
operator=input('sign:');
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

