def output(x):
    if x <= 0:
        return 0
    else:
        return 1

def Proc_UnitI(a1, w1, bias):  
    Weighted_sum = a1*w1
    X =Weighted_sum - bias
    S= output(X)
    return S

def Proc_unitO(a1,a2,w1,w2,bias):
    weighted_sum = a1*w1 + a2*w2
    X =weighted_sum - bias
    S = output(X)
    return S

for a1 in range(2):
    for a2 in range(2):
        S1 = Proc_UnitI(a1,-1,-1)
        S2 = Proc_UnitI(a2,-1,-1)
        S = Proc_unitO(S1, S2, 1, 1, 0)
        print("a1: "+ str(a1) + " a2: "+ str(a2) + " s: " + str(S))