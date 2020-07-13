#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from Style import Style


class Plotter(Style):

    def __init__(self):
        super().__init__()
        # Initiate a figure and an ax
        self._figure = plt.figure()
        self._ax = self._figure.subplots()

    def __del__(self):
        plt.close(self._figure)

    def plot(self, data):
        self._ax.plot(*data, color=self._line_color, lw=self._line_width)
        return self

    def set_title(self, title, size=None):
        # We can use set_title_size method to set title size or set directly set
        # size with title
        if size:
            self._title_size = size
        self._ax.set_title(title, fontsize=self._title_size)
        return self

    def set_xlabel(self, xlabel, size=None):
        if size:
            self._axis_label_size = size
        self._ax.set_xlabel(xlabel, fontsize=self._axis_label_size)
        return self

    def set_ylabel(self, ylabel, size=None):
        if size:
            self._axis_label_size = size
        self._ax.set_ylabel(ylabel, fontsize=self._axis_label_size)
        return self

    def set_legend(self, show, *attrv, **attrkw):
        # WORKAROUND: There is so many attributions in legend face, so we use
        # attrv and attrkw to pass the attributions
        self._ax.legend(*attrv, **attrkw)
        return self

    def savefig(self, save_path):
        self._figure.savefig(save_path)
        return self


if __name__ == '__main__':
    import numpy as np
    from Color import Color

    xs = np.linspace(0, 1, 100)
    ys = np.sin(xs)
    plotter = Plotter()
    colors = Color(('r', 'g', 'b'))
    plotter.plot((xs, ys)).set_line_color(colors).set_title("sin(x)", 24).set_xlabel("x").set_ylabel("sin(x)").set_legend(True)
