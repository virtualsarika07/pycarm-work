'''Wap to enter name and the check characters
and print message'''
name=input('Enter your name: ')
if len(name) < 3 :
    print("Name must be atleast three characters:")

elif len (name) > 50:
    print("Name can be of maximum 50 chaarcters")

else:
    print("Name looks good")
