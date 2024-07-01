import logging

from trader_tweets_core.model.tweet_mood import TweetMood

from trader_tweets_core.service.gpt_service import ask_gpt_for_response
from trader_tweets_core.strategy.response_parsers import parse_mood_response


def classify_tweet_mood(tweet_text) -> TweetMood:
    logging.info('Classifying tweet for mood:\t' + tweet_text)

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

    classification = parse_mood_response(response)

    logging.debug('GPT response: \t\t' + response)

    return classification
