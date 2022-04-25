n = int(input())

splitar = [int(a) for a in str(n)]

sp0 = splitar[0]
sp1 = splitar[1]
sp2 = splitar[2]

qtd_par = int(0)

if sp0%2==0:
  qtd_par += 1
if sp1%2==0:
  qtd_par += 1
if sp2%2==0:
  qtd_par += 1

print(qtd_par)