def solution(s):
    answer = 0
    dic={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    word=[]
    eng=''
    
    for i in s:
        if i.isdigit():
            word+=i
        elif i.isalpha():
            
            eng+=i
            if eng in dic.keys():
                word+=dic[eng]
                eng=''
            
    answer=int(''.join(word))
    return answer