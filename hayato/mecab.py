# -*- coding: utf-8 -*-

from natto import MeCab

def get_noun(text):
    nouns = []
    with MeCab() as nm:
      for n in nm.parse(text.encode('utf8'), as_nodes=True):
        if not n.is_eos():
            surface = n.surface
            feature = n.feature.split(',')
            if feature[0] == "名詞":
                nouns.append({'noun': surface, 'feature_1': feature[1], 'feature_2': feature[2]})

    return nouns

def get_news_noun(text):
    nouns = []
    noun = None 
    featurea = None
    with MeCab() as nm:
      for n in nm.parse(text.encode('utf8'), as_nodes=True):
        if not n.is_eos():
            surface = n.surface
            features = n.feature.split(',')
            if features[0] == "名詞":
                if features[1] == "接尾" or features[1] == "サ変動詞" or features[1] == "数":
                    if noun:
                        noun = noun + surface
                        feature = feature + features[1]
                    else:
                        noun = surface
                        feature = features[1]
                elif features[1] == "非自立" or features[1] == "代名詞":
                    next
                else:
                    if noun:
                        nouns.append({'noun':noun, 'feature':feature})
                    noun = surface
                    feature = features[1]
            else:
                if noun:
                    nouns.append({'noun':noun, 'feature':feature})
                    noun = None
                    feature = None

    return nouns         

