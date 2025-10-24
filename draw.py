import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


def draw(box, items):
    for r in items:
        print(r)
    fig = plt.figure(figsize=box)
    ax = fig.add_subplot()
    for r in items:
        ax.add_patch(plt.Rectangle(r.orig, r.w, r.h, ec="r", alpha=0.5))
        ax.text(
            r.x + r.w / 2,
            r.y + r.h / 2,
            # "{} {:0.2}".format(r.v, r.area),
            str(r.v),
            ha="center",
            va="center",
        )
    plt.xlim(-1, box[0])
    plt.ylim(box[1], -1)
    plt.show()


def draw_vor(box, items):
    points = np.array([(r.x + r.w / 2, r.y + r.h / 2) for r in items])
    vor = Voronoi(points, qhull_options="Qz")
    fig = voronoi_plot_2d(vor, point_size=0, show_vertices=False)
    for r in items:
        plt.text(
            r.x + r.w / 2,
            r.y + r.h / 2,
            str(r.v),
            ha="center",
            va="center",
        )
    plt.xlim(-1, box[0])
    plt.ylim(box[1], -1)
    plt.show()
