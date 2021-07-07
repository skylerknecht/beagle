import re

from beagle import color, nose, stomach

stomach.__version__ = '0.2'

def hunt(args):
    stomach.verbose = args.verbose
    stomach.srcip = re.compile(args.srcip)
    stomach.dstport = re.compile(args.dstport)
    _nose = nose.Nose(args.interface)
    _nose.sniff()
