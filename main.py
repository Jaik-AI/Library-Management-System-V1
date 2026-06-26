import os

def read_file():
    with open("books.txt","r") as f:
        return f.read()
def add_book(n,a):
    content = read_file()
    for i in content.splitlines():
        book = i.split(",")[0]
        if(n.title()==book):
            print("Book already exists.")
            return
    print("Adding book...")
    with open("books.txt","a") as f:
        f.write(f"{n.title()},{a.title()}\n")
    print("Book added.")

def view_books():
    print("Showing all books..")
    content = read_file()
    if(content==""):
        print("No record exists.")
        return
    else:
        books = content.splitlines()
        for i,book in enumerate(books,start=1):
            print(f"{i}.{book}")
        
def search_book(n):
    print("Searching book...")
    content = read_file()
    if(content==""):
        print("No record exists.")
        return
    found = False
    for i in content.splitlines():
        book,author = i.split(",")
        if(n==book):
            print(f"The book {book} is found written by {author}. ")
            found = True
            break
    if(found==False):   
        print(f"The book {n} doesn't exists in library. ")
    
def delete_book(n):
    content = read_file()
    if(content==""):
        print("No record exists.")
        return
    deleted = False
    remaining_book = []
    for i in content.splitlines():
        book,author = i.split(",")
        if(n==book):
            deleted = True
            continue
        else:
            remaining_book.append(f"{book},{author}")

    remaining_content = "\n".join(remaining_book)
    with open("books.txt","w") as f:
        f.write(remaining_content)
    if(deleted==True):
        print(f"The book {n} is deleted.")
    else:
        print(f"The book {n} doesn't exists in library. ")

def total_books():
    content = read_file()
    if(content == ""):
        print("No record exists.")
        return
    count = 0
    for i in content.splitlines():
        count += 1

    print(f"Total number of books available in library are {count}.")

if not(os.path.exists("books.txt")):
    print("No record exists.")
    with open("books.txt","a") as f:
        pass

while(True):
    try:
        o = int(input("\nOperations:\n1.Add book.\n2.View all book.\n3.Search book.\n4.Delete book.\n5.Count total books.\n6.Exit.\nSelect:"))
    except ValueError:
        print("Please select a valid option!")
        continue

    if(o==1):
        n = input("Enter name of book:")
        a = input("Enter name of author:")
        add_book(n,a)

    elif(o==2):
        view_books()

    elif(o==3):
        n = input("Enter name of book:")
        search_book(n.title())

    elif(o==4):
        n = input("Enter name of book:")
        delete_book(n.title())

    elif(o==5):
        total_books()

    elif(o==6):
        print("Goodbye...")
        exit()
    
    else:
        print("Please choose between 1 and 6")

