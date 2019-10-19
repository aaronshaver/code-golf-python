# A number is a divisor of another number if it can divide into it with no remainder.
# Print the positive divisors of each number from 1 to 100 inclusive, on their own line, with each divisor separated by a space.
for i in range(1,101):
 for j in range(1,i+1):
  if i%j==0:print(j,end=' ')
 print()