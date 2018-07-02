from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import string
# define training data

#sentences = open('new_file_sentence.txt', 'r', encoding='utf-8')
path = 'challenge_dataset_tracks.txt'
#path2 = 'new_playlist1.txt'

input_texts = []
with open(path) as f:
    lines = f.read().split('\n')
#with open('mpd_tracks_sorted.txt') as p:
#with open('mpd_dataset_predict.txt') as p:
    #p_new = p.read()
    print(len(lines))
    for line in lines[: min(1000000, len(lines) - 1)]:
        input_text = line.split(',')
        '''
        if ("#spotify:track") in (input_text[0]+","):
            input_text[0] = (input_text[0][1:])
            #input_text[0].strip('#')
            input_texts.append(input_text)
            continue
        if (input_text[0]+",") not in p_new:
            print(input_text[0]+",")
            input_text[0] = "#summer"
            print(input_text)
            #input_text[0].strip('#')
        #print(input_text[0])
        input_text[0] = (input_text[0][1:])
        #print(input_text[0])
        '''
        input_texts.append(input_text)
print(input_texts)

# load model
new_model = Word2Vec.load('model.bin')
print(new_model)
#print(model.wv.most_similar(['radioactive', topn=10))
#sample1, sample2, sample3, sample4 = []



#sample1 = model.wv.most_similar('party!', topn=500)
#print(sample1[:])

output_file = open("predictions_v11_1500.txt", "w")
#output_file.write("country songs:")

for word in input_texts:
        most_similar = ', '.join('%s (%.0f)' % (similar, dist) for similar, dist in new_model.most_similar(word, topn=1500))
        print(most_similar)
        sample1 = most_similar.replace(" (1)", "")
        sample1 = sample1.replace(" (0)", "")
        #output_file.write('\n')
        output_file.write(sample1)
        output_file.write('\n')
#print(sample1)

#sample1 = most_similar.replace(" (1)", "")
#print(sample1)

#print(sample11)
'''
output_file = open("predictions.txt", "w")
output_file.write("country songs:")
output_file.write('\n')
output_file.write(sample1)
output_file.write('\n')
'''
#print(sample1)


