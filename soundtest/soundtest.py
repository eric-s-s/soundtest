from winsound import Beep
import argparse


def beep_it():
    for fac in range(1, 20):
        Beep(fac * 100, 200)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', nargs='?', default=1)

    args = parser.parse_args()
    print(args.num)

    for _ in range(1):
        beep_it()

if __name__ == '__main__':
    main()

