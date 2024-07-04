from isaac_analyzer.logging import getLogger
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch

logger = getLogger(__name__)


def plot_shop(shops: dict, title):
    values = [shops[key] for key in shops.keys()]
    labels = ["Greed", "Normal", "Skipped"]

    fig, plot = plt.subplots(nrows=1, ncols=1, layout="constrained", figsize=(9, 5))

    def func(pct, allvals):
        absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d})"

    plot.pie(
        values,
        labels=labels,
        colors=["yellowgreen", "green", "steelblue"],
        autopct=lambda pct: func(pct, values),
        labeldistance=None,
    )

    plot.legend(loc="upper right", bbox_to_anchor=(1.25, 1))

    fig.suptitle(title, size="x-large", weight="bold")
    logger.debug("Figure created successfully")

    return fig


def plot_curses(curses: dict, title):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)

    total_curses = curses["Total curses"]
    overall = [curses["Total curses"], curses["No Curse"]]
    labels = ["Curse", "No Curse"]
    explode = [0.1, 0]
    angle = -45

    def func(pct, allvals):
        absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d})"

    wedges, *_ = ax1.pie(
        overall,
        autopct=lambda pct: func(pct, overall),
        startangle=angle,
        labels=labels,
        explode=explode,
        colors=["darkred", "green"],
    )

    del curses["No Curse"]
    del curses["Total curses"]

    detail_values = [curses[key] / total_curses for key in curses.keys()]
    detail_labels = curses.keys()
    bottom = 1
    width = 0.2

    # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(detail_values, detail_labels)])):
        if height > 0:
            bottom -= height
            bc = ax2.bar(
                0,
                height,
                width,
                bottom=bottom,
                color="darkred",
                label=label,
                alpha=0.125 * j,
            )
            ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type="center")

    ax2.set_title("Curse Type")
    ax2.legend(loc="upper right", bbox_to_anchor=(1.25, 1))
    ax2.axis("off")
    ax2.set_xlim(-2.5 * width, 2.5 * width)

    # use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(detail_values)

    # draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(
        xyA=(-width / 2, bar_height),
        coordsA=ax2.transData,
        xyB=(x, y),
        coordsB=ax1.transData,
    )
    con.set_color([0, 0, 0])
    con.set_linewidth(4)
    ax2.add_artist(con)

    # draw bottom connecting line
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(
        xyA=(-width / 2, 0), coordsA=ax2.transData, xyB=(x, y), coordsB=ax1.transData
    )
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(4)

    fig.suptitle(title, size="x-large", weight="bold")
    return fig


def plot_deals(deals, chances, title):
    logger.debug("Starting plot_deals function")
    logger.debug(f"Deals: {deals}")
    logger.debug(f"Chances: {chances}")
    logger.debug(f"Title: {title}")

    fig, plots = plt.subplots(nrows=1, ncols=2, layout="constrained", figsize=(9, 5))

    ### Chances Plot
    chances_plot = plots[0]
    logger.debug("Creating chances plot")

    # Plotting the stacked bar chart
    hit_bars = chances_plot.bar(
        chances["buckets"], chances["hits"], label="Hits", color="green"
    )
    miss_bars = chances_plot.bar(
        chances["buckets"],
        chances["misses"],
        bottom=chances["hits"],
        label="Misses",
        color="red",
    )

    # Adding labels and title
    chances_plot.set_xlabel("Deal chance")
    chances_plot.set_ylabel("Count")
    chances_plot.set_title("Hit or Miss of a deal based on chance")
    chances_plot.legend()
    logger.debug("Chances plot created")

    for i in range(len(chances["buckets"])):
        if chances["hits"][i] > 0:
            chances_plot.annotate(
                f'{chances["hit_percentages"][i]:.1f}%',
                xy=(
                    hit_bars[i].get_x() + hit_bars[i].get_width() / 2,
                    chances["hits"][i] / 2,
                ),
                xytext=(0, 0),  # No offset
                textcoords="offset points",
                ha="center",
                va="center",
                color="white",
            )
        if chances["misses"][i] > 0:
            chances_plot.annotate(
                f'{chances["miss_percentages"][i]:.1f}%',
                xy=(
                    miss_bars[i].get_x() + miss_bars[i].get_width() / 2,
                    chances["hits"][i] + chances["misses"][i] / 2,
                ),
                xytext=(0, 0),  # No offset
                textcoords="offset points",
                ha="center",
                va="center",
                color="white",
            )
    logger.debug("Annotations added to chances plot")

    ### Deals plot
    deal_plot = plots[1]
    logger.debug("Creating deals plot")

    def func(pct, allvals):
        absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d})"

    deal_plot.pie(
        deals["values"],
        labels=deals["labels"],
        colors=deals["colors"],
        autopct=lambda pct: func(pct, deals["values"]),
        labeldistance=None,
    )

    deal_plot.set_title("Deal type and count")
    deal_plot.legend(loc="upper right")
    logger.debug("Deals plot created")

    fig.suptitle(title, size="x-large", weight="bold")
    logger.debug("Figure created successfully")

    return fig
