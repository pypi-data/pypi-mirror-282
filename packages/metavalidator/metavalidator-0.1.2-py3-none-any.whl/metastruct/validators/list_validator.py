from metastruct.validators.item_constructor import any_from_text


def is_list_of_str(s) -> bool:
    if isinstance(s, list):
        data = s
    else:
        data = any_from_text(s)
    if isinstance(data, list):
        return all(isinstance(v, str) for v in data)
    else:
        return False
