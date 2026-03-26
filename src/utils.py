#This part is to better overview of the CLI-feature

def menu():
    options = [
        "1.  Show all books",
        "2.  Add book",
        "3.  Remove book",
        "4.  Update book",
        "5.  Search book",
        "6.  Borrow book",
        "7.  Return book",
        "8.  Show members",
        "9.  Add member",
        "10. Remove member",
        "11. Update member",
        "12. Show loan history",
        "13. Exit"
    ]
    print("\n" + "=" * 40)
    print("Library Menu".center(40))
    print("=" * 40)
    for option in options:
        print(option)
    
    print("=" * 40)