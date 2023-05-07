# A list of Characters that we use and have a special meaning for REGEX Design 

```

'.'   Any Character except a new line
'*'   0 or More repetitions
'+'   1 or More repetitions
'?'   0 or 1 repetition
{m}   m repetitions
{m,n} m-n repetitions
'^'   Matches the start of the string 
'$'   matches the end of the string or just before the newline at the end of the string 
[]    set of the characters 
[^]   complementing the set

```

```

    Example:

        r"^.+@.+\.edu$"

    a partial list of the patterns you can use within a regular expression : 

    \d : decimal digit 
    \D : Not a decimal digit
    \s : whitespace characters 
    \S : not a whitespace character 
    \w : word character ... as well as numbers and underscore 
    \W : not a word character 

```

```
    A|B = Either A or B
    (...) = a group
    (?:...) = non-capturing version

```

```

    Flags:
        re.IGNORECASE
        re.MULTILINE
        re.DOTALL

```