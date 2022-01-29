import typer
from ssg.site import Site


def main(source="content", dest="dist"):

    # configuration dictionary
    config = {
        "source": source,
        "dest": dest
    }

    # create instance of Site class
    site = Site(config.source, config.dest)
    site.build()
