def get_initials(my_name):
    name_list = my_name.split(" ")
    init = ""
    for name in name_list:
        init += name[0]
    return init.upper()

def main():
    my_name = input("What is your full name?")
    print(get_initials(my_name))


if __name__ == "__main__":
    main()