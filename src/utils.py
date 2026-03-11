def menu():
    options = [
        "1. List books",
        "2. Add book",
        "3. Remove book",
        "4. Borrow book",
        "5. Return book",
        "6. Add member",
        "7. Show members",
        "8. Remove member",
        "9. Exit"
    ]
    print("\n" + "=" * 40)
    print("Library Menu".center(40))
    print("=" * 40)
    for option in options:
        print(option)
    
    print("=" * 40)