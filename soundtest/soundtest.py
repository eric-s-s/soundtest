from winsound import Beep
from time import sleep
import argparse


def beep_it():
    for factor in range(1, 20):
        Beep(factor * 100, 200)
        sleep(0.15)


def beep_for_times(times):
    for _ in range(times):
        beep_it()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num', nargs='?', default=1, type=int)

    args = parser.parse_args()

    beep_for_times(args.num)


if __name__ == '__main__':
    main()
