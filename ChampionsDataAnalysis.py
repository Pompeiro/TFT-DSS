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

df = pd.read_csv("scaledChampionsdf.csv")

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


#################### Frames with champions that cost x

ChampionsThatCostOne = df.query("Cost == 1.0")
ChampionsThatCostOneList = ChampionsThatCostOne.T.values.tolist()


ChampionsThatCostOneDF = pd.DataFrame(ChampionsThatCostOneList).transpose()
ChampionsThatCostOneDF.columns = list(df.columns)


ChampionsThatCostTwo = df.query("Cost == 2.0")
ChampionsThatCostTwoList = ChampionsThatCostTwo.T.values.tolist()


ChampionsThatCostTwoDF = pd.DataFrame(ChampionsThatCostTwoList).transpose()
ChampionsThatCostTwoDF.columns = list(df.columns)


ChampionsThatCostThree = df.query("Cost == 3.0")
ChampionsThatCostThreeList = ChampionsThatCostThree.T.values.tolist()


ChampionsThatCostThreeDF = pd.DataFrame(ChampionsThatCostThreeList).transpose()
ChampionsThatCostThreeDF.columns = list(df.columns)


ChampionsThatCostFour = df.query("Cost == 4.0")
ChampionsThatCostFourList = ChampionsThatCostFour.T.values.tolist()


ChampionsThatCostFourDF = pd.DataFrame(ChampionsThatCostFourList).transpose()
ChampionsThatCostFourDF.columns = list(df.columns)


ChampionsThatCostFive = df.query("Cost == 5.0")
ChampionsThatCostFiveList = ChampionsThatCostFive.T.values.tolist()


ChampionsThatCostFiveDF = pd.DataFrame(ChampionsThatCostFiveList).transpose()
ChampionsThatCostFiveDF.columns = list(df.columns)


##########################


data = [
    ["AS", "DMG", "DPS", "HP", "    MEANHP"],
]


def plotChampionsThatCost(ChampionsThatCostXDF=ChampionsThatCostFiveDF):
    for i in range(0, 11, 1):
        data.append(
            (
                r"$\bf{" + ChampionsThatCostXDF.Champion[i] + "}$",
                [
                    [
                        ChampionsThatCostXDF.AS[i],
                        ChampionsThatCostXDF.DMG[i],
                        ChampionsThatCostXDF.DPS[i],
                        ChampionsThatCostXDF.HP[i],
                        ChampionsThatCostXDF.MEANHP[i],
                    ]
                ],
            )
        )


plotChampionsThatCost(ChampionsThatCostFourDF)

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
