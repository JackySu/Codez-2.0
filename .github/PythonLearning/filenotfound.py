try:
    with open('1.txt', 'r'):
        pass
except FileNotFoundError as e:
    print(e)
