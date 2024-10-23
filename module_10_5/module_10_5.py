import io
import datetime
import multiprocessing


def read_info(name):
    all_data = []
    fs = io.open(name, 'r')
    while line := fs.readline():
        if line != '':
            all_data.append(line)
        else:
            break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    tstart = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    print(f'{datetime.datetime.now() - tstart} (линейный)')
    tstart = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(f'{datetime.datetime.now() - tstart} (многопроцессорный)')
