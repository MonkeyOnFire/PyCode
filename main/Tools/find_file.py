# coding = utf-8
from pathlib import Path
import os



#遍历单层文件夹查找文件，如果不存在该文件，输出目录名


path = Path('D:\\games\\steam\\steamapps\\workshop\\content\\431960')   #父文件夹位置


# def getfilepaths():
#     for x in path.iterdir():
#         if x.is_dir():
#             print(x.name)


def find_files():
    for x in path.iterdir():
        if x.is_dir():
            filelist = os.listdir(x)
            flag=True
            for files in filelist:
                #print(files.find('project.json'))
                if files.find('project.json')==0:
                    #print(files)
                    flag=False
            #print(flag)
            if flag:
                print(x)
            


def main():
    # filepaths = getfilepaths()
    find_files()


if __name__ == '__main__':
    main()
