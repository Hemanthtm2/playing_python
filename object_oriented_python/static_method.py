#!/usr/bin/python


class String:
    
      @staticmethod
      def is_palindrome(s,case_insensitive=True):
          s= ' '.join(c for c in s if s.isalnum())
          if case_insensitive:
             s=s.lower()
          for c in range(len(s)):
              if s[c] !=s[-c -1]:

                 return False
          return True
      
      @staticmethod
      def get_unique_words(sentence):
          return set(sentence.split())

print(String.is_palindrome('Radar',case_insensitive=False))
