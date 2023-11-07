user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

# print(list(user_preferences.items()))

def update_preferences(user_pref):
    for key, value in list(user_pref.items()):
        if value is None:
            del user_preferences[key]
    updated_user_pref = user_pref
    return updated_user_pref

print(update_preferences(user_preferences))
