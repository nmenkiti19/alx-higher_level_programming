#!/usr/bin/python3
# 101-stats.py

"""reads std input line by line 
and computes metrics
"""

def print_stats(size, status_codes):
    """Print metrics accrued"""
    print("File size: {}".format(size))
    for indx in sorted(status_codes):
        print("{}: {}".format(indx, status_codes[indx]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    axptd = ['200', '301', '400', '401', '403', '404', '405', '500']
    i = 0

    try:
        for lyn in sys.stdin:
            if i == 10:
                print_stats(size, status_codes)
                i = 1
            else:
                i += 1

            lyn = lyn.split()

            try:
                size += int(lyn[-1])
            except (IndexError, ValueError):
                pass

            try:
                if lyn[-2] in axptd:
                    if status_codes.get(lyn[-2], -1) == -1:
                        status_codes[lyn[-2]] = 1
                    else:
                        status_codes[lyn[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
