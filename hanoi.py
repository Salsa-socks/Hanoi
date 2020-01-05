def move(f,t):
    print("Move Disc from {} to {}".format(f,t))
    
def move_via(f,v,t):
    move(f,v)
    move(v,t)
    
def hanoi(n,f,h,t):
    if n == 0:
        pass
    else:
        hanoi(n-1, f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)
        
if __name__ == '__main__':
    hanoi(4,"A", "B", "C")