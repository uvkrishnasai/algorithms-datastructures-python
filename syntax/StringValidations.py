def string_validations():
    s = input()
    print(any(i.isalnum() for i in list(s)))
    print(any(i.isalpha() for i in list(s)))
    print(any(i.isdigit() for i in list(s)))
    print(any(i.islower() for i in list(s)))
    print(any(i.isupper() for i in list(s)))
    pass
