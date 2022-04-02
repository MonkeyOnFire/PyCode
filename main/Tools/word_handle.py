#分析爬虫log数据

f = open('C:\\code\\github\\XiaoShuoSpider\\ysbookstore\\ysbookstore\\log\\scrapy_2022_4_1_11_0.log', mode='r',encoding='utf-8')
f2 = open('result.txt',mode='x')

line = f.readline()             # 调用文件的 readline()方法  
while line:  
    if -1 != line.find('ERROR'):
        f2.write(line)
    line = f.readline() 
f.close()
f2.close()