import os
import requests
from hashlib import md5
from time import localtime
SavePath = "./musicFile"

def DownloadFile(mp3_url):
    try:
        if mp3_url is None or SavePath is None:
            print('参数错误')
            return None
        # 文件夹不存在，则创建文件夹
        folder = os.path.exists(SavePath)
        if not folder:
            os.makedirs(SavePath)
        # 读取MP3资源
        res = requests.get(mp3_url,stream=True)
        # 获取文件地址
        (urlPath,fileExt)=os.path.splitext(mp3_url)
        prefix = md5(str(localtime()).encode('utf-8')).hexdigest()
        fileName = prefix+fileExt
        file_path = os.path.join(SavePath, fileName)
        print('开始写入文件：', file_path)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)
        return SavePath+fileName
    except:
        print('下载错误')
        return None