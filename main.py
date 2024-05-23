import tkinter as tk
from tkinter import messagebox
from time import strftime
from mail import mail_sender as ms
from admin import *


# from PIL import Image, ImageTk


# --------------------------------- password and id for admins -------------------------------------

patient_name = 0
# --------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title('AIML')
root.geometry('925x500+200+150')
root.configure(bg="cyan")
root.resizable(False, False)
hosp_name = 'SRAV HOSPITAL'


# ----------------------------------------------------------------

def main():
    import data_base

    helper = data_base.DBHelper()
    frame = tk.Frame(root, width=925, height=1000, bg='cyan')
    frame.place(x=0, y=0)
    hospital_name = tk.Label(root, text=f'{hosp_name}', bg='pink', fg='#800000',
                             font=('Arial', 27, 'bold'))
    hospital_name.place(x=330, y=15)

    # --------------------------------------------time function-----------------------------------
    def time_function():
        time_string = strftime('%H:%M:%S %p\n'
                               '%D')
        time_label = tk.Label(text=time_string, font=('raleway', 12, 'bold'), bg='cyan')
        time_label.place(x=800, y=450)
        time_label.after(1000, time_function)
        hii_56 = strftime('%Y/%m/%d')
        return hii_56

    # ---------------------------------------------Home button----------------------------------------------------
    def Home_button():
        button__ = tk.Button(text='Home', bg='yellow', fg='red3', cursor='hand2', font=('raleway', 15, 'bold'),
                             command=main)
        button__.place(x=380, y=450)

    # -------------------------------------------Add new patient---------------------------------------------------
    def new_patient_function():
        frame.destroy()

        def new_():
            id_ = entry_1.get()
            name_ = entry_2.get()
            age_ = entry_3.get()
            date = entry_4.get()
            reason_ = entry_5.get()
            bill_ = entry_6.get()
            email_ = entry_7.get()
            helper.insert_patient(id_, name_, age_, date, reason_, bill_, email_)
            operation_ = 'new'
            ms(name_, id_, email_, bill_, operation_, reason_, date)
            messagebox.showwarning('AIML', 'patient added successfully!!')
            entry_1.delete(0, 'end')
            entry_2.delete(0, 'end')
            entry_3.delete(0, 'end')
            entry_5.delete(0, 'end')
            entry_6.delete(0, 'end')
            entry_7.delete(0, 'end')

        frame_1_3 = tk.Frame(width=925, height=375, bg='cyan')
        frame_1_3.place(x=0, y=70)
        lable_1 = tk.Label(frame_1_3, text='Patient ID', bg='snow3', fg='black', width=13, font=('raleway', 15, 'bold'))
        lable_1.place(x=250, y=5)
        lable_2 = tk.Label(frame_1_3, text='Patient Name', bg='snow3', fg='black', width=13,
                           font=('raleway', 15, 'bold'))
        lable_2.place(x=250, y=55)
        lable_3 = tk.Label(frame_1_3, text='Patient Age', bg='snow3', fg='black', width=13,
                           font=('raleway', 15, 'bold'))
        lable_3.place(x=250, y=105)
        lable_4 = tk.Label(frame_1_3, text='Date', bg='snow3', fg='black', width=13, font=('raleway', 15, 'bold'))
        lable_4.place(x=250, y=155)
        lable_5 = tk.Label(frame_1_3, text='Reason', bg='snow3', fg='black', width=13, font=('raleway', 15, 'bold'))
        lable_5.place(x=250, y=205)
        label_6 = tk.Label(frame_1_3, text='Bill', bg='snow3', fg='black', width=13, font=('raleway', 15, 'bold'))
        label_6.place(x=250, y=255)
        lable_7 = tk.Label(frame_1_3, text='Email', bg='snow3', fg='black', width=13, font=('raleway', 15, 'bold'))
        lable_7.place(x=250, y=305)
        h = time_function()

        entry_1 = tk.Entry(frame_1_3, font=('raleway', 15))
        entry_1.place(x=500, y=5)
        entry_2 = tk.Entry(frame_1_3, font=('raleway', 15))
        entry_2.place(x=500, y=55)
        entry_3 = tk.Entry(frame_1_3, font=('raleway', 15))
        entry_3.place(x=500, y=105)
        entry_4 = tk.Entry(frame_1_3, font=('raleway', 15))
        entry_4.place(x=500, y=155)
        entry_5 = tk.Entry(frame_1_3, font=('raleway', 15))
        entry_5.place(x=500, y=205)
        entry_6 = tk.Entry(frame_1_3, font=('raleway', 15))
        entry_6.place(x=500, y=255)
        entry_7 = tk.Entry(frame_1_3, font=('raleway', 15))
        entry_7.place(x=500, y=305)

        button_1 = tk.Button(text='ADD', bg='light green', fg='black', font=('raleway', 11, 'bold'), cursor='hand2',
                             command=new_, width=10)
        button_1.place(x=410, y=410)
        entry_4.insert(0, h)
        entry_7.insert(0, 'Example@gmail.com')

    # ----------------------------------------Edit a patient details-----------------------------------------------

    def edit_patient_function():
        frame.destroy()

        def main_frames():
            def editing():
                import data_base as db
                helper_2 = db.DBHelper()
                editing_id = details[0]
                editing_name = entry_2.get()
                editing_age = entry_3.get()
                editing_date = details[3]
                editing_resion = entry_5.get()
                editing_bill = entry_6.get()
                editing_eid = entry_7.get()
                helper_2.update_patient(editing_id, editing_name, editing_age, editing_date, editing_resion,
                                        editing_bill, editing_eid)
                operation_ = 'edit'
                ms(editing_name, editing_id, editing_eid, editing_bill, operation_, editing_resion, editing_date)
                messagebox.showwarning('AIML', 'patient edited successfully!!')

            try:
                id_123 = int(entery123.get())
                details = helper.fetch_patient(id_123)
                patient_id_ = details[0]
                name = details[1]
                age = details[2]
                date = details[3]
                reason = details[4]
                bill = details[5]
                email_ = details[6]
                if patient_id_ == id_123:
                    frame_1_4 = tk.Frame(width=925, height=375, bg='cyan')
                    frame_1_4.place(x=0, y=70)
                    lable_1 = tk.Label(frame_1_4, text='Patient ID', bg='snow3', fg='black', width=13,
                                       font=('raleway', 15, 'bold'))
                    lable_1.place(x=250, y=5)
                    lable_2 = tk.Label(frame_1_4, text='Patient Name', bg='snow3', fg='black', width=13,
                                       font=('raleway', 15, 'bold'))
                    lable_2.place(x=250, y=55)
                    lable_3 = tk.Label(frame_1_4, text='Patient Age', bg='snow3', fg='black', width=13,
                                       font=('raleway', 15, 'bold'))
                    lable_3.place(x=250, y=105)
                    lable_4 = tk.Label(frame_1_4, text='Date', bg='snow3', fg='black', width=13,
                                       font=('raleway', 15, 'bold'))
                    lable_4.place(x=250, y=155)
                    lable_5 = tk.Label(frame_1_4, text='Reason', bg='snow3', fg='black', width=13,
                                       font=('raleway', 15, 'bold'))
                    lable_5.place(x=250, y=205)
                    label_6 = tk.Label(frame_1_4, text='Bill', bg='snow3', fg='black', width=13,
                                       font=('raleway', 15, 'bold'))
                    label_6.place(x=250, y=255)
                    lable_7 = tk.Label(frame_1_4, text='Email', bg='snow3', fg='black', width=13,
                                       font=('raleway', 15, 'bold'))
                    lable_7.place(x=250, y=305)

                    entry_1 = tk.Label(frame_1_4, text=patient_id_, font=('raleway', 15), width=20, anchor='w')
                    entry_1.place(x=500, y=5)
                    entry_2 = tk.Entry(frame_1_4, font=('raleway', 15))
                    entry_2.place(x=500, y=55)
                    entry_2.insert(0, name)
                    entry_3 = tk.Entry(frame_1_4, font=('raleway', 15))
                    entry_3.place(x=500, y=105)
                    entry_3.insert(0, age)
                    entry_4 = tk.Label(frame_1_4, text=date, font=('raleway', 15), width=20, anchor='w')
                    entry_4.place(x=500, y=155)
                    entry_5 = tk.Entry(frame_1_4, font=('raleway', 15))
                    entry_5.place(x=500, y=205)
                    entry_5.insert(0, reason)
                    entry_6 = tk.Entry(frame_1_4, font=('raleway', 15))
                    entry_6.place(x=500, y=255)
                    entry_6.insert(0, bill)
                    entry_7 = tk.Entry(frame_1_4, font=('raleway', 15))
                    entry_7.place(x=500, y=305)
                    entry_7.insert(0, email_)
                    button_2 = tk.Button(frame_1_4, text='EDIT', bg='light green', fg='black',
                                         font=('raleway', 11, 'bold'),
                                         cursor='hand2', command=editing, width=10)
                    button_2.place(x=510, y=340)

                    def canc():
                        messagebox.showwarning("AIML", "changes wont be saved")
                        edit_patient_function()

                    button_2 = tk.Button(frame_1_4, text='CANCEL', bg='light green', fg='black',
                                         font=('raleway', 11, 'bold'),
                                         cursor='hand2', command=canc, width=10)
                    button_2.place(x=310, y=340)
            except:
                messagebox.showwarning('warning', 'id did not matched')
                edit_patient_function()

        frame_1_5 = tk.Frame(width=925, height=375, bg='cyan')
        frame_1_5.place(x=0, y=70)
        lable_123 = tk.Label(frame_1_5, text='Enter ID', bg='snow3', fg='black', width=13, font=('raleway', 15, 'bold'))
        lable_123.place(x=250, y=105)
        entery123 = tk.Entry(frame_1_5, font=('raleway', 13, 'bold'), justify='center', fg='black', border=0, bg='cyan',
                             width=25)
        entery123.place(x=490, y=105)

        def on_enter(e):
            entery123.delete(0, 'end')

        def on_leave(e):
            patient_id = entery123.get()
            if patient_id == '':
                entery123.insert(0, 'Patient id')

        entery123.insert(0, "patient id")
        entery123.bind('<FocusIn>', on_enter)
        entery123.bind('<FocusOut>', on_leave)
        frame123 = tk.Frame(frame_1_5, width=250, bg='black', height=2)
        frame123.place(x=490, y=133)

        button123 = tk.Button(text='Search', bg='light green', fg='black', font=('raleway', 11, 'bold'), cursor='hand2',
                              command=main_frames, width=10)
        button123.place(x=430, y=243)

    # -------------------------------------Check patient details-------------------------------------------------
    def details_patient_function():
        frame_2_1 = tk.Frame(width=925, height=375, bg='cyan')
        frame_2_1.place(x=0, y=70)
        patient_label.destroy()
        staff_label.destroy()
        staff_button.destroy()
        patient_button.destroy()

        patient_login_label = tk.Label(frame_2_1, text='Enter the id', bg='snow3', fg='black',
                                       font=('raleway', 15, 'bold'))
        patient_login_label.place(x=297, y=155)

        # #################------------------------------------------------------------
        patient_login_entry = tk.Entry(frame_2_1, width=30, bg='cyan', justify='center', fg='black', border=0,
                                       font=('raleway', 11, 'bold'))
        patient_login_entry.place(x=480, y=160)

        def on_enter(e):
            patient_login_entry.delete(0, 'end')

        def on_leave(e):
            patient_id = patient_login_entry.get()
            if patient_id == '':
                patient_login_entry.insert(0, 'patient id')

        patient_login_entry.insert(0, 'patient id')
        patient_login_entry.bind('<FocusIn>', on_enter)
        patient_login_entry.bind('<FocusOut>', on_leave)
        patient_login_entry_frame = tk.Frame(frame_2_1, width=250, bg='black', height=2)
        patient_login_entry_frame.place(x=480, y=185)

        # -----------------------------------Patient search--------------------------------------------------------
        def patient_search():
            # name should receive from database
            frame_2_2 = tk.Frame(width=925, height=375, bg='cyan')
            frame_2_2.place(x=0, y=70)
            name = int(patient_login_entry.get())
            try:
                details = helper.fetch_patient(name)
                patient_id_ = details[0]
                if patient_id_ == name:
                    patient_login_entry.destroy()
                    patient_login_entry_frame.destroy()
                    patient_login_label.destroy()
                    patient_login_button1.destroy()
                    lable_1 = tk.Label(frame_2_2, text=details[1], font=('raleway', 17, 'bold'), width=15)
                    lable_1.place(x=525, y=90)
                    lable_1_ = tk.Label(frame_2_2, text='Name', font=('raleway', 17, 'bold'), width=15)
                    lable_1_.place(x=200, y=90)
                    lable_2 = tk.Label(frame_2_2, text=details[3], font=('raleway', 17, 'bold'), width=15)
                    lable_2.place(x=525, y=190)
                    lable_2_ = tk.Label(frame_2_2, text='Admission Date', font=('raleway', 17, 'bold'), width=15)
                    lable_2_.place(x=200, y=190)
                    lable_2 = tk.Label(frame_2_2, text=details[5], font=('raleway', 17, 'bold'), width=15)
                    lable_2.place(x=525, y=290)
                    lable_2_ = tk.Label(frame_2_2, text='Bill', font=('raleway', 17, 'bold'), width=15)
                    lable_2_.place(x=200, y=290)
            except:
                messagebox.showwarning('warning', 'id did not matched')
                main()

        patient_login_button1 = tk.Button(frame_2_1, text='Search', bg='light green', fg='black',
                                          font=('raleway', 13, 'bold'),
                                          command=patient_search, cursor='hand2')
        patient_login_button1.place(x=430, y=265)

    # --------------------------------------delete patient----------------------------------------------------------
    def delete_patient_function():
        frame.destroy()
        frame_1_4 = tk.Frame(width=925, height=375, bg='cyan')
        frame_1_4.place(x=0, y=70)

        def function_121():
            id = entery121.get()
            x = messagebox.askyesno('AIML', 'Do you want to delete permanently?')
            if x == 1:
                helper.delete_patient(id)
                messagebox.showwarning('AIML', f'id {id} deleted successfully!!')

        lable121 = tk.Label(frame_1_4, text='Enter patient id', font=('raleway', 15, 'bold'), width=18)
        lable121.place(x=240, y=180)

        entery121 = tk.Entry(frame_1_4, font=('raleway', 13, 'bold'), justify='center', fg='black', border=0, bg='cyan',
                             width=25)
        entery121.place(x=490, y=180)

        def on_enter(e):
            entery121.delete(0, 'end')

        def on_leave(e):
            patient_id = entery121.get()
            if patient_id == '':
                entery121.insert(0, 'patient id')

        entery121.insert(0, "patient id")
        entery121.bind('<FocusIn>', on_enter)
        entery121.bind('<FocusOut>', on_leave)
        frame121 = tk.Frame(frame_1_4, width=250, bg='black', height=2)
        frame121.place(x=490, y=210)

        button121 = tk.Button(frame_1_4, text='Delete', font=('raleway', 11, 'bold'), cursor='hand2',
                              command=function_121)
        button121.place(x=430, y=280)

    # patient login
    def patient():
        frame_2_1 = tk.Frame(width=925, height=375, bg='cyan')
        frame_2_1.place(x=0, y=75)
        patient_label.destroy()
        staff_label.destroy()
        staff_button.destroy()
        patient_button.destroy()

        patient_login_label = tk.Label(frame_2_1, text='Enter the id', bg='snow3', fg='black',
                                       font=('raleway', 15, 'bold'))
        patient_login_label.place(x=297, y=155)

        # #################------------------------------------------------------------
        patient_login_entry = tk.Entry(frame_2_1, width=30, bg='cyan', justify='center', fg='black', border=0,
                                       font=('raleway', 11, 'bold'))
        patient_login_entry.place(x=480, y=160)

        def on_enter(e):
            patient_login_entry.delete(0, 'end')

        def on_leave(e):
            patient_id = patient_login_entry.get()
            if patient_id == '':
                patient_login_entry.insert(0, 'patient id')

        patient_login_entry.insert(0, 'patient id')
        patient_login_entry.bind('<FocusIn>', on_enter)
        patient_login_entry.bind('<FocusOut>', on_leave)
        patient_login_entry_frame = tk.Frame(frame_2_1, width=250, bg='black', height=2)
        patient_login_entry_frame.place(x=480, y=185)

        # -----------------------------------Patient search--------------------------------------------------------
        def patient_search():
            # name should receive from database
            frame_2_2 = tk.Frame(width=925, height=375, bg='cyan')
            frame_2_2.place(x=0, y=70)
            name = int(patient_login_entry.get())
            try:
                details = helper.fetch_patient(name)
                patient_id_ = details[0]
                if patient_id_ == name:
                    patient_login_entry.destroy()
                    patient_login_entry_frame.destroy()
                    patient_login_label.destroy()
                    patient_login_button1.destroy()
                    lable_1 = tk.Label(frame_2_2, text=details[1], font=('raleway', 17, 'bold'), width=15)
                    lable_1.place(x=525, y=90)
                    lable_1_ = tk.Label(frame_2_2, text='Name', font=('raleway', 17, 'bold'), width=15)
                    lable_1_.place(x=200, y=90)
                    lable_2 = tk.Label(frame_2_2, text=details[3], font=('raleway', 17, 'bold'), width=15)
                    lable_2.place(x=525, y=190)
                    lable_2_ = tk.Label(frame_2_2, text='Admission Date', font=('raleway', 17, 'bold'), width=15)
                    lable_2_.place(x=200, y=190)
                    lable_2 = tk.Label(frame_2_2, text=details[5], font=('raleway', 17, 'bold'), width=15)
                    lable_2.place(x=525, y=290)
                    lable_2_ = tk.Label(frame_2_2, text='Bill', font=('raleway', 17, 'bold'), width=15)
                    lable_2_.place(x=200, y=290)
            except:
                messagebox.showwarning('warning', 'id did not matched')
                main()

        patient_login_button1 = tk.Button(frame_2_1, text='Search', bg='light green', fg='black',
                                          font=('raleway', 13, 'bold'),
                                          command=patient_search, cursor='hand2')
        patient_login_button1.place(x=430, y=265)

    patient_label = tk.Label(frame, text='Patient', bg='snow3', fg='black', height=1, width=9,
                             font=('Arial', 17, "bold"))
    patient_label.place(x=295, y=155)
    patient_button = tk.Button(frame, text='Next', bg='white', fg='red', command=patient, width=15,
                               cursor='hand2', font=('raleway', 11, "bold"))
    patient_button.place(x=505, y=155)

    # staff login
    def staff():

        patient_label.destroy()
        staff_label.destroy()
        staff_button.destroy()
        patient_button.destroy()

        def hello():
            user_id = id_.get()
            password = password_.get()
            if ((user_id == id_1) and (password == password_1)) or ((user_id == id_2) and (password == password_2)) or (
                    (user_id == id_3) and (password == password_3)) or (
                    (user_id == id_4) and (password == password_4)) or (
                    (user_id == id_5) and (password == password_5)):
                # main()
                login_label_frame.destroy()
                password_label_frame.destroy()
                login_label.destroy()
                password_label.destroy()
                password_.destroy()
                id_.destroy()
                staff_button2.destroy()

                add_patient_button = tk.Button(frame, text='Add New Patient', cursor='hand2',
                                               font=('raleway', 12, 'bold'), width=25, command=new_patient_function)
                add_patient_button.place(x=347, y=100)

                edit_patient_button = tk.Button(frame, text='Edit Existing Patient', cursor='hand2',
                                                font=('raleway', 12, 'bold'),
                                                width=25, command=edit_patient_function)
                edit_patient_button.place(x=347, y=150)

                delete_patient_button = tk.Button(frame, text='Delete a Patient', cursor='hand2',
                                                  font=('raleway', 12, 'bold'),
                                                  width=25, command=delete_patient_function)
                delete_patient_button.place(x=347, y=200)

                details_patient_button = tk.Button(frame, text='Check Details of a Patient', cursor='hand2',
                                                   font=('raleway', 12, 'bold'), width=25,
                                                   command=details_patient_function)
                details_patient_button.place(x=347, y=250)
            else:
                messagebox.showwarning('warning', 'check your id and password')

        # -----------------------------------------------------------------------------------------
        login_label = tk.Label(frame, text='User Id', bg='snow3', width=12, fg='black', font=('raleway', 12, 'bold'))
        login_label.place(x=297, y=155)
        id_ = tk.Entry(frame, width=30, bg='cyan', justify='center', fg='black', border=0, font=('raleway', 11, 'bold'))
        id_.place(x=465, y=155)
        login_label_frame = tk.Frame(frame, width=250, bg='black', height=2)
        login_label_frame.place(x=465, y=180)

        def on_id_enter(e):
            temp = id_.get()
            if temp == 'id':
                id_.delete(0, 'end')

        def on_id_leave(e):
            temp = id_.get()
            if temp == '':
                id_.insert(0, 'id')

        id_.insert(0, 'id')
        id_.bind('<FocusIn>', on_id_enter)
        id_.bind('<FocusOut>', on_id_leave)

        # ######################--------------------------------------------------------------------------------------------------
        password_label = tk.Label(frame, text='Password', bg='snow3', width=12, fg='black',
                                  font=('raleway', 12, 'bold'))
        password_label.place(x=297, y=230)
        password_ = tk.Entry(frame, width=30, bg='cyan', justify='center', fg='black', border=0,
                             font=('raleway', 11, 'bold'), show='*,bold')
        password_.place(x=465, y=230)
        password_.insert(0, 'Password')
        password_label_frame = tk.Frame(frame, width=250, bg='black', height=2)
        password_label_frame.place(x=465, y=255)

        def on_password_enter(e):
            temp = password_.get()
            if temp == 'Password':
                password_.delete(0, 'end')

        def on_password_leave(e):
            temp = password_.get()
            if temp == '':
                password_.insert(0, 'Password')

        password_.bind('<FocusIn>', on_password_enter)
        password_.bind('<FocusOut>', on_password_leave)

        # ##################------------------------------------------------------------------------------------------------------
        staff_button2 = tk.Button(frame, text='Login ', bg='light green', fg='black', cursor='hand2',
                                  font=('raleway', 12, "bold"),
                                  command=hello)
        staff_button2.place(x=440, y=310)

    staff_label = tk.Label(frame, text='Staff', bg='snow3', fg='black', height=1, width=9, font=('raleway', 17, 'bold'))
    staff_label.place(x=295, y=250)
    staff_button = tk.Button(text='Next', bg='white', cursor='hand2', fg='red', command=lambda: staff(), width=15,
                             font=('raleway', 11, 'bold'))
    staff_button.place(x=505, y=250)

    # quit
    def quit_():
        k = messagebox.askyesno('AIML', 'Do you want to Exit?')
        if k == 1:
            root.destroy()
        else:
            messagebox.showwarning('AIML', 'Then why did you press Quit')

    quit_ = tk.Button(root, text='Quit', bg='red2', fg='white', command=quit_, cursor='hand2',
                      font=('raleway', 15, 'bold'))
    quit_.place(x=480, y=450)

    Home_button()
    time_function()


main()
root.mainloop()
