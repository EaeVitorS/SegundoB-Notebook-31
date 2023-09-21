import math

def calcular_velocidade_inicial(forca, massa):
    return math.sqrt((2 * forca) / massa_bala)    

def calcular_tempo_de_voo(velocidade_inicial, angulo):
    angulo_rad = math.radians(angulo)
    return (2 * velocidade_inicial * math.sin(angulo_rad)) / 10

def calcular_alcance_horizontal(velocidade_inicial, angulo):
    angulo_rad = math.radians(angulo)
    return (velocidade_inicial ** 2) * math.sin(2 * angulo_rad) / 10

def calcular_posicao_queda(velocidade_inicial, angulo, tempo):
    angulo_rad = math.radians(angulo)
    x = calcular_alcance_horizontal(velocidade_inicial, angulo)
    y = (velocidade_inicial * math.sin(angulo_rad) * tempo) - (0.5 * 10 * tempo ** 2)
    return x, y

def calcular_velocidades(velocidade_inicial, angulo, tempo):
    angulo_rad = math.radians(angulo)
    vx = velocidade_inicial * math.cos(angulo_rad)
    vy = velocidade_inicial * math.sin(angulo_rad) - 10 * tempo
    return vx, vy

# Entrada de valores
coordenadax_canhao = float(input("Digite a coordenada X do canhão: "))
coordenaday_canhao = float(input("Digite a coordenada Y do canhão: "))
forca = float(input("Digite a força em newtons: "))
angulo = float(input("Digite o ângulo em graus: "))

massa_bala = 0.5  # kg

# Cálculos
velocidade_inicial = calcular_velocidade_inicial(forca, massa_bala)
tempo_voo = calcular_tempo_de_voo(velocidade_inicial, angulo)
alcance_horizontal = calcular_alcance_horizontal(velocidade_inicial, angulo)
posicao_queda = calcular_posicao_queda(velocidade_inicial, angulo, tempo_voo)
velocidades_no_tempo = [calcular_velocidades(velocidade_inicial, angulo, t) for t in range(int(tempo_voo) + 1)]

# Saída formatada
print("\nResultados:")
print(f"Velocidade Inicial: {velocidade_inicial:.2f} m/s")
print(f"Tempo de Voo: {tempo_voo:.2f} s")
print(f"Alcance Horizontal: {alcance_horizontal:.2f} m")
print(f"Posição de Queda: X = {posicao_queda[0]:.2f} m, Y = {posicao_queda[1]:.2f} m")

print("\nVelocidades no Tempo:")
for t, (vx, vy) in enumerate(velocidades_no_tempo):
    print(f"No instante {t}s: Velocidade Vertical = {vy:.2f} m/s, Velocidade Horizontal = {vx:.2f} m/s")

print(f"Distância entre o ponto de lançamento e o local da queda: {abs(posicao_queda[0] - coordenadax_canhao):.2f} m")

