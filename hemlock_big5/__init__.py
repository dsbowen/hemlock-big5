from hemlock import Embedded, Page, Label, Select, Debug as D, Validate as V
from sqlalchemy_mutable import partial

from random import choice, shuffle

def big5(*items, item_bank=None, page=False, require=False, include_instructions=True, shuffle_items=False, record_index=False):
    def gen_question(item):
        _, label, reverse_code = item_bank[item]
        values = list(range(1, 6))
        if reverse_code:
            values.sort(reverse=True)
        random_choice = choice(values) if require else choice(values+[''])
        return Select(
            label,
            [
                '',
                ('Very inaccurate', values[0]),
                ('Moderately inaccurate', values[1]),
                ('Neither accurate nor inaccurate', values[2]),
                ('Moderately accurate', values[3]),
                ('Very accurate', values[4])
            ],
            var='Big5'+item, data_rows=-1, record_index=record_index,
            validate=V.require() if require else None,
            debug=D.click_choices(random_choice)
        )

    item_bank = _get_item_bank(item_bank)
    if not items:
        items = item_bank.keys()
    questions = [gen_question(item) for item in items]
    if shuffle_items:
        shuffle(questions)
    if include_instructions:
        questions.insert(0, Label(instructions_label))
    if page:
        return Page(
            *questions,
            name='Big5',
            timer=('Big5Time', -1),
            submit=partial(_record_score, item_bank)
        )
    return questions

def _record_score(page, item_bank):
    scores = {}
    questions = [q for q in page.questions if q.var and (q.data != '')]
    for q in questions:
        trait = item_bank[q.var[len('Big5'):]][0]
        if trait not in scores:
            scores[trait] = []
        scores[trait].append(q.data)
    page.embedded = [
        Embedded(trait, sum(score)/float(len(score)), data_rows=-1) 
        for trait, score in scores.items()
    ]

def big5_trait(trait, item_bank=None, **kwargs):
    item_bank = _get_item_bank(item_bank)
    item_bank = {key: val for key, val in item_bank.items() if val[0] == trait}
    obj = big5(item_bank=item_bank, **kwargs)
    if isinstance(obj, Page):
        obj.name = 'Big5 '+trait
        obj.timer.var = 'Big5'+trait+'Timer'
    return obj

def _get_item_bank(item_bank):
    if item_bank is None:
        return IPIP_items
    if isinstance(item_bank, str):
        assert item_bank in ('IPIP', 'brief'), "When passing item_bank as str, must be 'IPIP' or 'brief'"
        if item_bank == 'IPIP':
            return IPIP_items
        elif item_bank == 'brief':
            return brief_big5_items
    return item_bank

instructions_label = 'How accurately do the following statements describe you?'

# https://socialwork.buffalo.edu/content/dam/socialwork/home/self-care-kit/brief-big-five-personality-inventory.pdf
brief_big5_items = {
    'Reserved': (
        'Extraversion',
        'I am reserved',
        True
    ),
    'Trusting': (
        'Agreeableness',
        'I am generally trusting',
        False
    ),
    'Lazy': (
        'Conscientiousness',
        'I tend to be lazy',
        True
    ),
    'Relaxed': (
        'Neuroticism',
        'I am relaxed and handle stress well',
        True
    ),
    'Artistic': (
        'Openness',
        'I have few artistic interests',
        True
    ),
    'Outgoing': (
        'Extraversion',
        'I am outgoing and sociable',
        False
    ),
    'Judgmental': (
        'Agreeableness',
        'I tend to find fault with others',
        True
    ),
    'Thorough': (
        'Conscientiousness',
        'I do a thorough job',
        False
    ),
    'Nervous': (
        'Neuroticism',
        'I get nervous easily',
        False
    ),
    'Imaginative': (
        'Openness',
        'I have an active imagination',
        False
    )
}

