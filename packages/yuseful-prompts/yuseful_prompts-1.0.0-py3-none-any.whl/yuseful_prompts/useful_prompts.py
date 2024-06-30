from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

current_model = "llama3"


def classify_sentiment(headline_text: str, model_name: str = current_model):
    template = """You are a stocks market professional. Your job is to label a headline with a sentiment IN ENGLISH.
    
Headlines that mention upside should be considered bullish. 
Any headline that mentions a sales decline, a drop in stock prices, a factory glut, an economic slowdown, increased selling pressure, or other negative economic indicators should be considered bearish instead of neutral. 
Only label a headline as neutral if it does not have any clear positive or negative sentiment or business implication.

You'll prefix a bullish or bearish sentiment with "very" if the headline is particularly positive or negative in its implications.
On the other hand, you'll prefix a slightly bullish or slightly bearish sentiment with "slightly" if the headline is only slightly positive or negative in its implications.

Here is the headline text you need to label, delimited by dashes:

--------------------------------------------------
{headline_text}
--------------------------------------------------

Here is the list of the possible sentiments, delimited by commas:

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
very bullish
bullish
slightly bullish
neutral
slightly bearish
bearish
very bearish
uncertain
volatile
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

You are to output ONLY ONE SENTIMENT WITH THE EXACT WORDING, from the provided list of sentiments.
DO NOT add additional content, punctuation, explanation, characters, or any formatting in your output."""
    sentiment_prompt = PromptTemplate.from_template(template)
    chain = sentiment_prompt | get_model(model_name)
    output = chain.invoke({"headline_text": headline_text})
    return output.content.strip().lower()


def get_model(model_name: str = current_model):
    return ChatOllama(model=model_name)
