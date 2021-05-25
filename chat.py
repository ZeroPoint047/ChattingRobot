import shibie
import luyin
import requests, json, time, random
from playsound import playsound
from threading import Thread
def asyn(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper
path=r'C:\Users\zhuqian\Desktop\s\myword.mp3'
@asyn
def chatting():
    
    #录音
    luyin.rec(path)
    #语音识别
    text=shibie.identify(path)
    print(text)

    userid = str(random.randint(1, 1000000000000000000000))
    apikey = 'ef9722561c97454e9c5d661f0fb9aac1'
            
    tulingdata1 = json.dumps({
                "perception": {
                "inputText": {
                    "text": text
                },

            },
                "userInfo": {
                    "apiKey": apikey,
                    "userId": userid
                }
    })
    robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
    jsrobot1 = json.loads(robot1.text)['results'][0]['values']['voice']
    jsrobot2 = json.loads(robot1.text)['results'][1]['values']['text']
    print(jsrobot2)
    playsound(jsrobot1)
    global flag
    flag=0
    print(flag)
    time.sleep(2)





