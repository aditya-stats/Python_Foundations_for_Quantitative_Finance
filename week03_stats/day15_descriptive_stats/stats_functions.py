#Important functions-

def mean(data):
    """
    Compute the arithmetic mean.
    """
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    return sum(data) / len(data)


def variance(data, ddof=0):
    """
    Compute variance.
    ddof=0 -> population variance
    ddof=1 -> sample variance
    """
    n = len(data)
    if n == 0:
        raise ValueError("Data cannot be empty")
    if n - ddof <= 0:
        raise ValueError("Degrees of freedom <= 0")

    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (n - ddof)


def std_dev(data, ddof=0):
    """
    Compute standard deviation.
    """
    return variance(data, ddof) ** 0.5


def skewness(data):
    """
    Compute population skewness.
    """
    n = len(data)
    if n < 3:
        raise ValueError("Need at least 3 data points")

    m = mean(data)
    s = std_dev(data, ddof=0)

    return sum((x - m) ** 3 for x in data) / (n * s ** 3)


def kurtosis(data):
    """
    Compute excess kurtosis (kurtosis - 3).
    """
    n = len(data)
    if n < 4:
        raise ValueError("Need at least 4 data points")

    m = mean(data)
    s = std_dev(data, ddof=0)

    return sum((x - m) ** 4 for x in data) / (n * s ** 4) - 3