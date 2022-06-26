#Aryan Tripthi
#12th - A

from tkinter import *
from tkinter import ttk
import csv,ctypes,os

#window quality 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def open_csv(method):
    '''This function opens csv in read/write/append according to the argument passed.'''
    try:
        file = open(r"D:\Aryan\Code\HHW\back.csv", method ,newline='')
    except:
        print('File error!\nCheck if file is open in another window!')

    if method == 'r':
        dbread = csv.reader(file)
        dbread = [i for i in dbread]
        file.close()
        return dbread
    
    if method in ['w','a']:
        dbwrite = csv.writer(file)
        return dbwrite 
        
main = Tk()
main.title('Student Information System')
main.geometry('1920x1080')              #window size
main.state('zoomed')                    #window maximise
main.iconbitmap('D:\Aryan\Code\HHW\database icon.ico')#window icon

#style
main.configure(background='#DFF6FF')    #background color
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)

#heading(STUDENT INFORMATION SYSTEM)
heading = Label(main, text='STUDENT INFORMATION SYSTEM', font='Arial 50 bold underline', fg='#1363DF',
bg='#DFF6FF', pady=10)
heading.grid(row=0, columnspan=2)

#style
style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview',font='Arial 20', rowheight=50, background='#90E0EF', fieldbackground='#90E0EF')
style.configure('Treeview.Heading', font='Bahnschrift 35 bold', rowheight=88)
style.configure('TButton', font='Arial 20 bold')

def input_check(insert_data):
    '''Checks inputs entered by user return True if any input is of incorrect data type'''
    global error_code
    
    #school no datatype
    try:
        int(insert_data[0])
    except:
        error_code = 'S'
        return True

    if not (insert_data[1]).isalpha():
        error_code = 'N'
        return True
    
    if not (insert_data[2]).isalpha():
        error_code = 'C'
        return True

    try:
        float(insert_data[3])
    except:
        error_code = 'F'
        return True
    
    return False

def error_window(e):
    '''Pops up an error window which displays the error.'''
    error_win = Toplevel(main)
    error_win.title('ERROR')
    error_win.iconbitmap('D:\Aryan\Code\HHW\error.ico')
    error_win.geometry('350x50')

    ecodes = {'S':'School no error!\nEnter valid value!',
    'N':'Name error!\nEnter valid value!',
    'C':'City error!\nEnter valid value!',
    'F':'Fees error!\nEnter valid value!',
    'M':'Select a Record!',
    'SE':'Record not Found!'}

    msg = Label(error_win, text=ecodes.get(e), font='Arial 15 bold', fg='red')
    msg.anchor('center')
    msg.pack()

    error_win.after(5000, error_win.destroy)
    error_win.mainloop()

def ams_window(mf,values):
    '''Opens a new window for data entry'''
    icon = {'SEARCH RECORD': 'D:\Aryan\Code\HHW\search_icon.ico',
    'MODIFY RECORD':'D:\Aryan\Code\HHW\modify icon.ico',
    'ADD RECORD':r'D:\Aryan\Code\HHW\add icon.ico'}
    
    win = Toplevel(main)
    win.title(mf)
    win.geometry('1200x400')
    win.iconbitmap(icon.get(mf))

    def b_command():        
        inp_values = [school_inp.get(), name_inp.get(), city_inp.get(), fees_inp.get()]

        db_read = open_csv('r')

        if mf == 'SEARCH RECORD':
            n = 0
            for inp in inp_values:
                if inp != '': n+=1
 
            results = []

            for record in db_read:
                m = 0
                for i in range(4):
                    if inp_values[i] != '':
                        if inp_values[i] == record[i]: m+= 1

                if m == n:
                    results.append(record)

            if len(results) == 0:
                error_window('SE')
                win.destroy()

            s_win = Toplevel(win)
            s_win.title('SEARCH RESULTS')
            s_win.geometry('1800x1000')

            heading_s = Label(s_win, text='SEARCH RESULTS', font='Arial 50 bold', 
            fg='#F15412', pady=10)
            heading_s.pack()

            S_style = ttk.Style()
            S_style.theme_use('clam')
            S_style.configure('Treeview',font='Arial 20', rowheight=50, background='#90E0EF', fieldbackground='#90E0EF')
            S_style.configure('Treeview.Heading', font='Bahnschrift 35 bold', rowheight=88)

            #table
            S_tree = ttk.Treeview(s_win, columns=("c1", "c2", "c3", "c4"),show='headings', height=11, selectmode='browse')

            S_tree.column("# 1",anchor=CENTER, stretch=NO, width=350)
            S_tree.heading("# 1", text="School No.")

            S_tree.column("# 2",anchor=CENTER, stretch=YES, width=600)
            S_tree.heading("# 2", text='Name')

            S_tree.column("# 3",anchor=CENTER, stretch=YES, width=300)
            S_tree.heading("# 3", text='City')

            S_tree.column("# 4",anchor=CENTER, stretch=YES, width=250)
            S_tree.heading("# 4", text='Fees')

            for r in results:
                S_tree.insert('', END, values=(r))

            S_tree.pack()
            
            s_win.mainloop()

        if input_check(inp_values):
            error_window(error_code)
            return

        if mf == 'MODIFY RECORD':
            selection = select('')
            selection = list(selection)
            i = db_read.index(selection)
            db_read[i] = inp_values

            writerw = open_csv('w')
            for record in db_read:
                writerw.writerow(record)

        if mf == 'ADD RECORD':
            writera = open_csv('a')
            writera.writerow(inp_values)
        
        win.quit()

    #style
    win.configure(background='#FEF9A7')
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.columnconfigure(2, weight=1)
    win.columnconfigure(3, weight=1)

    heading = Label(win, text=mf, font='Arial 40 bold underline', background='#FEF9A7', fg='#F77E21')
    heading.grid(row=0, columnspan=4, pady=10)

    school = Label(win, text='School no:', font='Bahnschrift 20', background='#FEF9A7')
    school.grid(row=1, column=0, sticky=W, padx=10)
    school_inp = Entry(win, borderwidth=1, font='Calibri 20', fg='#A5BECC')
    school_inp.grid(row=1, column=1, sticky=W)

    name = Label(win, text='Name:', font='Bahnschrift 20', background='#FEF9A7')
    name.grid(row=2, column=0, sticky=W, padx=10)
    name_inp = Entry(win, borderwidth=1, font='Calibri 20', fg='#A5BECC')
    name_inp.grid(row=2, column=1, sticky=W)

    city = Label(win, text='City:', font='Bahnschrift 20', background='#FEF9A7')
    city.grid(row=1, column=2, sticky=W)
    city_inp = Entry(win, borderwidth=1, font='Calibri 20', fg='#A5BECC')
    city_inp.grid(row=1, column=3, sticky=W)
    
    fees = Label(win, text='Fees:', font='Bahnschrift 20', background='#FEF9A7')
    fees.grid(row=2, column=2, sticky=W)
    fees_inp = Entry(win, borderwidth=1, font='Calibri 20', fg='#A5BECC')
    fees_inp.grid(row=2, column=3, sticky=W)

    if mf == 'MODIFY RECORD':
        if values == '':
            win.destroy()
            error_window("M")
            return

        school_inp.insert(0, values[0])
        name_inp.insert(0, values[1])
        city_inp.insert(0, values[2])
        fees_inp.insert(0, values[3])

    action = ''
    if mf in ['ADD RECORD', 'MODIFY RECORD']:
        action = 'SAVE'
    else:
        action = 'SEARCH'

    action_b = Button(win, text=action, font='Arial 20 bold', activebackground='#FBCB0A', command=b_command)
    action_b.grid(row=3, columnspan=4, pady=10)

    win.mainloop()

    main.destroy()
    os.system('D:\Aryan\Code\HHW\GUI.py')
        
