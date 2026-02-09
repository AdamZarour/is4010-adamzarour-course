def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)






def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Parameters
    ----------
    users : list of dict
        A list of dictionaries, where each dictionary represents a user
        and has 'name', 'age', and 'email' keys. It is recommended to
        convert this list into a more efficient data structure for lookups.
    name : str
        The name of the user to find.

    Returns
    -------
    dict or None
        The dictionary of the found user, or None if no user is found.
    """
    if not users:
        return None
    user_lookup = {user['name']: user for user in users}
    return user_lookup.get(name)






def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    list of int
        A new list containing only the even integers from the input list.
    """
    if not numbers:
        return []
    return [num for num in numbers if isinstance(num, int) and num % 2 == 0]