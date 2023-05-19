import tkinter as tk
from tkinter import ttk
import numpy
import matplotlib.pyplot as plt

root = tk.Tk()
notebook = ttk.Notebook(root)
root.title("Obliczenia")
root.geometry("500x500")

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1,text="Trygonometria")
notebook.add(tab2,text="Kwadratowa")
notebook.grid(column=0,row=0)

cos_var = tk.IntVar()
sin_var = tk.IntVar()
tan_var = tk.IntVar()
ctan_var = tk.IntVar()


def check_function():
        get_img = nazwa_pliku.get()
        
        zakres_x_od = x_od.get()
        zakres_x_do = x_do.get()
        zakres_y_od = y_od.get()
        zakres_y_do = y_do.get()
        nazwa_os_y = os_y.get()
        nazwa_os_x = os_x.get()

        new_file_name = str(get_img) + ".png"

        tryg_func = []
        cos_result = cos_var.get()
        sin_result = sin_var.get()
        tan_result = tan_var.get()
        ctan_result = ctan_var.get()
        results = [cos_result,sin_result,tan_result,ctan_result]
        x = numpy.linspace(float(zakres_x_od),float(zakres_x_do),200)

        if results[0] == 1:
            tryg_func.append(
                {
                    "name":"cos(x)",
                    "value":numpy.cos(x)
                })
        if results[1] == 1:
            tryg_func.append(
                {
                    "name":"sin(x)",
                    "value":numpy.sin(x)
                })
        if results[2] == 1:
            tryg_func.append(
                {
                    "name":"tan(x)",
                    "value":numpy.tan(x)
                })
        if results[3] == 1:
            tryg_func.append(
                {
                    "name":"ctan(x)",
                    "value":numpy.cos(x)/numpy.sin(x)
                })

        
        for func in tryg_func:
            plt.plot(x,func['value'],label=func['name'])

        plt.legend()
        plt.xlabel(nazwa_os_x)
        plt.ylabel(nazwa_os_y)
        plt.grid()
        plt.xlim(float(zakres_x_od),float(zakres_x_do))
        plt.ylim(float(zakres_y_od),float(zakres_y_do))
        plt.savefig(new_file_name)

def Trygonometria(root):

    global nazwa_pliku,y_od,y_do,x_od,x_do,os_x,os_y
    
    tk.Label(root,text="Wybierz funkcje",font="arial").grid(column=1,row=0)
    check_cos = tk.Checkbutton(root,text = "cos(x)",variable=cos_var)
    check_cos.grid(column=1,row=1)
    check_sin = tk.Checkbutton(root,text = "sin(x)",variable=sin_var)
    check_sin.grid(column=1,row=2)
    check_tan = tk.Checkbutton(root,text = "tan(x)",variable=tan_var)
    check_tan.grid(column=1,row=3)
    check_ctan = tk.Checkbutton(root,text = "ctan(x)",variable=ctan_var)
    check_ctan.grid(column=1,row=4)

    tk.Label(root,text="Dane",font="arial").grid(column=1,row=5)
    tk.Label(root,text="Oś X").grid(column=1,row=6)
    os_x = tk.Entry(root,width=10)
    os_x.grid(column=2,row=6)
    tk.Label(root,text="Oś Y").grid(column=1,row=7)
    os_y = tk.Entry(root,width=10)
    os_y.grid(column=2,row=7)

    

    tk.Label(root,text="oś X od ").grid(column=1,row=8)
    x_od = tk.Entry(root,width=10)
    x_od.grid(column=2,row=8)
    tk.Label(root,text="oś X do ").grid(column=3,row=8)
    x_do = tk.Entry(root,width=10)
    x_do.grid(column=4,row=8)

    tk.Label(root,text="oś Y od ").grid(column=1,row=9)
    y_od = tk.Entry(root,width=10)
    y_od.grid(column=2,row=9)
    tk.Label(root,text="oś Y do ").grid(column=3,row=9)
    y_do = tk.Entry(root,width=10)
    y_do.grid(column=4,row=9)

    tk.Label(root,text="").grid(column=1,row=14)

    tk.Label(root,text="").grid(column=1,row=10)

    tk.Label(root,text="Podaj nazwe pliku").grid(column=1,row=11)
    nazwa_pliku = tk.Entry(root,width=20,font="arial")
    nazwa_pliku.grid(column=2,row=11)
    img = tk.Label(root,image="").grid(column=2,row=20)

    btn = tk.Button(root,command=check_function,text="wyslij").grid(column=2,row=15)



Trygonometria(tab1)


root.mainloop()