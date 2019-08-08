import urllib3
import requests



def get_info():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url = 'https://www.ixigua.com/i6718605439249992964/'
    try:
        res = requests.session().get(url, headers=headers, verify=False)
        json = res.json()
        print(json)

        # json = res.json()
        # data = json['data']
        # l = len(data)
        # self.countnow += l
        # self.max_behot_time = str(json['next']['max_behot_time'])
        # for d in data:
        #     self.rett.append(d)
        # if self.countnow >= self.maxcount:
        #     return
    except Exception as e:
        print(e)


def download(url):
    pass
    # print("downloading with urllib2")
    # # url = 'http://www.pythontab.com/test/demo.zip'
    # urllib3.util.request
    # f = urllib3.urlopen(url)
    # data = f.read()
    # with open("demo2.mp4", "wb") as code:
    #     code.write(data)

if __name__ == '__main__':
    # download("http://v9-default.ixigua.com/1aae12c5de4675368426e332eaaccca4/5d3d9ab2/video/m/22041947a5a04594b15808a290bc7b454eb1162d565800003e47c64820dd/?rc=am05Mzg5bnZwbjMzNjczM0ApQHRAbzs6NjMzMzgzMzM4NDUzNDVvQGg2dilAZzN3KUBmM3UpZHNyZ3lrdXJneXJseHdmOzpAYnNua2RvZmJoXy0tLy0vc3MtbyNvIzAtNi8yMi4uNC42NTQ2LTojbyM6YS1vIzpgLXAjOmB2aVxiZitgXmJmK15xbDojMy5e")
    get_info()
    # https: // www.ixigua.com / home / 83930454166 / hotsoon /