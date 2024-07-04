import re
import io, os
import urllib.request
from urllib.parse import urlparse

def get_filename_from_url(url):
    return os.path.basename(urlparse(url).path)

def is_url(url):
    """
    Not to be used for actually validating a url, but in our use case we only 
    care if it's a url or a file path, and they're pretty distinguishable
    """
    parts = urlparse(url)
    return all([parts.scheme, parts.netloc, parts.path])

def fetch_image(url):
    """
    Attempts to fetch an image from a url. 
    If successful returns a bytes object, else returns None

    :return:
    """
    try:
        with urllib.request.urlopen(url) as response:
            # security flaw?
            return io.BytesIO(response.read())
    except urllib.error.URLError:
        return None

def remove_last_occurence(ls, x):
    ls.pop(len(ls) - ls[::-1].index(x) - 1)

def remove_whitespace(string, leading=False, trailing=False):
    """Remove white space from a string.

    Args:
        string(str): The string to remove white space from.
        leading(bool, optional): Remove leading new lines when True.
        trailing(bool, optional): Remove trailing new lines when False.

    Returns:
        str: The input string with new line characters removed and white space squashed.

    Examples:

        Single or multiple new line characters are replaced with space.

            >>> remove_whitespace("abc\\ndef")
            'abc def'
            >>> remove_whitespace("abc\\n\\n\\ndef")
            'abc def'

        New line characters surrounded by white space are replaced with a single space.

            >>> remove_whitespace("abc \\n \\n \\n def")
            'abc def'
            >>> remove_whitespace("abc  \\n  \\n  \\n  def")
            'abc def'

        Leading and trailing new lines are replaced with a single space.

            >>> remove_whitespace("\\nabc")
            ' abc'
            >>> remove_whitespace("  \\n  abc")
            ' abc'
            >>> remove_whitespace("abc\\n")
            'abc '
            >>> remove_whitespace("abc  \\n  ")
            'abc '

        Use ``leading=True`` to remove leading new line characters, including any surrounding
        white space:

            >>> remove_whitespace("\\nabc", leading=True)
            'abc'
            >>> remove_whitespace("  \\n  abc", leading=True)
            'abc'

        Use ``trailing=True`` to remove trailing new line characters, including any surrounding
        white space:

            >>> remove_whitespace("abc  \\n  ", trailing=True)
            'abc'
    """
    # Remove any leading new line characters along with any surrounding white space
    if leading:
        string = re.sub(r'^\s*\n+\s*', '', string)

    # Remove any trailing new line characters along with any surrounding white space
    if trailing:
        string = re.sub(r'\s*\n+\s*$', '', string)

    # Replace new line characters and absorb any surrounding space.
    string = re.sub(r'\s*\n\s*', ' ', string)
    # TODO need some way to get rid of extra spaces in e.g. text <span>   </span>  text
    return re.sub(r'\s+', ' ', string)

def delete_paragraph(paragraph):
    # https://github.com/python-openxml/python-docx/issues/33#issuecomment-77661907
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None