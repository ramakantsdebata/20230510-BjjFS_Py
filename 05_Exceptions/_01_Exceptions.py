def Add( a, b)-> int:
    result = None
    try:
        if a == None or b == None:
            raise ValueError("Values passed can not be 'None' type.")

        result = a + b
        return result
    except (KeyError, TypeError) as e:
        # SomeAction
        print("")
        raise

    # except TypeError as e:
    #     # Some action
    #     print("")
    # return result

def main():
    import sys
    try:
        print(Add(None, 2))
    except ValueError as e:
        # print(e.__repr__())
        print(f"{e!r}", file=sys.stderr)

main()
