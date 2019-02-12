import spacy 
nlp = spacy.load('en')

probs = {w.orth: w.prob for w in nlp.vocab}
usually_titled = [w for w in nlp.vocab if w.is_title and probs.get(nlp.vocab[w.orth].lower, -10000) < probs.get(w.orth, -10000)]

for lex in usually_titled:
   lower = nlp.vocab[lex.lower]
   lower.shape = lex.shape
   lower.is_title = lex.is_title
   lower.cluster = lex.cluster
   lower.is_lower = lex.is_lower

def get_ner(utterance):
    doc = nlp(utterance.decode('utf_8'))
    locations = []
    time = []
    print doc.ents
    for e in doc.ents:
        print e.label_
        if e.label_ == 'GPE':
            locations.append(e.text.encode('utf_8'))    
        elif e.label_ == 'DATE' or e.label_ == 'TIME':
            time.append(e.text.encode('utf_8'))
    print locations
    print time

if __name__ == '__main__':
    get_ner('hey! what is the weather like in berlin tomorrow ?')
    get_ner('berlin new delhi today and tomorrow')
    get_ner('berlin new delhi today tomorrow')

