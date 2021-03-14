n, B = list(map(int, input().strip().split()))
T = 0


sum1 = 0
total = []

for i in range(1,n+1):
  j = n-i
      
  if i%2 == 0:
    p = (2**i) + 1      # these are for 
    sum1 = p**j         # the formula
    total.append(sum1)   # I appended the outputs to the list [64,25,28,1]
              
  else:
    p = (3**i) + 1   
    sum1 = p**j
    total.append(sum1)
toplam = sum(total)         
 
boşliste= []
left = 0
right = 10000
for a in range(left,right):
  if a*toplam > B:
    T = a
    break
  elif a*toplam < B:
    T += 1

    


print(T)