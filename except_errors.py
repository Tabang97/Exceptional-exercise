from tkinter import*
from tkinter import messagebox
window = Tk()
window.title("Exception")
window.geometry("400x300")




#tatus feedback
def status():

    res = int(check_txt.get())

    if res >= 3000:
        messagebox.showinfo("Congratulations", "You qualify to go to Malaysia")

    elif res < 3000:
        messagebox.showerror("Info", "Please deposit more funds for this excursion.")




#check qualification btn & entry
check_txt = Entry(window,borderwidth=4)
check_txt.pack()
check_btn = Button(window,text="Check qualification", command=status)
check_btn.pack()

window.mainloop()

