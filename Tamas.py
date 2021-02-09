import os
import shutil
import easygui
import tkinter
from tkinter import simpledialog





# a mappak eleresi utvonala, ahova akarod szortirozni a fajlokat
# neked linuxon nyilvan a / slash jel kell es egy eleg belole
# csak hozza kell irni egy ujat, ha hozza akarsz adni
# es az action-be is bele kell irni a minta szerint

dir_pdf = "C:\\Users\\Svab\\Desktop\\teszt\\pdf"
dir_jpg = "C:\\Users\\Svab\\Desktop\\teszt\\jpg"
dir_png = "C:\\Users\\Svab\\Desktop\\teszt\\png"
dir_egyeb = "C:\\Users\\Svab\\Desktop\\teszt\\egyeb"



# ez az algoritmushoz kell, nem piszka!
def moveto(dst):
    return lambda src: shutil.move(src, dst)


# ide kell majd hozzairni a minta szerint amit meg akarsz
# pl ha .torrent fajlokat szortirozzon, akkor
# 'torrent': moveto(dir_torrent),
# ha bizonyos kiterjesztesu fileokat torolni szeretnel, vedd mi a # jelet

action = {
    'pdf': moveto(dir_pdf),
    'jpg': moveto(dir_jpg),
    'png': moveto(dir_png),
    #'py': os.remove,
}



# ez a gyokermappa amiben a fajlokat szeretnenk szortirozni
src_dir = "C:\\Users\\Svab\\Desktop\\teszt"


# algoritmus
for file in os.listdir(src_dir):
    ext = os.path.splitext(file)[1][1:]
    
    # ha a kiterjesztes szerepel az action libraryben
    if ext in action:
        action[ext](os.path.join(src_dir, file))

    # ha a kiterjesztes ismeretlen, beletesszuk a dir_egyeb mappaba
    elif ext not in action and ext != "":
        shutil.move(src_dir+"\\"+file, dir_egyeb)

    # ha nincs kiterjesztes/mappa, csak megy a kovetkezore
    else:
        continue


# lista a kiterjesztesekrol
ext_added = ["jpg", "png", "pdf", "torrent"]

def go_sort():
    ############# TO DO ####################
    # 1. mappak letrehozasa                #
    # 2. fajlok belepakolasa a mappakba    #
    # 3. log fajl keszitese                #
    ########################################

    # path: source_path
    # kiterjesztesek: ext_added

    # kellene egy checkbutton, hogy a maradek filet hagyjuk ugy,
    # vagy beletegyuk egy egyeb mappaba
    
    return

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
    global wd, szortir, szortir_gomb, listbox_label, ext_list

    ext_listazas()

    add_btn = tkinter.Button(wd, text="Hozzaad", command=ext_hozzaadas)
    add_btn.grid(row=4, column=1)
    remove_btn = tkinter.Button(wd, text="Eltavolit", command=ext_eltavolitas)
    remove_btn.grid(row=4, column=2)

    go_sort_btn = tkinter.Button(wd, text="Mehet", bg="lightblue", fg="red", command=go_sort)
    go_sort_btn.grid(row=5, column=1)


def utvonal_done():
    global wd, source_path, kiiras, biztos, biztos1, biztos2, szortir, szortir_gomb
    kiiras.destroy()
    biztos.destroy()
    biztos1.destroy()
    biztos2.destroy()
    szortir.destroy()
    szortir_gomb.destroy()
    tkinter.Label(wd, text="Ezt a mappat fogom szortirozni:\n{}".format(source_path)).grid(row=1, column=1)
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
    ext_list = tkinter.Listbox(wd)
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

