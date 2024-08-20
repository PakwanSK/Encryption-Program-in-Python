from tkinter import *
from tkinter import messagebox
import base64
import os

correct_password = "4321"

def decrypt():
    password = code.get()

    if password == "":
        messagebox.showerror("decryption", "Input Password")
    elif password != correct_password:
        messagebox.showerror("decryption", "Invalid Password")
    else:
        screen1 = Toplevel(screen)
        screen1.title("decryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        encrypted_message = text1.get(1.0, END)

        # ถอดรหัส Base64 ก่อน
        base64_bytes = encrypted_message.encode("ascii")
        message_bytes = base64.b64decode(base64_bytes)
        decoded_message = message_bytes.decode("ascii")

        # ถอดรหัส XOR ด้วยรหัสผ่านที่ผู้ใช้ป้อนมา
        decrypted_chars = []
        for i in range(len(decoded_message)):
            key_c = password[i % len(password)]  # ใช้รหัสผ่านหมุนวน
            decrypted_c = chr(ord(decoded_message[i]) ^ ord(key_c))
            decrypted_chars.append(decrypted_c)

        decrypted_message = ''.join(decrypted_chars)

        Label(screen1, text="DECRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message)

correct_password = "4321"

def encrypt():
    password = code.get()

    if password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != correct_password:
        messagebox.showerror("encryption", "Invalid Password")
    else:
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)

        # ปรับแต่งข้อความโดยใช้ XOR กับรหัสผ่าน
        encrypted_chars = []
        for i in range(len(message)):
            key_c = password[i % len(password)]  # ใช้รหัสผ่านหมุนวน
            encrypted_c = chr(ord(message[i]) ^ ord(key_c))
            encrypted_chars.append(encrypted_c)

        encrypted_message = ''.join(encrypted_chars)

        # เข้ารหัสแบบ Base64
        encode_message = encrypted_message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)
        

def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("375x398")

    #icon
    image_icon=PhotoImage(file="C:\poy\mini-project\encryption.png")
    screen.iconphoto(False,image_icon)
    screen.title("Encryption and Decryption App")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter text for encryption and decryption",fg="black",font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",13)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)


    screen.mainloop()

main_screen()