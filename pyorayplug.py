import requests

class orayplug:
    def __init__(self, url, sn, key, time, proxies=None):
        self.url = url
        self.sn = sn
        self.key = key
        self.time = time
        self.proxies=proxies
    def query(self):
        try:
            r = requests.get(f'{self.url}/plug?sn={self.sn}&_api=get_plug_status&key={self.key}&time={self.time}', proxies=self.proxies)
            return {x['index']: bool(x['status']) for x in r.json()['response']}
        except:
            return []
    def set(self, index, on: bool):
        try:
            r = requests.get(f'{self.url}/plug?sn={self.sn}&_api=set_plug_status&key={self.key}&time={self.time}&index={index}&status={1 if on else 0}', proxies=self.proxies)
            return r.json()['result'] == 0
        except:
            return False