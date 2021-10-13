import turicreate

train = turicreate.SFrame('/home/kali/ML material/image_train/image_train_data/m_504edbda459b24ff.frame_idx') # load CIFAR-10 data

# training a nearest neighbors model for retrieving images using deep features
knn_model = turicreate.nearest_neighbors.create(train, features=['deep_features'], label='id')

# use the image retrieval model with deep features to find similar images
cat = train[18:19]

def get_images_from_id(query_result):
    return train.filter_by(query_result['reference_label'], 'id')

cat_neighbors = get_images_from_id(knn_model.query(cat))
cat_neighbors['image'].explore()
