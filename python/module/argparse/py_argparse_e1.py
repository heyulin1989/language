import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("echo", help='echo the string you use here')
parser.add_argument("square", help='display a square of a given number', type=int)
args = parser.parse_args()
print args.square**2
