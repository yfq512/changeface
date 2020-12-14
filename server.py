import os
import re
import time
import random
import base64
from flask import Flask,render_template,request

def getRandomSet(bits):
    num_set = [chr(i) for i in range(48,58)]
    char_set = [chr(i) for i in range(97,123)]
    total_set = num_set + char_set
    value_set = "".join(random.sample(total_set, bits))
    return value_set

app = Flask(__name__)

@app.route("/facemerge",methods = ['GET', 'POST'])

def face_merge():
    if request.method == "POST":
        imgdata1 = request.form.get('imgdata1')
        imgname1 = request.form.get('imgname1')
        imgdata2 = request.form.get('imgdata2')
        imgname2 = request.form.get('imgname2')
        alpha = request.form.get('alpha') # 0.85
        mat_multiple = request.form.get('mat_multiple') # 0.9

        alpha = float(alpha)
        mat_multiple = float(mat_multiple)

        imgdata1 = re.sub(r'data:image/[a-zA-Z]*;base64,', "",imgdata1) # 适配js库base64
        imgdata1 = imgdata1.replace("data:image/jpeg;base64,", "") # 适配多种图像类型
        imgdata1 = base64.b64decode(imgdata1)
        img_stye1 = '.' + imgname1.split('.')[-1]
        img_path_temp1 = getRandomSet(15) + img_stye1
        f1 = open(img_path_temp1, 'wb')
        f1.write(imgdata1)
        f1.close()

        imgdata2 = re.sub(r'data:image/[a-zA-Z]*;base64,', "",imgdata2) # 适配js库base64
        imgdata2 = imgdata2.replace("data:image/jpeg;base64,", "") # 适配多种图像类型
        imgdata2 = base64.b64decode(imgdata2)
        img_stye2 = '.' + imgname2.split('.')[-1]
        img_path_temp2 = getRandomSet(15) + img_stye2
        f2 = open(img_path_temp2, 'wb')
        f2.write(imgdata2)
        f2.close()
        print(img_path_temp1)
        print(img_path_temp2)
        return "<h1>Face merge!</h1>"
    else:
        return "<h1>Face merge!</h1>"

if __name__ == '__main__':
    host = '127.0.0.1'
    port = '8881'
    app.run(debug=True, host=host, port=port)
