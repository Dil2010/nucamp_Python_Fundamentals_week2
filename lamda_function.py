x=lambda n,k:n+k

print(x(2,3))

y=lambda r,l:pow(r,l)

print(y(9,10))

def callback(x):
    return pow(x,6)

def b_fun(r):
    return r(9)+3

print(b_fun(callback))