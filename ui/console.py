from termcolor import colored
from domain.transaction import create_dict
from domain.bank import modify_sum_in_transaction, setup_bank, modify_day_in_transaction, modify_type_in_transaction, \
    remove_from_dict_by_day, remove_from_dict_by_dayinterval, remove_from_dict_by_type, search_dict_greater_than, \
    search_dict_greater_than_and_before, search_dict_by_type, sum_type, sold_date, sort_trans_by_sum, \
    elim_trans_by_type, elim_trans_by_type_and_sum


def print_trans_list(mylist):
    for i in range(len(mylist)):
        print(i, 'Zi', colored(mylist[i]['zi'], 'blue'), '- Suma:',
              colored(mylist[i]['suma'], 'blue'), '-Tipul:', colored(mylist[i]['tipul'], 'blue'))


def add_transaction_ui(my_list):
    try:
        zi = int(input("Ziua tranzactiei:"))
        suma = int(input("Suma tranzactiei:"))
        tipul = input("Tipul tranzactiei(intrare/iesire):")
        create_dict(my_list, zi, suma, tipul)
        print(colored("Adaugare realizata cu succes.", 'green'))
    except ValueError:
        print(colored("Introduceti numere pentru zi si suma.", 'red'))


def modify_transaction_ui(my_list):
    try:
        new_zi = int(input("Ziua modificata a tranzactiei:"))
        new_suma = int(input("Suma modificata tranzactiei:"))
        new_tipul = input("Tipul nou al tranzactiei(intrare/iesire):")
        if new_zi != '':
            modify_day_in_transaction(my_list, new_zi)
        if new_suma != '':
            modify_sum_in_transaction(my_list, new_suma)
        if new_tipul != '':
            modify_type_in_transaction(my_list, new_tipul)
    except ValueError:
        print(colored("Introduceti numere pentru zi si suma.", 'red'))


def delete_by_day_ui(my_list):
    day = input('Ziua este:')
    remove_from_dict_by_day(my_list, day)


def remove_from_dict_by_dayinterval_ui(mylist):
    my_daybefore = int(input('Ziua initiala este:'))
    my_dayafter = int(input('Ziua finala este:'))
    remove_from_dict_by_dayinterval(mylist, my_daybefore, my_dayafter)


def remove_by_type_ui(mylist):
    transtype = input('Tipul(intrare/iesire) este:')
    remove_from_dict_by_type(mylist, transtype)


def search_trans_greater_than_sum_ui(mylist):
    my_sum = int(input("Introduceti suma de comparat: "))
    print(search_dict_greater_than(mylist, my_sum))


def search_trans_greater_than_sum_and_before_ui(mylist):
    my_sum = int(input("Introduceti suma de comparat: "))
    my_day = int(input("Introduceti ziua de comparat: "))
    print(search_dict_greater_than_and_before(mylist, my_sum, my_day))


def search_trans_type_as_ui(mylist):
    my_type = input("Introduceti tipul de tranzactie cautat(intrare/iesire): ")
    print(search_dict_by_type(mylist, my_type))


def sum_type_ui(mylist):
    mytype = input("Introduceti tipul de tranzactie cautat(intrare/iesire): ")
    print("Suma este ", sum_type(mylist, mytype))


def sold_date_ui(mylist):
    myday = int(input("Introduceti ziua in care sa verificati soldul: "))
    print(sold_date(mylist, myday))


def sort_trans_by_sum_ui(mylist):
    my_type = input("Introduceti tipul de tranzactie cautat(intrare/iesire): ")
    print(sort_trans_by_sum(mylist, my_type))


def elim_trans_by_type_ui(mylist):
    mytype = input("Introduceti tipul de tranzactie cautat(intrare/iesire): ")
    print(elim_trans_by_type(mylist, mytype))


def elim_trans_by_type_and_sum_ui(mylist):
    mytype = input("Introduceti tipul de tranzactie cautat(intrare/iesire): ")
    mysum = int(input("Introduceti suma de comparat: "))
    print(elim_trans_by_type_and_sum(mylist, mytype, mysum))


def start():
    my_list = setup_bank()
    print("add, modify, del, search, reports, undo, print, exit")
    x = input()
    while x != '':
        if x == 'add':
            add_transaction_ui(my_list)
            x = input()
        elif x == 'modify':
            modify_transaction_ui(my_list)
            x = input()
        elif x == 'del':
            print("delete_by_day, delete_by_dayinterval, delete_by_type")
            y = input()
            if y == 'delete_by_day':
                delete_by_day_ui(my_list)
                x = input()
            elif y == 'delete_by_dayinterval':
                remove_from_dict_by_dayinterval_ui(my_list)
                x = input()
            elif y == 'delete_by_type':
                remove_by_type_ui(my_list)
                x = input()
        elif x == 'search':
            print("search_trans_greater_than_sum, search_dict_greater_than_and_before, search_trans_type")
            z = input()
            if z == 'search_trans_greater_than_sum':
                search_trans_greater_than_sum_ui(my_list)
                x = input()
            elif z == 'search_dict_greater_than_and_before':
                search_trans_greater_than_sum_and_before_ui(my_list)
                x = input()
            elif z == 'search_trans_type':
                search_trans_type_as_ui(my_list)
                x = input()
        elif x == 'reports':
            print("sum_type, sold_date, sort_trans_by_sum")
            f = input()
            if f == 'sum_type':
                sum_type_ui(my_list)
                x = input()
            elif f == 'sold_date':
                sold_date_ui(my_list)
                x = input()
            elif f == 'sort_trans_by_sum':
                sort_trans_by_sum_ui(my_list)
                x = input()
        elif x == 'undo':
            print("nu functioneaza")
            x = input()
        elif x == 'print':
            print_trans_list(my_list)
            x = input()
        elif x == 'exit':
            return 0
    if x == '':
        print("trebuie sa introduceti o optiune")
