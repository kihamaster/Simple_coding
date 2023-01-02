#!/usr/bin/env python
# coding: utf-8

# # 숫자 입력받으면, 예를 들어 1을 입력받으면 January 출력

# In[5]:


# sol 1


# In[6]:


Month = { '1':'January', '2':'February', '3':'March', '4':'April', '5':'May', 
         '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', 
         '11':'November', '12':'December'}
a=input('달의 번호: ')
if a in Month:
        Month[a]
        str(Month[a])
        print('달의 이름: ', Month[a])
else:
        print('없음')


# In[7]:


# sol 2


# In[8]:


Month = { '1':'January', '2':'February', '3':'March', '4':'April', '5':'May',
         '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', 
         '11':'November', '12':'December'}
a=input('달의 번호: ')
if a in Month:
        b=f'달의 이름: {Month[a]}'
        str(b)
        print(b)
else:
        print('없음')

