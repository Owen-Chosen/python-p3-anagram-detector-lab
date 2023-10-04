# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, list_of_words = []):
        list_of_anagrams = []
        for current_word in list_of_words:
            num_of_iteration = 0
            list_of_words = list(current_word)
            for letter in list_of_words:
                if (letter in self.word):
                    num_of_iteration+=1
                else:
                  break  
            if(num_of_iteration == len(self.word)):
                list_of_anagrams.append(current_word)
        return list_of_anagrams
    

# ananaa = Anagram("listens")
# print(ananaa.match(['enlists', 'google', 'inlets', 'banana']))