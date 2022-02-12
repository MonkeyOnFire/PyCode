# coding = utf-8
from pathlib import Path
import os



# 清理wallpapaer engine壁纸目录用
# 遍历单层目录查找文件，如果不存在该文件，输出目录名


path = Path('C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\431960')   #父文件夹位置


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
