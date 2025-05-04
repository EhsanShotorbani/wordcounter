class FileProcessor:
    def __init__(self, input_file, word_to_find):
        self.input_file = input_file
        self.word_to_find = word_to_find
        self.output_file = "output.txt"
        self.word_list = {}

    def process_files(self):
        try:
            with open(self.input_file, 'r') as my_input_file:
                for line in my_input_file:
                    word_list = line.lower().split()
                    for word in word_list:
                        clean_word = word.strip('.,!?:;\"\'')
                        if clean_word:
                            self.word_list[clean_word] = self.word_list.get(clean_word, 0) + 1

            word_count = self.word_list.get(self.word_to_find.lower(), 0)

            with open(self.output_file, 'w') as my_output_file:
                my_output_file.write("Word Counts:\n")

                for word, count in sorted(self.word_list.items()):
                    my_output_file.write(f"{word}: {count}\n")

            print(f"There is '{word_count}' '{self.word_to_find}'  in '{self.input_file}'.")

        except FileNotFoundError:
            # If the input file is not found, tell the user
            print(f"Error: The file '{self.input_file}' was not found.")
        except Exception as e:
            # If something else goes wrong, show the error
            print(f"An error occurred: {e}")

x = FileProcessor("data.txt", "hello")
x.process_files()