import turicreate

   # load some data
people = turicreate.SFrame('/home/kali/ML material/wiki_people.sframe/people_wiki.sframe/m_cf05efad0f89a530.frame_idx')
#print(people.head())

   # get the word count for obama
# obama = people[people['name'] == 'Barack Obama']
# obama['word_count'] = turicreate.text_analytics.count_words(obama['text'])       # gives the word count for obama's article

   # sort thr word counts for obama article
# obama_count_table = obama[['word_count']].stack('word_count', new_column_name=['word', 'count'])     #this makes a table for count and words
# obama_count_table = obama_count_table.sort('count', ascending=False)
# print(obama_count_table.head())

   # compute tf-idf for the corpus
people['word_count'] = turicreate.text_analytics.count_words(people['text'])                           #creates a new column of word count for 'people'
people['tfidf'] = turicreate.text_analytics.tf_idf(people['text'])                                               #calcs tf-idf by using word counts

   # examine tfidf
obama = people[people['name'] == 'Barack Obama']
table = obama[['tfidf']].stack('tfidf', new_column_name=['word', 'tfidf']).sort('tfidf', ascending=False)   #this creates tdidf dor obama article and makes a table-
                                                                                                            #-of words and tfidf sorted decs format(with most imp word on top
   # manually compute distances between a few people
clinton = people[people['name'] == 'Bill Clinton']
table2 = clinton[['tfidf']].stack('tfidf', new_column_name=['word', 'tfidf']).sort('tfidf', ascending=False)
david = people[people['name'] == 'David Beckham']
table3 = david[['tfidf']].stack('tfidf', new_column_name=['word', 'tfidf']).sort('tfidf', ascending=False)

   # is obama closer to clinton ot david?
# print(turicreate.distances.cosine(obama['tfidf'][0], clinton['tfidf'][0]))            #lesser the cosine distance value closer is the article to obama
# print(turicreate.distances.cosine(obama['tfidf'][0], david['tfidf'][0]))

   # build a nearest neighbor model for document retrieval
knn_model = turicreate.nearest_neighbors.create(people, features=['tfidf'], label='name')

   # applying the nearest neighbor model
print(knn_model.query(obama))






