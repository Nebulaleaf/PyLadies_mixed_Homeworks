pets = ['dog', 'cat', 'rabbit', 'snake'] 


def d_petlist(pets):
  d_pets = []
  for pet in pets:
    if pet[0] == 'd' or pet[0] == 'D':
      d_pets.append(pet)
  return d_pets

pets = ['dog', 'cat', 'rabbit', 'snake']
print(d_petlist(pets))

