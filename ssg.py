import typer
from ssg.site import Site


def main(source="content", dest="dist"):

    # configuration dictionary
    config = {
        "source": source,
        "dest": dest
    }

    # Unpack dictionary with **
    Site(**config).build()


typer.run(main)
