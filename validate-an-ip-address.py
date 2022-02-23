import re
def isValid(s):
    #code here
    s=s.split('.')
    c=0
    regex=re.compile('[@_!#$%^&*()<>?/\|}{~:] ')
    for i in s:
        if i=='':
            return 0
    
        if i[0]=='0' and len(i)>1:
            return 0
        if regex.search(i) !=None:
            return 0
            
        res=bool(re.match('[a-zA-Z\s+$]',i))
        
        
        if res:
            return 0
        k=int(i)
        c+=1
        
        if k>255 or k<0:
            return 0
        if c==5:
            return 0
    if c!=4:
        return 0
    return 1
            
