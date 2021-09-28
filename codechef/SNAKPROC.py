# cook your dish here
try:
    n=int(input())
    for i in range(n):
        nn=int(input())
        text=str(input())
        text=text.replace(".","")
        #print(text,len(text))
        if len(text)==0:
            print("Valid")
        elif text[0]=="T":
            print("Invalid")
        else:
            flag=0
            i=0
            while i<len(text):
                #print(i)
                #(text[i:i+2])
                if text[i:i+2]=="HT":
                    #print("match")
                    i+=2
                    pass
                else:
                    flag=1
                    print("Invalid")
                    break
            if flag!=1:
                print("Valid")
        
        
       
        
                    
except:
    pass
