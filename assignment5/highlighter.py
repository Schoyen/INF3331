from sys import argv
from re import findall, sub, MULTILINE

def highlighter(regex, color_theme, source_code):
    return sub(regex, lambda hit: "\033[{0}m{1}\033[0m".format(color_theme, hit.group()), source_code, flags=MULTILINE)

def _read_syntax(syntaxfile):
    regex_dict = {}
    with open(syntaxfile, 'r') as f:
        for line in f:
            regex_dict[findall(r": (\w+$)", line)[0]] = findall(r"\"(.*)\":", line)[0]
    return regex_dict

def _read_theme(themefile):
    theme_dict = {}
    with open(themefile, 'r') as f:
        for line in f:
            theme_dict[findall(r"(^\w*):", line)[0]] = findall(r": (.*$)", line)[0]
    return theme_dict

def _read_source(sourcefile):
    with open(sourcefile, 'r') as f:
        return f.read()

def _sort_dictonary(dictionary):
    """Create a list with sorted keys to make sure coloring is done in the right order.

    This function filters on *_n where n is a number from 1 and rising. The number only
    counts for regexes with the same name and differing number. A *_0 means that this
    regex will occur last. If there are no numbers this regex pattern will occur randomly.
    """
    sorted_list = []
    for key in dictionary:
        sorted_list.append(key)
    return sorted(sorted_list)

def highlight_source(regex_dict, color_theme_dict, source_code):
    sorted_keys = _sort_dictonary(regex_dict)
    for key in sorted_keys:
        source_code = highlighter(regex_dict[key], color_theme_dict[key], source_code)
    return source_code

if __name__ == '__main__':
    try:
        syntaxfile = argv[1]
        themefile = argv[2]
        sourcefile = argv[3]
    except IndexError:
        raise IndexError("""Not enough command-line arguments.
Usage: %s <syntaxfile> <themefile> <sourcefile>""" % argv[0])

    regex = _read_syntax(syntaxfile)
    color_theme = _read_theme(themefile)
    source_code = _read_source(sourcefile)

    print (highlight_source(regex, color_theme, source_code))

#    syntax_text = {}
#    for key in regex:
#        syntax_text[key] = highlighter(regex[key], color_theme[key], source_code)
#    print (syntax_text['def_function'])
#    print (syntax_text['function_text'])
