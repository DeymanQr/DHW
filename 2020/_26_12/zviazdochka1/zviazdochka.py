import os


def del_files(dir_path, size_func):
    for i in os.listdir(dir_path):
        new_path = dir_path + '/' + i
        if os.path.isdir(new_path):
            del_files(new_path, size_func)
            continue
        if size_func(os.path.getsize(new_path)):
            #os.remove(dir_path+'/'+i)
            print(f'{new_path} (with size {os.path.getsize(new_path)}b) deleted')


if __name__ == '__main__':
    del_files('../zviazdochka1', lambda x: x > 100)