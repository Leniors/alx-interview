#!/usr/bin/python3
""" Reads `stdin` line by line and computes metrics """

import sys

if __name__ == '__main__':

    fileSize, counter = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    statusCount = {k: 0 for k in codes}

    def print_statistics(statusCount: dict, file_size: int) -> None:
        print("File size:", fileSize)
        for k, v in sorted(statusCount.items()):
            if v != 0:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in statusCount:
                    statusCount[status_code] += 1
            except BaseException:
                pass
            try:
                fileSize += int(data[-1])
            except BaseException:
                pass
            if counter % 10 == 0:
                print_statistics(statusCount, fileSize)
        print_statistics(statusCount, fileSize)
    except KeyboardInterrupt:
        print_statistics(statusCount, fileSize)
        raise