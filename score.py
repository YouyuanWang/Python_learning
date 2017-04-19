# !user/bin/vin python
# coding:gbk
#项目一：统计成绩

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
    data.append(str(total))        #求总成绩
    data.append(str(round(total/9.0,2)))  #平均分
    new.append(data)
new.sort(key = lambda x:x[10],reverse = True)   #排名
#print new

average_list = []
average_list.append('0')
average_list.append('平均分')
for i in range(9):
    total = 0
    for j in range(len(new)):
        total += int(new[j][i+1])
        if int(new[j][i+1])<60:
            new[j][i+1] = '不及格'
    average_list.append(str(round(1.0*total/len(new),2)))
#print average_list
#print new
rank = 1
for i in new:
    i.insert(0,str(rank))
    rank +=1

title =['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
f = open('new.txt','w')
f.write(' '.join(title)+'\n')
f.write(' '.join(average_list)+'\n')
for i in new:
    f.write(' '.join(i)+'\n')
f.close()
# print new





