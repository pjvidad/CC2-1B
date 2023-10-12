word = input("Enter a word: ")
reverse = ''
for i in word:
    reverse +=i
print("The word read backwards is:", reverse)

if word == reverse:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
    


