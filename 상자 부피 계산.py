#!/usr/bin/env python
# coding: utf-8

# # 상자 부피 계산

# In[1]:


class Box():
    def __init__(self,H,L,D):
        self.H=H
        self.L=L
        self.D=D
        
    
    def getHeight(self):
        result=self.H
        return result
        
    
    def getLength(self):
        result=self.L
        return result
    
    
    def getDepth(self):
        result=self.D
        return result
        
    
b1 = Box(100, 100, 100)


print(b1.getHeight(), b1.getLength(), b1.getDepth())   # (L, h, d) 값 출력
print("상자의 부피는 %d " %(b1.getHeight()*b1.getLength()*b1.getDepth()))

