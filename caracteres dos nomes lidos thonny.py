nome = input()
estado_civil = input()

if '1' in estado_civil:
  print('casado')
else:
  print('solteiro')

if '1' in estado_civil:
  nome_conjuge = input()

qtd_letra = ''.join(nome.split())
qtd_letrac = ''.join(nome_conjuge.split()) 



print(len(qtd_letra) + len(qtd_letrac))