# https://ipip.ori.org/new_ipip-50-item-scale.htm
IPIP_items = {
    'LifeOfParty': (
        'Extraversion', 
        'I am the life of the party', 
        False
    ),
    'ConcernForOthers': (
        'Agreeableness', 
        'I feel little concern for others', 
        True
    ),
    'Prepared': (
        'Conscientiousness',
        'I am always prepared',
        False
    ),
    'Stressed': (
        'Neuroticism',
        'I get stressed out easily',
        False
    ),
    'Vocab': (
        'Openness',
        'I have a rich vocabulary',
        False
    ),
    'Talkative': (
        'Extraversion',
        "I don't talk a lot",
        True
    ),
    'InterestedInPeople': (
        'Agreeableness',
        'I am interested in people',
        False
    ),
    'Disorganized': (
        'Conscientiousness',
        'I leave my belongings around',
        True
    ),
    'Relaxed': (
        'Neuroticism',
        'I am relaxed most of the time',
        True
    ),
    'UnderstandAbstraction': (
        'Openness',
        'I have difficulty understanding abstract ideas',
        True
    ),
    'ComfortableAroundPeople': (
        'Extraversion',
        'I feel comfortable around people',
        False
    ),
    'Insulting': (
        'Agreeableness',
        'I insult people',
        True
    ),
    'DetailOriented': (
        'Conscientiousness',
        'I pay attention to detail',
        False
    ),
    'Worry': (
        'Neuroticism',
        'I worry about things',
        False
    ),
    'VividImagination': (
        'Openness',
        'I have a vivid imagination',
        False
    ),
    'Background': (
        'Extraversion',
        'I keep in the background',
        True
    ),
    'Sympathetic': (
        'Agreeableness',
        "I sympathize with others' feelings",
        False
    ),
    'Messy': (
        'Conscientiousness',
        'I make a mess of things',
        True
    ),
    'SeldomBlue': (
        'Neuroticism',
        'I seldom feel blue',
        True
    ),
    'InterestedAbstraction': (
        'Openness',
        'I am not interested in abstract ideas',
        True
    ),
    'StartConversations': (
        'Extraversion',
        'I start conversations',
        False
    ),
    'InterestedInOthersProblems': (
        'Agreeableness',
        "I am not interested in other people's problems",
        True
    ),
    'Timely': (
        'Conscientiousness',
        'I get chores done right away',
        False
    ),
    'Disturbed': (
        'Neuroticism',
        'I am easily disturbed',
        False
    ),
    'ExcellentIdeas': (
        'Openness',
        'I have excellent ideas',
        False
    ),
    'Laconic': (
        'Extraversion',
        'I have little to say',
        True
    ),
    'SoftHeart': (
        'Agreeableness',
        'I have a soft heart',
        False
    ),
    'Forgetful': (
        'Conscientiousness',
        'I often forget to put things back in their proper place',
        True
    ),
    'Upset': (
        'Neuroticism',
        'I get upset easily',
        False
    ),
    'GoodImagination': (
        'Openness',
        "I don't have a good imagination",
        True
    ),
    'TalkToManyPeople': (
        'Extraversion',
        'I talk to a lot of different people at parties',
        False
    ),
    'InterestedInOthers': (
        'Agreeableness',
        'I am not really interested in other',
        True
    ),
    'Orderly': (
        'Conscientiousness',
        'I like order',
        False
    ),
    'Moody': (
        'Neuroticism',
        'I change my mood a lot',
        False
    ),
    'Quick': (
        'Openness',
        'I am quick to understand things',
        False
    ),
    'DrawAttention': (
        'Extraversion',
        "I don't like to draw attention to myself",
        True
    ),
    'TimeForOthers': (
        'Agreeableness',
        'I take time out for others',
        False
    ),
    'Shirk': (
        'Conscientiousness',
        'I shirk my duties',
        True
    ),
    'MoodSwings': (
        'Neuroticism',
        'I have frequent mood swings',
        False
    ),
    'DifficultWords': (
        'Openness',
        'I use difficult words',
        False
    ),
    'CenterOfAttention': (
        'Extraversion',
        "I don't mind being the center of attention",
        False
    ),
    'FeelOthersEmotions': (
        'Agreeableness',
        "I feel others' emotions",
        False
    ),
    'Schedule': (
        'Conscientiousness',
        'I follow a schedule',
        False
    ),
    'Irritable': (
        'Neuroticism',
        'I get irritated easily',
        False
    ),
    'Reflective': (
        'Openness',
        'I spend time reflecting on things',
        False
    ),
    'Quiet': (
        'Extraversion',
        'I am quiet around strangers',
        True
    ),
    'FeelAtEase': (
        'Agreeableness',
        'I make people feel at ease',
        False
    ),
    'Exacting': (
        'Conscientiousness',
        'I am exacting in my work',
        False
    ),
    'OftenBlue': (
        'Neuroticism',
        'I often feel blue',
        False
    ),
    'Creative': (
        'Openness',
        'I am full of ideas',
        False
    )
}