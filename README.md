## changeface
基于图像的人脸替换. 
### 该项目在 https://github.com/gyp03/yry 基础上进行优化
## 效果
<img src="https://github.com/yfq512/changeface/blob/master/images/1.jpg" width="200" height="200" >+
<img src="https://github.com/yfq512/changeface/blob/master/images/2.jpg" width="200" height="200" >=
<img src="https://github.com/yfq512/changeface/blob/master/images/output.jpg" width="200" height="200" >
## 环境
该项目无需*特殊*环境，需要时可参考环境文件：requirements.txt
## 运行
1. 在 https://console.faceplusplus.com.cn/dashboard 上注册API  
2. 在core/recognizer.py > def landmarks_by_face__函数中的api_key，api_secret替换为自己的  
3. 运行:ModuleTest.py
## 展望
1. 将face++的API换成开源的脸部关键点提取算法。
2. 生成的图像有时会有黑色像素块。
# 声明：该项目仅用做学习交流，若用于其他途径而产生的法律责任请自行承担
