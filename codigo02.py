# Leitura de dados
h_1 = int(input())
m_1 = int(input())
h_2 = int(input())
m_2 = int(input())

# Cálculo do tempo dormido
a = (24 - h_1) + h_2
b = (60 - m_1) + m_2
if m_1 < m_2:
    horas_d = a
if m_2 < m_1:
    horas_d = a - 1

# Impressão da resposta
print(horas_d >= 8)
