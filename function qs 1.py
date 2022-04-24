list=[1,2,3,4,5,6,7,8,9]
def even_list(list):
    n=len(list)
    i=0
    req_list=[]
    while i<n:
        if list[i]%2==0:
            req_list.append(list[i])
        i+=1
    print(req_list)
even_list(list)