import logging
from typing import List

from trader_tweets_core.model.classified_tweet import create_classified_tweet
from trader_tweets_core.model.prompt.prompt import Prompts
from trader_tweets_core.model.twitter.simple_tweet import SimpleTweet
from trader_tweets_core.model.tweet_type import TweetType
from trader_tweets_core.prompt_factory import create_prompt_from_tweet
from trader_tweets_core.service.gpt_service import legacy_ask_gpt_for_response, BABBAGE

DEFAULT_PROMPT_TEMPLATE = Prompts.simple_openai_separator_hyphen

DEFAULT_FINETUNED_GPT_MODEL = BABBAGE
DEFAULT_BASE_GPT_MODEL = 'gpt-3.5-turbo-instruct'


def classify_tweet_types_with_gpt(tweets: List[SimpleTweet]):
    trades = []

    for tweet in tweets:
        classification = _classify_tweet_type(tweet.text, tweet.author)

        trades.append(
            create_classified_tweet(
                classification=classification,
                tweet=tweet
            )
        )

    return trades


def _classify_tweet_type(tweet_text, author=None, prompt_template=DEFAULT_PROMPT_TEMPLATE) -> TweetType:
    author_name = author.name if author is not None else None
    prompt = create_prompt_from_tweet(author_name, tweet_text, prompt_template.filename)
    logging.info('Classifying tweet type of :\t' + tweet_text)
    return classify_tweet_prompt(prompt, gpt_model=DEFAULT_FINETUNED_GPT_MODEL, max_tokens=prompt_template.max_gpt_response_tokens)


def classify_tweet_prompt(prompt: str, gpt_model=DEFAULT_BASE_GPT_MODEL, max_tokens: int = 5) -> TweetType:
    logging.debug('Querying gpt with prompt: \n' + prompt)
    response = legacy_ask_gpt_for_response(prompt, max_tokens, gpt_model)

    classification = parse_gpt_response_text(response)

    logging.debug('GPT response: \t\t' + response)

    return classification


def parse_gpt_response_text(response_text: str) -> TweetType:
    return DEFAULT_PROMPT_TEMPLATE.parser(response_text)
