from domain.get_and_set import set_sum, set_day, set_type, get_trans, get_type, get_undo_list, set_undo_list,\
    set_trans_list
from domain.transaction import create_dict


def generate_trans():
    return [{'12', '123', 'intrare'}, {'13', '345', 'iesire'}, {'14', '567', 'intrare'}, {'15', '789', 'iesire'}, {'16', '897', 'int'}]


def setup_bank():
    mylist = []
    return mylist


def modify_day_in_transaction(mylist, new_day):
    set_day(mylist, new_day)


def modify_sum_in_transaction(mylist, new_sum):
    set_sum(mylist, new_sum)


def modify_type_in_transaction(mylist, new_type):
    set_type(mylist, new_type)


def remove_from_dict_by_day(mylist, my_day):
    for i in range(len(mylist)):
        if mylist[i]['zi'] != my_day:
            del mylist[i]
            break
    return mylist


def remove_from_dict_by_dayinterval(mylist, my_day1, my_day2):
    for i in range(len(mylist)):
        if my_day1 < mylist[i]['zi'] < my_day2:
            del mylist[i]
            break
        elif my_day1 == mylist[i]['zi'] or my_day2 == mylist[i]['zi']:
            del mylist[i]
            break
    return mylist


def remove_from_dict_by_type(mylist, mytype):
    for i in range(len(mylist)):
        if mylist[i]['zi'] != mytype:
            del mylist[i]
            break
    return mylist


def search_dict_greater_than(mylist, mysum):
    res = list(filter(lambda i: i['suma'] > mysum, mylist))
    return res


def search_dict_greater_than_and_before(mylist, mysum, myday):
    res = list(filter(lambda i: (i['suma'] > mysum and i['zi'] < myday), mylist))
    return res


def search_dict_by_type(mylist, mytype):
    res = list(filter(lambda i: i['tipul'] == mytype, mylist))
    return res


def sum_type(mylist, mytype):
    s = 0
    for i in range(len(mylist)):
        if mylist[i]['tipul'] == mytype:
            s = s + mylist[i]['suma']
    return s


def sold_date(mylist, myday):
    s = 0
    s1 = 0
    for i in range(len(mylist)):
        if mylist[i]['zi'] <= myday and mylist[i]['tipul'] == "intrare":
            s = s + mylist[i]['suma']
        if mylist[i]['zi'] <= myday and mylist[i]['tipul'] == "iesire":
            s1 = s1 + mylist[i]['suma']
    sf = s - s1
    return sf


def sortingkey(e):
    return e['suma']


def sort_trans_by_sum(mylist, mytype):
    res = list(filter(lambda i: i['tipul'] == mytype, mylist))
    res.sort(key=sortingkey)
    return res


def elim_trans_by_type(mylist, mytype):
    res = list(filter(lambda i: i['tipul'] != mytype, mylist))
    return res


def elim_trans_by_type_and_sum(mylist, mytype, mysum):
    res = list(filter(lambda i: (i['tipul'] == mytype and i['suma'] < mysum), mylist))
    return res


def undo(mylist):
    undo_list = get_undo_list(mylist)
    if len(undo_list) == 0:
        raise ValueError("Nu se mai poate face undo.")
    else:
        previous_list = undo_list[-1]
        set_trans_list(mylist, previous_list)
        set_undo_list(mylist, undo_list[:-1])

# tests


def test_remove_by_type():
    test_list1 = generate_trans()
    initial_length = len(test_list1)
    test_list1 = elim_trans_by_type(test_list1, 'iesire')

    assert (len(test_list1) == initial_length - 2)

    test_list2 = []
    test_list2 = elim_trans_by_type(test_list2, 'iesire')
    assert (len(test_list2) == 0)


def test_elim_trans_by_type():
    test_trans = setup_bank()
    create_dict(test_trans, 69, 420, 'intrare')
    create_dict(test_trans, 7, 12, 'iesire')

    assert (len(get_trans(test_trans)) == 2)
    elim_trans_by_type(setup_bank, 'iesire')
    assert (len(get_trans(test_trans)) == 1)


def test_filter_by_name():
    test_list = []
    filtered_list1 = search_dict_by_type(test_list, 'ies')
    assert (len(filtered_list1) == 0)

    test_list2 = generate_trans()

    filtered_list2 = search_dict_by_type(test_list2, 'iesire')
    assert (len(filtered_list2) == 2)

    filtered_list3 = search_dict_by_type(test_list2, 'int')
    assert (len(filtered_list3) == 1)
    assert (get_type(filtered_list3[0]) == 'int')

    filtered_list4 = search_dict_by_type(test_list2, 'schimbare')
    assert (len(filtered_list4) == 0)

    filtered_list5 = search_dict_by_type(test_list2, '')
    assert (len(filtered_list5) == 0)


def test_elim_trans_by_type_and_sum():
    test_trans = setup_bank()
    create_dict(test_trans, 69, 420, 'intrare')
    create_dict(test_trans, 7, 12, 'iesire')

    assert (len(get_trans(test_trans)) == 2)
    elim_trans_by_type_and_sum(setup_bank, 'iesire', 100)
    assert (len(get_trans(test_trans)) == 1)


def test_sort_trans_by_sum():
    test_list = []
    filtered_list1 = sort_trans_by_sum(test_list, 'iesire')
    assert (len(filtered_list1) == 0)
