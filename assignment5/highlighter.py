from sys import argv
from re import findall, sub, search

def highlighter(regex, color_theme, source_code):
    new_source = ''
    for line in source_code.split('\n'):
        for key in regex.keys():
            if search(r"%s" % regex[key], line):
                replacement_string = "\033[{0}m{1}\033[0m\n".format(color_theme[key], ''.join(findall("%s" % regex[key], line)))
                new_source += sub(r"%s" % regex[key], replacement_string, line)
            else:
                new_source += line + '\n'
    print (new_source)

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
    highlighter(regex, color_theme, source_code)
#    for key in regex.keys():
#        highlighter(regex[key], color_theme[key], source_code)
