def menu():
    options = [
        "1.  List books",
        "2.  Add book",
        "3.  Remove book",
        "4.  Update book",
        "5.  Borrow book",
        "6.  Return book",
        "7.  Show members",
        "8.  Add member",
        "9.  Remove member",
        "10. Update member",
        "11. Exit"
    ]
    print("\n" + "=" * 40)
    print("Library Menu".center(40))
    print("=" * 40)
    for option in options:
        print(option)
    
    print("=" * 40)