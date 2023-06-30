from scanner import SiteRecon
from argparse import ArgumentParser
from update import Settings, read_settings


default_values = read_settings()


parser = ArgumentParser(
    prog="siterecon",
    description="Discover information about a given website.",
    epilog="Use responsibly.",
)
parser.add_argument("url", action="store")
parser.add_argument(
    "-c",
    "--count",
    type=int,
    default=default_values["maxSiteSearch"],
    action="store",
    metavar="<int>",
    help="The number of webpages you want to scan.",
)
aggression = parser.add_argument_group("aggression")
aggression.description = "Affects the wait time between each request. Default is M."
aggression.add_argument(
    "-ag",
    "--aggression",
    choices=["A", "M", "P"],
    help=f"A: {default_values['aggressiveMinWait']}s-{default_values['aggressiveMaxWait']}s | M: {default_values['moderateMinWait']}s-{default_values['moderateMaxWait']}s | P: {default_values['passiveMinWait']}s-{default_values['passiveMaxWait']}s",
    default=default_values["defaultAggression"],
    action="store",
)
aggression.add_argument(
    "-ca",
    "--custom-aggression",
    type=int,
    nargs=2,
    action="store",
    help="Customize wait time between requests.",
    metavar=("<min>", "<max>"),
    default=None,
)
output = parser.add_argument_group("output")
output.description = "Options for creating the report file."
output.add_argument(
    "-fp",
    "--filepath",
    help="Location of where you want the output file.",
    default=default_values["filePath"],
    action="store",
    type=str,
    metavar="<path>",
)
defaults = parser.add_argument_group("defaults")
defaults.description = "Change the defaults for all the flags"
defaults.add_argument(
    "-Dag",
    "--default-aggression",
    help="Change the default mode for the -ag flag.",
    type=str,
    action="store",
    choices=["A", "M", "P"],
    default=None,
)
defaults.add_argument(
    "-Dfp",
    "--default-filepath",
    type=str,
    action="store",
    metavar="<path>",
    help="Change the default filepath.",
    default=None,
)
defaults.add_argument(
    "-Dc",
    "--default-count",
    type=str,
    action="store",
    metavar="<int>",
    help="Change the default count.",
    default=None,
)
defaults.add_argument(
    "-Daw",
    "--default-aggressive-wait",
    type=int,
    action="store",
    metavar=("<min>", "<max>"),
    help="Change the default aggressive wait.",
    default=None,
    nargs=2,
)
defaults.add_argument(
    "-Dmw",
    "--default-moderate-wait",
    type=int,
    action="store",
    metavar=("<min>", "<max>"),
    help="Change the default moderate wait.",
    default=None,
    nargs=2,
)
defaults.add_argument(
    "-Dpw",
    "--default-passive-wait",
    type=int,
    action="store",
    metavar=("<min>", "<max>"),
    help="Change the default passive wait.",
    default=None,
    nargs=2,
)
defaults.add_argument(
    "-ss", "--show-settings", action="store_true", help="Shows all the default values."
)
args = parser.parse_args()
settings = Settings(
    args.default_filepath,
    args.default_count,
    args.default_aggression,
    args.default_aggressive_wait,
    args.default_moderate_wait,
    args.default_passive_wait,
)
settings.update_settings()
if args.show_settings:
    settings.show_settings()
if args.url.lower() != "none":
    sr = SiteRecon(
        args.url, args.aggression, args.custom_aggression, args.count, args.filepath
    )
    sr.run_program()
