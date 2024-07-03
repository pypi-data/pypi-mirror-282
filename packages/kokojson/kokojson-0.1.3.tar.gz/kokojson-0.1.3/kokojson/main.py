import json

def load(data):
    """
    Load JSON data and return a dictionary-like object that allows safe access to keys.

    Args:
        data (str): The JSON data as a string.

    Returns:
        SafeDict: A dictionary-like object that allows safe access to keys.
    """
    json_data = json.loads(data)
    return SafeDict(json_data)

def wild_append(json_data):
    """
    Prepares a JSON-like data structure for appending.
    Ensures that all keys in the structure have list values,
    converting non-list values to single-item lists.
    
    :param json_data: The JSON-like data structure (dictionary)
    :return: The modified json_data
    """
    for key in json_data:
        if not isinstance(json_data[key], list):
            json_data[key] = [json_data[key]] if json_data[key] is not None else []
    return json_data

class SafeDict(dict):
    """
    A dictionary-like object that allows safe access to keys.

    If a key doesn't exist, it returns None instead of raising a KeyError.
    """

    def __missing__(self, key):
        """
        Called when a key is not found in the dictionary.

        Args:
            key (str): The key being accessed.

        Returns:
            None
        """
        return None

    def get(self, key, default=None):
        """
        Get the value of a key, or return a default value if the key doesn't exist.

        Args:
            key (str): The key to access.
            default (Any, optional): The default value to return if the key doesn't exist.

        Returns:
            Any: The value of the key, or the default value if the key doesn't exist.
        """
        return super().get(key, default)
