#!/usr/bin/env python
"""main.py: Interfaz gráfica para la gestión y almacenamiento de la información de los
estudiantes en la base de datos del sistema de registro de asistencia"""
__author__ = "Ana María Manso Rodríguez"
__credits__ = ["Ana María Manso Rodríguez"]
__version__ = "1.0"
__status__ = "Development"

import tkinter as tk

from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import Calendar
from PIL import Image
from PIL import ImageTk

from db_functions import *
from widget_aux import *
from resources_aux import resource_path


# Página principal
class MainMenu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.image = Image.open(resource_path('Captura.jpg'))
        self.image = self.image.resize((271, 129))
        self.image = ImageTk.PhotoImage(self.image)

        self.logo = tk.Label(self.frame, image=self.image)
        self.logo.grid(row=0, column=0, pady=20)

        # -----------Buttons-----------

        # New Record Date button
        self.buttonNewRecordDate = tk.Button(self.frame, text='Crear nuevo evento', height=1, width=25, bg="SteelBlue1",
                                             fg="white", command=self.openNewRecordDate)
        self.buttonNewRecordDate.grid(row=1, column=0, pady=4)

        # Get Record button
        self.buttonGetRecord = tk.Button(self.frame, text='Registros', height=1, width=25, bg="SteelBlue1", fg="white",
                                         command=self.openGetRecords)
        self.buttonGetRecord.grid(row=2, column=0, pady=4)

        # Students Administration button
        self.buttonStudentsAdmin = tk.Button(self.frame, text="Gestión alumnos", height=1, width=25, bg="SteelBlue1",
                                             fg="white", command=self.openStudentsAdmin)
        self.buttonStudentsAdmin.grid(row=3, column=0, pady=4)

        self.frame.pack(expand=True)
        self.frame.config(bg="white")

    # Open New Record Date window
    def openNewRecordDate(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("ETSIDI Asistencia - Crear nuevo evento")
        self.newWindow.config(bg="white")
        self.newWindow.geometry("600x350")
        self.app = NewRecordDate(self.newWindow)

    # Open Get Records window
    def openGetRecords(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("ETSIDI Asistencia -Registros")
        self.app = GetRecords(self.newWindow)

    # Open Students Administration window
    def openStudentsAdmin(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("ETSIDI Asistencia - Gestión estudiantes")
        self.app = StudentsAdmin(self.newWindow)


# Ventana de aplicación - Crear nuevo evento
class NewRecordDate:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.description = tk.StringVar()
        self.email = tk.StringVar()

        # -----------Labels------------

        self.descripLabel = tk.Label(self.frame, text="Descripción :")
        self.descripLabel.grid(row=0, column=0, padx=10, pady=10)
        self.descripLabel.config(bg="SteelBlue1", fg="white", height=1, width=25)

        self.emailLabel = tk.Label(self.frame, text="Email :")
        self.emailLabel.grid(row=1, column=0, padx=10, pady=10)
        self.emailLabel.config(bg="SteelBlue1", fg="white", height=1, width=25)

        self.datetimeLabel = tk.Label(self.frame, text="")
        self.datetimeLabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
        self.datetimeLabel.config(bg="SteelBlue1")

        self.groupLabel = tk.Label(self.frame, text="")
        self.groupLabel.grid(row=3, column=1, sticky="e", padx=10, pady=10)
        self.groupLabel.config(bg="SteelBlue1")

        self.subjectLabel = tk.Label(self.frame, text="")
        self.subjectLabel.grid(row=4, column=1, sticky="e", padx=10, pady=10)
        self.subjectLabel.config(bg="SteelBlue1")

        # -----------Entrys------------

        self.descripEntry = tk.Entry(self.frame, textvariable=self.description)
        self.descripEntry.grid(row=0, column=1, padx=10, pady=10)
        self.descripEntry.config(fg="SteelBlue1", justify="right", width=40)

        self.emailEntry = tk.Entry(self.frame, textvariable=self.email)
        self.emailEntry.grid(row=1, column=1, padx=10, pady=10)
        self.emailEntry.config(fg="SteelBlue1", justify="right", width=40)

        # -----------Buttons-----------

        # Open Datetime window button
        self.dateButton = tk.Button(self.frame, text="Seleccionar fecha y hora", height=1, width=25, bg="SteelBlue1",
                                    fg="white", command=self.chooseDatetime)
        self.dateButton.grid(row=2, column=0, padx=10, pady=10)

        # Open Groups window button
        self.groupButton = tk.Button(self.frame, text="Seleccionar grupos", height=1, width=25, bg="SteelBlue1",
                                     fg="white", command=self.chooseGroups)
        self.groupButton.grid(row=3, column=0, padx=10, pady=10)

        # Open Subjects window button
        self.subjectButton = tk.Button(self.frame, text="Seleccionar asignaturas", height=1, width=25, bg="SteelBlue1",
                                       fg="white", command=self.chooseSubject)
        self.subjectButton.grid(row=4, column=0, padx=10, pady=10)

        # Sets New Event in DB
        self.setEventButton = tk.Button(self.frame, text="Establecer fecha examen", height=1, width=25, bg="SteelBlue1",
                                        fg="white", command=self.set_event)
        self.setEventButton.grid(row=5, column=0, padx=10, pady=10)

        # Exit button
        self.quitButton = tk.Button(self.frame, text='Salir', width=25, command=self.close_windows)
        self.quitButton.grid(row=6, column=0)

        self.frame.pack(expand=True)
        self.frame.config(bg="white")

    # Open Datetime window
    def chooseDatetime(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("Seleccionar fecha de examen")
        self.newWindow.config(bg="white")
        self.app = Datetime(self.newWindow, self.datetimeLabel)

    # Open Groups window
    def chooseGroups(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("Seleccionar grupos")
        self.newWindow.config(bg="white")
        self.app = Groups(self.newWindow, self.groupLabel)

    # Open Subjects window
    def chooseSubject(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("Seleccionar asignaturas")
        self.newWindow.config(bg="white")
        self.app = Subjects(self.newWindow, self.subjectLabel, self.groupLabel.cget("text"))

    # Set new event into database
    def set_event(self):
        if self.description.get() and self.datetimeLabel.cget("text") and self.groupLabel.cget("text") and \
                self.subjectLabel.cget("text") and self.email.get():
            # Insert data to DDBB
            inserted = insert_new_event_date(self.description.get(), self.datetimeLabel.cget("text"), self.groupLabel.cget("text"),
                                             self.subjectLabel.cget("text"), self.email.get())
            if inserted:
                messagebox.showinfo("BBDD", "Fecha de examen establecida")
            else:
                messagebox.showerror("BBDD", "No se ha podido establecer la fecha de examen")
        else:
            messagebox.showerror("Establecer fecha de examen", "Falta algun campo por rellenar")

    # Destroys current window
    def close_windows(self):
        self.master.destroy()


# Ventana de aplicación - Fecha y hora
class Datetime:
    def __init__(self, master, label):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.config(bg="white")
        self.cal = Calendar(self.frame, select="day", year=2021, month=2, day=9)
        self.cal.grid(row=0, column=0, padx=20, pady=20)
        self.time = App(self.frame)
        self.time.grid(row=1, column=0, padx=10, pady=10)
        self.label = label

        # -----------Buttons-----------

        # Select datetime button
        self.pickDateButton = tk.Button(self.frame, text="Seleccionar fecha y hora", command=self.grab_date)
        self.pickDateButton.grid(row=2, column=0, pady=20, padx=20)

        # Exit button
        self.quitButton = tk.Button(self.frame, text='Salir', width=25, command=self.close_windows)
        self.quitButton.grid(row=3, column=0, padx=20, pady=20)

        self.frame.pack()

    # Prints chosed date into parent window (NewRecordDate)
    def grab_date(self):
        chosedDatetime = self.cal.get_date() + " " + self.time.hourstr.get() + ":" + self.time.minstr.get()
        self.label.config(text=chosedDatetime)

    # Destroys current window
    def close_windows(self):
        self.master.destroy()


# Ventana de aplicación - Grupos
class Groups:
    def __init__(self, master, label):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.config(bg="white")
        self.label = label
        self.lista = []
        self.variables = []

        for i in get_groups():
            self.variables.append(tk.IntVar())
            self.lista.append(i[0])

        # -----------Buttons-----------

        # Drop down record list
        for i in range(len(self.lista)):
            tk.Checkbutton(self.frame, text=self.lista[i], bg="light green", variable=self.variables[i], onvalue=1,
                           offvalue=0, command=self.optionGroups).grid(row=i, column=0, padx=10, pady=10)

        # Exit button
        self.quitButton = tk.Button(self.frame, text='Salir', width=25, command=self.close_windows)
        self.quitButton.grid(row=1, column=1, padx=20, pady=20)

        self.frame.pack()

    def optionGroups(self):
        selectedGroups = ""
        for i in range(len(self.lista)):
            if self.variables[i].get() == 1:
                selectedGroups += " " + self.lista[i]
        self.label.config(text=selectedGroups)

    # Destroys current window
    def close_windows(self):
        self.master.destroy()


# Ventana de aplicación - Asignaturas
class Subjects:
    def __init__(self, master, label, groups):
        self.master = master
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)
        self.label = label
        self.subjects_labels = []
        self.desplegableData = []
        self.var = groups.split()

        for i in range(len(self.var)):
            self.subjects_labels.append(tk.Label(self.frame1, text=self.var[i]))
            self.subjects_labels[i].grid(row=i, column=0, sticky="e", padx=10, pady=10)
            self.subjects_labels[i].config(bg="SteelBlue1", fg="white")
            valores = []
            for j in get_subjets(self.var[i]):
                valores.append(j[0])
            self.desplegableData.append(Desplegable(valores, self.frame1))
            self.desplegableData[i].grid(row=i, column=1)

        # -----------Buttons-----------

        # Choose subject
        self.pickSubjectButton = tk.Button(self.frame2, text="Seleccionar asignaturas", command=self.grab_subject)
        self.pickSubjectButton.grid(row=0, column=0, padx=20, pady=20)

        # Exit button
        self.quitButton = tk.Button(self.frame2, text='Salir', width=25, command=self.close_windows)
        self.quitButton.grid(row=1, column=0, padx=20, pady=20)

        self.frame1.pack(expand=True)
        self.frame2.pack(expand=True)
        self.frame1.config(bg="white")
        self.frame2.config(bg="white")

    # Prints chosed subjects into parent window (NewRecordDate)
    def grab_subject(self):
        selectedSubjects = ""
        for i in range(len(self.desplegableData)):
            if i == 0:
                selectedSubjects += self.desplegableData[i].combo.get()
            else:
                selectedSubjects += '\n' + self.desplegableData[i].combo.get()

        self.label.config(text=selectedSubjects)

    # Destroys current window
    def close_windows(self):
        self.master.destroy()


# Ventana de aplicación - Registros
class GetRecords:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        values = get_record_dates()

        # Drop down list widget
        self.desplegable = Desplegable(values, self.frame)
        self.desplegable.grid(row=0, column=0, padx=10, pady=10)

        # -----------Buttons-----------

        # Get Record button
        self.getRecordsButton = tk.Button(self.frame, text='Descargar Registros', command=self.getStudentsRecords)
        self.getRecordsButton.grid(row=1, column=0, padx=10, pady=10)

        # Exit button
        self.quitButton = tk.Button(self.frame, text='Salir', width=25, command=self.close_windows)
        self.quitButton.grid(row=2, column=0, padx=10, pady=10)

        self.frame.pack(expand=True)
        self.frame.config(bg="white")

    # Downloads information from database to Excel file
    def getStudentsRecords(self):
        selected_event = self.desplegable.combo.get()
        id_selected_event, name_selected_event = selected_event.split('···')[0], selected_event.split('···')[1]
        get_students_records(id_selected_event, name_selected_event)

    # Destroys current window
    def close_windows(self):
        self.master.destroy()


# Ventana de aplicación - Gestión alumnos
class StudentsAdmin:
    def __init__(self, master):
        self.master = master
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)

        # -----------Labels------------

        self.registrationLabel = tk.Label(self.frame1, text="Gestión nuevos alumnos")
        self.registrationLabel.grid(row=0, column=0, sticky="e", pady=20, padx=20)
        self.registrationLabel.config(bg="white")

        self.newStudentsLabel = tk.Label(self.frame2, text="Gestión matriculas")
        self.newStudentsLabel.grid(row=0, column=0, sticky="e", pady=20, padx=20)
        self.newStudentsLabel.config(bg="white")

        # -----------Buttons-----------

        # Upload new students to DB button
        self.buttonUploadNewStudents = tk.Button(self.frame1, text="Subir alumnos de nuevo ingreso al sistema",
                                                 bg="SteelBlue1", fg="white", command=self.s_csv_to_db)
        self.buttonUploadNewStudents.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        # Upload student's data (subjects, groups) to DB button
        self.buttonUploadStudents = tk.Button(self.frame2, text="Subir nuevas matriculas al sistema", bg="SteelBlue1",
                                              fg="white", command=self.csv_to_ddbb)
        self.buttonUploadStudents.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        # Delete student's data from DB
        self.deleteStudentsRegistration = tk.Button(self.frame2, text="Eliminar matriculas del sistema",
                                                    bg="SteelBlue1", fg="white", command=self.deleteRegistration)
        self.deleteStudentsRegistration.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        # Exit button
        self.quitButton = tk.Button(self.frame2, text='Salir', width=25, command=self.close_windows)
        self.quitButton.grid(row=3, column=0, padx=10, pady=10)

        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=1, sticky="nsew")
        self.frame1.config(bg="SteelBlue1")
        self.frame2.config(bg="SteelBlue2")

    # Insert students into database from CSV or Excel file
    def s_csv_to_db(self):
        file = filedialog.askopenfilename(title="Abrir", initialdir="/home/pi/Desktop/",
                                          filetypes=(("Todos los archivos excel", "*.xls *.xlsx *.csv"),))
        if new_students_to_db(file):
            messagebox.showinfo("BBDD", "Nuevos alumnos insertados correctamente")
        else:
            messagebox.showerror("BBDD", "Error, no se ha podido dar de alta los nuevos usuarios")

    # Insert Apolo's students data into database from CSV or Excel file
    def csv_to_ddbb(self):
        file = filedialog.askopenfilename(title="Abrir", initialdir="/home/pi/Desktop/",
                                          filetypes=(("Todos los archivos excel", "*.xls *.xlsx *.csv"),))
        apolo_file_to_ddbb(file)
        messagebox.showinfo("BBDD", "Información actualizada correctamente")

    # Delete student's groups and subjects data from database
    def deleteRegistration(self):
        delete_from_table("examn_groups")
        delete_from_table("subjects")
        delete_from_table("registration")
        messagebox.showinfo("BBDD", "Información eliminada correctamente")

    # Destroys current window
    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    root.title("ETSIDI Asistencia")
    root.geometry("600x350")
    root.config(bg='white')
    app = MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
