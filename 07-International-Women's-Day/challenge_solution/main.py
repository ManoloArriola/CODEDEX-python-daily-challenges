def analyze(percentages):

    # Net Change Per Year
    first = percentages[0]
    last = percentages[-1]
    years = len(percentages)

    net_change = (last - first) / (years - 1)
    net_change = round(net_change, 4)

    # Trend
    first_avg = sum(percentages[:3]) / 3
    last_avg = sum(percentages[-3:]) / 3

    if last_avg > first_avg:
        trend = "improving"
    elif last_avg == first_avg:
        trend = "stagnating"
    else:
        trend = "declining"

    # Dips
    dips = 0
    for i in range(1, len(percentages)):
        if percentages[i] < percentages[i-1]:
            dips += 1

    return net_change, trend, dips
