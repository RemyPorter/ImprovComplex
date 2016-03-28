from . import show
import sys
import optparse
def build_parser():
    parser = optparse.OptionParser()
    files = optparse.OptionGroup(parser, "File Options",
        "Specify where to get settings for for phrases, intros and outtros.")
    files.add_option("-p", "--phrases", dest="phrases",
        default="phrases.txt", help="Where to load the phrasebank from.")
    files.add_option("-i", "--intro", dest="intro",
        default="intro.txt", help="Where to load the intro-script from.")
    files.add_option("-o", "--outro", dest="outro",
        default="outro.txt", help="Where to load the outro-script from.")
    parser.add_option_group(files)

    showing = optparse.OptionGroup(parser, "Show Settings",
        "How to run and manager a show.")
    showing.add_option("-n", "--no-autonag", action="store_true",
        help="Disable automated nagging- run interactive only.",
        default=False, dest="no_auto")
    showing.add_option("-t", "--nag-rate", default=35,
        help="The frequency of nagging, meausred in seconds.",
        dest="nag_rate", type=int)
    showing.add_option("-j", "--jitter", default=0.1,
        help="How much the timing can drift from the nag-rate, from 0-1",
        dest="jitter", type=float)
    showing.add_option("-v", "--voice", default="Vicki",
        help="The synthesized voice to use.", dest="voice")
    parser.add_option_group(showing)

    return parser

parser = build_parser()
(opts, args) = parser.parse_args(sys.argv)
show.main(**opts.__dict__)