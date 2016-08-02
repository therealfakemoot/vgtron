#!/opt/imh-python/bin/python
import argparse
from subprocess import Popen

def vegeta(host):
    pass

def parse_args():
    parser = argparse.ArgumentParser(description='Vegeta convenience wrapper')

    tuning_parser = parser.add_argument_group('Request Tuning', 'These flags are optional and can be provided to change the quantiy/duration of test requests.')

    tuning_parser.add_argument('-d', '--duration', dest='duration', default=10)
    tuning_parser.add_argument('-r', '--rate', dest='rate', default=1000)
    tuning_parser.add_argument('-s', '--step', dest='step', default=10)
    tuning_parser.add_argument('-m', '--max', dest='max', default=10000)

    target_parser = parser.add_argument_group('Target Files', 'This flag is used to specify a target file for your attack. Exclusive with Manual Target.')
    target_parser.add_argument('-f', '--file', dest='file', nargs='?', default=None)

    manual_parser = parser.add_argument_group('Manual Target', 'This flag allows you manually specify the target hostname and HTTP Verb. Exclusive with Target Files.')
    manual_parser.add_argument('-t', '--target', dest='target')
    manual_parser.add_argument('-v', '--verb', dest='verb', default='GET', type=lambda v:v.upper())

    args = parser.parse_args()

    if args.file and args.target:
        raise ValueError('--file and --target are mutually exclusive and cannot be used together.')

def main(args):
    pass

if __name__ == '__main__':
    args = parse_args()
    main(args)

    if args.file:
        file_attack(args.file, args.duration, args.rate, args.step, args.max)
    elif args.target:
        target_attack(args.target, args.duration, args.rate, args.step, args.max)
