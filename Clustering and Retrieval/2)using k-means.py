import turicreate
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, normalize
from sklearn.metrics import pairwise_distances

wiki = turicreate.SFrame('/home/kali/ML material/people_wiki.sframe(week3)(candr)/m_cf05efad0f89a530.frame_idx')

wiki['tf_idf'] = turicreate.text_analytics.tf_idf(wiki['text'])

def sframe_to_scipy(x, column_name):
    assert type(x[column_name][0]) == dict
    x = x.add_row_number()
    x = x.stack(column_name, ['features', 'value'])

    unique_words = sorted(x['features'].unique())
    mapping = {word:i for i,word in enumerate(unique_words)}
    x['feature_id'] = x['feature'].apply(lambda x: mapping[x])

    row_id = np.array(x['id'])
    col_id = np.array(x['feature_id'])
    data = np.array(x['value'])

    width = x['id'].max() + 1
    height = x['feature_id'].max() + 1
    mat = csr_matrix((data, (row_id, col_id)), shape=(width, height))
    return mat, mapping

tf_idf, map_index_to_word = sframe_to_scipy(wiki, 'tf_idf')
tf_idf = normalize(tf_idf)

def get_initial_centroids(data, k, seed=None):
    if seed is not None:
        np.random.seed(seed)
    n = data.shape[0]

    rand_indices = np.random.randint(0, n, k)
    centroids = data[rand_indices, :].toarray()
    return centroids

queries = tf_idf[100:102,:]
dist = pairwise_distances(tf_idf, queries, metric='euclidean')















