from sys import argv
from re import findall, sub, search

def highlighter(regex, color_theme, source_code):
    return sub(regex, lambda hit: "\033[{0}m{1}\033[0m".format(color_theme, hit.group()), source_code)

def read_syntax(syntaxfile):
    regex_dict = {}
    with open(syntaxfile, 'r') as f:
        for line in f:
            regex_dict[findall(r": (\w+$)", line)[0]] = findall(r"\"(.*)\":", line)[0]
    return regex_dict

def read_theme(themefile):
    theme_dict = {}
    with open(themefile, 'r') as f:
        for line in f:
            theme_dict[findall(r"(^\w*):", line)[0]] = findall(r": (.*$)", line)[0]
    return theme_dict

def read_source(sourcefile):
    with open(sourcefile, 'r') as f:
        return f.read()

if __name__ == '__main__':
    try:
        syntaxfile = argv[1]
        themefile = argv[2]
        sourcefile = argv[3]
    except IndexError:
        raise IndexError("""Not enough command-line arguments.
Usage: %s <syntaxfile> <themefile> <sourcefile>""" % argv[0])

    regex = read_syntax(syntaxfile)
    color_theme = read_theme(themefile)
    source_code = read_source(sourcefile)
    for key in regex:
        print (highlighter(regex[key], color_theme[key], source_code))
#    with open('test.ny', 'w') as f:
#        for key in regex:
#            f.write(highlighter(regex[key], color_theme[key], source_code))
