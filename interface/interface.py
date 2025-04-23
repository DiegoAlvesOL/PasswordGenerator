import customtkinter

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
mainWindown.geometry("500x280")
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

# Campo para informar o tamanho da senha
# Field to enter the password length
length_entry = customtkinter.CTkEntry(mainWindown, placeholder_text="Enter the password length",
                                      width=200,
                                      justify="center")
length_entry.grid(row=2, column=0, columnspan=3, pady=5)
# length_entry.insert(0,"16")

# Apenas um frame para agrupar os botões, quase que um container para os botões do app
# Just a frame to group the buttons, almost like a container for the app buttons
butto_frame = customtkinter.CTkFrame(mainWindown, fg_color="transparent")
butto_frame.grid(row=3, column=0, columnspan=3, pady=10)

# Botão para gerar a senha
# Button to generate the password
generate_button = customtkinter.CTkButton(butto_frame, text="Generate Password",
                                          command = update_password)
generate_button.grid(row=0, column=0, padx=5)

# Botão para copiar senha:
# Button to copy the password
copy_button = customtkinter.CTkButton(butto_frame, text="Copy Password",
                                      command= copy_password)
copy_button.grid(row=0, column=1,padx=5)

# Botão para atualizar a senha
# Update password button
refresh_button = customtkinter.CTkButton(butto_frame, text="Reload",
                                         command= update_password)
refresh_button.grid(row=0, column=3, padx=5)


mainWindown.mainloop()

