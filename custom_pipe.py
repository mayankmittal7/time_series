import spacy

text = "this is a sentence...hello...and another sentence."

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
print("Before:", [sent.text for sent in doc.sents])
for token in doc:
    print(token,token.i)
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        print(token, token.i)
        if token.text == "...":

            doc[token.i+1].is_sent_start = True
    return doc

nlp.add_pipe(set_custom_boundaries, before="parser")
doc = nlp(text)
print("After:", [sent.text for sent in doc.sents])