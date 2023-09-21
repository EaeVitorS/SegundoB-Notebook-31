#calcula a media entre 2 valores a e b

def media(a,b):
    s = a+b
    m = s/2
    return m


def mediaponderada(a, b, pa, pb):
    s = a*pa + b*pb
    p = pa + pb
    m = s / p
    return m

print(media(7,8))

print(mediaponderada(7,8,10,5))
