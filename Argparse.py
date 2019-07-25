import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', type = float, default = 1.0, help='Please enter first number')
    parser.add_argument('--b', type = float, default = 1.0, help='Please enter second number')
    parser.add_argument('--ops', type = str, default = 'add', help='Please enter operation')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
    
def calc(args):
    if args.ops == 'add' or '+':
        return args.a + args.b
    elif args.ops == 'sub' or '-':
        return args.a - args.b
    elif args.ops == 'mul' or '*':
        return args.a * args.b
    elif args.ops == 'div' or '/':
        return args.a / args.b
    
if __name__ == '__main__':
    main()
