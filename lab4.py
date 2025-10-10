def convertToBase(num, base):
    convertedNum = ""
    if num == 0:
        return ""
    else:
        quotient, remainder = divmod(num, base)
        return convertToBase(quotient, base) + str(remainder)


def validInput(values_to_sort, base):
    if values_to_sort is None:
        raise ValueError("invalid_arguments")
    elif values_to_sort == []:
        raise ValueError("invalid_arguments")
    elif base <= 2:
        raise ValueError("invalid_arguments")


def radix_base(values_to_sort, base):
    if validInput(values_to_sort, base):
        try:
            # Radix sort logic here
        except:
            raise ValueError("invalid_list_element")
