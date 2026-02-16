def max_function(number):
    i = number[0]
    for x in number:
        if i < x:
            i = x
    print(i)
    return i    
ls = [21,46,4,646,46,4]
max_function(ls)
print("highest ls " ,max(ls))