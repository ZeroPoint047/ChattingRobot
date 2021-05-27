# -*- coding: utf-8 -*-
import requests, json, time, random
feature_text = '''
大家好！我是你的聊天机器人小乐。

我有问必答，有人会问我“今天深圳天气怎么样？”，也有人问我“你喜欢我吗？”
快来问我问题呀，欢迎来撩！

【温馨提示】如果你要删除自己输入的内容，要按两次删除，才可以删掉一个汉字奥！
（因为在计算机世界里，中文是占两个字符的！）
>'''
print(feature_text)
while True:
    user1 = input('>>>>:退出聊天请输入88:')
    if user1.strip() == '88':
        print('\n我走啦，下次见！')
        time.sleep(2)
        break
    elif user1=='':
        print('你还没说话呢，再输入一次吧！')
        time.sleep(1)
    else:
        time.sleep(1)
        userid = str(random.randint(1, 1000000000000000000000))
        apikey = '8e8494cc7d164abc97eb13610c480763'
        # 超过1w有风险，19-01-19
        tulingdata1 = json.dumps({"perception": {
            "inputText": {
                "text": user1
            },

        },
            "userInfo": {
                "apiKey": apikey,
                "userId": userid
            }
        })
        robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
        jsrobot1 = json.loads(robot1.text)['results'][0]['values']['text']
        print(jsrobot1)
        time.sleep(2)
