import os
import shutil
import easygui
import tkinter
from tkinter import simpledialog
import datetime


# lista a kiterjesztesekrol
ext_added = ["jpg", "png", "pdf", "torrent"]


def moving_to(file, ext, src):
    linux = False
    if src[0] == '/':
        linux = True

    if linux:
        shutil.move(src+'/'+file, src+'/'+ext+'/'+file)
    else:
        shutil.move(src+'\\'+file, src+'\\'+ext+'\\'+file)




# ez csinalja a szortirozast
def szortirozas_metodus1():
    global source_path
    print("szortirozas_metodus1")
    os.chdir(source_path)
    cwd = os.getcwd()

    if ext_added:
        for dic_ext in ext_added:
            try:
                os.mkdir(dic_ext)
            except:
                continue

    linux = False
    if source_path[0] == '/':
        linux = True

    if linux:
        try:
            f = open(cwd+"/szortir_log.txt", "a")
        except:
            print("Letezik a fajl")
    else:
        try:
            f = open(cwd+"\\szortir_log.txt", "a")
        except:
            print("Letezik a fajl")

    date_append = str(datetime.datetime.now())
    
    f.write(date_append + '_________\n')
    
    for file in os.listdir(source_path):
        ext = os.path.splitext(file)[1][1:]
        print(file)
        if file == "szortir_log.txt":
            continue
        elif ext in ext_added:
            moving_to(file, ext, cwd)
            f.write(file+" --> "+ext+"\n")
        else:
            continue
    f.write(3*'\n')
    f.close()
    print("f1 bezarasa")



# meg ez
def szortirozas_metodus2():
    global source_path
    print("szortirozas_metodus2")
    os.chdir(source_path)
    cwd = os.getcwd()

    if ext_added:
        for dic_ext in ext_added:
            try:
                os.mkdir(dic_ext)
            except:
                continue
        
    try:
        os.mkdir("Egyeb")
    except:
        os.mkdir("Egyeb3123jlk3948")

    linux = False
    if source_path[0] == '/':
        linux = True

    if linux:
        try:
            f = open(cwd+"/szortir_log.txt", "a")
        except:
            print("Letezik a fajl")
    else:
        try:
            f = open(cwd+"\\szortir_log.txt", "a")
        except:
            print("Letezik a fajl")

    date_append = str(datetime.datetime.now())
    
    f.write(date_append + '_________\n')
    
    for file in os.listdir(source_path):
        print(file)
        ext = os.path.splitext(file)[1][1:]
        if file == "szortir_log.txt":
            continue
        elif ext in ext_added:
            moving_to(file, ext, cwd)
            f.write(file+" --> "+ext+"\n")
        elif ext not in ext_added and ext != '':
            moving_to(file, "Egyeb", cwd)
            f.write(file+" --> Egyeb\n")
        else:
            continue

    f.write(3*'\n')
    f.close()
    print("f2 bezarasa")
    

def open_log():
    try:
        os.startfile("szortir_log.txt")
    except:
        print("wut")


def destroying_everything():
    wd = tkinter.Tk()
    wd.geometry("300x120")

    tkinter.Label(wd, text="Keszitettem egy logot a szortirozott fajlokrol...\nMegnyitod?").pack()
    tkinter.Button(wd, text="Megnyitas", command=open_log).pack()
    tkinter.Button(wd, text="Program bezarasa", command=wd.destroy).pack()


def go_sort():
    global wd, szortir, szortir_gomb, listbox_label, ext_list, egyeb_szoveg, legyen_egyeb_mappa_var, egyeb_cb
    
    print(legyen_egyeb_mappa_var.get())

    wd.destroy()
    destroying_everything()
    
    if legyen_egyeb_mappa_var.get():
        szortirozas_metodus2()
    else:
        szortirozas_metodus1()


def ext_eltavolitas():
    global wd, szortir, szortir_gomb, listbox_label, ext_list
    removable = str(ext_list.get(tkinter.ACTIVE))
    if removable in ext_added:
        ext_added.remove(removable)
    ext_listazas()


def ext_hozzaadas():
    global wd, szortir, szortir_gomb, listbox_label, ext_list
    answer = simpledialog.askstring("Input", "Milyen kiterjesztest akarsz hozzaadni?", parent=wd)
    ext_list.destroy()
    if answer is not None:
        ext_added.append(answer)
    ext_listazas()

