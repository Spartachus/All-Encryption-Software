from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import pyperclip
from morse import moirses as Msc
from ceasar import cipher, decipher
from ttkbootstrap import *


def help():
    messagebox.showinfo("N͔͕̪c̟͉̙r̡̻̠y̞̪̺p͍̦͎t͖̻̼ W͕͇i̺͍͜k͇̞͇i̡̙͜",message="AͣDͩDͩ ᴛⷮOͦ EͤNCͨRͬY Рⷬᴛⷮ")

# ---------------------------- Ceasar's Cipher ------------------------------- #
def cypher():
    Sentence = text_textt.get('1.0','end-1c')
    ceaser = cipher(Sentence,5)
    text_textt.delete(1.0,END)
    text_textt.insert(END,ceaser)
    pyperclip.copy(ceaser)
    with open("Cipher.txt", "w") as f:
       f.write(ceaser)
    messagebox.showinfo("N͔͕̪c̟͉̙r̡̻̠y̞̪̺p͍̦͎t͖̻̼ W͕͇i̺͍͜k͇̞͇i̡̙͜",message="㆜ԋҽ ടρҽ𝓬ιαɬ ടԋι⨍𝜏 α𝓶σᥙɳ𝜏 ⨍σɾ 𝜏ԋҽ 𝓬ҽαടαɾ'ട 𝓬ιρԋҽɾ ιട 5.")

def decyphr():
    Sentence = text_textt.get('1.0','end-1c')
    ceaser = decipher(Sentence,5)
    text_textt.delete(1.0,END)
    text_textt.insert(END,ceaser)
    pyperclip.copy(ceaser)
    with open("Decipher.txt", "w") as f:
       f.write(ceaser)
    messagebox.showinfo("N͔͕̪c̟͉̙r̡̻̠y̞̪̺p͍̦͎t͖̻̼ W͕͇i̺͍͜k͇̞͇i̡̙͜",message="Ⲉ𝓿ⲉꞅⲩ ⲉⲛⲥꞅⲩⲣⲧⲓⲟⲛ 𝓰ⲉⲧ𝛓 𝛓ⲁ𝓿ⲉⲇ ⲓⲛ .ⲧⲭⲧ 𝓯ⲓ𝓵ⲉ \n ⲁⲛⲇ ⲁ𝓵𝛓ⲟ ⲥⲟⲣⲣⲓⲉⲇ ⲓⲛⲧⲟ ⲩⲟ𐌵ꞅ ⲥ𝓵ⲓⲣⲃⲟⲁꞅⲇ.")
    

# ---------------------------- Morse Code ------------------------------- #
def morse_code():
    Sentence = text_textt.get('1.0','end-1c')
    morse = Msc(input=Sentence)
    text_textt.delete(1.0,END)
    text_textt.insert(END,morse)
    pyperclip.copy(morse)
    with open("morse.txt", "w") as f:
       f.write(morse)
    messagebox.showinfo("N͔͕̪c̟͉̙r̡̻̠y̞̪̺p͍̦͎t͖̻̼ W͕͇i̺͍͜k͇̞͇i̡̙͜",message="Ⲉ𝓿ⲉꞅⲩ ⲉⲛⲥꞅⲩⲣⲧⲓⲟⲛ 𝓰ⲉⲧ𝛓 𝛓ⲁ𝓿ⲉⲇ ⲓⲛ .ⲧⲭⲧ 𝓯ⲓ𝓵ⲉ \n ⲁⲛⲇ ⲁ𝓵𝛓ⲟ ⲥⲟⲣⲣⲓⲉⲇ ⲓⲛⲧⲟ ⲩⲟ𐌵ꞅ ⲥ𝓵ⲓⲣⲃⲟⲁꞅⲇ.")


# ---------------------------- Encryption ------------------------------- #
def add():
    data = text_textt.get('1.0','end-1c')

    with open("data.txt","a") as Keystore:
       Keystore.write(data)

