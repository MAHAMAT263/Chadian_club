def coffe_shope():
    available_coffe = ['Black coffe', 'Milk tea' , 'Milk Chocolate']
    for i in available_coffe:
        print(i)
    X = input('Choose one of the avialbel coffe: ')
    available_coffe.append(X)
    for b in available_coffe:
        c = available_coffe.index(b)
        print(c,b)
coffe_shope()
