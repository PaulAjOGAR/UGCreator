import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

BANNED_WORDS = ["spam", "fake", "scam", "buy now", "click here", "free money"]


def check_guidelines(text: str):
    # Fail if too short
    if len(text.split()) < 10:
        return 0.0, False

    # Fail if banned words
    for word in BANNED_WORDS:
        if word in text.lower():
            return 0.1, False

    # Score calculation
    doc = nlp(text)
    word_count = len(text.split())
    sentence_count = len(list(doc.sents))
    has_nouns = any(token.pos_ == "NOUN" for token in doc)
    has_verbs = any(token.pos_ == "VERB" for token in doc)
    blob = TextBlob(text)
    sentiment = abs(blob.sentiment.polarity)

    score = (
            min(word_count / 100, 0.4) +
            min(sentence_count / 5, 0.2) +
            (0.2 if has_nouns and has_verbs else 0) +
            min(sentiment * 0.2, 0.2)
    )

    return round(score, 2), score > 0.3