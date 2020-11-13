from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("Exception")
root.geometry("400x300")

#first login screen
def check():
    all_logs = {'Tabang':'0000', 'asive': '1234'}
    my_user = label1.get()
    password = pass1.get()
    if (my_user, password) in all_logs.items():
        messagebox.showinfo("INFO", "CORRECT LOGIN")
        root.withdraw
    else:
        messagebox.showinfo("INFO","INCORRECT LOGIN")

        label_1.delete(0,END)
        pass_1.Entry.delete(0, END)



#top label
myLabel = Label(root, text="Please enter Login details",)
myLabel.pack()

#Username label & entry
label_1 = Label(root, text="Username", height=2)
label_1.pack()
label1 = Entry(root, borderwidth=4)
label1.pack()
#password label & entry
pass_1 = Label(root, text="Password", height=2)
pass_1.pack()
pass1 = Entry(root, borderwidth=4, show="*")
pass1.pack()

#Button
log_btn = Button(root, text="Login", height=1, bg="purple", width=10, command=check)
log_btn.pack()



# #status feedback
# def status():
#     check_btn = messagebox.showinfo("Congratulations", "You qualify to go to Malaysia")
#     if  check_btn>3000:
#         Label(root)
#
#     if check_btn<3000:
#         Label(root)
#         messagebox.showerror("Please deposit more funds for this excursion.")
#
#
# #check qualification btn & entry
# check_btn = Entry(root, borderwidth=4)
# check_btn.pack()
# check_btn = Button(root, text="Check qualification", command=status)
# check_btn.pack()
#
#
#



root.mainloop()
