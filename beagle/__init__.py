from beagle import color, nose, stomach

def hunt(args):
    stomach.verbose = args.verbose
    _nose = nose.Nose(args.interface)
    _nose.sniff()
