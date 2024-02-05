# exemplo 1

print("""
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
        ***
        ***
        ***""")

# exemplo 2

print('         ', '*')
print('        ', '*' * 3)
print('       ', '*' * 5)
print('      ', '*' * 7)
print('     ', '*' * 9)
print('    ', '*' * 11)
print('   ', '*' * 13)
print('  ', '*' * 15)
print(' ', '*' * 17)
print('', '*' * 19)
print('        ', '*' * 3)
print('        ', '*' * 3)
print('        ', '*' * 3)

# exemplo 3

cont = 10

for i in range(1, 20, 2):
    print(' ' * cont, '*' * i)
    cont = cont - 1

for i in range(1, 4):
    print(' ' * 9, '*' * 3)
