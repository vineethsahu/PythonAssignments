#import operator
def freq(str):

    c = {}
    for i in str:
        if i in c.keys():
            c[i] = c[i]+1
        else:
            c[i] = 1
    #desc = dict(sorted(c.items(), key=operator.itemgetter(1), reverse=True))
    desc = dict(sorted(c.items(), key=lambda x:x[1], reverse=True))
    return desc

n = input("enter a string: ")
print("the string is -> ", n)

print(freq(n))
