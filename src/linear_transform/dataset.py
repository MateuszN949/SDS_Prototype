def load(path):
    f=open(path)
    out=[]
    for l in f:
        out.append(float(l.strip()))
    return out