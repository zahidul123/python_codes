import sys
sys.setrecursionlimit(1500)
def falvious(n,k):
    if n == 0:
        return 0
    else:
        return (falvious(n-1,k)+k-1)% k+1

nc=int(input())
for i in range(nc):
    n=int(input())
    k=int(input())
    res=falvious(n,k)
    print(res)