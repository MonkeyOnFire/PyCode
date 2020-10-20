# coding = utf-8
from pathlib import Path
import os
import shutil

#将文件夹内文件取到父文件夹


path = Path('D:\\repertory\\media\\1')   #父文件夹位置


# def getfilepaths():
#     for x in path.iterdir():
#         if x.is_dir():
#             print(x.name)


def mvfiles():
    for x in path.iterdir():
        if x.is_dir():
            filelist = os.listdir(x)
            for files in filelist:
                filename = os.path.splitext(files)[0] + os.path.splitext(files)[1]  # 读取文件名

                # print(filename)
                despath = os.path.join(path, filename)  # 获取源文件路径+ filename
                srcpath = os.path.join(x, filename)  # 获取移动后文件路径+ filename
                # print(srcpath)
                # print(despath)
                shutil.move(srcpath, despath)


def main():
    # filepaths = getfilepaths()
    mvfiles()


if __name__ == '__main__':
    main()
