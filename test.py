import os
for info in os.listdir(r'E:\python_rr\test_rr\逐个读取文件\re'):
    domain = os.path.abspath(r'E:\python_rr\test_rr\逐个读取文件\re')
    info = os.path.join(domain,info)
    info = open(info,'r')
    print(info.imread())
    info.close()