import os
import random
import string
import time

os.system('cls||clear')

print ('VITAL MESSAGE'
       '\n')

while True:
  D = int(input('HOW DIFFICULT [4-10]'))
  if D>=4 and D<= 10:
     break

M = ''

for i in range(D):
   M += random.choice(string.ascii_uppercase)

   os.system('cls||clear')

   print ('SEND THIS MESSAGE'
          '\n'
          '\n', M)
   
time.sleep(0.5*D)

os.system('cls||clear')

N = input(' ')

if N == M:
   print('CORRECT MESSAGE'
         '\n'
         'THE WAR IS OVER')
else: print('NOooo..'
            '\n)'
            "You're so Wrong!!"
            '\n'
            'You Should have sent:-', M)