def encrypt():#the encryption function
    key = Fernet.generate_key()
    cryptography_entry.insert(0,key)
  # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    messagebox.showinfo("N͔͕̪c̟͉̙r̡̻̠y̞̪̺p͍̦͎t͖̻̼ W͕͇i̺͍͜k͇̞͇i̡̙͜",message="🆃🅷🅴 🅲🆁🆈🅿🆃🅾🅶🆁🅰🅿🅷🆈 🅺🅴🆈 🅸🆂 🅰 🆂🅿🅴🅲🅸🅰🅻 🅺🅴🆈 🆂🅾 🅺🅴🅴🅿 🅸🆃 🆂🅰🅵🅴❗❗.")


  # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
  
  # using the generated key
    fernet = Fernet(key)
  
  # opening the original file to encrypt
    with open('data.txt', 'rb') as file:
        original = file.read()
      
  # encrypting the file
    encrypted = fernet.encrypt(original)
  
  # opening the file in write mode and
  # writing the encrypted data
    with open('Encrypted.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# using the key
def decrypt(): #the decryption function
  with open('filekey.key', 'rb') as f:
     key = f.read()
  fernet = Fernet(key)
  
  # opening the encrypted file
  with open('Encrypted.txt', 'rb') as enc_file:
      encrypted = enc_file.read()
  
  # decrypting the file
  decrypted = fernet.decrypt(encrypted)
  
  # opening the file in write mode and
  # writing the decrypted data
  with open('Decrypted.txt', 'wb') as dec_file:
      dec_file.write(decrypted)
  messagebox.showinfo("N͔͕̪c̟͉̙r̡̻̠y̞̪̺p͍̦͎t͖̻̼ W͕͇i̺͍͜k͇̞͇i̡̙͜",message="Ⲉ𝓿ⲉꞅⲩ ⲉⲛⲥꞅⲩⲣⲧⲓⲟⲛ 𝓰ⲉⲧ𝛓 𝛓ⲁ𝓿ⲉⲇ ⲓⲛ .ⲧⲭⲧ 𝓯ⲓ𝓵ⲉ \n ⲁⲛⲇ ⲁ𝓵𝛓ⲟ ⲥⲟⲣⲣⲓⲉⲇ ⲓⲛⲧⲟ ⲩⲟ𐌵ꞅ ⲥ𝓵ⲓⲣⲃⲟⲁꞅⲇ.")    


# ---------------------------- UI SETUP ------------------------------- #

window = Window(themename="superhero")
window.title("Ɲ𝓬ɾყρ𝜏.ιò")
window.geometry("480x500")

#title_label = Label(text="Ɲ𝓬ɾყρ𝜏.ιò")
canvas = Canvas(width=200, height = 200)
# #logo_img = PhotoImage(file= "logo.png")
canvas.create_text(75,75,text = "Ɲ𝓬ɾყρ𝜏.ιò", font=("Arial", 30, "bold"), fill="black")
# #canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0,column = 1, columnspan=3)



#Labels
text_label = Label(text = "t͒́͝e̽̈́̚x̾̓̿t͆̕͝:",)
cryptography_label = Label(text = "⼕尺丫尸七ㄖᎶ尺闩尸卄丫\n长🝗丫")


cryptography_label.grid(row = 2, column = 0)
text_label.grid(row = 1, column = 0)

#Entries
text_textt = Text(width=30,height=5)
cryptography_entry = Entry(width = 35)

text_textt.focus()

cryptography_entry.grid(row = 2, column = 1, columnspan = 2,pady=10)
text_textt.grid(row = 1, column = 1, columnspan = 2)

#Buttons

Decrypt_Button = Button(text = "ᗪ🝗⼕尺ㄚ尸ㄒ", command = decrypt,width=15)
Encrypt_Button = Button(text = "ꓕԀ⅄ꓤϽNƎ", command = encrypt,width=15)
Morse_Button = Button(text = "ᙏσɾടҽ", command = morse_code,width=15)
help_Button = Button(text = "Help", command = help,width=15)
Cipher_Button = Button(text = "ɹǝɥdᴉϽǝᗡ", command = cypher,width=15)
Decipher_Button = Button(text = "🅲🅸🅿🅷🅴🆁", command = decyphr,width=15)
Add_Button = Button(text = "🅰🅳🅳", command =add,width=40)

Decrypt_Button.grid(row = 5, column = 1,pady=5)
Encrypt_Button.grid(row = 5, column = 2)
Morse_Button.grid(row = 5, column = 0)
help_Button.grid(row = 6, column = 0)
Cipher_Button.grid(row = 6, column = 2)
Decipher_Button.grid(row = 6, column = 1,pady=5)
Add_Button.grid(row= 7, column = 1, columnspan=3)

window.mainloop()