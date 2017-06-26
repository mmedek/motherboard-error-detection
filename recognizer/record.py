# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:27:55 2017

@author: mmedek
"""

import imghdr
import sys


class Record:
    def __init__(self, input):

        self.path = input

        if (self.__checkJPEG() == False):
            sys.exit('Unrecognized image ' + input)
        else:
            if (self.__parseInput() == False):
                sys.exit('Wrong format of image. Use JPEG image')
            else:
                print('Image name ' + input + ' was successfully parsed')

            return None

    def __parseInput(self):
        "shape of input: BlueTooth_TX-55AS650B_%NH-4540390(35418).jpg"
        splitted = self.path.split("_")

        if (len(splitted) != 3):
            return False

        "BlueTooth"
        self.component = splitted[0]
        "TX-55AS650B"
        self.motherboard = splitted[1]
        identifier = splitted[2].rsplit('.', 1)[0]
        "%NH-4540390"
        self.photo_id = identifier.rsplit('(', 1)[0]
        "(35418)"
        self.photo_number = '(' + identifier.rsplit('(', 1)[1]
        "jpg"
        self.suffix = splitted[2].rsplit('.', 1)[1]
        self.full_path = self.path

        return True

    def __checkJPEG(self):
        try:
            type = imghdr.what(self.path)
        except:
            return False

        if (type == self.__CONST_JPG()):
            return True

        return False

    def __CONST_JPG(self):
        return "jpeg"