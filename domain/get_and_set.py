def set_day(mylist, new_day):
    e = {'ziua': new_day}
    for i in mylist:
        i.update(e)


def set_sum(mylist, new_sum):
    d = {'suma': new_sum}
    for i in mylist:
        i.update(d)


def set_type(mylist, new_type):
    f = {'tipul': new_type}
    for i in mylist:
        i.update(f)


def get_trans(trans):
    return trans[0]


def get_type(trans):
    return trans[2]


def get_undo_list(mylist):
    return mylist[0]


def set_trans_list(mylist, new_products_list):
    mylist[0] = new_products_list


def set_undo_list(mylist, new_undo_list):
    mylist[1] = new_undo_list
