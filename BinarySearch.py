def BinarySearch(lt,s):
    low=0
    hight=len(lt)
    while(low<=hight):
        mid=int((low+hight)/2)
        result=lt[mid]
        if result==s:
            return mid
        else:
            if s<lt[mid] :
                hight=mid-1
            else:
                low=mid+1
    return -1


searchList=input('请输入要查找的列表，元素之间用空格分开：').split()

searchList.sort()

print('排序后的列表：{}'.format(searchList))
ss=input('请输入要查找的元素：')
position=BinarySearch(searchList,ss)
if position!=-1:
    print('你要查找的元素{}在列表的第{}个位置'.format(ss,str(position)))
else:
    print('在列表中没有找到元素{}'.format(ss))

