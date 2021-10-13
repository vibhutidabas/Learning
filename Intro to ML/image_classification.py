import turicreate

train = turicreate.SFrame('/home/kali/ML material/image train data/image_train_data/m_504edbda459b24ff.frame_idx')
test = turicreate.SFrame('/home/kali/ML material/image test data/image_test_data/m_e16f5ffd2c088370.frame_idx')

# train a classifier on the raw image pixels
#   raw_pixels = turicreate.logistic_classifier.create(train, target='label', features=['image_array'])

# make a prediction with model based on raw pixels
#   print(raw_pixels.predict(test[0:3]))

# evaluating raw pixel model on test data
#   print(raw_pixels.evaluate(test))

# improving the model
deep = turicreate.load_model('imagenet_model_iter45')
train['deep_features'] = deep.extract_features(train)

# given the deep features let's make a classifier
deep_model = turicreate.logistic_classifier.create(train, features=['deep_features'], target='label')

# accuracy of the deep features model
print(deep_model.evaluate(test))
