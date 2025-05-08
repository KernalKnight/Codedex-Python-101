print('===============\nThe Sorting Hat\n===============')


gy = "🦁 Gryffindor"
ra = "🦅 Ravenclaw"
hu = "🦡 Hufflepuff"
sy = "🐍 Slytherin"


g = 0
r = 0
h = 0
s = 0


q1 = int(input("Q1) Do you like Dawn or Dusk? \n"
    " 1) Dawn \n"
    " 2) Dusk \n" \
    "Enter answer (1-2): "))



q2 = int(input("\n Q2) When I’m dead, I want people to remember me as \n"
    " 1) The Good \n"
    " 2) The Great \n"
    " 3) The Wise \n"
    " 4) The Bold: \n" \
    " Enter answer (1-4): "))



q3 = int(input(" \n Q3) Which kind of instrument most pleases your ear? \n"
    " 1) The violin \n"
    " 2) The trumpet \n"
    " 3) The piano \n"
    " 4) The drum: \n"
    " Enter answer (1-4): "))


if q1 == 1:
  g += 1 
  r += 1
elif q1 == 2:
  h += 1
  s += 1
else:
  print("Wrong input.")



if q2 == 1:
  h += 2
elif q2 == 2:
  s += 2
elif q2 == 3:
  r += 2
elif q2 == 4:
  g += 2
else:
  print("Wrong input.")



if q3 == 1:
  s += 4
elif q3 == 2:
  h += 4
elif q3 == 3:
  r += 4
elif q3 == 4:
  g += 4
else:
  print("Wrong input.") 

 
print(f"\nScores:\n {gy} = {g}\n {ra} = {r}\n {hu} = {h}\n {sy} = {s} \n")


# Bonus code to practise control flows 

if g > r and g > h and g > s:
  print(f'The house with most points "{gy}" \n')
elif r > g and r > h and r > s:
  print(f'The house with most points "{ra}" \n')
elif h > r and h > g and h > s:
  print(f'The house with most points "{hu}" \n')
else:
  print(f'The house with most points "{sy}" \n')