weight=int(input("Enter your weight:"))
unit=input('(L)bs or (k)g')
if unit.upper() == 'L':
    convert = weight * 0.45
    print(f"you are{convert}kilo")
else:
    convert = weight /0.45
    print( print(f"you are{convert}pounds"))

