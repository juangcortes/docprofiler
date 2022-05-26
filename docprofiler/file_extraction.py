import os
import re

class DirManager:
    def read_dir(path:str):
        return os.listdir(filedir).sorted()

    def define_subdirs(filedir:str):
        dc = DocCleanser()
        unique_files = set(map(dc.clean_filext, filedir))
        clean_subdirs = [*map(dc.clean_filenames, unique_files)] 
        _ = zip(clean_subirs, unique_files)
        return {j:[re.search(k)] for j, k in _}

    def create_subdirs(filemap:dict, path:str):
        pass
