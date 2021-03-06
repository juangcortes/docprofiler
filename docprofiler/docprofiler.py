import os
import re

class DocCleanser:
    def clean_filext():
        pass

    def clean_filenames():
        pass


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

class DocProfiler:
    def __init__(
        self,
        path:str):

        self.dirpath = path

    def run(self):
        dm = DirManager()
        filedir = dm.read_dir(self.dirpath)
        filemap = dm.define_subdirs(filedir)
        dm.create_subdirs(filemap, self.dirpath)
