import spacy


nlp = spacy.load("en_core_web_sm")

BANNED_WORDS = ["spam", "fake", "scam", "buy now", "click here", "free money"]

def check_guidelines():
