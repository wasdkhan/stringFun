import re
option = raw_input('enter option: ')
string = raw_input('enter string: ')
def rev(string):  #reverse
  newString = ''
  for i in range(len(string)):
    newString += string[-i-1] #Last character starts on -1
  return newString
if option == 'rev': print rev(string)
if option == 'pal': #palindrome
  newString = string.lower()
  print newString == rev(string.lower())
if option == 'wc': #wordcount
  words = re.findall(r'[\w\']+',string)
  print len(words)
if option == 'vow': #vowels
  vowelCount = {'a':0,'e':0,'i':0,'o':0,'u':0} #vowel count dict
  for letter in string: #iterate through letters
    for vowel in vowelCount.keys(): #iterate through vowels
      if letter.lower() == vowel: 
        vowelCount[vowel] +=1 #add one when hit
        break #stop when same
  for vowel,count in vowelCount.items():
    print vowel, '>', count,  #print vowel along with count  
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
