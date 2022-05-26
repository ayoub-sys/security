def disemvowel(string):
    s=[i for i in string if i.upper() not in ["A","E","O","U","I"]]
    return "*".join(s)

print(disemvowel("this is y"))
def disemvowel1(string):
    v = 'aeiouAEIOU'
    return filter(lambda x: x not in v, string)

for x in disemvowel1("eeqsda"):
  print(x)
def reccurent(n):
    if n==0:
        return 1
    elif n==1:
        return 2 
    else:
        return 6*reccurent(n-2)*reccurent(n-1)/(5*(reccurent(n-2))+reccurent(n-1))

print(reccurent(17))