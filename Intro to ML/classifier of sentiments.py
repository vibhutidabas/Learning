import turicreate

c = turicreate.SFrame('amazon_baby.sframe/m_bfaa91c17752f745.frame_idx')

# building the word count vector
#  c['count_words'] = turicreate.text_analytics.count_words(c['review'])
#  print(c.head())

# explore vulli sophie
g = c[c['name'] == 'Vulli Sophie the Giraffe Teether']
#  g['rating'].show()

# build a sentiment classifier
   # build a word count
c['count_words'] = turicreate.text_analytics.count_words(c['review'])

   # what is positive or negative
c = c[c['rating'] != 3]
c['sentiment'] = c['rating'] >= 4

   # training the sentiment classifier
train, test = c.random_split(.8, seed=0)
sent_model = turicreate.logistic_classifier.create(train, target='sentiment', features=['count_words'], validation_set=test)

   # applying model to understand giraffe reviews
c['predicted_sentiment'] = sent_model.predict(c, output_type='probability')
g = g.sort(c['predicted_sentiment'], ascending=False)
print(g[-1]['review'])