# Assignment 5 - Regex

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
3. In choosing C as one of my other languages to color, the highlighting
   in Vim is rather boring. All the control-flow statements are colored
   the same way, and currently I have copied that solution.

## Status
I have currently not managed to get assumption 1 to hold for strings.
