base_values = '1h 45m,360s,25m,30m 120s,2h 60s'
base_values=base_values.replace(',',' ')
lst = base_values.split()

for i in range(0,len(lst)):
    
    if 'h' in lst[i]:
        lst[i] = lst[i].replace( 'h','')
        lst[i]=int(lst[i])*60
    
    elif 'm' in lst[i]:
        lst[i] = int(lst[i].replace( 'm',''))
        
    elif 's' in lst[i]:
        lst[i] = lst[i].replace( 's','')
        lst[i]=int(lst[i])//60    

result = 0        

for i in range(0,len(lst)):
    result += lst[i]        
        
print(result)