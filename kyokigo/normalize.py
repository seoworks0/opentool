# -*- coding: utf-8 -*-
import re
import unicodedata

import nltk
from nltk.corpus import wordnet



def normalize(text):
    normalized_text = normalize_unicode(text)
    normalized_text = lower_text(normalized_text)
    normalized_text = normalize_number(normalized_text)
    return(normalized_text)


def lower_text(text):
    return text.lower()


def normalize_unicode(text, form='NFKC'):
    normalized_text = unicodedata.normalize(form, text)
    return normalized_text


def lemmatize_term(term, pos=None):
    if pos is None:
        synsets = wordnet.synsets(term)
        if not synsets:
            return term
        pos = synsets[0].pos()
        if pos == wordnet.ADJ_SAT:
            pos = wordnet.ADJ
    return nltk.WordNetLemmatizer().lemmatize(term, pos=pos)


def normalize_number(text):
    text = text.replace(".","")
    text = text.replace("0","1")
    if text.isdigit():
        zero = "0"
        return zero
    else:
        return(text)
