# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
e=input().split(' ')

n=int(input())
f=input().split(' ')

e=set(e)
f=set(f)

print(len(e.difference(f)))