def help_from_sam(number):
    count=1
    num=1
    while num*2<=number:
        num*=2
    return count+(number-num)

number=int(input())
print(help_from_sam(number))