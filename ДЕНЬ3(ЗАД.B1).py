import datetime
def printTimeStamp(name):
    print('prodaivoda yan prodaivoda dan: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))




import math

coef = 1 

rows = int(input("Enter the number of rows :")) 

stringVal = "" 

for i in range(rows): 

    for space in range(1,rows - i + 1): 

     stringVal = stringVal + " " 
    for j in range(0,i + 1): 
     if(i == 0 or j == 0): 
      coef = 1 
     else: 
      coef = coef * (i - j + 1)/j 

     temp = coef 
     TotalSpace=0 
     while(temp != 0): 
      TotalSpace = TotalSpace + 1 
      temp = int(math.floor(temp/10)) 
     p=0 
     while((p+TotalSpace)!=4): 
      stringVal = stringVal + " " 
      p=p+1 
     stringVal = stringVal + str(int(math.floor(coef))) 
    stringVal = stringVal + "\n" 
print(stringVal)


