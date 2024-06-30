import re


def to_snake_case(string):
    if isinstance(string, str):
        string = string.replace(" ", "_").replace("/", "_").replace(".", "_")
        string = string.replace("{", "").replace("}", "")
        string = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", string)
        string = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", string)
        string = string.replace("-", "_").lower().strip("_")
        return string


def to_camel_case(string):
    if isinstance(string, str):
        words = re.findall(r"[a-zA-Z0-9]+", string)
        is_camel_case = lambda x: bool(re.match(r"^[A-Z][a-z0-9]*([A-Z][a-z0-9]*)*$", x))  # noqa: E731
        camel_case_words = [word.capitalize() if not is_camel_case(word) else word for word in words]
        camel_case_title = "".join(camel_case_words)
        return camel_case_title
