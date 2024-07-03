from isaac_analyzer.logging import getLogger
import matplotlib.pyplot as plt
import numpy as np

logger = getLogger(__name__)


def plot_deals(deals, chances, title):
    logger.debug("Starting plot_deals function")
    logger.debug(f"Deals: {deals}")
    logger.debug(f"Chances: {chances}")
    logger.debug(f"Title: {title}")

    fig, plots = plt.subplots(nrows=1, ncols=2, layout="constrained", figsize=(10, 4))

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
