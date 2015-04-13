def num (s):
    try:
        return int(s)
    except exceptions.ValueError:
        return float(s)


