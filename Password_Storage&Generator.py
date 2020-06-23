import string
from random import *
import numpy as np

add = input("Do you want to add or read from the dictonary(a/r): ").strip()
site = input("Enter the name of the site: ").strip()

login_details = {}

if add == "a":
    login = input("Enter you username: ").strip()
    characters = string.ascii_letters + string.digits + string.punctuation
    password =  "".join(choice(characters) for x in range(randint(8, 16)))
    #print (password)

    login_details[site] = {login, password}
    print(login_details)

    np.save('my_file.npy', login_details)
    read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item()
    print(read_dictionary[site])
elif add == "r":
    read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item()
    print(read_dictionary[site])

