# Assignment 5 - Regex

![](http://imgs.xkcd.com/comics/regex_golf.png)
[http://imgs.xkcd.com/comics/regex_golf.png](http://imgs.xkcd.com/comics/regex_golf.png).

## Structure
The programs highlighter.py and my\_diff.py is located in the root
directory. To output the documentation run them with

```shell
Terminal> python highlighter.py --doc
Terminal> python my_diff.py --doc
```

The syntax file for Python is located in `python_regex_dict/python.syntax`
with the two themes located in `python_regex_dict/python.theme` and
`python_regex_dict/python2.theme`. During development I have used the
script test.py. For a short test run

```shell
Terminal> python highlighter.py python_regex_dict/python.syntax python_regex_dict/python.theme test.py
```

In the directories `java_regex_dict/` and `c_regex_dict/` there are syntax
and theme files for Java and C. For two short tests run

```shell
Terminal> python highlighter.py c_regex_dict/c.syntax c_regex_dict/c.theme test.c
Terminal> python highlighter.py java_regex_dict/java.syntax java_regex_dict/java.theme test.java
```


## Assumptions
For the syntax highlighting I have tried to color the syntax in a manner
similar to my editor (Vim). That has lead to the following assumptions:

1. If there is a comment at the start of a line, all other syntax should
   not be colored.
2. If a sentence is not complete, the syntax should still be highlighted.
   For example:

   ```Python
       for:
           if:
               pass
   ```

   Here both `for` and `if` (obviously `pass` as well) should be colored.

## Status
I have currently not managed to get assumption 1 to hold for strings.

## Peculiarities
My version of highlighter.py is not able to color the Naython-examples
correctly without setting the syntax regex to non-greedy, i.e.,

    "NNNN.*?(?:$|\n)": comment

I have been struggling a lot with negative lookbehinds not behaving the way
I've intended. This leads to some pecularities when a string is a comment
and the regex does not find the comment-pattern thus coloring trailing
syntax. Trying to replace the matching pattern to include the coloring
syntax does not improved the problem. If someone has figured this out I
would love some feedback!
