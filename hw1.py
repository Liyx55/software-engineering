# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:27:17 2021

@author: LiYX
"""
class maxium():
    '''
    初始化
    '''
    def __init__(self,numbers):
        self.numbers=numbers
        
    '''
    一维数组求最大子数组之和
    '''
    def sum1(self,numbers):
        max_sum = numbers[0]
        tmp_sum = 0
        for i in numbers:
            if tmp_sum < 0:
                tmp_sum = i
            else:
                tmp_sum += i
            max_sum = max(tmp_sum, max_sum)
        return max(0, max_sum)
    
    '''
    二维数组求最大子数组之和
    '''
    def sum2(self,numbers,row,column):
        p=[0]*row
        for i in range(len(p)):
            p[i]=[0]*column
        if(row==0 or column==0):
            return 0
        for i in range(row):
            for j in range(column):
                if(i==0):
                    if(j==0):
                        p[i][j]=numbers[i][j]
                    else:
                        p[i][j]=p[i][j-1]+numbers[i][j]
                else:
                    if(j==0):
                        p[i][j]=p[i-1][j]+numbers[i][j]
                    else:
                        p[i][j]=p[i][j-1]+p[i - 1][j]-p[i - 1][j - 1]+numbers[i][j]
        #maxium=numbers[0][0]
        sss=0
        if(column==1):
            for i in range(row):
                for j in range(i,row):      
                    if(i == 0):               
                        temp = p[j][column - 1]
                    else:              
                        temp = p[j][column - 1] - p[i - 1][column - 1]
                    if(sss<temp):
                        sss=temp
        else:
            for i in range(row):
                for j in range(i,row):
                    if (i == 0):
                        temp = p[j][column - 1]-p[j][column-2]
                    else:
                        temp = p[j][column - 1]-p[j][column-2]-p[i-1][column-1]+p[i-1][column-2]	
    				  #k=column-2
                    for k in range(column-2,-1,-1):
                        if(temp<0):
                            temp=0
                        if(i==0):
                            if(k==0):
                                temp+=p[j][k]
                            else:
                                temp+=p[j][k]-p[j][k-1]
                        else:
                            if(k==0):
                                temp+=p[j][k]-p[i-1][k]
                            else:
                                temp+=p[j][k]-p[j][k-1]-p[i-1][k]+p[i-1][k-1]
                        if(sss<temp):
                            sss=temp
                      
        return sss
    


if __name__ == '__main__':
    
    c=int(input('请选择文件输入(输入1);控制台输入(输入2):'))
    #文件作为输入
    if(c==1):
        d=int(input('请选择测试一维数组(输入1);二维数组(输入2):'))
        if(d==1):     
            with open('data.txt', 'r') as f1:
                n = f1.read()
                a = [ int(x) for x in n.split(' ')]    # 把文件内容转为列表
                L1=maxium(a)
                print('一维数组的最大子数组之和为：',L1.sum1(a))
        if(d==2):
            file1 = open('data2.txt', 'r')#按数组形式存贮
            row_ =file1.readlines()
            a2 = []
            for i in range(len(row_)):
                column_list = row_[i].strip().split(" ")  # 每一行split后是一个列表
                a2.append(column_list)                # 在末尾追加到list_source
            for i in range(len(a2)):  # 行数
                for j in range(len(a2[i])):  # 列数
                    a2[i][j]=int(a2[i][j])
                    #print(a2[i][j])
            file1.close()
            row=int(len(a2))
            column=int(len(a2[0]))
            #print(a2)
            L2=maxium(a2)
            print('二维数组的最大子数组之和为：',L2.sum2(a2,row,column))
        if(d!=1 and d!=2):
            print('输入错误！')
    #控制台作为输入          
    if(c==2):
        #print()
        e=int(input('请选择测试一维数组(输入1);二维数组(输入2):'))
        if(e==1):         
            n=input('请输入一维数组的个数为：')
            arr = input("请输入{}个元素的值:".format(n))    #输入一个一维数组，每个数之间使空格隔开
            num = [int(n) for n in arr.split()]    #将输入每个数以空格键隔开做成数组
            L3=maxium(num)
            print('一维数组的最大子数组之和为：',L3.sum1(num))
        if(e==2):
            nums = []
            rows = eval(input("请输入二维数组的行数："))
            columns = eval(input("请输入二维数组的列数："))
            #print("请输入第{}个元素的值：".format(rows*columns))
            kk=1
            for row in range(rows):
                nums.append([])#append精确插入一个元素，可以是元组也可以是序列。不可以超过一个或为空
                for column in range(columns):
                    num = eval(input("请输入第{}个元素的值：".format(kk)))
                    nums[row].append(num)
                    kk=kk+1
            #print(nums)
            L4=maxium(nums)
            print('二维数组的最大子数组之和为：',L4.sum2(nums,rows,columns))            #打印二维数组
        if(e!=1 and e!=2):
            print('输入错误！')
    if(c!=1 and c!=2):
        print('输入错误！')
    
    
    
 
    
    