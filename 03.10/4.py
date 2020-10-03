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
        memory_capacity_units = ['b', 'kb', 'mb', 'gb', 'tb']
        size_unit = 'b'
        size = len(''.join(self.file.readlines()).encode('utf-8'))
        while size // 1024 > 0:
            try:
                size_unit = memory_capacity_units[memory_capacity_units.index(size_unit)+1]
                size //= 1024
            except IndexError:
                break
        return size, size_unit

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
print(kek.get_file_size())