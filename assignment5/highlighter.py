from sys import argv, exit
from re import findall, sub, MULTILINE, DOTALL

def highlighter(regex, color_theme, source_code):
    """Function used to replace a regex with itself but with bash-coloring wrapped around.
    Args:
        regex: A regex-pattern.
        color_theme: An ANSI escape code to color the matched regex.
        source_code: The complete source code to search for a regex match.

    Returns:
        str: The (possibly) updated source code string with color formatting.
    """
    return sub(regex, lambda hit: "\033[{0}m{1}\033[0m".format(color_theme, hit.group()), source_code, flags=MULTILINE|DOTALL)

def _read_file(filename, key, value):
    """Function used to create a dictionary from the syntax and theme files for highlighting.

    Args:
        filename: The filename of a syntax/theme-file.
        key: A regex with the pattern to search for in the file to use as key in the dictionary.
        value: A regex with the pattern to search for in the file to use as a value in the dictionary.

    Returns:
        dict: A dictionary where the key is the name of the pattern to search for in highlighter and
              where the value is either a regex or an ANSI escape code.
    """
    ret_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            ret_dict[findall(key, line)[0]] = findall(value, line)[0]
    return ret_dict

def _read_source(sourcefile):
    """Function used to read the entire source code verbatim.

    Args:
        sourcefile: The filename of the source code.

    Returns:
        str: The source code.
    """
    with open(sourcefile, 'r') as f:
        return f.read()

def highlight_source(regex_dict, color_theme_dict, source_code):
    """Function used to iterate over all the keys and values in the regex and color theme dictionaries.

    The function proceeds to call the highlighter method with a regex and a theme with a gradually more
    colored source code.

    Args:
        regex_dict: A dictionary with the name of the pattern as a key and the regex pattern as value.
        color_theme_dict: A dictionary with the name of the pattern as a key and the color theme as value.
        source_code: The entire source code as a string.

    Returns:
        str: The (possibly) colored source code.
    """

    msg = """The keys in regex_dict and color_theme dict are unequal.
Make sure the .syntax and .theme file share the same name on the regex and ANSI escape code."""
    assert sorted(regex_dict) == sorted(color_theme_dict), msg
    for key in sorted(regex_dict):
        source_code = highlighter(regex_dict[key], color_theme_dict[key], source_code)
    return source_code

if __name__ == '__main__':
    try:
        syntaxfile = argv[1]
        themefile = argv[2]
        sourcefile = argv[3]
    except IndexError:
        print("""Not enough command-line arguments.
Usage: %s <syntaxfile> <themefile> <sourcefile>""" % argv[0])
        exit(1) # EXIT_FAILURE

    regex = _read_file(syntaxfile, r": (\w+$)", r"\"(.*)\":")
    color_theme = _read_file(themefile, r"(^\w*):", r": (.*$)")
    source_code = _read_source(sourcefile)

    print (highlight_source(regex, color_theme, source_code))
