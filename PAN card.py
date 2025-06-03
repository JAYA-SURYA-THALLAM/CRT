s=input()
dc=s[5:9]
s1=s[0:5]
print(len(s),s[-1],dc,s1)
if (len(s)!=10 and s[-1].isalpha and dc.isdigit() and s1.isalpha):
    print("valid")
else:
    print("invalid")    