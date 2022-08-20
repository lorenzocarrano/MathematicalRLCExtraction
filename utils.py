def matrixProduct(m1,m2):
    #limited to 2x2 case
    res = []
    if len(m1) == 4 and len(m2) == 4:
        t = m1[0] * m2[0] + m1[1] * m2[2]
        res.append(t)
        t = m1[0] * m2[1] + m1[1] * m2[3]
        res.append(t)
        t = m1[2] * m2[0] + m1[3] * m2[2]
        res.append(t)
        t = m1[2] * m2[1] + m1[3] * m2[3]
        res.append(t)
    
    return res