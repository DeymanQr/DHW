class FileMaker:
    def __init__(self, name: str, expansion: str):
        self.file_path = f"{name}.{expansion}"
        self.file = open(self.file_path, "r+", encoding='UTF-8')

    def close_file(self):
        self.file.close()

    def get_unic_elements(self):
        self.file.seek(0)
        return len(set(''.join(self.file.readlines())))

    def get_file_size(self):
        size = len(self.file.read().encode("UTF-8"))
        while size / 1024 > 0:
            size = size / 1024
            lol = "kb"
        return size

    def add_text_to_start(self, text):
        self.file.seek(0)
        file_text = self.file.readlines()
        file_text.insert(0, text)
        self.file.seek(0)
        self.file.write(''.join(file_text))

    def add_text_to_end(self, text):
        self.file.seek(0, 2)
        self.file.write(text)



kek = FileMaker('kek', 'html')
print(kek.get_unic_elements())
kek.close_file()