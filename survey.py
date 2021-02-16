import hemlock_big5 as big5
from hemlock import Branch, Page, Label, route

@route('/survey')
def start():
    return Branch(
        big5.measure_trait('Extraversion', require=True, page=True),
        big5.measure_trait('Agreeableness', require=True, page=True),
        big5.measure_trait('Conscientiousness', require=True, page=True),
        big5.measure_trait('Neuroticism', require=True, page=True),
        big5.measure_trait('Openness', require=True, page=True),
        Page(
            Label('The end'), 
            terminal=True
        )
    )