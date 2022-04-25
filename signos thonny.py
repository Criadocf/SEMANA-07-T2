def sig(d,m):
  if m == 1:
    if d <= 19:
      return 'Capricórnio'
    else:
      return 'Aquário'
  
  elif m == 2:
    if d <= 18:
      return 'Aquário'
    else:
      return 'Peixes'

  elif m == 3:
    if d <= 20:
      return 'Peixes'
    else: 
      return 'Áries'

  elif m == 4:
    if d <= 4:
      return 'Áries'
    else: 
      return 'Touro'

  elif m == 5:
    if d <= 20:
      return 'Touro'
    else:
      return 'Gêmeos'
  
  elif m == 6:
    if d <= 21:
      return 'Gêmeos'
    else:
      return 'Câncer'

  elif m == 7:
    if d <= 22:
      return 'Câncer'
    else:
      return 'Leão'

  elif m == 8:
    if d <= 22:
      return 'Leão'
    else:
      return 'Virgem'

  elif m == 9:
    if d <= 22:
      return 'Virgem'
    else:
      return 'Libra'

  elif m == 10:
    if d <= 22:
      return 'Libra'
    else:
      return 'Escorpião'
    
  elif m == 11:
    if d <= 21:
      return 'Escorpião'
    else:
      return 'Sagitário'
    
  elif m ==12:
    if d <= 21:
      return 'Sagitário'
    else: 'Capricórnio'

d_n = int(input())
m_n = int(input())


ch1 = sig(d_n, m_n)

print(ch1)