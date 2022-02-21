
def wage_transform(x):
    x = str(x)
    if "K" in x:
        x = x.replace("K", "").replace("€", "")
        y = int(x) * 1000
    else:
        x = x.replace("€", "")
        y = int(x)
    return y
