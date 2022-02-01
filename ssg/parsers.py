from typing import List
from pathlib import Path
from shutil import copy2


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with open(path) as file:
            return file

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        copy2(path, self.dest / path.relative_to(self.source))


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parser(self, path: Path, source: Path, dest: Path):
        self.copy(path,source, dest)