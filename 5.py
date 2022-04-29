likelion = 300
past = 1992
future = 2022
fB = 3500
Interest = 0
rate=0.085

def friendA(future):
    # Interest = likelion*rate*(future-past)
    fA =likelion*((1+rate)**(future-past))
    print(fA)
    return fA

fA = friendA(future)

if(fA>fB):
    print(fA-fB,"만원 차이로 친구A가 맞았습니다.")
else:
    print(fB-fA,"만원 차이로 친구B가 맞았습니다.")