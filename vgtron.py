#!/opt/imh-python/bin/python
import argparse
from subprocess import Popen

def build_command(args):
    pass

def vegeta(host):
    pass

def main():
    parser = argparse.ArgumentParser(description='Vegeta convenience wrapper')
    subparser = parser.add_subparsers()

    target = subparser.add_parser('target')
    target.add_argument('-f', '--file', dest='file', help='This is a file path to a Vegeta target file', nargs='?', default=None)

    live = subparser.add_parser('live')
    live.add_argument('-t', '--target', dest='target')
    live.add_argument('-v', '--verb', dest='verb', default='GET', type=lambda v:v.upper())

    tuning_parser = parser.add_argument_group('Request Tuning', 'These flags are optional and can be provided to change the quantiy/duration of test requests.')

    tuning_parser.add_argument('-d', '--duration', dest='duration', default=10)
    tuning_parser.add_argument('-r', '--rate', dest='rate', default=1000)
    tuning_parser.add_argument('-s', '--step', dest='step', default=10)
    tuning_parser.add_argument('-m', '--max', dest='max', default=10000)

    args = parser.parse_args()

if __name__ == '__main__':
    main()