def utvonal_done2():
    global wd, szortir, szortir_gomb, listbox_label, ext_list, egyeb_szoveg, legyen_egyeb_mappa_var, egyeb_cb, remove_btn, add_btn, go_sort_btn

    ext_listazas()
    
    add_btn = tkinter.Button(wd, text="Hozzaad", command=ext_hozzaadas)
    add_btn.grid(row=4, column=1, sticky="W")
    remove_btn = tkinter.Button(wd, text="Eltavolit", command=ext_eltavolitas)
    remove_btn.grid(row=4, column=1, sticky="E")

    egyeb_szoveg = tkinter.Label(wd, text="\nA nem hozzaadott kiterjesztesu fajlokat\n beletegyem egy kulon Egyeb mappaba,\nvagy hagyjam a helyukon?")
    egyeb_szoveg.grid(row=5, column=1)
    legyen_egyeb_mappa_var = tkinter.IntVar()
    egyeb_cb = tkinter.Checkbutton(wd, text="Csinaljam?", variable=legyen_egyeb_mappa_var)
    egyeb_cb.grid(row=6, column=1)
    
    go_sort_btn = tkinter.Button(wd, text="Mehet", bg="lightblue", fg="red", command=go_sort)
    go_sort_btn.grid(row=7, column=1)


def utvonal_done():
    global wd, source_path, kiiras, biztos, biztos1, biztos2, szortir, szortir_gomb, szoveg1
    kiiras.destroy()
    biztos.destroy()
    biztos1.destroy()
    biztos2.destroy()
    szortir.destroy()
    szortir_gomb.destroy()
    szoveg1 = tkinter.Label(wd, text="Ezt a mappat fogom szortirozni:\n{}".format(source_path))
    szoveg1.grid(row=1, column=1)
    utvonal_done2()


def choose_path2():
    global wd, source_path, kiiras, biztos, biztos1, biztos2, szortir, szortir_gomb
    kiiras.destroy()
    biztos.destroy()
    biztos1.destroy()
    biztos2.destroy()
    source_path = tkinter.filedialog.askdirectory()
    print(source_path)
    kiiras = tkinter.Label(wd, text="A szortirozando mappa:\n{}".format(source_path), fg="blue")
    kiiras.grid(row=3, column=1)
    biztos = tkinter.Label(wd, text="Biztos? ", fg="red")
    biztos.grid(row=4, column=1)
    biztos1 = tkinter.Button(wd, text="IGEN", command=utvonal_done)
    biztos1.grid(row=4, column=2)
    biztos2 = tkinter.Button(wd, text="NEM", command=choose_path2)
    biztos2.grid(row=4, column=3)

def choose_path():
    global wd, source_path, kiiras, biztos, biztos1, biztos2, szortir, szortir_gomb
    source_path = tkinter.filedialog.askdirectory()
    kiiras = tkinter.Label(wd, text="A szortirozando mappa:\n{}".format(source_path), fg="blue")
    kiiras.grid(row=3, column=1)
    biztos = tkinter.Label(wd, text="Biztos? ", fg="red")
    biztos.grid(row=4, column=1)
    biztos1 = tkinter.Button(wd, text="IGEN", command=utvonal_done)
    biztos1.grid(row=4, column=2)
    biztos2 = tkinter.Button(wd, text="NEM", command=choose_path2)
    biztos2.grid(row=4, column=3)

def ext_listazas():
    global wd, szortir, szortir_gomb, listbox_label, ext_list

    listbox_label = tkinter.Label(wd, text="Ezeket a kiterjeszteseket szortirozom mappakba:", fg="blue")
    listbox_label.grid(row=2, column=1)
    ext_list = tkinter.Listbox(wd, width=43, height=15)
    ext_list.grid(row=3, column=1)
    
    ext_added.sort()
    for i, ext in enumerate(ext_added):
        ext_list.insert(i, ext)
        

def main():
    global wd, szortir, szortir_gomb, listbox_label, ext_list
    wd = tkinter.Tk()
    wd.geometry("750x500")

    szortir = tkinter.Label(wd, text="Valaszd ki, melyik mappaba szeretned a szortirozast:")
    szortir.grid(row=1, column=1)
    szortir_gomb = tkinter.Button(wd, text="Eleresi ut megadasa", command=choose_path)
    szortir_gomb.grid(row=2, column=1)



    
    



    wd.mainloop()




if __name__ == "__main__":
    main()

