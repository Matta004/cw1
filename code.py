#Introduction
print ("Welcome to the playfare encrypter ")
#Inputing the key 
key=input("Enter key(Choose a word with no repeating letter[example: *keyword*]):  ")
key=key.replace(" ", "")
key=key.upper()
with open('key text', 'w') as f:
    f.write(key)

def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key:
 #storing key
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
#storing other character
for i in range(65,91): 
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
#initialize matrix
my_matrix=matrix(5,5,0)
#making matrix 
for i in range(0,5): 
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1
#get location of each character
def locindex(c): 
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
#Encryption part
def encrypt():  
    msg=str(input("ENTER word:  "))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    with open('decripted text', 'w') as f:
        f.write(msg)

    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
   
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2      
  
#decryption
def decrypt(): 
    msg=str(input("ENTER CIPHER TEXT:  "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT:",end=' ')
    i=0
    plain=""
    with open('encripted text', 'w') as f:
        f.write(msg)
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        
        if loc[1]==loc1[1]:
            l1=my_matrix[(loc[0]-1)%5][loc[1]]
            l2=my_matrix[(loc1[0]-1)%5][loc1[1]]
            
            
           
        elif loc[0]==loc1[0]: 
            l1=my_matrix[loc[0]][(loc[1]-1)%5]
            l2=my_matrix[loc1[0]][(loc1[1]-1)%5]
        else:   
            l1=my_matrix[loc[0]][loc1[1]]
            l2=my_matrix[loc1[0]][loc[1]]
        plain+=l1
        plain+=l2
        i=i+2    
   # plain=plain.replace(" ","")  
    print(plain)  
#If condition to make choices eather to Encrypt, Decrypt or Exit
while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT   "))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        print("Thank you for using this program. bye bye :)")
        exit()
    else:
        print("Choose correct choice")