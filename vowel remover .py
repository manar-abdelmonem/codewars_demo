# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
 # Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata
  # result :
     def shortcut( s ):
    vowel =['a','e' ,'o','u' ,'i']
    result =[]
    for letter  in s :
        if letter not in vowel:
            result . append (letter)
    return "" . join (result)
