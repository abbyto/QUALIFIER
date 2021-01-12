import difflib

words= ['i','have','want','a','test','like','am','cheese','coding','sleeping','sandwich','burger']

def word_check(s):
  for word in s.casefold().split():
    if word not in words:
      suggestion= difflib.get_close_matches(word, words)
      print(f'Did you mean {",".join(str(x)for x in suggestion)} instead of {word}?')


s = input('Input a string: ')
word_check(s)

# mod from python.org, https://docs.python.org/3/library/difflib.html
            
            print("lol")
