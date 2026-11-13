n, k=map(int,input().split())
score =list(map(int, input().split()))
count=0
for i in score:
    if i >= score[k-1] and i > 0:
        count+=1
print(count)