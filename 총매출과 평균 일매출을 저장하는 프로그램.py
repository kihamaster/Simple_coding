#!/usr/bin/env python
# coding: utf-8

# # 총매출과 평균 일매출을 저장하는 프로그램

# In[7]:


# 입력 파일 이름, 출력 파일 이름 설정
inputfile=input("입력파일이름: ")
outputfile=input("출력파일이름: ")


# In[8]:


# sales.txt 파일에 정보 적기
f1=open("sales.txt", "w")
f1.close()
f2=open("sales.txt", "a")
f2.write("1000000")
f2.write("\n")
f2.write("1000000")
f2.write("\n")
f2.write("1000000")
f2.write("\n")
f2.write("500000")
f2.write("\n")
f2.write("1500000")
f2.close()


# In[9]:


# 값 초기화 해주기
sum=0
count=0


# In[10]:


# 기본 값 설정하기
infile=open(inputfile, "r")
line = infile.readline()
while line != "" : 
    s = int(line) 
    sum += s 
    count += 1
    line = infile.readline()
print(sum)
print(count)


# In[11]:


# 결과 값 도출하기
aver=sum/count
outfile=open(outputfile, 'w')
mon="총매출: %d \n" %sum
dmon="일평균 매출: %d" %aver
outfile.write(mon)
outfile.write(dmon)

infile.close()
outfile.close()


# In[12]:


outfile=open(outputfile, 'r')
data=outfile.readlines()
print(data)
outfile.close()


# In[ ]:




