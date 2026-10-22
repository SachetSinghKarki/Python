def outer():
    print("Outer function")
    def inner():
        print("inner fun")
    # inner()
    return inner
something = outer()
something()