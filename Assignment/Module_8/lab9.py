def test():
    try:
        print("hello"+123)
        return 10
    except Exception as e:
        print(e)
        return 0
    finally:
        print("function ended")

test()