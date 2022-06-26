import csv
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def open_csv(method):
    '''Opens csv file in read/write/append according to the argument passed.'''
    try:
        file = open(r'D:\Aryan\Python\HHW\back.csv', method ,newline='')
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
        
def data_inps():
    '''Takes input of data and verifies the correct datatype for each field'''
    print('Enter particulars of Student')
    while True: #school_no
        school_no = eval(input('    School No: '))
        if school_no == '' or type(school_no) != int:
            print(Fore.RED + 'Enter valid value')
        else:
            break

    while True: #name
        name = input('    Name: ')
        if name == '' or type(name) != str:
            print(Fore.RED + 'Enter valid value')
        else:
            break
    
    while True: #city
        city = input('    City: ')
        if city == '' or type(city) != str:
            print(Fore.RED + 'Enter valid value')
        else:
            break
    
    while True: #fee
        fee = eval(input('    Fee: '))
        if fee == '' or (type(fee) not in [int, float]):
            print(Fore.RED + 'Enter valid value')
        else:
            break

    w = [school_no,name.title(),city.title(),fee]

    return w

def addrecord():
    '''Adds record to desired index.'''
    dlist = open_csv('r')

    while True:
        index = input('Enter index to add record: ')
        if not index.isdigit() or int(index) not in range(0,len(dlist)):
            print(Fore.RED + 'Select a valid index!')
        else:
            break
    
    dlist.insert(int(index)-1,data_inps())
    
    dbwrite = open_csv('w')
    for r in dlist:
        dbwrite.writerow(r)

    print('Record successfully added')

    if input('Add another record?(y/n): ') in ['y','Y']:
        addrecord()
    else: return

def append_record():
    '''Appends records.'''
    writer = open_csv('a')
    writer.writerow(data_inps())
    print('Record succesfully appended!')
    if input('Append another record?(y/n): ') in ['y','Y']:
        append_record()
    else: return

def modify_record():
    '''Modifies the exsisting records. It requires the index of the record to be modified.'''
    dlist = open_csv('r')

    while True:
        try:
            index = int(input('Enter index of record to be modified: ')) - 1
        except:
            print(Fore.RED + 'Enter valid input!')
            continue

        try:
            print(dlist[index])
            break
        except:
            print(Fore.RED + 'Index out of range!')
            continue

    if input('Continue?(y/n): ') in ['y','Y']:
        print('Enter Modified data')
        dlist[index] = data_inps()
    else:
        modify_record()
        pass

    dbread = open_csv('w')
    for r in dlist:
        dbread.writerow(r)

    print(dlist[index])
    print('Record modified!')

    if input('Modify another record?(y/n): ') in ['y','Y']:
        modify_record()
    else: return

s_options = {
    1: 'School no: ',
    2: 'Name: ',
    3: 'City: ',
    4: 'Fee: '}

def search_record():
    '''Searches records by School no, Student Name, City and Fee. Returns all records with 
    the same field name and also returns 'Record not Found' if record is not found.'''
    
    print('''Search by:
    Enter 1 to Search by School no
    Enter 2 to Search by Name
    Enter 3 to Search by City
    Enter 4 to Search by Fee''')
        
    while True:
        op = eval(input('    Select option: '))
        if type(op) != int or op not in range(1,5):
            print(Fore.RED + '    Select a valid option!')
        else:
            break

    dlist = open_csv('r')

    search = input(s_options.get(op))
    
    n = True
    for record in dlist:
        if record[op - 1] == search:
            n = False
            print(record)
    
    if n:
        print(Fore.RED + 'Record not Found')

    if input('Search another record?(y/n): ') in ['y','Y']:
        search_record()
    else: return

def delete_record():
    '''Deletes records by School no, Student Name, City, Fee and Index. Returns all 
    records with the same field name and asks user for each record. Returns 'Record not Found' 
    if record is not found.'''
    print('''Delete by:
    Enter 1 to Delete by School no
    Enter 2 to Delete by Name
    Enter 3 to Delete by City
    Enter 4 to Delete by Fee
    Enter 5 to Delete by Index''')

    while True:
        try:
            op = int(input('    Select option: '))
            break
        except:
            print(Fore.RED + '    Select a valid option!')

    dbread = open_csv('r')

    if op == 5:
        while True:
            try:
                delete = int(input('Index: '))-1
                print(dbread[delete])
                if input('Continue?(y/n): ') in ['y','Y']:
                    dbread.pop(delete)
                    print('Record deleted!')
                else: return
                
            except:
                print(Fore.RED + 'Enter valid index!')

    else:
        delete = input(s_options.get(op))

        n = True
        for record in dbread:
            if delete in record[op-1]:
                n = False
                print(record, 'will be deleted')
                
                if input('Continue?(y/n): ') in ['y','Y']:
                    dbread.remove(record)
                    print('Record is deleted!')
                else:
                    continue

    if n:
        print(Fore.RED + 'Record not found!')
        delete_record()
    
    writer = open_csv('w')

    for r in dbread:
        writer.writerow(r)

    if input('Delete another record?(y/n): ') in ['y','Y']:
        modify_record()
    else: return

while True:
    #option
    print(Fore.GREEN + '\nStudent Information System')
    print(Fore.YELLOW + '-------------------------------------------')
    option = int(input('''    Enter 1 to Add Record
    Enter 2 to Display Record
    Enter 3 to Append Record
    Enter 4 to Modify Record
    Enter 5 to Search Record
    Enter 6 to Delete Record
    Enter 7 to Exit
    Select option: '''))
        
    if option == 1:         #Add Record
        print(Fore.YELLOW + '-------------------------------------------')
        print(Fore.BLUE + 'ADD RECORD')
        addrecord()
        print(Fore.YELLOW + '-------------------------------------------')

    elif option == 2:       #Display record
        dlist = open_csv('r')

        print(Fore.YELLOW + '-------------------------------------------')
        print(Fore.BLUE + 'ALL RECORDS:')

        if len(dlist) == 0:
            print('no records!')
            pass

        i = 1
        for line in dlist:
            line = ' '.join(line)
            print(f'{i}. {line}')
            i += 1

        print(Fore.YELLOW + '-------------------------------------------')

    elif option == 3:       #Append
        print(Fore.YELLOW + '-------------------------------------------')
        print(Fore.BLUE + 'APPEND RECORD')
        append_record()
        print(Fore.YELLOW + '-------------------------------------------')

    elif option == 4:       #Modifiy
        print(Fore.YELLOW + '-------------------------------------------')
        print(Fore.BLUE + 'MODIFY RECORD')
        modify_record()  
        print(Fore.YELLOW + '-------------------------------------------')   

    elif option == 5:       #Search
        print(Fore.YELLOW + '-------------------------------------------')
        print(Fore.BLUE + 'SEARCH RECORD')
        search_record()
        print(Fore.YELLOW + '-------------------------------------------')

    elif option == 6:       #Delete
        print(Fore.YELLOW + '-------------------------------------------')
        print(Fore.BLUE + 'DELETE RECORD')
        delete_record()
        print(Fore.YELLOW + '-------------------------------------------')

    elif option == 7:       #End program
        exit()

    else:
        print(Fore.RED + 'Enter valid value!')