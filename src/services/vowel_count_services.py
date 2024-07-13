class VowelCountServices:
    """Counts the number of vowels in a given string"""

    @staticmethod
    def vowel_count(words=dict) -> dict:
        """Counts the number of vowels in a given string"""
        response = dict()
        vowels = set('aeiouAEIOU')
        for word in words:
            counter = 0
            for i in range(len(word)):
                if word[i] in vowels:
                    counter += 1
                    response[word] = counter
        return response
