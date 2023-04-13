#!/usr/bin/python3
"""Reads from standard input and computes metrics"""


def print_stats(size, status_codes):
    """This prints, reads stdin line by line and
    computes metrics accumulated metrics
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = set(['200', '301', '400', '401', '403', '404', '405', '500'])
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            line_parts = line.split()

            try:
                size += int(line_parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                status_code = line_parts[-2]
                if status_code in valid_codes:
                    status_codes[status_code] = status_codes.get(status_code, 0) + 1
            except IndexError:
                pass

            if count == 10:
                print_stats(size, status_codes)
                count = 0

        if count > 0:
            print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
