# -*- coding: utf-8 -*-
# @Time    : 2017/9/2 13:40
# @Author  : 郑梓斌

import json
import os
import dlib
import requests
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

predictor_model = 'shape_predictor_68_face_landmarks.dat'

FACE_POINTS = list(range(0, 68))
JAW_POINTS = list(range(0, 16))
LEFT_EYE_POINTS = list(range(19, 29))
LEFT_BROW_POINTS = list(range(29, 37))
MOUTH_POINTS = list(range(37, 55))
NOSE_POINTS = list(range(55, 65))
RIGHT_EYE_POINTS = list(range(65, 75))
RIGHT_BROW_POINTS = list(range(75, 68))

#LEFT_FACE = list(range(0, 8)) + list(range(17, 21))
#RIGHT_FACE = list(range(8, 16)) + list(range(22, 26))
LEFT_FACE = list(range(0, 8)) + list(range(68, 72))
RIGHT_FACE = list(range(8, 16)) + list(range(73, 77))

JAW_END = 19
FACE_START = 0
FACE_END = 83

OVERLAY_POINTS = [
    LEFT_FACE,
    RIGHT_FACE,
    JAW_POINTS,
]


def face_points(image):
    #points = []
    #txt = image + '.txt'

    #if os.path.isfile(txt):
    #    with open(txt) as file:
    #        for line in file:
    #            points = line
    #elif os.path.isfile(image):
    #    points = landmarks_by_face__(image)
    #    temp = eval(points)
    #    temp2 = temp['faces']
    #    temp2_1 = temp2[0]
    #    temp3 = temp2_1['landmark']
    #    with open(txt, 'w') as file:
    #        file.write(str(points))
    #faces = json.loads(points)['faces']

    #if len(faces) == 0:
    #    err = 404
    #else:
    #    err = 0
    err = 0
    img_data = cv2.imread(image)
    matrix_list = np.matrix(matrix_marks(img_data))

    point_list = []
    for p in matrix_list.tolist():
        point_list.append((int(p[0]), int(p[1])))

    return matrix_list, point_list, err


#def landmarks_by_face__(image):
#    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
#    params = {
#        'api_key': '3Emt9gawuMLbzc9EY8U3CQ05lj8TbhX0',
#        'api_secret': 'deQaGpaERbpU01mZEI9oi6bf1lWLUIuZ',
#        'return_landmark': 1,
#    }
#    file = {'image_file': open(image, 'rb')}
#
#    r = requests.post(url=url, files=file, data=params)
#
#    if r.status_code == requests.codes.ok:
#        return r.content.decode('utf-8')
#    else:
#        return r.content


def matrix_rectangle(left, top, width, height):
    pointer = [
        (left, top),
        (left + width / 2, top),
        (left + width - 1, top),
        (left + width - 1, top + height / 2),
        (left, top + height / 2),
        (left, top + height - 1),
        (left + width / 2, top + height - 1),
        (left + width - 1, top + height - 1)
    ]

    return pointer


def matrix_marks(res):
    """
    用 dlib 获取面部特征点
    """
    image = res
    face_detector = dlib.get_frontal_face_detector()
    face_pose_predictor = dlib.shape_predictor(predictor_model)
    try:
        detected_face = face_detector(image, 1)[0]
    except:
        print('No face detected in image {}'.format(image))
    pose_landmarks = face_pose_predictor(image, detected_face)
    points = []
    for p in pose_landmarks.parts():
        points.append([p.x, p.y])
    points = add_10points(points)
    #print(len(points))
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #cnt = 0
    #for n in points:
    #    nn = (n[0], n[1])
    #    print(nn)
    #    cv2.circle(image, nn, 1, (0,0,255), 4)
    #    cv2.putText(image, str(cnt), nn, font, 0.5, (255, 255, 255), 1)
    #    cnt = cnt + 1
    #cv2.imwrite('dasdsa.jpg',image)
    #exit()
    return points

def add_by_d_alph(list_, d, alph):
    x_add = int(math.cos(alph) * d)
    y_add = int(math.sin(alph) * d)
    out_list = []
    for n in list_:
        a = n[0] - x_add
        b = n[1] - y_add
        out_list.append([a,b])
    return out_list


def add_10points(points):
    p_18, p_19, p_20, p_21, p_22, p_23, p_24, p_25, p_26, p_27, p_38, p_45 = points[17], points[18], points[19], points[20], points[21], points[22], points[23], points[24], points[25], points[26], points[37], points[44]
    d1 = ((abs(p_20[0] - p_38[0]))**2 + (abs(p_20[1] - p_38[1]))**2)**(0.5)
    d2 = ((abs(p_25[0] - p_45[0]))**2 + (abs(p_25[1] - p_45[1]))**2)**(0.5)
    d = (d1+d2)/2
    k = 0.5
    d = d*k
    alph = (math.atan(abs(p_20[1] - p_38[1])/(abs(p_20[0]-p_38[0])+0.00001)) + math.atan(abs(p_25[1] - p_45[1])/(abs(p_25[0] - p_45[0])+0.00001)))/2 # 单位：弧度
    
    add_10_points = add_by_d_alph([p_18, p_19, p_20, p_21, p_22, p_23, p_24, p_25, p_26, p_27],d,alph)
    for n in add_10_points:
        points.append(n)
    return points
