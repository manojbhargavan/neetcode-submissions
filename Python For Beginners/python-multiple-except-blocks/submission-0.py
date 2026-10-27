def divide_numbers(a: str, b: str) -> None:
    try:
        print(int(a) / int(b))
    except ValueError:
        print('Error: Invalid value!')
    except ZeroDivisionError:
        print('Error: Division by zero!')
    except Exception as e:
        print(f'An error occured: {e}')



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
