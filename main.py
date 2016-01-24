import re
option = raw_input('enter option: ')
string = raw_input('enter string: ')
newString = ''
if option == 'rev': #reverse
  for i in range(len(string)):
    newString += string[-i-1] #Last character starts on -1
  print newString
if option == 'pl':  #pig latin
  wordPuncs = re.findall(r'(\w+)(\W*)',string)  #search for words and punctuation
  vowels = ('a','e','i','o','u')
  numbers = ('0','1','2','3','4','5','6','7','8','9')
  if wordPuncs:
    for wordPunc in wordPuncs:
      if wordPunc[0][0].lower() in vowels:
        pword = wordPunc[0] + 'yay' #pword is pig latin word
      elif wordPunc[0][0] in numbers:
        pword = wordPunc[0] + '*'  #number words need have *
      else:
        vowel = re.search('[aeiou]',wordPunc[0],re.IGNORECASE) #search for first vowel
        if vowel: vowelLoc = vowel.start()  #location of first vowel
        else: vowelLoc = 1
        pword = wordPunc[0][vowelLoc:] + wordPunc[0][:vowelLoc] + 'ay'  # 'ool'+'sch'+'ay'
      newString += (pword+wordPunc[1]+' ') #combine word, punctuation, and space
  newString = newString[:-1]  #remove last space
  print newString
        
#    'Hi, my name is Jim!'
#    'iHay, ymay amenay isay imJay!'
#    contractions may be a problem ex) that's
