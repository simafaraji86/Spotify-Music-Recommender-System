import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Plots:

    def data_line_plot(self, x, y, xlabel, ylabel, title, colors = None, xticks_rotation = 0):
        fig = plt.figure(figsize=(15, 10))
        sns.lineplot(x=x, y=y, hue=colors, ci=None)
        plt.title(title, fontsize=20)
        plt.xlabel(xlabel, fontsize=14)
        plt.ylabel(ylabel, fontsize=14)
        plt.xticks(fontsize=12, rotation=xticks_rotation)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=12)
        plt.show()


    def data_scatter_plot(self, x, y, xlabel, ylabel, title, colors = None, xticks_rotation = 0):
        fig = plt.figure(figsize=(15, 10))
        sns.scatterplot(x=x, y=y, hue=colors, ci=None)
        plt.title(title, fontsize=20)
        plt.xlabel(xlabel, fontsize=14)
        plt.ylabel(ylabel, fontsize=14)
        plt.xticks(fontsize=12, rotation=xticks_rotation)
        plt.yticks(fontsize=12)
        plt.legend(fontsize=12)
        plt.show()
