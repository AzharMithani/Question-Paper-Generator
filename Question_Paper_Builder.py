# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:26:15 2017

@author: Azhar Mithani
"""
from random import randint
import random
import pandas as pd
from time import sleep
with open("Datasetforai.csv","r",encoding="mac_roman",newline="") as csvfile:
    df=pd.read_csv(csvfile)
    df_1=df.iloc[:51,:4]
f=open('questionpaper.doc','w+') 
#f.write('hello')
#f.close()   
df2=df.iloc[:51,:4].values
print(df2[1][1]) 
dict1={0:[[2,3,5,10],[1,2,3,5]],1:[[10,10],[5,6]],2:[[5,5,10],[2,3,4]],3:[[5,5,5,5],[1,2,4,4]],4:[[2,8,10],[1,5,6]],5:[[4,6,10],[3,3,2]],6:[[4,4,8,4],[2,3,4,2]]}
unit=[1,2,3,8,9,10]
vis=[]
print(set(unit)-set(vis))
q1=[]
q2=[]
nlist=[0,1,2,3,4,5,6]
n=random.choice(nlist)
print(n)
bdic={1:'REM',2:'UND',3:'Apply',4:'Analyze',5:'Evaluate',6:'Create'}
#print(df_1[][1])    
seq=dict1[n]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                vis.append(ch)
                q1.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                k=1
                c=1
            j=j+1
nlist.remove(n)
n1=random.choice(nlist)
print(n1)

#print(df_1[][1])
vis=[]    
seq=dict1[n1]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                
                if df2[j][1] not in q1:
                    vis.append(ch)
                    q2.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                    k=1
                    c=1
            j=j+1    
unit=[1,2,3,8,9,10]
vis=[]
print(set(unit)-set(vis))
q1_1=[]
q2_1=[]
nlist=[0,1,2,3,4,5,6]
n=random.choice(nlist)
print(n)
bdic={1:'REM',2:'UND',3:'Apply',4:'Analyze',5:'Evaluate',6:'Create'}
#print(df_1[][1])    
seq=dict1[n]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                vis.append(ch)
                q1_1.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                k=1
                c=1
            j=j+1
nlist.remove(n)
n1=random.choice(nlist)
print(n1)

#print(df_1[][1])
vis=[]    
seq=dict1[n1]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                
                if df2[j][1] not in q1:
                    vis.append(ch)
                    q2_1.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                    k=1
                    c=1
            j=j+1    
unit=[1,2,3,8,9,10]
vis=[]
print(set(unit)-set(vis))
q1_2=[]
q2_2=[]
nlist=[0,1,2,3,4,5,6]
n=random.choice(nlist)
print(n)
bdic={1:'REM',2:'UND',3:'Apply',4:'Analyze',5:'Evaluate',6:'Create'}
#print(df_1[][1])    
seq=dict1[n]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                vis.append(ch)
                q1_2.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                k=1
                c=1
            j=j+1
nlist.remove(n)
n1=random.choice(nlist)
print(n1)

#print(df_1[][1])
vis=[]    
seq=dict1[n1]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                
                if df2[j][1] not in q1:
                    vis.append(ch)
                    q2_2.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                    k=1
                    c=1
            j=j+1  
unit=[1,2,3,8,9,10]
vis=[]
print(set(unit)-set(vis))
q1_3=[]
q2_3=[]
nlist=[0,1,2,3,4,5,6]
n=random.choice(nlist)
print(n)
bdic={1:'REM',2:'UND',3:'Apply',4:'Analyze',5:'Evaluate',6:'Create'}
#print(df_1[][1])    
seq=dict1[n]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                vis.append(ch)
                q1_3.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                k=1
                c=1
            j=j+1
nlist.remove(n)
n1=random.choice(nlist)
print(n1)

#print(df_1[][1])
vis=[]    
seq=dict1[n1]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                
                if df2[j][1] not in q1:
                    vis.append(ch)
                    q2_3.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                    k=1
                    c=1
            j=j+1 
unit=[1,2,3,8,9,10]
vis=[]
print(set(unit)-set(vis))
q1_4=[]
q2_4=[]
nlist=[0,1,2,3,4,5,6]
n=random.choice(nlist)
print(n)
bdic={1:'REM',2:'UND',3:'Apply',4:'Analyze',5:'Evaluate',6:'Create'}
#print(df_1[][1])    
seq=dict1[n]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                vis.append(ch)
                q1_4.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                k=1
                c=1
            j=j+1
nlist.remove(n)
n1=random.choice(nlist)
print(n1)

#print(df_1[][1])
vis=[]    
seq=dict1[n1]
for i in range(len(seq[0])):
    m=seq[0][i]
    b=seq[1][i]
    c=0
    while c==0:
        ch=random.choice(list(set(unit)-set(vis)))
        print("chapter choice ",ch)
        k=0
        j=0
        while j<len(df2) and k==0:
            print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
            #sleep(1.0)
            if int(df2[j][0])==ch and int(df2[j][2])==m:
                #print(df2[j][0],df2[j][2],df2[j][3],'expected sequence',seq[0][i],seq[1][i])
                
                if df2[j][1] not in q1:
                    vis.append(ch)
                    q2_4.append(df2[j][1]+'--'+'('+str(m)+')'+' '+bdic[b])
                    k=1
                    c=1
            j=j+1    
f.write('MSRIT AI QUETION PAPER 2018----FOR THE FIRST TIME SET BY AN AI')
f.write('\n')
f.write('\n')
f.write('\n')
f.write('UNIT 1')
f.write('\n')
f.write('\n')
        
k=1
for i in range(len(q1)):
    f.write(str(k)+'.'+q1[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('OR')
f.write('\n')
f.write('\n')
for i in range(len(q2)):
    f.write(str(k)+'.'+q2[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('\n')
f.write('\n')
f.write('UNIT 2')
f.write('\n')
f.write('\n')
for i in range(len(q1_1)):
    f.write(str(k)+'.'+q1_1[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('OR')
f.write('\n')
f.write('\n')
for i in range(len(q2_1)):
    f.write(str(k)+'.'+q2_1[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('\n')
f.write('\n')
f.write('UNIT 3')
f.write('\n')
f.write('\n')
for i in range(len(q1_2)):
    f.write(str(k)+'.'+q1_2[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('OR')
f.write('\n')
f.write('\n')
for i in range(len(q2_2)):
    f.write(str(k)+'.'+q2_2[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('\n')
f.write('\n')
f.write('UNIT 4')
f.write('\n')
f.write('\n')
for i in range(len(q1_3)):
    f.write(str(k)+'.'+q1_3[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('OR')
f.write('\n')
f.write('\n')
for i in range(len(q2_3)):
    f.write(str(k)+'.'+q2_3[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('\n')
f.write('\n')
f.write('UNIT 5')
f.write('\n')
f.write('\n')
for i in range(len(q1_4)):
    f.write(str(k)+'.'+q1_4[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.write('OR')
f.write('\n')
f.write('\n')
for i in range(len(q2_4)):
    f.write(str(k)+'.'+q2_4[i])
    f.write('\n')
    f.write('\n')
    k=k+1
f.close()    
    
        

    
    
    
    
    

