import logging

from trader_tweets_core.model.tweet_stance import TweetStance

from trader_tweets_core.service.gpt_service import ask_gpt_for_response
from trader_tweets_core.strategy.response_parsers import parse_stance_response


def classify_tweet_stance(tweet_text) -> TweetStance:
    logging.info('Classifying tweet for stance:\t' + tweet_text)

    messages = [
        {
            "role": "system",
            "content": [
                {
                    "text": "You are to read tweets and determine whether they are more bearish, bullish, or neutral. "
                            "The tweets will be from crypto twitter accounts and sometimes they'll be sharing their "
                            "view on the market or a trade.\n\n\"Bullish\" when the tweet leans bullish / positive, "
                            "is about buying / going long\n\"Bearish\" when the tweet leans bearish / negative, "
                            "is about selling / going short\nOtherwise neutral.",
                    "type": "text"
                },
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": tweet_text
                }
            ]
        },
    ];

    response = ask_gpt_for_response(messages, 5, 'gpt-3.5-turbo')
    logging.debug('GPT response: \t\t' + response)

    return parse_stance_response(response)
