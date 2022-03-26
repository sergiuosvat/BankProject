
def create_dict(my_list, zi, suma, tipul):
    my_list.append(dict(zi=zi, suma=suma, tipul=tipul))
    return my_list


def create_dict_test():
    this_list = []
    t1 = create_dict(this_list, 12, 123, 'intrare')
    assert (type(t1) == list)

    assert (t1[0] == 12)
    assert (t1[1] == 123)
    assert (t1[2] == 'intrare')

