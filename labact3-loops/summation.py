term = int(input("Enter a number: "))
num = 0
print("input:", term)
print("formula:", end = " ")
for i in range(1, term+1):
  if(i%1==0):
    print(i, end=" ")
    num+=i
print("\noutput:",num)
