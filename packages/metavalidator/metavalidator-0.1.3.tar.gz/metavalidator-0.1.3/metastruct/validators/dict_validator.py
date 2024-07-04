from metastruct.validators.item_constructor import any_from_text


def is_dict_of_list(raw) -> bool:
    if isinstance(raw, str):
        data = any_from_text(raw)
        if not isinstance(data, dict):
            return False
    elif isinstance(raw, dict):
        data = raw
    else:
        raise TypeError("Input must be a string or a dictionary")

    return all(isinstance(v, list) for v in data.values())
