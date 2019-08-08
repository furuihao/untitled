import urllib.request

def head():
    headers = {'User_Agent': ''}
    response = urllib.request.Request('http://python.org/', headers=headers)
    html = urllib.request.urlopen(response)
    result = html.read().decode('utf-8')
    print(result)



def main():
    response = urllib.request.urlopen('http://www.baidu.com')
    result = response.read().decode('utf-8')
    print(result)


if __name__ == '__main__':
    main()