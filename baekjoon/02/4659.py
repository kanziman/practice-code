
import sys
read = sys.stdin.readline

vowel = 'aeiou'
while 1:
    lcnt,vcnt,v_include = 0,0,0
    l = read().rstrip()
    if l == 'end':
        break
    
    flag = True
    for i in range(len(l)):
        if l[i] in vowel:
            vcnt += 1
            lcnt = 0
            v_include = 1
        else: 
            vcnt = 0
            lcnt += 1
            
        if vcnt == 3 or lcnt == 3: 
            flag = False
            break
        if i>0 and l[i] == l[i-1]:
            if l[i] not in 'eo':
                flag = False
                break
        
        prev = i
        
    if v_include == 0: flag = False
    if not flag:
        print('<'+l+'> is not acceptable.')
    else :
        print('<'+l+'> is acceptable.')
        
    
