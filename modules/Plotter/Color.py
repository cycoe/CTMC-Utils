#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numbers
import random

class Color(object):
    """ A color generator
    """

    def __init__(self, colors):
        """ colors: a finite iterable container
        """
        super().__init__()
        self.__colors = list(colors)
        self.__size = len(colors)

    def __str__(self):
        return "A color generator with {}".format(self.__colors)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        """Get the next color
        Before the self.__index is used, it will be cut off with mod operation,
        ensure not out of range
        """
        self.__index = self.__index % self.__size
        color = self.__colors[self.__index]
        self.__index += 1
        return color

    def __getitem__(self, index):
        if isinstance(index, numbers.Integral):
            return self.__colors[index % self.__size]

    def all(self):
        return self.__colors

    def shuffle(self):
        """ Shuffle the colors in the generator
        """
        random.shuffle(self.__colors)


if __name__ == '__main__':
    colors = Color(['red', 'green', 'blue', 'black'])
    print(colors)
    for index in range(10):
        print(index, colors[index])

    colors.shuffle()
    color_iter = iter(colors)
    for index in range(10):
        print(index, next(color_iter))
