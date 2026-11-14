n= int(input())
while True:
    n+=1
    digits =str(n)
    if len(set(digits))==len(digits):
        print(n)
        break
    