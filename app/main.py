import spacy
import verb
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords

nltk.data.path.append('./nltk_models')

# Load WordNet
wordnet.ensure_loaded()
# Load stopwords
stop_words = stopwords.words('english')
#retrieve synonym for root word
def get_synonym(root):

    listofsyns = wordnet.synsets(root[0])
    synonym = ""
    for syn in listofsyns:
        if syn.name().split(".")[1] == 'v' and syn.name().split(".")[0] != root[0]:
            synonym = syn.name().split(".")[0]
            break
    if synonym == "":
        raise Exception("No synonym found for root word")
    print("Synset: ", listofsyns)
    print("Synonym: ", synonym)
    # synonym = listofsyns[3].name().split(".")[0]
    if root[1] =='VBD':
        synonym = verb.verb_past(synonym)
    elif root[1] =='VBG':
        synonym = verb.verb_present_participle(synonym)
    elif root[1] =='VBN':
        synonym = verb.verb_past_participle(synonym)
    elif root[1] =='VBP':
        synonym = verb.verb_present(synonym, person=3, negate=True)
    elif root[1] =='VBZ':
        synonym = verb.verb_present(synonym, person=3, negate=False)
    print("Synonym final form: ", synonym)
    return synonym
def get_paraphrase(input_str,verbs):
    list_str = input_str.split()
    stop = set(stopwords.words('english'))
    paraphrase = []
    for word in list_str:
        try:
            if word in verbs.keys() and word.lower() not in stop:
                paraphrase.append(get_synonym([word,verbs[word]]))
            else:
                paraphrase.append(word)
        except Exception:
            paraphrase.append(word)
    paraphrased_str = " ".join(paraphrase)
    return paraphrased_str
def get_root(input_str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_str)
    root = None
    for token in doc:
        if token.dep_ == "ROOT":
            root = [token.text, token.tag_]
    return root
def get_verbs(input_str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_str)
    verbs = {}
    for token in doc:
        if token.pos_ == "VERB":
            verbs[token.text] = token.tag_
    print("Verbs: ", verbs)
    return verbs


input_str = "This company will eventually find a way of conquering that startup."
result = get_paraphrase(input_str,get_verbs(input_str))
print(result)
