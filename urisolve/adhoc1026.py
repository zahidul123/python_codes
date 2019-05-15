while True:
    try:
        a=int(input())
        b=int(input())
        if a==0 or b==0:
            break
        else:
          res=a^b
          print(res)
          print("\n")
    except IOError:
        break

