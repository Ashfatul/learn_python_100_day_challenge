# dictionary

user = {
    "name": "User",
    "age": 27,
}

print(user["name"])


nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

nested_dictionary = {
    "name": "test",
    "nested": {
        "nested_item": "nested_value"
    }
}

print(nested_dictionary["nested"]["nested_item"])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Barlin", "Hamburg", "Stuttgart"],
        "total_visits": 99
    }
}

print(travel_log["Germany"]["cities_visited"][2])