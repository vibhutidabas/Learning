import turicreate
import matplotlib.pyplot as plt
import numpy as np

wiki = turicreate.SFrame('/home/kali/ML material/people_wiki.sframe(assign1)(week2)(candr)/m_cf05efad0f89a530.frame_idx')

# adding a word count vector
wiki['word_count'] = turicreate.text_analytics.count_words(wiki['text'])

# find nearest neighbor by euclidean method
model = turicreate.nearest_neighbors.create(wiki, label='name', features=['word_count'], method='brute_force', distance='euclidean')
# print(model.query(wiki[wiki['name'] == 'Barack Obama'], label='name', k=10))

# makes a table with most frequent words in the given person's wikipedia page
def top_words(name):
    row = wiki[wiki['name'] == name]
    word_count_table = row[['word_count']].stack('word_count', new_column_name=['word', 'count'])
    return word_count_table.sort('count', ascending=False)

# makes a table for obama
obama_words = top_words('Barack Obama')
# print(obama_words)
barrio_words = top_words('Francisco Barrio')
# print(barrio_words)

# finds the frequency of words after combining tables
combined_words = obama_words.join(barrio_words, on='word')
combined_words = combined_words.rename({'count': 'Obama', 'count.1': 'Barrio'})
combined_words = combined_words.sort('Obama', ascending=False)
# print(combined_words)

k = []
for l in range(5):
    k.append(combined_words['word'][l])
    l+=1

common_words = {}
for i in range(5):
    common_words[k[i]] = combined_words['Obama'][i]
    i+=1

# common_words = set(common_words)
# print(common_words)
z = set(common_words.keys())
# print(z.issubset(common_words))

# checks if the set of words is present in the set of wiki and finds the article with common set
def has_top_words(word_count_vector):
    t = set(word_count_vector.keys())
    return z.issubset(t)

# print('output from you func:', has_top_words(wiki[33]['word_count']))
# print('correct output: false')
# print('also check the length of unique_words')
print(len(wiki[33]['word_count']))

########-------END OF NORMAL CODE---------############





#######-------TFIDF STARTS HERE-----------##########

wiki['tf_idf'] = turicreate.text_analytics.tf_idf(wiki['word_count'])
model_tf_idf = turicreate.nearest_neighbors.create(wiki, label='name', features=['tf_idf'], method='brute_force', distance='euclidean')
# print(model_tf_idf.query(wiki[wiki['name'] == 'Barack Obama'], label='name', k=10))

def top_words_tf_idf(name):
    row = wiki[wiki['name'] == name]
    word_count_table = row[['tf_idf']].stack('tf_idf', new_column_name=['word','weight'])
    return word_count_table.sort('weight', ascending=False)

obama_tf_idf = top_words_tf_idf('Barack Obama')
# print(obama_tf_idf)

schiliro_tf_idf = top_words_tf_idf(('Phil Schiliro'))
# print(schiliro_tf_idf)

combined_words = obama_tf_idf.join(schiliro_tf_idf, on='word')
combined_words = combined_words.rename({'weight': 'Obama', 'weight.1': 'schiliro'})
combined_words = combined_words.sort('Obama', ascending=False)
# print(combined_words)

k = []
for l in range(5):
    k.append(combined_words['word'][l])
    l+=1

common_words = {}
for i in range(5):
    common_words[k[i]] = combined_words['Obama'][i]
    i+=1

common_words = set(common_words)
# print(common_words)
z = set(common_words)
# print(z.issubset(common_words))

# checks if the set of words is present in the set of wiki and finds the article with common set
def has_top_words(word_count_vector):
    t = set(word_count_vector.keys())
    return z.issubset(t)

print('output from you func:', has_top_words(wiki[33]['word_count']))
print('correct output: false')
# print('also check the length of unique_words')
# print(len(wiki[33]['word_count']))

# there is sometihing in follow along code about the length of the articles and a histogram showing something, refer that



##########----------COSINE SIMI MODEL--------##########

model2_tf_idf = turicreate.nearest_neighbors.create(wiki, label='name', features=['tf_idf'], method='brute_force', distance='cosine')
nearest_neighbor_cosine = model2_tf_idf.query(wiki[wiki['name'] == 'Barack Obama'], label='name', k=100)
# nearest_neighbor_cosine = nearest_neighbor_cosine.join(wiki[['name', 'length']], on={'reference_label': 'name'})

# nearest_neighbor_cosine = nearest_neighbor_cosine.sort('rank')
print(nearest_neighbor_cosine)
# then again those histograms









