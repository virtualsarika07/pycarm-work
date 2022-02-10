#GUI Application Development :
#Widgets
import tkinter

root = tkinter.Tk()

root.title('First Application')
root.geometry("400x400")
root.configure(bg='Orange')

lblHeading = tkinter.Label(root,text = 'My First Application')
lblHeading.pack()

lblAccNo = tkinter.Label(root,text='Account No : ')
lblAccNo.pack()


root.mainloop()