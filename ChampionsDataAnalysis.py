# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:09:11 2020

@author: Janusz
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

df = pd.read_csv("champions_data_scaled.csv")

df.drop("Unnamed: 0", axis=1, inplace=True)


def radar_factory(num_vars, frame="circle"):
    """Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle' | 'polygon'}
        Shape of frame surrounding axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

    class RadarAxes(PolarAxes):

        name = "radar"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location("N")

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == "circle":
                return Circle((0.5, 0.5), 0.5)
            elif frame == "polygon":
                return RegularPolygon((0.5, 0.5), num_vars, radius=0.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def draw(self, renderer):
            """ Draw. If frame is polygon, make gridlines polygon-shaped """
            if frame == "polygon":
                gridlines = self.yaxis.get_gridlines()
                for gl in gridlines:
                    gl.get_path()._interpolation_steps = num_vars
            super().draw(renderer)

        def _gen_axes_spines(self):
            if frame == "circle":
                return super()._gen_axes_spines()
            elif frame == "polygon":
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(
                    axes=self,
                    spine_type="circle",
                    path=Path.unit_regular_polygon(num_vars),
                )
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(
                    Affine2D().scale(0.5).translate(0.5, 0.5) + self.transAxes
                )

                return {"polar": spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta


# Frames with champions that cost x

champions_that_cost_one = df.query("cost == 1.0")
champions_that_cost_one_list = champions_that_cost_one.T.values.tolist()


champions_that_cost_one_df = pd.DataFrame(champions_that_cost_one_list).transpose()
champions_that_cost_one_df.columns = list(df.columns)


champions_that_cost_two = df.query("cost == 2.0")
champions_that_cost_two_list = champions_that_cost_two.T.values.tolist()


champions_that_cost_two_df = pd.DataFrame(champions_that_cost_two_list).transpose()
champions_that_cost_two_df.columns = list(df.columns)


champions_that_cost_three = df.query("cost == 3.0")
champions_that_cost_three_list = champions_that_cost_three.T.values.tolist()


champions_that_cost_three_df = pd.DataFrame(champions_that_cost_three_list).transpose()
champions_that_cost_three_df.columns = list(df.columns)


champions_that_cost_four = df.query("cost == 4.0")
champions_that_cost_four_list = champions_that_cost_four.T.values.tolist()


champions_that_cost_four_df = pd.DataFrame(champions_that_cost_four_list).transpose()
champions_that_cost_four_df.columns = list(df.columns)


champions_that_cost_five = df.query("cost == 5.0")
champions_that_cost_five_list = champions_that_cost_five.T.values.tolist()


champions_that_cost_five_df = pd.DataFrame(champions_that_cost_five_list).transpose()
champions_that_cost_five_df.columns = list(df.columns)


##########################


data = [
    ["AS", "DMG", "DPS", "HP", "    MEANHP"],
]


def plot_champions_that_cost(champions_that_cost_x_df=champions_that_cost_five_df):
    for i in range(0, 11, 1):
        data.append(
            (
                r"$\bf{" + champions_that_cost_x_df.champion[i] + "}$",
                [
                    [
                        champions_that_cost_x_df.as_[i],
                        champions_that_cost_x_df.dmg[i],
                        champions_that_cost_x_df.dps[i],
                        champions_that_cost_x_df.hp[i],
                        champions_that_cost_x_df.mean_hp[i],
                    ]
                ],
            )
        )


plot_champions_that_cost(champions_that_cost_four_df)

N = len(data[0])
theta = radar_factory(N, frame="polygon")

spoke_labels = data.pop(0)
title, case_data = data[0]


fig, axes = plt.subplots(
    figsize=(20, 10), nrows=3, ncols=4, subplot_kw=dict(projection="radar")
)
fig.subplots_adjust(wspace=0.4, hspace=0.20, top=0.85, bottom=0.05)

colors = ["m", "r", "g", "b", "y"]
# Plot the four cases from the example data on separate axes
for ax, (title, case_data) in zip(axes.flat, data):
    ax.set_rgrids([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_title(
        title,
        weight="bold",
        size="medium",
        position=(0.5, 1.1),
        horizontalalignment="center",
        verticalalignment="center",
    )
    for d, color in zip(case_data, colors):
        ax.set_ylim(bottom=0)

        line = ax.plot(theta, d, color=color)

        ax.fill(theta, d, facecolor="y", alpha=0.25)

    ax.set_varlabels(spoke_labels)

# delete last plot because there are odd number of champions
ax = axes[2, 3]
ax.axis("off")

fig.text(
    0.5,
    0.965,
    "Tier 4 champions stats",
    horizontalalignment="center",
    color="black",
    weight="bold",
    size="large",
)

plt.show()
