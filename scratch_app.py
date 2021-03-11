import eventlet
eventlet.monkey_patch()

from flask_login import current_user
from hemlock import Branch, Page, Label, create_app, route
from hemlock.tools import html_list
from hemlock_big5 import big5

@route('/survey')
def start():
    return Branch(
        big5(version='TIPI', page=True),
        Page(
            Label(compile=display_score), 
            terminal=True
        )
    )

def display_score(label):
    label.label = 'Big 5 scores:'+html_list(*[
        '{}: {}'.format(trait, score) 
        for trait, score in current_user.g['Big5'].items()
    ])

app = create_app()

if __name__ == '__main__':
    from hemlock.app import socketio
    socketio.run(app, debug=True)