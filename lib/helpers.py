class CookieHelper:
    separator = ":"

    def __init__(self):
        pass

    def to_list(self, value_string):
        return value_string.split(self.separator)

    def to_string(self, value_list):
        return self.separator.join(map(str, value_list))

    def add(self, current_value, new_value):
        if type(current_value) is str:
            current_value = self.to_list(current_value)
        current_value.append(new_value)
        return self.to_string(current_value)

    def remove(self, current_value, item_to_remove):
        if type(current_value) is str:
            current_value = self.to_list(current_value)
        try:
            current_value.remove(item_to_remove)
        except ValueError:
            print(item_to_remove + " not in list")
        return self.to_string(current_value)
