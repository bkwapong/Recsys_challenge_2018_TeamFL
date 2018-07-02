from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import gensim
import string
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# define training data
'''
sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
			['this', 'is', 'the', 'second', 'sentence'],
                        ['this', 'is', 'the', 'second', 'sentence'],
			['yet', 'another', 'sentence'],
			['one', 'more', 'sentence'],
			['and', 'the', 'final', 'sentence']]

'''
#sentences = open('new_file_sentence.txt', 'r', encoding='utf-8')
path = 'mpd_tracks_sorted.txt'
assert gensim.models.doc2vec.FAST_VERSION > -1

print('\nPreparing the sentences...')
#max_sentence_len = 40
with open(path) as file_:
  docs = file_.readlines()
#sentences = [[word for word in doc.lower().replace("\"","").strip().split(",")] for doc in docs]
sentences = [[word for word in doc.replace("\"","").strip().split(",")] for doc in docs]
print('Num sentences:', len(sentences))
#sentences =

# train model
#bigram_transformer = gensim.models.Phrases(sentences)
#model = Word2Vec(bigram_transformer[sentences], min_count=1, size=250, workers=8, window=4)#, batch_words=10000)
model = Word2Vec(sentences, min_count=1, size=500, workers=8, window=1)#, batch_words=10000)
#model = Word2Vec(sentences, min_count=1, size=500, workers=10, window=2)#, batch_words=10000)
model.train(sentences, total_examples=model.corpus_count, epochs=150)#model.iter)
print(model)
# summarize vocabulary
#words = list(model.wv.vocab)
#print(words)
# access vector for one word
#print(model['cody'])
# save model
model.save('model.bin')
print(model.wv.most_similar_cosmul('spotify:track:0YHUAjtMrO7zIFfdgSWELR', topn=20))
print(model.wv.most_similar_cosmul('spotify:track:4cuti7K7IqIUm5f9pcCGjh', topn=20))
print(model.wv.most_similar_cosmul('spotify:track:07RXBKfyCYIYRMLCvlGWXU', topn=20))
print(model.wv.most_similar_cosmul('spotify:track:63thx7OANplv4I4BQsanHk', topn=20))
print(model.wv.most_similar_cosmul('spotify:track:6KIKRz9eSTXdNsGUnomdtW', topn=20))
