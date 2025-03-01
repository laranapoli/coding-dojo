a = 'A'
b = 'B'
c = 1.1

formato = 'a={} c={:.2f}'.format(a, c)

# Tem como passar um parâmetro nomeado para o format
formato = 'a={} c={nome3:.2f}'.format(a, nome3=c)
print(formato)