from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import string
import fnmatch
# define training data

#sentences = open('new_file_sentence.txt', 'r', encoding='utf-8')
path = 'predictions_v11_1500_clean.txt'

output_file = open("predictions_v11_500.txt", "w")

input_texts = ()
with open(path) as f:
    lines = f.read().split('\n')
for line in lines[: min(1000000, len(lines) - 1)]:
    line = line.replace(' ','').split(',')
    str = ''
    #print(line)
    #x = 'spotify*'
    for i in range(500):
        if 'spotify:track:' in line[i]:
            str += line[i]
            str += ','
            print(line[i])
    output_file.write(str)
    output_file.write('\n')
    #y = not (fnmatch.filter(line, x))
   # print(y)
        #print(line[i])
    #print(line)
    #print(x for x in line if 'spotify' in x)
    #if "spotify" not in line:
     #   print(line)
       # line=line[i].replace(line[i], '')
        #print(line)
    #input_texts.append(line)
    #output_file.write(input_texts)
    #output_file.write('\n')

#import fnmatch
#l = ['RT07010534.txt', 'RT07010533.txt', 'RT02010534.txt']
#pattern = 'RT0701*.txt'
#matching = fnmatch.filter(l, pattern)
#print(matching)
#print(sample1)


