# -*- coding: utf-8 -*-
# @Time    : 2017/9/2 13:40
# @Author  : 郑梓斌

import json
import os
import dlib
import requests
import numpy as np
import cv2

predictor_model = 'shape_predictor_68_face_landmarks.dat'

FACE_POINTS = list(range(0, 68))
JAW_POINTS = list(range(0, 16))
LEFT_EYE_POINTS = list(range(19, 29))
LEFT_BROW_POINTS = list(range(29, 37))
MOUTH_POINTS = list(range(37, 55))
NOSE_POINTS = list(range(55, 65))
RIGHT_EYE_POINTS = list(range(65, 75))
RIGHT_BROW_POINTS = list(range(75, 68))

LEFT_FACE = list(range(0, 8)) + list(range(17, 21))
RIGHT_FACE = list(range(8, 16)) + list(range(22, 26))

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

    return points
