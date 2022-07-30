def vowels(word):
    c=0
    for i in word:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            c=c+1
    print("the num of vowels is ",c)

x=input("Enter your word ")
vowels(x)