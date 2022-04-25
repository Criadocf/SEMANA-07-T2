n = int(input())

splitado = [int(a) for a in str(n)]

sp0 = splitado[0]
sp1 = splitado[1]

if sp0%2==1 and sp1%2==1:
  print('Os dois dígitos são ímpares')
elif sp0%2!=1 and sp1%2!=1:
  print( 'Nenhum dígito é impar')
else:
  print('Apenas um dígito é impar')