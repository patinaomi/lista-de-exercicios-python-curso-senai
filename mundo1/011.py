# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tintas necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = altura * largura

tinta = area / 2

print(f'Sua parede tem a dimensão de {altura}x{largura} e sua área é de {area}m2')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')