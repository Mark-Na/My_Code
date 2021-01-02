#csv module
# reader: lets you iterate over rows of the CSV as lists
#DictReader: ets you iterate over the rows as oredered dicts

# from csv import reader
# with open(fighters.csv) as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")

# with open(fighters.csv) as file:
#     csv_reader = DictReader(file):
#     for row in csv_reader:
#         print(row['Name'])
# reader accepts delimiter kwarg in case data isnt separated by commas
#csv_reader = reader(file,delimeter = "\")

#writer, dictwriter
# writerow is used alot 

# import csv
# with open("cats.csv","w") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Name","Age"])
#     csv_writer.writerow(['Blue',4])
#     csv_writer.writerow(['Kitty',1])
# [[s.upper() for s in row]for row in csv_reader]

# do this for small changes to new file
# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     with open('screaming_fighters','w'):
#         csv_writer = writer(file)
#         for fighter in csv_reader:
#             csv_writer.writerow([s.upper() for s in fighter])

# creates writer objecr for writing using dictionaries
# fieldnames kwarg for dictwriter
#write header
# writerow

# from csv import writer,DictWriter
# with open("cats.csv", "w") as file:
#     headers = ["Name", "Breed","Age"]
#     csv_writer = DictWriter(file,fieldnames = headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Name":"Garfield", 
#         "Breed":"Tabby",
#         "Age":10
#     })

# def cm_to_in(cm):
#     return float(cm) * 0.393701

# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     fighters = print(list(csv_reader))

# with open("inces_fighters.csv","w") as file:
#     headers = ("Name","Country","Height")
#     csv_writer = DictWriter(file,fieldnames = headers)
#     csv_writer = writeheader()
#     for f in fighters:
#         csv_writer.writerow({
#             "Name":f["Name"],
#             "Country":f["Country"],
#             "Height":cm_to_in(f["Height (in cm)"])
#         })
# use "a" to append to an existing file

#pickling:
# when shut down, wants to save all the contents of the file like deck off cards
# import pickle
#stores the data
# with open("pets.pickle","wb") as file:
#     pickle.dump(blue,file)

# opens it again
#quick to dump and can get later
# with open("pets.pickle","rb") as file:
#     zombie_blue = pickle.load(file)
#     print(zombie_blue)
#     print(zombie_blue.play())

# import json
# j = json.dumps(['fpp',{'bar':('baz,None,1.0,2')}])#formats to json
# print(j)
