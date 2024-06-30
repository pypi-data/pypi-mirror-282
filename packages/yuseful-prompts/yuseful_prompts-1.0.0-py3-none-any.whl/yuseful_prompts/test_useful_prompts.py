import pytest

from .useful_prompts import classify_sentiment

@pytest.mark.parametrize("headline_input,expected", [
    (
            {
                'headline_text': ('Asure Partners with Key Benefit Administrators',
                                  'to Offer Proactive Health Management Plan (PHMP) to Clients')},
            {'possible_sentiments': ['bullish', 'neutral', 'slightly bullish', 'very bullish']}
    ),
    (
            {
                'headline_text': ('Everbridge Cancels Fourth Quarter',
                                  'and Full Year 2023 Financial Results Conference Call')},
            {'possible_sentiments': ['bearish', 'neutral', 'slightly bearish', 'uncertain', 'very bearish']}
    ),
    (
            {
                'headline_text': ("This Analyst With 87% Accuracy Rate Sees Around 12% Upside In Masco -",
                                  "Here Are 5 Stock Picks For Last Week From Wall Street's Most Accurate Analysts "
                                  "- Masco (NYSE:MAS)")},
            {'possible_sentiments': ['bullish', 'slightly bullish', 'very bullish']}
    ),
    (
            {'headline_text': 'Tesla leads 11% annual drop in EV prices as demand slowdown continues'},
            {'possible_sentiments': ['bearish', 'slightly bearish', 'very bearish']}
    ),
    (
            {'headline_text': "Elon Musk Dispatches Tesla's 'Fireman' to China Amid Slowing Sales"},
            {'possible_sentiments': ['bearish', 'slightly bearish']}
    ),
    (
            {'headline_text': "OpenAI co-founder Ilya Sutskever says he will leave the startup"},
            {'possible_sentiments': ['bearish', 'neutral', 'slightly bearish', 'uncertain']}
    ),
    (
            {'headline_text': "Hedge funds cut stakes in Magnificent Seven to invest in broader AI boom"},
            {'possible_sentiments': ['bearish', 'bullish', 'neutral', 'slightly bearish', 'slightly bullish']} # the "broader AI boom" part can be seen as bullish
    )
])
def test_classify_sentiment(headline_input, expected):
    assert classify_sentiment(**headline_input) in expected['possible_sentiments']
