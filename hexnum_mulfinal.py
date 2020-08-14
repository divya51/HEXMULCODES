binary_dict={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"};
#READ INPUT FROM TWO INPUT TXT FILES 
with open ('num1.txt', 'rt') as f1,open ('num2.txt', 'rt') as f2:
	a=f1.readline()
	b=f2.readline()
	
a=a.rstrip()
b=b.rstrip()
#CONVERTING 'A' INTO BINARY
abinary="";
#a='AEBCD';
for i in range(0,len(a)):
    abinary+=binary_dict[a[i]];

#CONVERTING 'B' INTO BINARY
bbinary='';
#b='AEDEE';
for j in range(0,len(b)):    
    bbinary+=binary_dict[b[j]];

def add_binary_nums(x,y):
        max_len = max(len(x), len(y))
        x = x.zfill(max_len)
        y = y.zfill(max_len)
        result = ''
        carry = 0
        for i in range(max_len-1, -1, -1):
            r = carry
            r += 1 if x[i]=='1' else 0
            r += 1 if y[i]=='1' else 0
            result= ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1       
        if carry !=0 : result = '1' + result
        return result.zfill(max_len)

#ADDITION OF BINARY NUMBERS ACCORDING TO VALUE
sum="";
count=0;
for k in range(len(bbinary)-1,-1,-1):
    count+=1;
    
    if(bbinary[k]=='1'):        
        sum=add_binary_nums(abinary.ljust(len(abinary)+count-1, '0'),sum);
       
    else:
        sum=add_binary_nums('0'.ljust(len(abinary)+count-1,'0'),sum);
    

#CONVERTING THE TOTAL BINARY ADDITION INTO HEXADECIMAL    
result="";
if(len(sum)%4!=0):
    n=len(sum)%4;
    sum=sum.rjust(len(sum)+4-n,'0')
    
for l in range(0,len(sum),4):
    m=sum[l:l+4];
    for k,v in binary_dict.items(): 
            if v==m:              
                result+=k;
     
#RESULT IS THE FINAL OUTPUT
with open('result.txt', 'w') as w:
	w.write(str(result))
w.close()
