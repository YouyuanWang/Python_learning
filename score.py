# !user/bin/vin python
# coding:gbk
#��Ŀһ��ͳ�Ƴɼ�

with open('report.txt') as f:
    filelines = f.readlines()

new = []
for line in filelines:
    data = line.strip()
    data = data.split(' ')
   # print type(data)
    total = 0
    for i in range(1,10):
        total += int(data[i])
    data.append(str(total))        #���ܳɼ�
    data.append(str(round(total/9.0,2)))  #ƽ����
    new.append(data)
new.sort(key = lambda x:x[10],reverse = True)   #����
print new

average_list = []
average_list.append('0')
average_list.append('ƽ����')
for i in range(9):
    total = 0
    for j in range(len(new)):
        total += int(new[j][i+1])
        if int(new[j][i+1])<60:
            new[j][i+1] = '������'
    average_list.append(str(round(1.0*total/len(new),2)))
print average_list
print new
rank = 1
for i in new:
    i.insert(0,str(rank))
    rank +=1

title =['����','����','����','��ѧ','Ӣ��','����','��ѧ','����','����','��ʷ','����','�ܷ�','ƽ����']
f = open('new.txt','w')
f.write(' '.join(title)+'\n')
f.write(' '.join(average_list)+'\n')
for i in new:
    f.write(' '.join(i)+'\n')
f.close()
# print new





