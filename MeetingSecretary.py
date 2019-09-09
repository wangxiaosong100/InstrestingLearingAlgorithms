import numpy as np
import operator
class Meet(object):

    def __init__(self,beg,end,num):
        self.beginTime=beg
        self.endTime=end
        self.meetNum=num


a=list()

n=input('请输入会议数量:')
for i in range(int(n)):

    beg,end=input('请输入第%s会议起止时间，以空格分开:'%str(i+1)).split()
    while int(end)<int(beg):
        print('\033[4;31;43m 请输入有效的会议参数，会议结束时间应大于会议开始时间！！！\033[0m')
        beg, end = input('请输入第%s会议起止时间，以空格分开:' % str(i + 1)).split()
    m = Meet(beg,end,i+1)
    a.append(m)
# 排序
sortkey=operator.attrgetter('endTime','beginTime') #取到排序的依据属性，这里优先使用endTime排序，然后再再使用beginTime排序
a.sort(key=sortkey)

choseMeet=[]
choseMeet.append(a[0])
etime=a[0].endTime
print('排序后的会议信息如下：(以会议结束时间升序，结束时间相同时，以会议开始时间排序)')
print('会议号\t\t\t会议开始时间\t\t\t会议结束时间')

for l in a:
    print('  '+str(l.meetNum)+'\t\t\t\t\t  '+l.beginTime+'    \t\t\t\t  '+l.endTime)

for i in range(1,len(a)):
    if a[i].beginTime>=etime:
        choseMeet.append(a[i])
        etime=a[i].endTime

print('会议密秘书为你选择的会议如下：')
print('会议号\t\t\t会议开始时间\t\t\t会议结束时间')
for l in choseMeet:
    print('  ' + str(l.meetNum) + '\t\t\t\t\t  ' + l.beginTime + '    \t\t\t\t  ' + l.endTime)