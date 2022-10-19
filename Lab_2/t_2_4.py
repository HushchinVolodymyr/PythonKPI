class Files_counter:
    def __init__(self, filename):
        self.filename = filename

    def characters(self):
        count_character = 0
        file = open(self.filename, 'r')
        text = ''

        for el in file:
            text += el

        for el in text:
            count_character += 1

        return count_character

    def words(self):
        count_word = 0
        file = open(self.filename, 'r')
        text = ''

        for el in file:
            text += el

        for el in text:
            if el in " ":
                count_word += 1

        return count_word

    def sentences(self):
        count_sentances = 0
        file = open(self.filename, "r")
        text = ''

        for el in file:
            text += el
        for el in text:
            if el in ".":
                count_sentances += 1
        return count_sentances

first_file = Files_counter("Text.txt")

print(first_file.characters())
print(first_file.words())
print(first_file.sentences())