arr=[2,2,2,4,4,4,3,3,10,1]
freq={}
for num in arr:
    freq[num]=freq.get(num,0)+1
  
#output
maxi=max(freq,key=freq.get)
mini=min(freq,key=freq.get)
print("maximum frequency number:",maxi)
print("minimum frequency number:",mini)    
