import shibie
import luyin

path=r'C:\Users\zhuqian\Desktop\s\myword.mp3'
luyin.rec(path)
text=shibie.identify(path)
print(text)

