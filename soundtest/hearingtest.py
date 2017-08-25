from winsound import Beep

MAX_FREQ = 32767
MIN_FREQ = 37


def hearing_test():
    print('freq from : {} to : {}'.format(MIN_FREQ, MAX_FREQ))
    Beep(1000, 350)
    frequency = MIN_FREQ
    while frequency < MAX_FREQ:
        time = 200
        if frequency > 10000:
            time = 450
        Beep(frequency, time)
        float_freq = frequency * 1.1
        frequency = int(float_freq)
    Beep(1000, 350)


if __name__ == '__main__':
    hearing_test()
