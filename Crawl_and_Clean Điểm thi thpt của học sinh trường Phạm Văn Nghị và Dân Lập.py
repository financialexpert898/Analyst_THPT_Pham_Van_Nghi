#!/usr/bin/env python
# coding: utf-8

# In[3]:


#lấy dữ liệu và làm sạch điểm của học sinh phạm văn nghị thi thpt quốc gia
import csv
import requests
from bs4 import BeautifulSoup
start = 25006318
end = 25006429
data=[]
for sbd in range(start,end):
    url = "https://thptquocgia.edu.vn/diemthi/?sbd="+str(sbd)
    # Lấy dữ liệu từ trang web
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    # Lấy tất cả dữ liệu trong bảng
    rows = soup.find_all('td')
    data.append(rows)
file = open('dữ_liệu123.txt','w',encoding='utf_8')
for cells in data:
    for cell in cells:
        if (str(cell.text) != '   GỢI Ý CHỌN NGUYỆN VỌNG VÀO TRƯỜNG ĐẠI HỌC '): # lọc các chữ "  GỢI Ý CHỌN NGUYỆN VỌNG VÀO TRƯỜNG ĐẠI HỌC" ra khỏi file
            file.write(str(cell.text)) #viết hết các điểm thi vào file
            file.write(",")#thêm dấu phẩy sau mỗi điểm
    file.write('\n')#xuống dòng sau khi hết điểm của 1 thí sinh
file.close()
sbd1 = 25006318
file = open('dữ_liệu123.txt','r',encoding='utf_8')
file1 = open('dữ_liệu123.csv','w',encoding='utf_8')
data2 = file.read().split("\n")
for data1 in data2:
    if(data1 != ''):#xóa bỏ các dòng trống ra khỏi flile
        file1.write(str(sbd1))
        file1.write(',')
        file1.write(data1+"\n")
    sbd1+=1
file1.close()


# In[ ]:




