def cal_average(num):
    touches = 0
    for t in num:
        touches = touches + t

    avg = touches / len(num)
    return avg

print("SPM:", cal_average([18, 19, 16, 22, 20]))
