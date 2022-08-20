
#formula  do calculo do retangulo A=B.H, do perímetro do retângulo P = 2*(b+h), diagonal do retângulo d² = b²+h²
#formula do quadrado A = l² ou A = b.h, perímetro do quadrado P = 4l ,
#formula  do círculo A = pi*r², perimetro P = 2*pi*r

print('Calcule a área e o perímetro do retângulo' )

b = float(input('\nIndique o valor da base '))
h = float(input('Indique a altura '))

print('\nO retângulo com {} base e altura de {}, resultam  a área do retângulo em {}cm²'. format( b , h , b*h))
print('O perímetro deste retângulo é de {} cm'. format( 2*(b+h)))

print('\nCalculo da  área e perímetro do quadrado ')
l = float(input('\nIndique o valor do lado '))
l1 = float(input('Indique o valor do lado '))
l2 = float(input('Indique o valor do lado '))
l3 = float(input('Indique o valor do lado '))

if l == l1 and l1 ==l2 and l2 ==l3:
    print('\nÉ possivel formar um quadrado, pois os quadrados lados são iguais')
    print('A área deste quadrado com os 4 lados de {}, resulta {}cm²'.format( l ,l**2 ))
    print('O perímetro deste quadrado é de {}cm '.format(4*l))
else:
    print('\nNão é possivel formar um quadrado, pois  algum dos lados é diferente ')

print('Calcule  o pi do círculo')

p = float(input('\nO valor do perímetro '))
d = float(input('O valor do diâmetro '))
r = float(input('o valor do raio '))
pi = p / d
a = pi*r**2
print('\nO perímetro deste circulo é de {} e o diâmetro {} seu pi é de {:.2f}'.format( p, d , pi ))
print('E sua área é de {}'.format(a))