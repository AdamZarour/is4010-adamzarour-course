def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)






def find_user_by_name(users, name):
    user_lookup = {user['name']: user for user in users}
    return user_lookup.get(name)






def get_list_of_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]