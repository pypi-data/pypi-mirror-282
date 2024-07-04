from isaac_analyzer.logging import getLogger
from isaac_analyzer.run_loader import load_run_file
from isaac_analyzer.plotter import plot_deals, plot_curses, plot_shop
from os.path import join
from glob import glob
from PIL import Image

logger = getLogger(__name__)

def get_shop_details(run):
    logger.debug("Calculating shop greed and visiting rate.")
    shops = {"visited_boss": 0, "visited": 0, "skipped": 0}

    for floor in run["floors"]:
        if "shop" in floor:
            if floor["shop"]["visited"]:
                if "boss" in floor["shop"]:
                    shops["visited_boss"] += 1
                else:
                    shops["visited"] += 1
            else:
                shops["skipped"] += 1

    logger.debug(f"Shop details: {shops}")
    return shops

def get_curse_distribution(run):
    logger.debug("Calculating curse distribution for run.")
    curses = {
        "Curse of the Blind": 0,
        "Curse of Darkness": 0,
        "Curse of the Lost": 0,
        "Curse of the Maze": 0,
        "Curse of the Unknown": 0,
        "Curse of the Labyrinth": 0,
        "Curse of the Cursed": 0,
        "Curse of the Giant": 0,
        "No Curse": 0,
        "Total curses": 0,
    }

    for floor in run["floors"]:
        curse_type = floor.get("curseType", "No Curse")
        curses[curse_type] += 1
        if curse_type != "No Curse":
            curses["Total curses"] += 1

    logger.debug(f"Curse distribution: {curses}")
    return curses

def get_deal_type(run):
    logger.debug("Calculating deal types for run.")
    deals = {"total": 0, "angel": 0, "devil": 0}

    for floor in run["floors"]:
        if "deal" in floor and floor["deal"]["type"]:
            deal_type = floor["deal"]["type"]
            deals[deal_type] += 1
            deals["total"] += 1

    logger.debug(f"Deal types calculated: {deals}")
    return deals

def get_deal_chances(run):
    logger.debug("Calculating deal chances for run.")
    deal_buckets = {
        "<0.355": {"hit": 0, "miss": 0},
        "<0.755": {"hit": 0, "miss": 0},
        ">0.755": {"hit": 0, "miss": 0},
    }

    for floor in run["floors"]:
        if "deal" in floor:
            chance = floor["deal"]["chance"]
            deal_type_present = bool(floor["deal"]["type"])
            bucket = "<0.355" if chance <= 0.355 else "<0.755" if chance <= 0.755 else ">0.755"
            deal_buckets[bucket]["hit" if deal_type_present else "miss"] += 1

    logger.debug(f"Deal chances calculated: {deal_buckets}")
    return deal_buckets

def analyze_run_file(run_file):
    logger.info(f"Analyzing run file with run number {run_file['run_number']}.")
    for run in run_file["runs"]:
        analytics = {
            "deals": get_deal_type(run),
            "dealChance": get_deal_chances(run),
            "curses": get_curse_distribution(run),
            "shops": get_shop_details(run),
        }
        run["analytics"] = analytics
    logger.debug(f"Run file analysis complete: {run_file}")
    return run_file

def analyze_single_run(file_path, output_path):
    logger.info(f"Analyzing single run from file: {file_path}")
    run_file = load_run_file(file_path)
    analyzed_run_file = analyze_run_file(run_file)
    logger.info(f"Single run analysis complete. Results: {analyzed_run_file}")
    # Additional code to save or process analyzed_run_file can be added here

def analyze_runs(directory_path, output_path):
    logger.info(f"Analyzing all runs in directory: {directory_path}")
    yaml_files = glob(join(directory_path, "*.y*ml"))
    analyzed_runs = []

    for yaml_file in yaml_files:
        logger.info(f"Loading run file: {yaml_file}")
        run_file = load_run_file(yaml_file)
        analyzed_run = analyze_run_file(run_file)
        analyzed_runs.append(analyzed_run)
        logger.info(f"Run file {yaml_file} analyzed.")

    logger.info("All run files analyzed. Generating plots.")
    generate_plots(analyzed_runs, output_path)
    logger.info("Plot generation complete.")

def generate_plots(analyzed_runs, output_path):
    generate_deal_plot(analyzed_runs, output_path)
    generate_curses_plot(analyzed_runs, output_path)
    generate_shop_plot(analyzed_runs, output_path)
    combine_plots(output_path)

