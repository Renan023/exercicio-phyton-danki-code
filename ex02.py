print('Conversão de reais em doláres ')
r = float(input('\nQual o valor da conversão em reais R$ '))
print('\nO valor convertido R$ {:.2f} dá em U$$ {:.2f}'. format( r , r/5.18))

print('\nA conversão de doláres em reais ')
d = float(input('\nValor em U$$ '))
print('\nO valor U$$ {} ficou em R$ {:.2f}'.format(d, d*5.18))

