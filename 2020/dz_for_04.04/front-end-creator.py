# def create_el(teg="", place="body", file=""):
#    pass

class HTMLDOK:
    def __init__(self, file=""):
        self.file = file

    def create_scelet(self):
        """creates scelet of HTML document"""
        with open(self.file, "w", encoding="UTF-8") as f:
            f.write(
                "<!DOCTYPE html><html><head><meta charset='utf-8'></head><body></body></html>")

    def place_of_word(self, word="", string=""):
        """finds id(s) of first letter of string"""
        answ = []
        for i in range(len(string)):
            if string[i:i+len(word)] == word:
                answ.append(i)
        if len(answ) == 0:
            raise ValueError(f"no such word as '{word}'.")
        if len(answ) == 1:
            return answ[0]
        return answ

    def done(self):
        """make file pretty to read"""
        with open(self.file, "r", encoding="UTF-8") as f:
            info = f.read().strip()
        if len(info) == 0:
            raise ValueError("this file is empty")
        end_file = [""]
        info = info[15:]
        for i in info:
            end_file[-1] += i
            if i == ">":
                end_file.append("")
        end_file.pop(-1)
        #print(end_file)
        tabs = 0
        for i in range(len(end_file)):
            end_file[i] = "\t" * tabs + end_file[i]
            if end_file[i][0] + "/" + end_file[i][1:] in end_file:
                if end_file.index(end_file[i][0] + "/" + end_file[i][1:]) != i + 1:
                    tabs += 1
            if "/" in end_file[i]:
                tabs -= 1
        with open(self.file, "w", encoding="UTF-8") as f:
            for i in end_file:
                f.write(i + "\n")


dok = HTMLDOK(file="kek.html")
dok.create_scelet()
dok.done()