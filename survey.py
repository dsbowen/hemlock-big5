from hemlock import Branch, Page, Label, route
from hemlock_big5 import big5

@route('/survey')
def start():
    return Branch(
        big5(page=True),
        Page(
            Label('The end'), 
            terminal=True
        )
    )