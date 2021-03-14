

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
  
            
 
boşliste= []
left = 0
right = 1000000
while left < right:
    
    T = (left + right) / 2
    toplam = int(sum(total)*T)   # sum of [64,25,28,1] times T means                                                           toplam
    
    if toplam > B:
      
      right = T            
     
      boşliste.append(T)   
    
    elif toplam < B:      
      left = T
    
    else:
      break
    
    if left >= right:
      T = -1
      break

if T > 10000:
  T = -1
else:
  T = round(int(T)+1)

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)