char = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']

def display(elem):
        assert type(elem) is int, 'Argument Must Be Interger'
        print('List Element', elem, '=', char[elem])


elem = 4
display(elem)


elem = elem / 2
display(elem)
