k=int(input("enter palindrome number"))
pal=0
s=k
while(k!=0):
    d=k%10
    pal=pal*10+d 
    k=k//10
    
if(pal==s):
    print("palindrome")
else:
    print("Non palindrome")
    
    