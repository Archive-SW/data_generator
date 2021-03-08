#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
import os
import numpy as np
import datetime
import time
import sys
from sensor_msgs.msg import Image
from std_msgs.msg import String
import math

import image_converter as ic

class DataCollection():
    def __init__(self):
        self.img_cvt = ic.ImageConverter()

        path = sys.argv[1]
        self.path = path
        self.time_stamp = 0
        self.image_stamp = 0

    def recorder_cb(self, data):
        if self.time_stamp % 30 is 0:
            img = self.img_cvt.imgmsg_to_opencv(data)
            file_full_path = str(self.path)+ 'image_' + str(self.image_stamp) + '.png'
            cv2.imwrite(file_full_path, img)
            sys.stdout.write(file_full_path + '\r')
            self.image_stamp += 1
        self.time_stamp += 1
                                                      


def main():
    dc = DataCollection()

    rospy.init_node('data_collection')
    rospy.Subscriber('/camera/rgb/image_raw', Image, dc.recorder_cb)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nBye...")    


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ')
        exit('$ rosrun data_collection data_collection.py save_data_path')

    main()