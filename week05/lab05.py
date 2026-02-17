# lab05.py

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
]


def calculate_average_age(users_list):
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users_list : list of dict
        A list where each item is a user dictionary that may contain an "age" key.

    Returns
    -------
    float
        The average of all valid integer ages. Returns 0.0 if no valid ages exist
        or if an error occurs.
    """
    try:
        total_age = 0
        count = 0

        for user in users_list:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                count += 1

        try:
            return total_age / count
        except ZeroDivisionError:
            print("error: cannot calculate average age of an empty list.")
            return 0.0

    except TypeError:
        # Handles cases like users_list being None or not iterable
        print("error: users_list must be a list of dictionaries.")
        return 0.0


def get_active_user_emails(users_list):
    """
    Get a list of emails for active users.

    A user is considered active if their "is_active" field is truthy, and an email
    is included only if the "email" field exists and is truthy.

    Parameters
    ----------
    users_list : list of dict
        A list where each item is a user dictionary that may contain "is_active"
        and "email" keys.

    Returns
    -------
    list of str
        A list of email strings for active users. Returns an empty list if no
        active emails exist or if an error occurs.
    """
    try:
        active_emails = []

        for user in users_list:
            try:
                if user.get("is_active") and user.get("email"):
                    active_emails.append(user.get("email"))
            except AttributeError:
                # Handles a bad element inside the list (e.g., not a dict)
                print("error: each user must be a dictionary.")
                continue

        return active_emails

    except TypeError:
        # Handles users_list being None or not iterable
        print("error: users_list must be a list of dictionaries.")
        return []


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
