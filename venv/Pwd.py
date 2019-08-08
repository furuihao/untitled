# coding:utf-8
import itertools as its

for count in range(6,10,2):
    print("pass"+str(count)+".txt")
    #打开文件,追加
    file = open("pass"+str(count)+".txt","w")

    # file.write("sssssssssss")

    words ='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    r = its.product(words,repeat=count)

    # print(r)

    for i in r:
        # print(i)
        file.write("".join(i))
        file.write("".join("\n"))

print("生成结束")


