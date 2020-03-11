import importlib

def get_all_candidates(ballots):
    '''(list)->list
    Given a list of strings, a list of lists, a list of dictionaries, or a
    mix of all three, this function returns all the unique strings in this
    list and its nested contents.

    ([{'GREEN':3, 'NDP':5}, {'NDP':2, 'LIBERAL':4},['CPC', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    ([['GREEN', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP','BLOC']
   ([{'GREEN':3, 'NDP':5}, {'NDP':2, 'LIBERAL':4}])
    ['GREEN', 'NDP','LIBERAL']
    '''
    new_list = []
    for e in ballots:
        if type(e) is dict:
            new_list.extend(get_all_candidates(e))
        if type(e) is dict:
            new_list.append(e.keys())
        elif type(e) is dict:
            new_list.append(e)
        return new_list

    print(new_list)

    get_all_candidates(ballots)