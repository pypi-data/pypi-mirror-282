from isaac_analyzer.logging import getLogger
from isaac_analyzer.run_loader import load_run_file
from isaac_analyzer.plotter import plot_deals
from os.path import join
from glob import glob

logger = getLogger(__name__)


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
            if chance <= 0.355:
                bucket = "<0.355"
            elif chance <= 0.755:
                bucket = "<0.755"
            else:
                bucket = ">0.755"

            if deal_type_present:
                deal_buckets[bucket]["hit"] += 1
            else:
                deal_buckets[bucket]["miss"] += 1

    logger.debug(f"Deal chances calculated: {deal_buckets}")
    return deal_buckets


def analyze_run_file(run_file):
    logger.info(f"Analyzing run file with run number {run_file['run_number']}.")
    for run in run_file["runs"]:
        analytics = {
            "deals": get_deal_type(run),
            "dealChance": get_deal_chances(run),
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

    logger.info("All run files analyzed. Generating deal plot.")
    generate_deal_plot(analyzed_runs, output_path)
    logger.info("Deal plot generation complete.")


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
    output_file = join(output_path, "deals.pdf")
    deal_figure.savefig(output_file)
    logger.info(f"Deal plot saved to {output_file}")
