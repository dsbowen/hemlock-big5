from docstr_md.python import PySoup, compile_md
from docstr_md.src_href import Github

src_href = Github('https://github.com/dsbowen/hemlock-big5/blob/master')
soup = PySoup(
    path='hemlock_big5/__init__.py', parser='sklearn', src_href=src_href
)
compile_md(soup, compiler='sklearn', outfile='docs_md/api.md')