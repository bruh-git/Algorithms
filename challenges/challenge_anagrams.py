def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end)
        quick_sort(numbers, start, p - 1)
        quick_sort(numbers, p + 1, end)


def partition(numbers, start, end):
    pivot = numbers[end]
    delimiter = start - 1

    for index in range(start, end):
        if numbers[index] <= pivot:
            delimiter = delimiter + 1
            numbers[index], numbers[delimiter] = (
                numbers[delimiter],
                numbers[index],
            )

    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    quick_sort(first_string, 0, len(first_string) - 1)
    quick_sort(second_string, 0, len(second_string) - 1)
    ordered_first_string = "".join((first_string))
    ordered_second_string = "".join((second_string))

    return (
        ordered_first_string,
        ordered_second_string,
        ordered_first_string == ordered_second_string,
    )


print(is_anagram("amor", "roma"))
