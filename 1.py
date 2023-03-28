def validate(username, password):
    half = len(max((username, password), key=len)) // 2
    print(half)

    def f1():
        return ((username, password[:half]), (username, password[half:]))

    def f2():
        return ((password, username[:half]), (password, username[half:]))

    print(f1(), f2())
    return not any((f1(), f2()))



print(validate("username", "myname"))
print(validate("sword", "password"))
print(validate("MASH", "M*A*S*H"))
