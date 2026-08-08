
def match_case_example():
    day = int(input("Enter a number (1-7): "))

    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case _: # That is the default case
            return "Weekend"

print(match_case_example())