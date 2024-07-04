from datetime import datetime


def calculate_le(first_date: datetime, birthday: datetime):
    '''Takes two datetime objects and returns the love equinox associated with them.'''
    if first_date < birthday:
        return None

    diff = birthday - first_date
    equinox = first_date - diff

    return equinox

def print_le(first_date: datetime, birthday: datetime):
    '''Takes two datetime objects and prints the love equinox associated with them.'''
    if first_date < birthday:
        print("Unable to complete request. First date earlier than birth day.")
        return

    diff = birthday - first_date
    equinox = first_date - diff

    print(f"Your love equinox is {equinox.strftime("%m/%d/%Y")}")


print(print_le(5, 6))