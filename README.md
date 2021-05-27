# ChattingRobot
python聊天机器人
> 调用了讯飞的语音转化和图灵机器人的接口，相关api在官网查看[讯飞](https://console.xfyun.cn/services/lfasr)     -----[图灵](http://www.tuling123.com/member/robot/index.jhtml)
* 聊天小狮子完整版.py  是用户说话，机器人语音回复，并有图形界面，要装齐插件
* 聊天机器人(文字输入输出).py 是用户文字输入聊天信息，机器人以纯文字的形式回复，不需要其他插件，只需要请求requests的插件
## 基本逻辑
### 一、录音

*   利用pyaudio来开启麦克风录音功能，若python没有安装这个包，请在控制台终端输入
> pip install pyaudio

> **提示：**如果安装不成功，请查看[解决办法](https://blog.csdn.net/jocker_775065019/article/details/107458134)这篇文章

### 二、识别录音并转为文字
> 实时语音转换还在开发中，目前是先将声音录下来，上传至讯飞，等待接受转化出的文字，一般两秒到三秒，有时候会有点慢
### 三、文字上传到图灵机器人接口

### 四、收到回复并播放声音
*   可以选择接受声音和接收纯文本，在图灵机器人的官网设置参数
*   利用playsound来开启系统播放音频功能，若python没有安装这个包，请在控制台终端输入
> pip install playsound

### 五、Python GUI界面
* 图片显示需要装处理图片的库
> pip install pillow
