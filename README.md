# IncludeXLS

A markdown extension to include xls files from markdown files (pagewise).

usage in markdown:

    :::markdown
    ...
    #xls filename pagenumber
    ...


usage in python:

    :::python
    from includexls import IncludeXLS

    ...
    markdown.markdown(text, extensions=[
        ...
        IncludeXLS(path=os.path.dirname(infile)),
        ...
    ])
    ...

## Installation

    :::bash
    pip install git+https://github.com/maxdoom-com/includexls.git
