#GUI Application Development :
#Widgets are Label, Entry and Button
#Layout Management place()
#Function of Button Widget


import tkinter

root = tkinter.Tk()

root.title('First Application')
root.geometry("400x400")
root.configure(bg='Orange')

sAccno = tkinter.StringVar()


#function for button widgets
def funSubmit():
    accno = sAccno.get()
    print('Account No ',accno)



lblHeading = tkinter.Label(root,text = 'My First Application')
lblHeading.place(x=100,y=10)

lblAccNo = tkinter.Label(root,text='Account No : ')
lblAccNo.place(x=10,y=40)


txtAccNo = tkinter.Entry(root,textvariable = sAccno)
txtAccNo.place(x=100,y=40)


btnSubmit = tkinter.Button(root,text='Submit',command=funSubmit)
btnSubmit.place(x=100,y=70)

root.mainloop()