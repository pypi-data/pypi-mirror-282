from typing import Dict, Any, List, Union
from .utils import add_prefix, convert_dict_of_lists_to_list_of_dicts, cut_end_lines
from .__init__implementation import _RemoveLines
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)


def format_insert(
    # Text to convert.
    text: str,
    # Custom open bracket.
    open: str = r"\[",
    # Custom close bracket.
    close: str = r"\]",
    # Wrap values with str(value).
    # Otherwise, values such as 1, None, True and non-string values will cause an error.
    safe: bool = True,
    # Target name & new text pairs.
    # Pass it like
    # 'format_insert(..., kwarg1='value1', kwarg2='value2')' or
    # 'format_insert(..., **dictionary)'
    **kwargs: Dict[str, str],
):
    """
    String format function with custom brackets.

    Parameters
    ----------
    text: str,
        Text to convert.
    open: str = r"\[",
        Custom open bracket.
    close: str = r"\]",
        Custom close bracket.
    **kwargs
        Target name & new text pairs.
        Pass it like
        'format_insert(..., kwarg1='value1', kwarg2='value2')' or
        'format_insert(..., **dictionary)'
    """
    for key, value in kwargs.items():
        if safe:
            value = _convert_to_str(value)

        pattern = open + key + close
        text = text.replace(pattern, value)

    return text


def format_indent(
    # Text to convert.
    text: str,
    # Custom open bracket.
    open: str = r"\{",
    # Custom close bracket.
    close: str = r"\}",
    # Wrap values with str(value).
    # Otherwise, values such as 1, None, True and non-string values will cause an error.
    safe: bool = True,
    # Target name & new text pairs.
    # Pass it like
    # 'format_insert(..., kwarg1='value1', kwarg2='value2')' or
    # 'format_insert(..., **dictionary)'
    **kwargs: Dict[str, str],
):
    """
    String format function with custom brackets.
    The line with the target pattern can't have other letter than the pattern.

    Parameters
    ----------
    text: str,
        Text to convert.
    open: str = r"\{",
        Custom open bracket.
    close: str = r"\}",
        Custom close bracket.
    **kwargs,
        Target name & new text pairs.
        Pass it like
        'format_insert(..., kwarg1='value1', kwarg2='value2')' or
        'format_insert(..., **dictionary)'
    """
    for key, value in kwargs.items():
        if safe:
            value = _convert_to_str(value)
        text = _format_indent_single(text, key, value, open, close)

    return text


def format_insert_loop(
    template: str,
    kwargs: Union[Dict[str, List[str]], Dict[str, List[str]]],
    open: str = r"\\[",
    close: str = r"\\]",
    safe: bool = True,
    cut_ends: bool = False,
):
    parsers = [_format_insert_loop_many, _format_insert_loop_list]
    errors = []

    for parser in parsers:
        try:
            return parser(template, kwargs, open, close, safe, cut_ends)
        except Exception as e:
            errors.append(f"{parser.__name__} error: {e}")
            continue

    raise ValueError(
        "Both format_insert_loop_many and format_insert_loop_legacy failed with errors: " + "; ".join(errors)
    )


def remove_lines(template: str, open: str = r"\(", close: str = r"\)") -> str:
    """Remove Lines based on the remove_keywords in brackets .

    It removes lines below r"\(remove_above:1\)" or above r"\(remove_above:1\)".
    The keywords blocks will be removed as well.

    Args:
        template (str): Template including keywords, such as r"\(remove_above:1\)" or r"\(remove_below:1\)"
        open (str, optional): open bracket. Defaults to r"\(".
        close (str, optional): close bracket. Defaults to r"\)".

    Returns:
        str: _description_
    """
    return _RemoveLines.remove_lines(template, open, close)


def _format_insert_loop_many(
    template: str,
    kwargs_many: Dict[str, List[str]],
    open: str = r"\\[",
    close: str = r"\\]",
    safe: bool = True,
    cut_ends: bool = False,
):
    kwargs_list = convert_dict_of_lists_to_list_of_dicts(kwargs_many)

    return _format_insert_loop_list(template, kwargs_list, open, close, safe, cut_ends)


def _format_insert_loop_list(
    template: str,
    kwargs_list: List[Dict[str, str]],
    open: str = r"\\[",
    close: str = r"\\]",
    safe: bool = True,
    cut_ends: bool = False,
):
    formatted_lines = []

    for kwargs in kwargs_list:
        formatted = format_insert(template, open, close, safe, **kwargs)
        formatted_lines.append(formatted)
    formatted = "".join(formatted_lines)

    if cut_ends:
        formatted = cut_end_lines(formatted)

    return formatted


def _convert_to_str(value: Any):
    return str(value)


def _format_indent_single(
    text: str,
    key: str,
    value: str,
    open: str = r"\{",
    close: str = r"\}",
):
    pattern = open + key + close
    new_lines = []
    for line in text.split("\n"):
        if line.find(pattern) != -1:
            _check_indent_line(line, pattern)
            indent = line[: line.find(pattern)]
            new_lines.append(add_prefix(value, indent))
        else:
            new_lines.append(line)

    return "\n".join(new_lines)


def _check_indent_line(text: str, pattern: str):
    remaining_text = text.replace(pattern, "").strip()

    if remaining_text:
        raise ValueError(f"The line contains characters other than '{pattern}'")

    return True
