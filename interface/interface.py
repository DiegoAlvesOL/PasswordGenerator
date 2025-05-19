from sys import path_importer_cache
import customtkinter
from customtkinter import CTkSlider, CTkSwitch
from passwordFunctions.passwordGenerator import generate_password
from models.password_entry import passwordEntry
from db.database import insert_password, create_table


# Função para gerar a senha e atualizar o campo de exibição
# Function to generate the password and update the display field
def update_password():
    length = int(length_slider.get())
    use_digits = switch_numbers.get() ==1
    use_letters = switch_letters.get() ==1
    use_symbols = switch_symbols.get() ==1
    if not (use_digits or use_letters or use_symbols):
        passwordDisplay.configure(text="⚠️ Activate at least one option (Letters, Digits or Symbols)")
    new_password = generate_password(length, use_digits,use_letters,use_symbols)
    passwordDisplay.configure(text=new_password)

# Função para copiar a senha
# Function to copy the password to clipboard
def copy_password():
    password = passwordDisplay.cget("text")
    mainWindow.clipboard_clear()
    mainWindow.clipboard_append(password)



# Essa função pegar as informações digitadas pelo usuário e enviar para classe passwordEntry no arquivo password_entry.py
def save_password():
    item = item_name.get()
    user = user_entry.get()
    site = website_address.get()
    password = passwordDisplay.cget("text")
    if not user or not site:
        passwordDisplay.configure(text= "⚠️ Please, entre with email and address of web site to save it")
        return
    save_password = passwordEntry(item,user,site,password)
    save_password.save_to_db()
    passwordDisplay.configure(text="✅ Password saved successfully!")
    print(save_password)



mainWindow = customtkinter.CTk()
# mainWindow.columnconfigure(0, weight=1)
# mainWindow.columnconfigure(1, weight=0)
mainWindow.geometry("330x450")
mainWindow.title("LockIt")
mainWindow.configure(fg_color="#051923")


# Todos os frames do App estão alocados aqui para facilitar a leitura todos os frames foram organizados de cima para baixo.

# Este frame é dedicado ao Display da senha.
display_frame = customtkinter.CTkFrame(mainWindow, fg_color="#003554")
display_frame.grid(row=1, column=0, columnspan=3,padx=10, pady=10)

# Este frame é dedicado container dedicado ao tamaho da senha.
slide_frame = customtkinter.CTkFrame(mainWindow)
slide_frame.grid(row=3,column=0,columnspan=3,padx=10,pady=10)

# Frame dedicado ao aos botões de swtich
switch_frame = customtkinter.CTkFrame(mainWindow)
switch_frame.grid(row=4,column=0,columnspan=3,padx=5,pady=5)

# Frame botão Generate Password
butto_frame_generate = customtkinter.CTkFrame(mainWindow, fg_color="transparent")
butto_frame_generate.grid(row=5,column=0,columnspan=3,padx=5,pady=5)
# Frame para bosão de salvar a senha
butto_frame_save = customtkinter.CTkFrame(mainWindow,fg_color="transparent")
butto_frame_save.grid(row=11,column=0,columnspan=3,padx=5,pady=5)


text = customtkinter.CTkLabel(mainWindow,
                              text="🔒 LockIt",
                              font=("Arial",24,"bold"))
text.grid(row=0, column=0, columnspan=3, pady =10, sticky="n")

# Campo de exibição da senha
# Password display field
passwordDisplay = customtkinter.CTkLabel(display_frame,
                                         text="Your password will appear here",
                                         text_color="White",
                                         font=("Courier",16),
                                         wraplength=300,
                                         justify="center")
passwordDisplay.grid(row=0, column=0, padx=5, pady=5)

# Botão para copiar a senha exibidao no passwordDisplay
copy_button = customtkinter.CTkButton(mainWindow, text="Copy this password",
                                      corner_radius=5,
                                      command= copy_password)
copy_button.grid(row=2, column=0,padx=2,pady=2)

# Botão para atualizar a senha
# Update password button
refresh_button = customtkinter.CTkButton(mainWindow, text="Reload",
                                         corner_radius=5,
                                         command= update_password)
refresh_button.grid(row=2, column=1, padx=2,pady=2)

# frame para linhar o layout do slide frame.
length_slider = CTkSlider(slide_frame,from_=4, to=40,
                          button_color="#00a6fb",
                          progress_color="#003554")
length_slider.grid(row=0,column=1,columnspan=2,padx=1,pady=1)
length_slider.set(12)
length_slider.configure(number_of_steps=36)


length_min = customtkinter.CTkLabel(slide_frame,
                                    text="4",
                                    text_color="White")
length_min.grid(row=0,column=0,padx=1,pady=1)

length_max = customtkinter.CTkLabel(slide_frame,
                                    text="40",
                                    text_color="White")
length_max.grid(row=0,column=3,padx=1,pady=1)

# 
switch_numbers = CTkSwitch(switch_frame,
                           text="Digits (e.g. 543)")
switch_numbers.grid(row=0,column=1,columnspan=2,padx=5)

switch_letters = CTkSwitch(switch_frame,
                           text="Letters (e.g. Aa)")
switch_letters.grid(row=1,column=1,columnspan=2,padx=5)
switch_letters.select()

switch_symbols = CTkSwitch(switch_frame,
                           text="Symbols (e.g. $#@!)")
switch_symbols.grid(row=2,column=1,columnspan=2,padx=5)

# Botão para gerar a senha
# Button to generate the password
generate_button = customtkinter.CTkButton(butto_frame_generate, text="Generate Password",
                                          corner_radius=5,
                                          command = update_password)
generate_button.grid(row=0,column=1,padx=2,pady=2)


# Campo para informar o tamanho da senha
# Field to enter the password length
# length_entry = customtkinter.CTkEntry(mainWindow, placeholder_text="Enter the password length",
#                                       width=300,
#                                       justify="center")
# length_entry.grid(row=7, column=0, columnspan=3,padx=5, pady=1)

item_name = customtkinter.CTkEntry(mainWindow, placeholder_text="Item name",
                                   text_color="White",
                                   width=300,
                                   justify="left",
                                   fg_color="#051923",
                                   border_color="#003554")
item_name.grid(row=8,column=0,columnspan=3,padx=5,pady=1)

user_entry = customtkinter.CTkEntry(mainWindow, placeholder_text="Enter with email/user",
                                    text_color="White",
                                    width=300,
                                    justify="left",
                                    fg_color="#051923",
                                    border_color="#003554")
user_entry.grid(row=9,column=0,columnspan=3,padx=5,pady=1)

website_address = customtkinter.CTkEntry(mainWindow, placeholder_text="Web address",
                                           text_color="White",
                                           width=300,
                                           justify="left",
                                           fg_color="#051923",
                                           border_color="#003554")
website_address.grid(row=10,column=0,columnspan=3,padx=5,pady=1)

save_button = customtkinter.CTkButton(butto_frame_save, text="Save",
                                      corner_radius=5,
                                      command= save_password)
save_button.grid(row=11,column=1,padx=1,pady=1)

create_table()

# length_entry.insert(0,"16")

mainWindow.mainloop()

