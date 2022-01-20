# coding = utf-8

from PIL import Image
import piexif
from pathlib import Path
import datetime



def mod():

    #创建时间戳列表
    for x in range(200):
        global t_datetime
        t_datetime = t_datetime + datetime.timedelta(minutes=1)
        times.append(t_datetime.strftime('%Y:%m:%d %H:%M:%S'))

    paths = []

    #按名字给图片排序
    for x in p.iterdir():
        strPath = str(x)
        paths.append(strPath)

    paths.sort(key=sortKeys)

    #执行修改
    for x in paths:
        strPath = str(x)
        modtime(strPath)
        global timeIndex
        timeIndex = timeIndex + 1


def modtime(strpath):
    im = Image.open(strpath)
    try:
        exif_dict = piexif.load(im.info["exif"])
    except KeyError:
        print(strpath + " KeyError: 'exif'")

    try:
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = times[timeIndex].encode()
    except UnboundLocalError:
        print(strpath + "UnboundLocalError: local variable 'exif_dict' referenced before assignment")
    #print(strpath + "_____" + str(exif_dict))
    try:
        exif_bytes = piexif.dump(exif_dict)
    except (ValueError,UnboundLocalError):
        print(strpath + " 我也不知道为啥出这个异常")
    try:
        piexif.remove(strpath)
    except UnboundLocalError:
        print(strpath + " UnboundLocalError: local variable 'file_type' referenced before assignment")
    try:
        piexif.insert(exif_bytes, strpath)
        print("修改成功:",strpath)
    except (piexif._exceptions.InvalidImageDataError,UnboundLocalError):
        print(strpath + " piexif._exceptions.InvalidImageDataError")


def sortKeys(pstr:str):
    s=""
    n=""
    for x in pstr:

        if x.isdigit() :

            n = n + x
        elif x == ".":
            break
        else:

            s = s + x
    c = chr(int(n)+100)

    d = s+c

    #print("d是", d)
    return d



startTime = '2005:09:21 13:29:01'
p = Path("D:\\repertory\\私立高校的女教师们")
t_datetime = datetime.datetime.strptime(startTime, "%Y:%m:%d %H:%M:%S")
times = []
timeIndex = 0
mod()



