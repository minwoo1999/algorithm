N=int(input())

books={}
for i in range(N):
    book=input()
    
    if book not in books:
        books[book]=1
    else:
        books[book]+=1
        
        

target=max(books.values())
array=[]
for book,count in books.items():
    
    if count==target:
        array.append(book)
        
array.sort()

print(array[0])