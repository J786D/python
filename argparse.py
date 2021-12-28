
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('name', help='NAME')
    args = parser.parse_args()
    print(args.name)
