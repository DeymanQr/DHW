from typing import Generator, Optional


def generator_factory(files: list) -> Generator[str, Optional[int], None]:
    if len(files) < 2:
        return 
    line = 1
    file = 1
    while True:
        with open(files[file-1], 'r', encoding='UTF-8') as f:
            for j, i in enumerate(f):
                if j + 1 == line:
                    data = yield f"{file}: {i.strip()}"
                    break
            else:
                return
        if isinstance(data, int) and data < len(files) + 1:
            file = data
        line += 1


gen = generator_factory(['one.txt', 'two.txt'])
print(next(gen))
print(gen.send(2))
print(next(gen))
print(next(gen))
print(next(gen))
print(gen.send(1))
print(next(gen))
print(next(gen))