import customtkinter
from customtkinter import CTkSlider, CTkSwitch

from passwordFunctions.passwordGenerator import generate_password

# Função para gerar a senha e atualizar o campo de exibição
# Function to generate the password and update the display field
def update_password():
    length = int(length_entry.get())
    new_password = generate_password(length)
    passwordDisplay.configure(text=new_password)

# Função para copiar a senha
# Function to copy the password to clipboard
def copy_password():
    password = passwordDisplay.cget("text")
    mainWindown.clipboard_clear()
    mainWindown.clipboard_append(password)

mainWindown = customtkinter.CTk()
# mainWindown.columnconfigure(0, weight=1)
# mainWindown.columnconfigure(1, weight=0)
mainWindown.geometry("460x380")
mainWindown.title("LockIt")

text = customtkinter.CTkLabel(mainWindown,
                              text="🔒 LockIt",
                              font=("Arial",24,"bold"))
text.grid(row=0, column=0, columnspan=3, pady =10, sticky="n")

display_frame = customtkinter.CTkFrame(mainWindown, fg_color="#4D4D4D")
display_frame.grid(row=1, column=0, columnspan=3, pady=10)

# Campo de exibição da senha
# Password display field
passwordDisplay = customtkinter.CTkLabel(display_frame,
                                         text="Your password will appear here",
                                         text_color="White",
                                         font=("Courier",16),
                                         wraplength=300,
                                         justify="center")
passwordDisplay.grid(row=0, column=0,columnspan=3, padx=5, pady=5)

copy_button = customtkinter.CTkButton(mainWindown, text="Copy this password",
                                      corner_radius=5,
                                      command= copy_password)
copy_button.grid(row=2, column=1,padx=5)

# frame para linhar o layout do slide frame.
slide_frame = customtkinter.CTkFrame(mainWindown)
slide_frame.grid(row=3,column=0,columnspan=3,padx=10,pady=10)
length_slider = CTkSlider(slide_frame,from_=4, to=40,
                          button_color="#00a6fb",
                          progress_color="#003554")
length_slider.grid(row=0,column=1,columnspan=2,padx=1,pady=1)

length_min = customtkinter.CTkLabel(slide_frame,
                                    text="4",
                                    text_color="White")
length_min.grid(row=0,column=0,padx=1,pady=1)

length_max = customtkinter.CTkLabel(slide_frame,
                                    text="40",
                                    text_color="White")
length_max.grid(row=0,column=3,padx=1,pady=1)

swtich_frame = customtkinter.CTkFrame(mainWindown)
swtich_frame.grid(row=4,column=0,columnspan=3,padx=5,pady=5)


swtich_numbers = CTkSwitch(swtich_frame,
                           text="Digits (e.g. Aa)")
swtich_numbers.grid(row=0,column=1,columnspan=2,padx=5)

swtich_letters = CTkSwitch(swtich_frame,
                           text="Letters (e.g. Aa)")
swtich_letters.grid(row=1,column=1,columnspan=2,padx=5)

swtich_symbols = CTkSwitch(swtich_frame,
                           text="Symbols (e.g. $#@!)")
swtich_symbols.grid(row=2,column=1,columnspan=2,padx=5)


# text_swtich_numbers = customtkinter.CTkLabel(swtich_frame,
#                                              text="Digits (e.g. 678)",
#                                              text_color="White")
# text_swtich_numbers.grid(row=0,column=0)
#
# text_swtich_letters = customtkinter.CTkLabel(swtich_frame,
#                                              text="Digits (e.g. Aa)",
#                                              text_color="White")
# text_swtich_letters.grid(row=1,column=0)
#
# text_swtich_symbols = customtkinter.CTkLabel(swtich_frame,
#                                              text="Digits (e.g. $#@!)",
#                                              text_color="White")
# text_swtich_symbols.grid(row=2,column=0)
#



# Campo para informar o tamanho da senha
# Field to enter the password length
length_entry = customtkinter.CTkEntry(mainWindown, placeholder_text="Enter the password length",
                                      width=200,
                                      justify="center")
length_entry.grid(row=5, column=0, columnspan=3, pady=5)
# length_entry.insert(0,"16")

# Apenas um frame para agrupar os botões, quase que um container para os botões do app
# Just a frame to group the buttons, almost like a container for the app buttons
butto_frame = customtkinter.CTkFrame(mainWindown, fg_color="transparent")
butto_frame.grid(row=5, column=0, columnspan=3, pady=10)

# Botão para gerar a senha
# Button to generate the password
generate_button = customtkinter.CTkButton(butto_frame, text="Generate Password",
                                          corner_radius=20,
                                          command = update_password)
generate_button.grid(row=0, column=0, padx=5)

# Botão para copiar senha:
# Button to copy the password
copy_button = customtkinter.CTkButton(butto_frame, text="Copy Password",
                                      corner_radius=20,
                                      command= copy_password)
copy_button.grid(row=0, column=1,padx=5)

# Botão para atualizar a senha
# Update password button
refresh_button = customtkinter.CTkButton(butto_frame, text="Reload",
                                         corner_radius=20,
                                         command= update_password)
refresh_button.grid(row=0, column=3, padx=5)


mainWindown.mainloop()

