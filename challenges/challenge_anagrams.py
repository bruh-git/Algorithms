def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    first_string = sorted(first_string)
    second_string = sorted(second_string)
    if first_string == second_string:
        return True
    else:
        return False
