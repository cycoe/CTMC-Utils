#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Style(object):

    def __init__(self):
        # Some default value for figure properties
        self._line_width = 1
        self._line_color = None
        self._title_size = 24
        self._axis_label_size = 16
        self._tick_label_size = 16
        self._legend_size = 16

    def __str__(self):
        pass

    def set_line_width(self, line_width):
        self._line_width = line_width
        return self

    def set_line_color(self, colors):
        self._line_color = colors
        return self

    def set_title_size(self, size):
        self._title_size = size
        return self

    def set_axis_label_size(self, size):
        self._axis_label_size = size
        return self

    def set_tick_label_size(self, size):
        self._tick_label_size = size
        return self

    def set_legend_size(self, size):
        self._legend_size = size
        return self
