from typing import List, Set


def is_valid_choice(
    choice: str,
    options: Set[str]
) -> bool:
    return choice in options


def are_all_valid_choices(
    choices: List[str],
    options: Set[str]
) -> bool:
    return all(is_valid_choice(choice, options) for choice in choices)


def is_valid_choiceseq(
    choices: List[str],
    options: Set[str]
) -> bool:
    return are_all_valid_choices(choices, options)


def is_valid_charseq(
    seq: str,
    options: Set[str]
) -> bool:
    """Check a sequence of chars contains only allowed chars

    Used to validate data like this:

        `YNYNYNYNNNNNNNNNYN`
    """
    return all(char in options for char in set(seq))