def combine_plots(output_path):
    logger.info("Combining plots into a single image.")
    image1 = Image.open(join(output_path, "deals.png"))
    image2 = Image.open(join(output_path, "curses.png"))
    image3 = Image.open(join(output_path, "shops.png"))

    height = image1.height + image2.height + image3.height
    width = max(image1.width, image2.width, image3.width)

    combined = Image.new("RGB", (width, height))
    combined.paste(image1, (0, 0))
    combined.paste(image2, (0, image1.height))
    combined.paste(image3, (0, image1.height + image2.height))

    combined.save(join(output_path, "combined.png"))
    logger.info("Combined plot saved.")

def generate_shop_plot(analyzed_runs, output_path):
    logger.info("Generating shop plot.")
    shops = {"visited_boss": 0, "visited": 0, "skipped": 0}
    for analyzed_run in analyzed_runs:
        for run in analyzed_run["runs"]:
            shops = add_dicts(shops, run["analytics"]["shops"])

    shop_figure = plot_shop(shops, title="Shops (June 2024)")
    output_file = join(output_path, "shops.png")
    shop_figure.savefig(output_file)
    logger.info(f"Shop plot saved to {output_file}")


def generate_curses_plot(analyzed_runs, output_path):
    logger.info("Generating curses plot.")
    curses = {
        "Curse of the Blind": 0,
        "Curse of Darkness": 0,
        "Curse of the Lost": 0,
        "Curse of the Maze": 0,
        "Curse of the Unknown": 0,
        "Curse of the Labyrinth": 0,
        "Curse of the Cursed": 0,
        "Curse of the Giant": 0,
        "No Curse": 0,
        "Total curses": 0,
    }
    for analyzed_run in analyzed_runs:
        for run in analyzed_run["runs"]:
            curses = add_dicts(curses, run["analytics"]["curses"])

    curses_figure = plot_curses(curses, title="Curses (June 2024)")
    output_file = join(output_path, "curses.png")
    curses_figure.savefig(output_file)
    logger.info(f"Curses plot saved to {output_file}")


def add_dicts(dict1, dict2):
    result_dict = {}
    for key in dict1:
        result_dict[key] = dict1[key] + dict2[key]
    return result_dict


def generate_deal_plot(analyzed_runs, output_path):
    logger.info("Generating deal plot.")
    deal_count = [0, 0]
    deal_chances = {
        "<0.355": {"hit": 0, "miss": 0},
        "<0.755": {"hit": 0, "miss": 0},
        ">0.755": {"hit": 0, "miss": 0},
    }

    for analyzed_run in analyzed_runs:
        for run in analyzed_run["runs"]:
            deal_count[0] += run["analytics"]["deals"]["devil"]
            deal_count[1] += run["analytics"]["deals"]["angel"]
            for bucket in deal_chances:
                deal_chances[bucket]["hit"] += run["analytics"]["dealChance"][bucket][
                    "hit"
                ]
                deal_chances[bucket]["miss"] += run["analytics"]["dealChance"][bucket][
                    "miss"
                ]

    buckets = list(deal_chances.keys())
    hits = [deal_chances[bucket]["hit"] for bucket in buckets]
    misses = [deal_chances[bucket]["miss"] for bucket in buckets]
    totals = [hits[i] + misses[i] for i in range(len(buckets))]
    hit_percentages = [
        hits[i] / totals[i] * 100 if totals[i] != 0 else 0 for i in range(len(buckets))
    ]
    miss_percentages = [
        misses[i] / totals[i] * 100 if totals[i] != 0 else 0
        for i in range(len(buckets))
    ]

    deal_figure = plot_deals(
        deals={
            "labels": ["devil", "angel"],
            "values": deal_count,
            "colors": ["dimgray", "whitesmoke"],
        },
        chances={
            "labels": ("<= 35.5%", "<= 75.5%", ">= 75.5%"),
            "buckets": ("0% - 35.5%", "35.6% - 75.5%", "75.6% - 100%"),
            "hits": hits,
            "misses": misses,
            "hit_percentages": hit_percentages,
            "miss_percentages": miss_percentages,
        },
        title="Devil and Angel Deals (June 2024)",
    )
    output_file = join(output_path, "deals.png")
    deal_figure.savefig(output_file)
    logger.info(f"Deal plot saved to {output_file}")
