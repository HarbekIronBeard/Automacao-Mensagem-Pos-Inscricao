import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import pyperclip  
from datetime import datetime 


def mostrar_informacoes():
    parentname = parentname_var.get()
    studentname = studentname_var.get()
    platformlogin = platformlogin_var.get()
    platformpassword = platformpassword_var.get()
    course = course_var.get()
    day = day_var.get()
    time = time_var.get()
    
    selected_date = calendar.get_date()
    formatted_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%d/%m") 
    gender = gender_var.get()

    if gender == "Menino":
        resultado = (
            f"Olá {parentname}, segue o link para que o {studentname} entre na plataforma: https://platform.kodland.org/pt/login/\n"
            f"Login: {platformlogin}\n" 
            f"Senha: {platformpassword}\n"
            f"Pedimos que sejam observadas as letras maiúsculas e minúsculas.\n"
            f"O {studentname} foi matriculado na turma de {course} de {day} às {time} e as aulas se iniciam em {formatted_date}."
        )
    else:
        resultado = (
            f"Olá {parentname}, segue o link para que a {studentname} entre na plataforma: https://platform.kodland.org/pt/login/\n"
            f"Login: {platformlogin}\n" 
            f"Senha: {platformpassword}\n"
            f"Pedimos que sejam observadas as letras maiúsculas e minúsculas.\n"
            f"A {studentname} foi matriculada na turma de {course} de {day} às {time} e as aulas se iniciam em {formatted_date}."
        )

    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, resultado)

def copiar_resultado():
    pyperclip.copy(resultado_text.get(1.0, tk.END).strip())

root = tk.Tk()
root.title("Cadastro de Aluno")
root.geometry("1024x960")
root.configure(bg="#2E2E2E")

style = ttk.Style()
style.theme_use('clam') 
style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF")
style.configure("TEntry", fieldbackground="#3E3E3E", background="#3E3E3E", foreground="#FFFFFF")
style.configure("TButton", background="#4E4E4E", foreground="#FFFFFF")

parentname_var = tk.StringVar()
studentname_var = tk.StringVar()
gender_var = tk.StringVar()
platformlogin_var = tk.StringVar()
platformpassword_var = tk.StringVar()
course_var = tk.StringVar()
day_var = tk.StringVar()
time_var = tk.StringVar()

ttk.Label(root, text="Nome do pai:").pack(pady=5)
ttk.Entry(root, textvariable=parentname_var).pack(pady=5)

ttk.Label(root, text="Nome do aluno:").pack(pady=5)
ttk.Entry(root, textvariable=studentname_var).pack(pady=5)

ttk.Label(root, text="Login do aluno:").pack(pady=5)
ttk.Entry(root, textvariable=platformlogin_var).pack(pady=5)

ttk.Label(root, text="Senha do aluno:").pack(pady=5)
ttk.Entry(root, textvariable=platformpassword_var).pack(pady=5)

courses = ('Roblox', 'Python', 'Scratch')
days = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
times = ('8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00')
gender = ('Menino', 'Menina')

ttk.Label(root, text="Gênero do aluno:").pack(pady=5)
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=gender)
gender_combobox.pack(pady=5)

ttk.Label(root, text="Selecione o Curso:").pack(pady=5)
course_combobox = ttk.Combobox(root, textvariable=course_var, values=courses)
course_combobox.pack(pady=5)

ttk.Label(root, text="Selecione o Dia:").pack(pady=5)
day_combobox = ttk.Combobox(root, textvariable=day_var, values=days)
day_combobox.pack(pady=5)

ttk.Label(root, text="Selecione a Hora:").pack(pady=5)
time_combobox = ttk.Combobox(root, textvariable=time_var, values=times)
time_combobox.pack(pady=5)

ttk.Label(root, text="Selecione a Data:").pack(pady=5)
calendar = Calendar(root)
calendar.pack(pady=5)

submit_button = ttk.Button(root, text="Mostrar Informações", command=mostrar_informacoes)
submit_button.pack(pady=5)

resultado_text = tk.Text(root, height=10, width=80, bg="#3E3E3E", fg="#FFFFFF")
resultado_text.pack(pady=5)

copy_button = ttk.Button(root, text="Copiar Resultado", command=copiar_resultado)
copy_button.pack(pady=5)

root.mainloop()

#AOS QUE FUTURAMENTE POSSAM MEXER NESSE CÓDIGO, O PYINSTALLER TEM ALGUM PROBLEMA COM O BABEL NUMBERS, PRA ELE FUNCIONAR DIREITO BASTA RODAR pyinstaller --hidden-import babel.numbers Main.py