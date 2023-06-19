A = 'Audi'
B = 'audi'

print( A == B)
print( A.lower() == B)

print( 1 == 2)
print( 1 < 2)
print( 1 <= 2)
print( 1 > 2)
print( 1 >= 2)

if (A == B) and (1 < 2):
    print( 'Y' )

if (A == B) or ( 1 < 2):
    print( 'N' )

car = ['audi']
if 'audi' in car:
    print("Yes")
if 'Audi' not in car:
    print("True")