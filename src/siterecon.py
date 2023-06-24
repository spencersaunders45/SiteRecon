from scanner import SiteRecon
from argparse import ArgumentParser


parser = ArgumentParser(
    prog="siterecon",
    description="Discover information about a given website.",
    epilog="Use responsibly."
    )
parser.add_argument("url", action="store")
parser.add_argument(
    '-c',
    '--count',
    type=int,
    default=20,
    action="store",
    metavar="<int>",
    help="The number of webpages you want to scan."
)
aggression = parser.add_argument_group("aggression")
aggression.description = "Affects the wait time between each request. Default is M."
aggression.add_argument(
    '-ag',
    '--aggression',
    choices=["A", "M", "P"],
    help="A: 0s | M: 30s-45s | P: 45s-90s",
    default="M",
    action="store"
    )
aggression.add_argument(
    '-ca',
    '--custom-aggression',
    type=int,
    nargs=2,
    action="store",
    help="Customize wait time between requests.",
    metavar=("<max>", "<min>"),
    default=None
)
output = parser.add_argument_group("output")
output.description = "Options for creating the report file."
output.add_argument(
    '-fp',
    '--filepath',
    help="Location of where you want the output file.",
    default="output.txt",
    action="store",
    type=str,
    metavar="<path>"
)
defaults = parser.add_argument_group("defaults")
defaults.description = "Change the defaults for all the flags"
defaults.add_argument(
    '-Dag',
    '--default-aggression',
    help="Change the default mode for the -ag flag.",
    type=str,
    action="store",
    choices=["A", "M", "P"]
)
defaults.add_argument(
    '-Dfp',
    '--default-filepath',
    type=str,
    action="store",
    metavar="<path>",
    help="Change the default filepath.",
)
defaults.add_argument(
    '-Dc',
    '--default-count',
    type=str,
    action="store",
    metavar="<int>",
    help="Change the default count.",
)
args = parser.parse_args()
sr = SiteRecon(
    args.url,
    args.aggression,
    args.custom_aggression,
    args.count,
    args.filepath,
    )
sr.run_program()