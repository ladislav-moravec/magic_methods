


oblibeneVeci= {
    'homer': 'koblihy',
    'marge': 'trouba',
    'bart': 'prak',
    'lisa': 'saxofon',
    'maggie':'dudlík'
}

simpson = input("Ahoj, zadej svého oblíbeného Simpsona (z rodiny Simpsonů): ")
if simpson in oblibeneVeci:
    print("%s má rád %s." % (simpson.lower(), oblibeneVeci[simpson]))
else:
    print("Hele, tohle není Simpson!")

