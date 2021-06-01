# -*- coding: utf-8 -*-
import requests, json, time, random
import shibie
import luyin
from playsound import playsound
path=r'C:\Users\zhuqian\Desktop\s\myword.mp3'
def chat_word(text):
    if text=='':
        return wenzihuifu('。。。')
    else:
        return wenzihuifu(text)

def wenzihuifu(text):
    time.sleep(1)
    userid = str(random.randint(1, 1000000000000000000000))
    apikey = '8e8494cc7d164abc97eb13610c480763'
    # 100次 一天
    tulingdata1 = json.dumps(
        {
            "perception":
                {
                    "inputText":
                        {
                            "text": text
                        },

                },
            "userInfo": {
                "apiKey": apikey,
                "userId": userid
            }
        })
    robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
    jsrobot1=''
    jsrobot1 = json.loads(robot1.text)['results'][0]['values']['text']

    if jsrobot1!='':
        print(jsrobot1)
        return jsrobot1


def chat_speak(text):
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
    time.sleep(2)


def i_speak():
    # 录音
    luyin.rec(path)
    # 语音识别
    text=''
    text = shibie.identify(path)

    if text!='':
        return text
    else:
        return '。。。'