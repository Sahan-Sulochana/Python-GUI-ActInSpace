str1="C:\\Users\\Lenovo\\Desktop\\Nordlys-1.jpg"

list1=list(str1)

list2=[]
for i in range(len(list1)-1,-1,-1):
    if list1[i]=="\\":
        break
    else:
        list2.append(list1.pop())
list2.reverse()
str2=""
str2="".join(list2)
link2="Python\\Output Image\\"+str2