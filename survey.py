from flask_login import current_user
from hemlock import Branch, Page, Label, route
from hemlock.tools import make_list
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
    label.label = f'''
        Big 5 scores:
        
        {make_list([f'{trait}: {score}' 
                    for trait, score in current_user.g['Big5'].items()])}
        '''