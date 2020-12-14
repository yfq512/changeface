# -*- coding: utf-8 -*-
# @Time    : 2017/9/2 13:40
# @Author  : 郑梓斌

import core

def main(src_img_path, dst_img_path, out_img_path, alpha, mat_multiple):
    core.face_merge(src_img=src_img_path,
                    dst_img=dst_img_path,
                    out_img=out_img_path,
                    face_area=[50, 30, 500, 485],
                    alpha=alpha,
                    blur_detail_x=15,
                    blur_detail_y=10,
                    mat_multiple=mat_multiple)
