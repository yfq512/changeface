import os
import re
import time
import random
import base64
import ModuleTest2
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
        try:
            imgdata1 = request.form.get('imgdata1')
            imgname1 = request.form.get('imgname1')
            imgdata2 = request.form.get('imgdata2')
            imgname2 = request.form.get('imgname2')
            alpha = request.form.get('alpha') # 0.85
            mat_multiple = request.form.get('mat_multiple') # 0.9

            alpha = float(alpha)
            mat_multiple = float(mat_multiple)

            temp_root = 'temp'

            imgdata1 = re.sub(r'data:image/[a-zA-Z]*;base64,', "",imgdata1) # 适配js库base64
            imgdata1 = imgdata1.replace("data:image/jpeg;base64,", "") # 适配多种图像类型
            imgdata1 = base64.b64decode(imgdata1)
            img_stye1 = '.' + imgname1.split('.')[-1]
            img_path_temp1 = getRandomSet(15) + img_stye1
            img_path_temp1 = os.path.join(temp_root, img_path_temp1)
            f1 = open(img_path_temp1, 'wb')
            f1.write(imgdata1)
            f1.close()

            imgdata2 = re.sub(r'data:image/[a-zA-Z]*;base64,', "",imgdata2) # 适配js库base64
            imgdata2 = imgdata2.replace("data:image/jpeg;base64,", "") # 适配多种图像类型
            imgdata2 = base64.b64decode(imgdata2)
            img_stye2 = '.' + imgname2.split('.')[-1]
            img_path_temp2 = getRandomSet(15) + img_stye2
            img_path_temp2 = os.path.join(temp_root, img_path_temp2)
            f2 = open(img_path_temp2, 'wb')
            f2.write(imgdata2)
            f2.close()

            rand_name = getRandomSet(15) + '.jpg'
            out_img_path = os.path.join('/opt/docker/python/imgs_facemerge', rand_name)

            ModuleTest2.main(img_path_temp1, img_path_temp2, out_img_path, alpha, mat_multiple)
            os.remove(img_path_temp1)
            os.remove(img_path_temp2)
            res = 'http://192.168.132.151:8801/' + 'imgs_facemerge/' + rand_name
            return {'sign':1, 'outimg':res}
        except:
            return {'sign':-1, 'outimg':''}
    else:
        return "<h1>Face merge!</h1>"

if __name__ == '__main__':
    host = '0.0.0.0'
    port = '8876'
    app.run(debug=True, host=host, port=port)