def delete_record():
    if select('') == '':
        error_window('M')
        win.destroy()
        return

    win = Toplevel(main)
    win.title('DELETE')
    win.geometry('350x140')
    win.iconbitmap('D:\Aryan\Code\HHW\delete icon.ico')

    t_f = False

    def option_f(value):
        nonlocal t_f
        t_f = value
        win.quit()

    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)

    prompt_msg = Label(win,text=f'Delete record?', fg='red', font='Arial 20')
    prompt_msg.grid(row=0, columnspan=2, pady=5, sticky=EW)

    option_yes = Button(win, text='YES', font='Arial 15 bold',
    command= lambda:option_f(True))
    option_yes.grid(row=1, column=0, padx=5, sticky=EW)
    
    option_no = Button(win, text='NO', font='Arial 15 bold',
    command= lambda:option_f(False))
    option_no.grid(row=1, column=1, padx=5, sticky=EW)

    win.mainloop()
    win.destroy()

    if not t_f:
        return

    db_read = open_csv('r')
    selection = select('')
    selection = list(selection)
    
    selected = tree.selection()
    tree.delete(selected)

    for record in db_read:
        if record == selection:
            db_read.remove(selection)

    writer = open_csv('w')
    for record in db_read:
        writer.writerow(record)

#value of selected item
def select(a):
    '''Returns data of record selected in Treeview/table'''
    curItem = tree.focus()
    value = (tree.item(curItem, 'values'))
    return value

#table
tree = ttk.Treeview(main, columns=("c1", "c2", "c3", "c4"),show='headings', height=11, selectmode='browse')

#selected data
tree.bind('<<TreeviewSelect>>', select)

tree.column("# 1",anchor=CENTER, stretch=NO, width=400)
tree.heading("# 1", text="SCHOOL NO")

tree.column("# 2",anchor=CENTER, stretch=YES, width=600)
tree.heading("# 2", text='NAME')

tree.column("# 3",anchor=CENTER, stretch=YES, width=300)
tree.heading("# 3", text='CITY')

tree.column("# 4",anchor=CENTER, stretch=YES, width=250)
tree.heading("# 4", text='FEES')

data = open_csv('r')
for record in data:
    tree.insert('', END, values=(record))

tree.grid(row=1, columnspan=2, pady=5)

add = ttk.Button(main, text='ADD', command=lambda:ams_window('ADD RECORD',''))
add.grid(row=2, column=0, pady=5)

delete = ttk.Button(main, text='DELETE', command=delete_record)
delete.grid(row=2, column=1, pady=5)

search = ttk.Button(main, text='SEARCH', command=lambda:ams_window('SEARCH RECORD',''))
search.grid(row=3, column=0, pady=5)

modify = ttk.Button(main, text='MODIFY', command=lambda:ams_window('MODIFY RECORD', select('')))
modify.grid(row=3, column=1, pady=5)

#scrollbar
sb = Scrollbar(main, orient=VERTICAL)
sb.grid(sticky=E)

main.mainloop()
