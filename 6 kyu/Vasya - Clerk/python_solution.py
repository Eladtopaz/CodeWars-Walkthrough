def tickets(people):
    starting_bills = []
    for p in people:
        if p == 25:
            starting_bills.append(25)
        elif p == 50:
            if 25 in starting_bills:
                starting_bills.remove(25)
                starting_bills.append(50)
            else:
                return "NO"
        elif p == 100:
            if starting_bills.count(50) >= 1 and starting_bills.count(25) >= 2:
                starting_bills.remove(50)
                starting_bills.remove(25)
                starting_bills.remove(25)
                starting_bills.append(100)
            elif starting_bills.count(25) >= 3:
                starting_bills.remove(25)
                starting_bills.remove(25)
                starting_bills.remove(25)
                starting_bills.append(100)  
            else:
                return "NO"
    return "YES"
