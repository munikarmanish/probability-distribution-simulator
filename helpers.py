import sys


def abort(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def parse_arguments():
    if len(sys.argv) < 4:
        abort("not enough arguments")

    # get sample size
    try:
        n = int(sys.argv[1].strip())
        assert n > 1
    except (ValueError, AssertionError):
        abort("invalid sample size")

    # get distribution name
    dist = sys.argv[2].strip().lower().replace("-", "_")

    # get distribution params
    params = [p.strip() for p in sys.argv[3:]]

    return n, dist, params
