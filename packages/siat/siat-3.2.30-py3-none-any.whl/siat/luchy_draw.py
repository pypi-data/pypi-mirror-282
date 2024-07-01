# -*- coding: utf-8 -*-

"""
本模块功能：幸运抽奖，仅限课堂案例演示用
创建日期：2024年6月29日
最新修订日期：
作者：王德宏 (WANG Dehong, Peter)
作者单位：北京外国语大学国际商学院
用途限制：仅限研究与教学使用，不可商用！商用需要额外授权。
特别声明：作者不对使用本工具进行证券投资导致的任何损益负责！
"""

#==============================================================================
#关闭所有警告
import warnings; warnings.filterwarnings('ignore')
import warnings; warnings.filterwarnings('ignore')

import pandas as pd
import pickle
import random
import datetime
import time
 
#==============================================================================
if __name__=='__main__':
    text="A B C"
    text_color='red'
    text_size=12
    delay=1
    
    typewriter(text,text_color='red',text_size=12,delay=1)        

def typewriter(text,text_color='blue',text_size=12,delay=1):
    from IPython.display import display_html
    
    text_html="<center><font size="+str(text_size)+" color="+text_color+">"+text
    display_html(text_html, raw=True)

    return

#==============================================================================

def pickle_write(df,pickle_path):
    with open(pickle_path, 'wb') as pickle_file:
        # 使用pickle模块的dump函数写入对象
        pickle.dump(df,pickle_file)     

if __name__=='__main__':
    file_path="S:\北外工作-24春\小学期-人大\学生名单\student_list.xlsx"
    pickle_path="student_list.pkl"
    skiprows=1
    column='Name'
    
    namelist_get(file_path,skiprows=1,column='Name',pickle_path="student_list.pkl")
    
def lucky_draw_initialize(file_path,skiprows=1,column='Name',pickle_path="student_list.pkl"):
    """
    功能：读入带有指定路径的Excel文件file_path，跳过前skiprows行
    Excel文件结构：抽奖名单字段为'Name'，字段位于第2行
    输出：存入pickle文件student_list.pkl
    """
    
    df = pd.read_excel(file_path,skiprows=skiprows)  
    
    df1=df[[column]].copy()  
    
    todaydt = str(datetime.date.today())
    df1['Date']=todaydt
    df1['Lucky']=0
    df1['Absent']=0
    df1['Answer']=0
    
    #排序
    df1.sort_values(by=[column,'Date','Lucky','Absent','Answer'],inplace=True)
    df1.reset_index(drop=True,inplace=True)
    
    pickle_write(df1,pickle_path)
    
    return

#==============================================================================
if __name__=='__main__':
    pickle_path="student_list.pkl"
    
    df=pickle_read(pickle_path)

def pickle_read(pickle_path="student_list.pkl"):   
    with open(pickle_path,'rb') as pickle_file:
        df = pickle.load(pickle_file)
    return df

#==============================================================================



def pickle_append(df,column='Name',pickle_path="student_list.pkl"):
    df_tmp=pickle_read(pickle_path)
    df_new=pd.concat([df_tmp,df])
    
    df_new.sort_values(by=[column,'Date'],inplace=True)
    
    pickle_write(df_new,pickle_path)
    
    return

#==============================================================================
if __name__=='__main__':
    alist=["A","B","C","D"]
    
    for i in range(4):
        print(random_select(alist))


def random_select(alist):
    return random.choice(alist)

#==============================================================================

if __name__=='__main__':
    prompt="Is the lucky person here in class?"
    
    read_yes_no(prompt)

    
def read_yes_no(prompt, default=None):
    if default is None:
        prompt += " [yes/no] "
    else:
        prompt += " [yes/no] (default: %s) " % ('yes' if default else 'no')
    while True:
        user_input = input(prompt).lower()
        if user_input in ['', 'yes', 'y', 'true']:
            return True
        elif user_input in ['no', 'n', 'false']:
            return False
        elif user_input == '' and default is not None:
            return default
        else:
            print("Please enter 'yes' or 'no' (or 'y'/'n').")
            
    return

#==============================================================================
if __name__=='__main__':
    draw_limit=2
    absent_limit=2
    column='Name'
    pickle_path="student_list.pkl"
    
    lucky_draw()
    df=pickle_read(pickle_path)
    

def lucky_draw(draw_limit=2,absent_limit=2,column='Name',pickle_path="student_list.pkl"):
    """
    draw_limit=2：整个课程每人最多2次抽签机会
    absent_limit=2：整个课程每人最多缺席2次，超过就丧失抽签资格
    """
    df=pickle_read(pickle_path)

    alist=list(set(list(df[column])))    
    
    found=False
    todaydt = str(datetime.date.today())
    prompt="*** Is the lucky person here on site?"
    prompt2="*** Do you expect to pass?"
    
    while True:
        while True:
            aname=random_select(alist)
            
            adf=df[df[column]==aname]
            atimes=adf['Lucky'].sum()
            aonsite=adf['Absent'].sum()
            
            if atimes < draw_limit and aonsite <= absent_limit:
                #检查今日是否被抽中过
                drew_today=False
                try:
                    adf_today=adf[adf['Date']==todaydt]
                    if len(adf_today) > 0:
                        if adf_today['Lucky'].sum() > 0 or adf_today['Absent'].sum() > 0:
                            drew_today=True
                except: pass
                
                if not drew_today:                    
                    found=True
                    break
                else: continue
            else:
                continue

        if not found:  
            print("Congratulations! all person has been lucky for",limit,"times")
        else:
            """
            print("\nThe lucky person is ",end='')
            typewriter(aname,delay=1) 
            """
            typewriter(text=aname,text_color='blue',text_size=12,delay=1)
            
            #print('')
            onsite=read_yes_no(prompt)
            #是否到场
            if onsite: absent=0
            else: absent=1
            
            onpass=False; answer=0
            if onsite:            
                onpass=read_yes_no(prompt2)
                #是否pass
                if onpass: answer=0
                else: answer=1 
            
            #只要抽中，不论是否到场都记录
            row=pd.Series({column:aname,'Date':todaydt,'Lucky':1,'Absent':absent,'Answer':answer})
            try:
                df=df.append(row,ignore_index=True)        
            except:
                df=df._append(row,ignore_index=True)
                            
            if onsite and not onpass:
                #到场且不pass，结束本轮抽签
                break
            else:
                #未到场或pass，继续抽签
                continue
    
    df.sort_values(by=[column,'Date'],inplace=True)
    pickle_write(df,pickle_path)
    
    return

#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================        







    


#==============================================================================#==============================================================================
#==============================================================================#==============================================================================
#==============================================================================#==============================================================================

#==============================================================================
