word=input()

search_word=input()

count=0

i=0

while i<=len(word)-len(search_word):
    
    if word[i:i+len(search_word)]==search_word:
        count+=1
        i+=len(search_word)
        
    else:
        i+=1
        
print(count)