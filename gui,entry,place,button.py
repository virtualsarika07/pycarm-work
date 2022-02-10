#GUI Application Development :
#Widgets are Label, Entry and Button
#Layout Management place()
import tkinter

root = tkinter.Tk()

root.title('First Application')
root.geometry("400x400")
root.configure(bg='Orange')

lblHeading = tkinter.Label(root,text = 'My First Application')
lblHeading.place(x=100,y=10)

lblAccNo = tkinter.Label(root,text='Account No : ')
lblAccNo.place(x=10,y=40)


txtAccNo = tkinter.Entry(root)
txtAccNo.place(x=100,y=40)


btnSubmit = tkinter.Button(root,text='Submit')
btnSubmit.place(x=100,y=70)

root.mainloop()