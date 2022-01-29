from pathlib import Path


class Site:
    def __init__(self, source, dest):
        # instantiate Path class with source and dest
        self.source = Path(source)
        self.dest = Path(dest)


def create_dir(self, path):
    directory = self.dest / path.relative_to(self.source)
    directory.mkdir(parents=True, exists_ok=True)


def build(self):
    self.dest.mkdir(parents=True, exists_ok=True)
    for path in self.source.rglob("*"):

        # test if the current path is a dir
        if path.is_dir():
            create_dir(path)

