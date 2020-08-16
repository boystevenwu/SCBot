with open('log.txt', 'a') as f:
    card = input("Add: ")
    f.write(' {}\n'.format(card))
    print("Added")
