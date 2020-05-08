def merge_the_tools(string, k):
    j=0
    while j+k<=len(string):
        prstr=""
        for i in string[j:j+k]:
            if i not in prstr:
                prstr+=i
        print(prstr)
        j+=k
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
