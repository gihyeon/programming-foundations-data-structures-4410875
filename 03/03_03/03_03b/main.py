user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

# Change values
user_preferences["language"] = "Spanish"
user_preferences["volume_level"] = 50

# Add item
user_preferences["highlight_color"] = "Yellow"

# Delete item
del user_preferences["currency"]
removed_value = user_preferences.pop("date_format", "N/A")

print(user_preferences)
print(removed_value)
