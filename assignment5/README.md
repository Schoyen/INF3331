# Assignment 5 - Regex

## Assumptions
For the syntax highlighting I have tried to color the syntax in a manner
similar to my editor (Vim). That has lead to the following assumptions:

1. If there is a comment at the start of a line, all other syntax should
   not be colored.
2. If a sentence is not complete, the syntax should still be highlighted.
   For example:

       for:
           if:
               pass

    Here both 'for' and 'if' should be colored.

## Status
I have currently not managed to get assumption 1 to hold for strings.
