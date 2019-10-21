# A number is a divisor of another number if it can divide into it with no remainder.
# Print the positive divisors of each number from 1 to 100 inclusive, on their own line, with each divisor separated by a space.
for i in range(1,101):
 for j in range(1,i+1):
  if i%j==0:print(j,end=' ')
 print()


# attempt at alternate solution using a nested list comprehension
# sadly it is 110 chars, way longer than the 84 chars above
# looked into translate() and r=str.replace but made no headway

print(str([y for x in range(1,101)for y in range(1,x+1)if x%y==0]).replace(' 1,','\n1').replace(',','')[1:-1])