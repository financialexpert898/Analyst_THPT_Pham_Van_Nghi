#!/usr/bin/env python
# coding: utf-8

# In[5]:
# READ FILE
with open("C:\\Users\\buith\\Downloads\\123.csv",encoding = "utf8") as file:
    data = file.read().split("\n")
header = data[0]
students = data[1:]
students.pop()
total_student = len(students)
header = header.split(";")
for i in range(len(students)):
    students[i]= students[i].split(";")
subject = header[5:]
not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]
print(students[-1])
for s in students:
    for i in range(5,16):
        if s[i]== "-1":
            not_take_exam[i-5]+=1
print(not_take_exam)
not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,11):
    not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student,2)
print(not_take_exam_percentage)
print(subject)


# In[2]:


import matplotlib.pyplot as plt
import numpy
figure,axis = plt.subplots()
y_pos = numpy.arange(len(subject))

plt.bar(subject, not_take_exam_percentage)
plt.xticks(rotation='vertical')
axis.set_ylim(0,100)

plt.title('số học sinh không thi các môn ')
plt.xlabel('Môn học')
plt.ylabel('phần trăm')
rects = axis.patches

# Make some labels.


for rect, label in zip(rects, not_take_exam_percentage):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height+2 , label, ha="center", va="bottom"
    )

plt.show()


# In[4]:


#tìm Số học sinh của phạm văn nghị và học sinh của trường dân lập
# học sinh được dân lập không phải thi ngoại ngữ và có 1 thí sinh thi thêm 2 môn
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0] #xem mỗi trường có bao nhiêu hoc sinh
average =[0,0,0,0,0,0,0,0,0,0,0,0] # thu dược học điểm trung bình của học sinh mỗi trường
for s in students:
    count = 0
    total = 0
    
    for i in range(11):
        if s[i+5] != "-1":
            total += float(s[i+5].replace(",","."))
            count+=1

    num_of_exam_taken[count] +=1
    average[count] += total/count
for i in range(12):
    if num_of_exam_taken[i] != 0:
        average[i] = round( average[i]/num_of_exam_taken[i],2)
# thu được điểm trung bình của học sinh mỗi trường
print(average)


# In[9]:



# trực quan hóa điểm trung bình của học sinh từng trường bằng đồ thị cột
import matplotlib.pyplot as plt
import numpy
figure,axis = plt.subplots()
y = numpy.arange(12)
x = numpy.arange(12)
plt.bar(x, average)
plt.xticks(x,y)
plt.title("Điểm trung bình của học sinh thi")
plt.xlabel("Số Môn thi của học sinh")
plt.ylabel("Điểm")
axis.set_ylim(0,10)

rects = axis.patches
# Make some labels.

for rect, label in zip(rects, average):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom"
    )

plt.show()


# In[11]:

# Xem điểm của học sinh theo tháng sinh của của mỗi học sinh để xem với 2004 thì học sinh đẻ tháng nào có điểm trội hơn
num_of_student_per_month_group = [0,0,0,0,0,0,0,0,0,0,0,0]
average_of_student_per_month_group=[0,0,0,0,0,0,0,0,0,0,0,0]
x = numpy.arange(1,13)

y= numpy.arange(1,13)
for s in students:
    month = s[3][3:5]
    num_of_student_per_month_group[int(month)-1] +=1
    sum_score=0
    count_score=0
    for i in range(11):
        if s[i+5] != "-1":
            count_score += 1
            sum_score += float(s[i+5].replace(",","."))

    average = sum_score/count_score
    average_of_student_per_month_group[int(month)-1]+= average 
for i in range(len(average_of_student_per_month_group)):
    
    average_of_student_per_month_group[i] = average_of_student_per_month_group[i]/num_of_student_per_month_group[i]
for i in range(len(average_of_student_per_month_group)):
     average_of_student_per_month_group[i] =  average_of_student_per_month_group[i]*7
figure,axis = plt.subplots()
plt.bar(x,num_of_student_per_month_group)
plt.title("Phân tích điểm trung bình của học sinh theo tháng sinh")
axis.set_xlabel("Tháng")
axis.set_ylabel("Số học sinh")
plt.plot(x,average_of_student_per_month_group,color ="red")
plt.xticks(x,y)
ax2 = axis.twinx()
ax2.tick_params('y', colors ='red')
ax2.set_ylabel("Điểm Trung Bình")
ax2.set_ylim(0,10)
rects = axis.patches
for rect, label in zip(rects,num_of_student_per_month_group):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height , label, ha="center", va="bottom"
    )
plt.show()


# In[ ]:


# In[ ]:





# In[ ]:





#%%
