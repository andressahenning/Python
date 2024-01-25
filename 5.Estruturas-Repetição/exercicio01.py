c = 0

while(c <= 5):

  if (c % 2 != 0):
    c += 1
    continue

  print("Regue a planta", c)
  c += 1

print('FIM')

c = -1

while(c <= 4):
  c += 1
  if(c == 2 or c == 3):
    continue
  print('Regue a planta',c)