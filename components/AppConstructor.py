import tkinter as tk
from tkinter import *
from ModbusExtract import ModbusMaster
from time import strftime

class AppConstructor(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("800x480")
        self.configure(bg='#262626')
        self.frame_menu = tk.Frame(self, bg='white', height=30, width=800)
        self.tab1 = tk.Button(self.frame_menu, text=f"{1}", anchor=N, height=2, width=21, bg='#4BB2AE',
                              fg='#032222',
                              activebackground='#4BB2AE', relief=SUNKEN)
        self.tab2 = tk.Button(self.frame_menu, text="2", anchor=N, height=2, width=21, bg='#8EF6F2',
                              fg='#032222',
                              activebackground='#4BB2AE', relief=RAISED)
        self.tab3 = tk.Button(self.frame_menu, text="3", anchor=N, height=2, width=21, bg='#8EF6F2',
                              fg='#032222',
                              activebackground='#4BB2AE', relief=RAISED)

        self.tab4 = tk.Button(self.frame_menu, text="4", anchor=N, height=2, width=21, bg='#8EF6F2',
                              fg='#032222',
                              activebackground='#4BB2AE', relief=RAISED)
        self.tab5 = tk.Button(self.frame_menu, text="5", anchor=N, height=2, width=21, bg='#8EF6F2',
                              fg='#032222',
                              activebackground='#4BB2AE', relief=RAISED)
        self.tab1.bind(sequence="<Button-1>", func=lambda event: chooseTab(self.tab1))
        self.tab2.bind(sequence="<Button-1>", func=lambda event: chooseTab(self.tab2))
        self.tab3.bind(sequence="<Button-1>", func=lambda event: chooseTab(self.tab3))
        self.tab4.bind(sequence="<Button-1>", func=lambda event: chooseTab(self.tab4))
        self.tab5.bind(sequence="<Button-1>", func=lambda event: chooseTab(self.tab5))

        def chooseTab(tab):
            self.tab1.configure(relief=RAISED, bg='#8EF6F2')
            self.tab2.configure(relief=RAISED, bg='#8EF6F2')
            self.tab3.configure(relief=RAISED, bg='#8EF6F2')
            self.tab4.configure(relief=RAISED, bg='#8EF6F2')
            self.tab5.configure(relief=RAISED, bg='#8EF6F2')
            tab.configure(relief=SUNKEN, bg='#4BB2AE')
            self.current_tab = tab.cget('text')

        self.frame_stand = tk.Frame(self, width=800, height=450, bg='white')
        self.diagram = tk.Frame(master=self.frame_stand, width=300, height=295, bg="#FFCF73")
        self.frame_set_panel = tk.Frame(master=self.frame_stand, width=470, height=295, bg='#032222')
        self.frame_time = tk.Frame(master=self.frame_stand, width=300, height=125, bg='#7FADFC')
        self.frame_info = tk.Frame(master=self.frame_stand, width=355, height=125, bg='#7FADFC')
        self.frame_buttons = tk.Frame(master=self.frame_stand, width=105, height=125, bg='#7FADFC')
        self.frame_buttons.place(anchor="nw", x=685, y=315)
        self.frame_info.place(anchor="nw", x=320, y=315)
        self.button_debug = tk.Button(self.frame_buttons, text="Отладка", anchor=CENTER, height=2, width=10,
                                      bg='#8EF6F2',
                                      fg='#032222',
                                      activebackground='#4BB2AE', relief=RAISED, command=self.replace)
        self.button_debug.place(x=0, y=0)
        self.button_change_solution = tk.Button(self.frame_buttons, text="Смена\nраствора", anchor=CENTER, height=2,
                                                width=10, bg='#8EF6F2',
                                                fg='#032222',
                                                activebackground='#4BB2AE', relief=RAISED)
        self.button_change_solution.place(x=0, y=42)
        self.button_power_off = tk.Button(self.frame_buttons, text="Выключить", anchor=CENTER, height=2, width=10,
                                          bg='#8EF6F2',
                                          fg='#032222',
                                          activebackground='#4BB2AE', relief=RAISED)

        self.frame_temp_set_element = tk.Frame(master=self.frame_set_panel, width=235, height=59, bg='#7FADFC')
        self.frame_temp_set_element.place(x=0, y=0)
        self.label_temp_set_element = tk.Label(self.frame_temp_set_element, text="T°C=", height=4, width=10, anchor="e")
        self.label_temp_set_element.place(x=0, y=0)
        self.label_temp_value = tk.Label(self.frame_temp_set_element, text="0", height=4, width=8)
        self.label_temp_value.place(x=80, y=0)
        self.button_temp_plus = tk.Button(self.frame_temp_set_element, text="∧", font=("bold", 9), anchor=CENTER,
                                          height=1, width=3,
                                          bg='#8EF6F2',
                                          fg='#032222',
                                          activebackground='#4BB2AE', relief=RAISED)
        self.button_temp_plus.bind(sequence="<Button-1>", func=lambda event: self.increase(self.label_temp_value,1))
        self.button_temp_plus.place(x=150, y=2)
        self.button_temp_minus = tk.Button(self.frame_temp_set_element, text="∨", font=("bold", 9), anchor=CENTER,
                                           height=1, width=3,
                                           bg='#8EF6F2',
                                           fg='#032222',
                                           activebackground='#4BB2AE', relief=RAISED)
        self.button_temp_minus.bind(sequence="<Button-1>", func=lambda event: self.decrease(self.label_temp_value,1))
        self.button_temp_minus.place(x=150, y=30)

        self.frame_time_work = tk.Frame(master=self.frame_set_panel, width=235, height=59, bg='#7FADFC')
        self.frame_time_work.place(x=0, y=60)
        self.label_time_work = tk.Label(self.frame_time_work, text="tч=", height=4, width=10, anchor="e")
        self.label_time_work.place(x=0, y=0)
        self.label_time_value = tk.Label(self.frame_time_work, text="0", height=4, width=8)
        self.label_time_value.place(x=80, y=0)
        self.button_time_plus = tk.Button(self.frame_time_work, text="∧", font=("bold", 9), anchor=CENTER,
                                          height=1, width=3,
                                          bg='#8EF6F2',
                                          fg='#032222',
                                          activebackground='#4BB2AE', relief=RAISED)
        self.button_time_plus.bind(sequence="<Button-1>", func=lambda event: self.increase(self.label_time_value,0))
        self.button_time_plus.place(x=150, y=2)
        self.button_time_minus = tk.Button(self.frame_time_work, text="∨", font=("bold", 9), anchor=CENTER,
                                           height=1, width=3,
                                           bg='#8EF6F2',
                                           fg='#032222',
                                           activebackground='#4BB2AE', relief=RAISED)
        self.button_time_minus.bind(sequence="<Button-1>", func=lambda event: self.decrease(self.label_time_value,0))
        self.button_time_minus.place(x=150, y=30)

        self.frame_period_uv = tk.Frame(master=self.frame_set_panel, width=235, height=59, bg='#7FADFC')
        self.frame_period_uv.place(x=0, y=120)
        self.label_period_uv = tk.Label(self.frame_period_uv, text="Euv=", height=4, width=10, anchor="e")
        self.label_period_uv.place(x=0, y=0)
        self.label_uv_value = tk.Label(self.frame_period_uv, text="0", height=4, width=8)
        self.label_uv_value.place(x=80, y=0)
        self.button_uv_plus = tk.Button(self.frame_period_uv, text="∧", font=("bold", 9), anchor=CENTER,
                                        height=1, width=3,
                                        bg='#8EF6F2',
                                        fg='#032222',
                                        activebackground='#4BB2AE', relief=RAISED)
        self.button_uv_plus.bind(sequence="<Button-1>", func=lambda event: self.increase(self.label_uv_value,0))
        self.button_uv_plus.place(x=150, y=2)
        self.button_uv_minus = tk.Button(self.frame_period_uv, text="∨", font=("bold", 9), anchor=CENTER,
                                         height=1, width=3,
                                         bg='#8EF6F2',
                                         fg='#032222',
                                         activebackground='#4BB2AE', relief=RAISED)
        self.button_uv_minus.bind(sequence="<Button-1>", func=lambda event: self.decrease(self.label_uv_value, 0))
        self.button_uv_minus.place(x=150, y=30)

        self.frame_period_read = tk.Frame(master=self.frame_set_panel, width=235, height=59, bg='#7FADFC')
        self.frame_period_read.place(x=0, y=180)
        self.label_period_read = tk.Label(self.frame_period_read, text="Tсчит=", height=4, width=10, anchor="e")
        self.label_period_read.place(x=0, y=0)
        self.label_read_value = tk.Label(self.frame_period_read, text="0", height=4, width=8)
        self.label_read_value.place(x=80, y=0)
        self.button_read_plus = tk.Button(self.frame_period_read, text="∧", font=("bold", 9), anchor=CENTER,
                                          height=1, width=3,
                                          bg='#8EF6F2',
                                          fg='#032222',
                                          activebackground='#4BB2AE', relief=RAISED)
        self.button_read_plus.bind(sequence="<Button-1>", func=lambda event: self.increase(self.label_read_value,0))
        self.button_read_plus.place(x=150, y=2)
        self.button_read_minus = tk.Button(self.frame_period_read, text="∨", font=("bold", 9), anchor=CENTER,
                                           height=1, width=3,
                                           bg='#8EF6F2',
                                           fg='#032222',
                                           activebackground='#4BB2AE', relief=RAISED)
        self.button_read_minus.bind(sequence="<Button-1>", func=lambda event: self.decrease(self.label_read_value, 0))
        self.button_read_minus.place(x=150, y=30)

        self.button_ok = tk.Button(self.frame_set_panel, text="ok", font=("bold", 12), anchor=CENTER,
                                   height=1, width=6,
                                   bg='#8EF6F2',
                                   fg='#032222',
                                   activebackground='#4BB2AE', relief=RAISED)
        self.button_ok.place(x=90, y=250)

        #
        self.frame_set_ph = tk.Frame(master=self.frame_set_panel, width=235, height=59, bg='#7FADFC')
        self.frame_set_ph.place(x=235, y=0)
        self.label_set_ph = tk.Label(self.frame_set_ph, text="Ph=", height=4, width=10, anchor="e")
        self.label_set_ph.place(x=0, y=0)
        self.label_ph_value = tk.Label(self.frame_set_ph, text="0", height=4, width=8)
        self.label_ph_value.place(x=80, y=0)
        self.button_ph_plus = tk.Button(self.frame_set_ph, text="∧", font=("bold", 9), anchor=CENTER,
                                        height=1, width=3,
                                        bg='#8EF6F2',
                                        fg='#032222',
                                        activebackground='#4BB2AE', relief=RAISED)
        self.button_ph_plus.bind(sequence="<Button-1>", func=lambda event: self.increase(self.label_ph_value, 1))
        self.button_ph_plus.place(x=150, y=2)
        self.button_ph_minus = tk.Button(self.frame_set_ph, text="∨", font=("bold", 9), anchor=CENTER,
                                         height=1, width=3,
                                         bg='#8EF6F2',
                                         fg='#032222',
                                         activebackground='#4BB2AE', relief=RAISED)
        self.button_ph_minus.bind(sequence="<Button-1>", func=lambda event: self.decrease(self.label_ph_value, 1))
        self.button_ph_minus.place(x=150, y=30)

        self.frame_set_oxygen = tk.Frame(master=self.frame_set_panel, width=235, height=59, bg='#7FADFC')
        self.frame_set_oxygen.place(x=235, y=60)
        self.label_set_oxygen = tk.Label(self.frame_set_oxygen, text="O2=", height=4, width=10, anchor="e")
        self.label_set_oxygen.place(x=0, y=0)
        self.label_oxygen_value = tk.Label(self.frame_set_oxygen, text="0", height=4, width=8)
        self.label_oxygen_value.place(x=80, y=0)
        self.button_oxygen_plus = tk.Button(self.frame_set_oxygen, text="∧", font=("bold", 9), anchor=CENTER,
                                            height=1, width=3,
                                            bg='#8EF6F2',
                                            fg='#032222',
                                            activebackground='#4BB2AE', relief=RAISED)
        self.button_oxygen_plus.bind(sequence="<Button-1>",
                                      func=lambda event: self.increase(self.label_oxygen_value, 1))
        self.button_oxygen_plus.place(x=150, y=2)
        self.button_oxygen_minus = tk.Button(self.frame_set_oxygen, text="∨", font=("bold", 9), anchor=CENTER,
                                             height=1, width=3,
                                             bg='#8EF6F2',
                                             fg='#032222',
                                             activebackground='#4BB2AE', relief=RAISED)
        self.button_oxygen_minus.bind(sequence="<Button-1>", func=lambda event: self.decrease(self.label_oxygen_value, 1))
        self.button_oxygen_minus.place(x=150, y=30)

        self.frame_set_procent = tk.Frame(master=self.frame_set_panel, width=235, height=59, bg='#7FADFC')
        self.frame_set_procent.place(x=235, y=120)
        self.label_set_procent = tk.Label(self.frame_set_procent, text="%=", height=4, width=10, anchor="e")
        self.label_set_procent.place(x=0, y=0)
        self.label_procent_value = tk.Label(self.frame_set_procent, text="0", height=4, width=8)
        self.label_procent_value.place(x=80, y=0)
        self.button_procent_plus = tk.Button(self.frame_set_procent, text="∧", font=("bold", 9), anchor=CENTER,
                                             height=1, width=3,
                                             bg='#8EF6F2',
                                             fg='#032222',
                                             activebackground='#4BB2AE', relief=RAISED)
        self.button_procent_plus.bind(sequence="<Button-1>",
                                       func=lambda event: self.increase(self.label_procent_value, 0))
        self.button_procent_plus.place(x=150, y=2)
        self.button_procent_minus = tk.Button(self.frame_set_procent, text="∨", font=("bold", 9), anchor=CENTER,
                                              height=1, width=3,
                                              bg='#8EF6F2',
                                              fg='#032222',
                                              activebackground='#4BB2AE', relief=RAISED)
        self.button_procent_minus.bind(sequence="<Button-1>", func=lambda event: self.decrease(self.label_procent_value, 0))
        self.button_procent_minus.place(x=150, y=30)
        self.button_reset = tk.Button(self.frame_set_panel, text="сброс", font=("bold", 12), anchor=CENTER,
                                      height=1, width=6,
                                      bg='#8EF6F2',
                                      fg='#032222',
                                      activebackground='#4BB2AE', relief=RAISED)
        self.button_reset.place(x=320, y=250)

        self.label_lead_time = tk.Label(self.frame_time, text="Время выполнения: ", height=2, width=45, anchor="nw")
        self.label_lead_time.place(x=0, y=3)
        self.label_left_time = tk.Label(self.frame_time, text="Оставшееся время: ", height=2, width=45, anchor="nw")
        self.label_left_time.place(x=0, y=43)
        self.label_current_time = tk.Label(self.frame_time, text="Текущее время: ", height=2, width=45, anchor="nw")
        self.label_current_time.place(x=0, y=83)
        self.lbl = tk.Label(self.label_current_time, font=('calibri', 15, 'bold'),
                            background='#7FADFC',
                            foreground='black')

        # Размещение Label в окне
        self.lbl.place(x=150,y=0)

        self.frame_temperatures = tk.Frame(master=self.frame_info, width=355, height=85, bg='gray')
        self.frame_temperatures.place(x=0, y=0)
        self.label_temp1 = tk.Label(self.frame_temperatures, text="t1=", height=1, width=22, anchor="nw")
        self.label_temp1.place(x=0, y=5)
        self.label_temp2 = tk.Label(self.frame_temperatures, text="t2=", height=1, width=22, anchor="nw")
        self.label_temp2.place(x=0, y=30)

        self.label_temp3 = tk.Label(self.frame_temperatures, text="t3=", height=1, width=22, anchor="nw")
        self.label_temp3.place(x=0, y=55)
        self.label_temp4 = tk.Label(self.frame_temperatures, text="t4=", height=1, width=22, anchor="nw")
        self.label_temp4.place(x=185, y=5)
        self.label_uv = tk.Label(self.frame_temperatures, text="Tuv=", height=1, width=22, anchor="nw")
        self.label_uv.place(x=185, y=30)

        self.frame_state = tk.Frame(master=self.frame_info, width=355, height=85, bg='green')
        self.frame_state.place(x=0, y=80)
        self.label_system_state = tk.Label(self.frame_state, text="Строка состояния", height=2, width=44, anchor="nw")
        self.label_system_state.place(x=0, y=5)

        self.frame_debug = tk.Frame(self, width=800, height=480, bg='white')
        # self.frame_debug.place(x=0,y=0)
        self.frame_engine1 = tk.Frame(master=self.frame_debug, width=500, height=60, bg='#032222')
        self.label_engine1 = tk.Label(
            master=self.frame_engine1,
            text="Регулировка первого мотора",
            height=1,
            bg='#032222',
            fg='#36ede8',
            activebackground='#0f9d9a'
        )
        self.button_decrease_eng1 = tk.Button(master=self.frame_engine1, text="-", height=1, width=1, bg='#032222',
                                              fg='#36ede8',
                                              activebackground='#0f9d9a')
        self.label_value_eng1 = tk.Label(master=self.frame_engine1, text="0", width=3, height=1, bg='#F2DDBB')

        self.button_increase_eng1 = tk.Button(master=self.frame_engine1, text="+", width=1, bg='#032222',
                                              fg='#36ede8',
                                              activebackground='#0f9d9a')
        self.frame_engine1.place(x=337, y=10)
        self.label_engine1.place(x=110, y=2)
        # регулятор

        self.button_decrease_eng1.place(x=120, y=25)
        self.label_value_eng1.place(x=195, y=30)
        self.button_increase_eng1.place(x=265, y=25)
        self.frame_engine2 = tk.Frame(master=self.frame_debug, width=500, height=60, bg='#032222')
        self.label_engine2 = tk.Label(
            master=self.frame_engine2,
            text="Регулировка второго мотора",
            height=1,
            bg='#032222',
            fg='#36ede8',
            activebackground='#0f9d9a'
        )
        self.button_decrease_eng2 = tk.Button(master=self.frame_engine2, text="-", height=1, width=1, bg='#032222',
                                              fg='#36ede8',
                                              activebackground='#0f9d9a')
        self.label_value_eng2 = tk.Label(master=self.frame_engine2, text="0", width=3, height=1, bg='#F2DDBB')

        self.button_increase_eng2 = tk.Button(master=self.frame_engine2, text="+", width=1, bg='#032222',
                                              fg='#36ede8',
                                              activebackground='#0f9d9a')
        self.frame_engine2.place(x=337, y=80)
        self.label_engine2.place(x=110, y=2)
        self.button_decrease_eng2.place(x=120, y=25)
        self.label_value_eng2.place(x=195, y=30)
        self.button_increase_eng2.place(x=265, y=25)
        self.button_debug_ok = tk.Button(master=self.frame_debug, text="ok", width=1, bg='black',
                                         fg='#36ede8',
                                         activebackground='#0f9d9a', command=self.ok_replace)
        self.button_debug_ok.place(x=380, y=440)

        self.button_power_off.place(x=0, y=84)

        self.frame_time.place(anchor="nw", x=10, y=315)
        self.frame_set_panel.place(anchor="nw", x=320, y=10)
        self.diagram.place(anchor="nw", x=10, y=10)
        self.frame_stand.place(x=0, y=32)
        self.frame_menu.place(x=0, y=0)
        self.tab1.place(x=0, y=0)
        self.tab2.place(x=160, y=0)
        self.tab3.place(x=320, y=0)
        self.tab4.place(x=480, y=0)
        self.tab5.place(x=640, y=0)
        # self.update_temp_label()
        self.time()

    def increase(self, lbl_value, value):
        if value == 0:
            lbl_value['text'] = int(lbl_value['text']) + 1
        else:
            lbl_value['text'] = round(float(lbl_value['text']) + 0.1, 2)

    def decrease(self, lbl_value,value):
        if value == 0:
            lbl_value['text'] = int(lbl_value['text']) - 1
        else:
            lbl_value['text'] = round(float(lbl_value['text']) - 0.1, 2)

    def replace(self):
        self.frame_stand.place_forget()
        self.frame_menu.place_forget()
        self.frame_debug.place(x=0, y=0)

    def ok_replace(self):
        self.frame_debug.place_forget()  # Скрываем frame_debug
        self.frame_menu.place(x=0, y=0)  # Возвращаем frame_menu на экран
        self.frame_stand.place(x=0, y=32)  # Возвращаем frame_stand на экран

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl.config(text=string)
        self.lbl.after(1000, self.time)

    # def update_temp_label(self):
    #
    #     # Fetch new data
    #
    #     self.ditc = ModbusMaster().read_data(1,0,6)
    #
    #     # Assuming the temperature value is at a specific index, e.g., 0
    #
    #
    #     # Update label_temp1 with the new value
    #     self.label_temp1.configure(text=f"t1= {round(self.ditc[0] / 100, 2)}")
    #     self.label_temp2.configure(text=f"t2= {round(self.ditc[1] / 100, 2)}")
    #     self.label_temp3.configure(text=f"t3= {round(self.ditc[2] / 100, 2)}")
    #     self.label_temp4.configure(text=f"t4= {round(self.ditc[3] / 100, 2)}")
    #
    #     # Call update_temp_label again after a delay (e.g., 1000ms)
    #     self.after(1000, self.update_temp_label)


if __name__ == "__main__":
    app = AppConstructor()
    app.mainloop()
