user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None,
}

# Dictionary comprehenshion
def update_preferences(user_pref):
    return {key: value for key, value in user_pref.items() if value is not None}

"""
def update_preferences(user_pref):
    updated_preferences = {}
    for key, value in user_pref.items():
        if value is not None:
            updated_preferences[key] = value
    return updated_preferences
"""

print(update_preferences(user_preferences))
