#!/opt/imh-python/bin/python
import argparse
from subprocess import Popen

def build_command(args):
    pass

def vegeta(host):
    pass

def main():
    parser = argparse.ArgumentParser(description='Vegeta convenience wrapper')

    tuning_parser = parser.add_argument_group('Request Tuning', 'These flags are optional and can be provided to change the quantiy/duration of test requests.')

    tuning_parser.add_argument('-d', '--duration', dest='duration', default=10)
    tuning_parser.add_argument('-r', '--rate', dest='rate', default=1000)
    tuning_parser.add_argument('-s', '--step', dest='step', default=10)

    parser.add_argument('-f', '--file', dest='file', nargs='?', default=None)

    parser.add_argument('-t', '--target', dest='target')
    parser.add_argument('-v', '--verb', dest='verb', default='GET', type=lambda v:v.upper())

    args = parser.parse_args()

if __name__ == '__main__':
    main()
