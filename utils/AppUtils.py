import os.path
import os
# 获取apk包的的路径
class AppUtils(object):
    def getApp(self):
        propath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        apkpath = propath + "\\apk"
        list = os.listdir(apkpath)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            path = os.path.join(apkpath, list[i])
            apkPage = path
            return apkPage
