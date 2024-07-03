def hello():
    print("hello")

"""
from sklearn import datasets
# Load the Iris dataset
iris = datasets.load_iris()

import pandas as pd
import numpy as np
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df.isnull().values.any()

df.isnull().values.any()

df = df.fillna(df.mean())



ONE HOT LABEL
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

LE = preprocessing.LabelEncoder()
OHE = OneHotEncoder()

# Separate features (X) and target variable (y)
X = iris.data
y = iris.target
# Create a LabelEncoder object
label_encoder = LabelEncoder()
# Encode the target variable (species)
y_encoded = label_encoder.fit_transform(y)

# Separate features (X) and target variable (y)
X = iris.data
y = iris.target
# Create a OneHotEncoder object
onehot_encoder = OneHotEncoder()
# Encode the target variable (species)
y_encoded = onehot_encoder.fit_transform(y.reshape(-1, 1))

#Feature Scaling

from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

data = iris.data
target = iris.target

# Create a MinMaxScaler object
scaler = MinMaxScaler((0, 1))

# Normalize the data
normalized_data = scaler.fit_transform(data)

== Standardization StandardScalar also Z score==
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

data = iris.data
target = iris.target

# Create a MinMaxScaler object
scaler = StandardScaler()

# Normalize the data
normalized_data = scaler.fit_transform(data)

# replace StandardScalar

== TFID VECTOR ==

import sklearn
from sklearn import feature_extraction
help(sklearn.feature_extraction.text.TfidfVectorizer)

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
vectorizer.get_feature_names_out()
print(X.shape)


== COSINE SIMILARITY ==
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = ["This is a sample document about apples",
              "This is another document about pineapples"]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

# Cosine similarity between the documents
similarity = cosine_similarity(vectors)
print(similarity)

== NAIVE BAYES CLASSIFIER == 
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

def classify_text(text_data, labels, new_text):

  # Feature Extraction (Bag-of-Words)
  vectorizer = CountVectorizer()
  X_counts = vectorizer.fit_transform(text_data)

  # Train the Naive Bayes Model
  clf = MultinomialNB()
  clf.fit(X_counts, labels)

  # Classify New Text
  new_text_counts = vectorizer.transform([new_text])
  predicted_category = clf.predict(new_text_counts)[0]

  return predicted_category

# Example Usage (replace with your data)
text_data = ["This is a spam email", "This is a legitimate email", "Buy now!"]
labels = ["spam", "not spam", "spam"]
new_text = "Click here for a great offer!"

predicted_category = classify_text(text_data, labels, new_text)

print("Predicted category:", predicted_category)

== NAIVE BAYES EMAIL CLASSIFIER == 

# Importing the required header files
import numpy as np
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Function for reading the emails and extracting the message
def read_file(path):
    
    for root, dirname, filenames in os.walk(path):
        
        for filename in filenames:
            
            path=os.path.join(root,filename)
            f=open(path,'r')
            lines=[]
            for line in f:
                lines.append(line)
            f.close()
            message='\n'.join(lines)
            yield message

train_mail=[]

# adding spam mails in training dataset
for message in read_file('Training_Set/spam'):
    train_mail.append([message,'spam'])
    
# adding ham mails in training dataset
for message in read_file('Training_Set/ham'):
    train_mail.append([message,'ham'])
    
# converting train_mail to a numpy array
train_data=np.asarray(train_mail)

# Shows 700 mails with 2 columns (message,(spam/ham))
print (train_data.shape)

# CountVectorizer helps to store the word frequency in a message
vectorizer=CountVectorizer()
counts=vectorizer.fit_transform(train_data[:,0])

# MultinomialNB is used for implementing naive bayes algorithm
# it takes the word counts and the training labels as arguments
classifer=MultinomialNB()
targets=train_data[:,1]
classifer.fit(counts,targets)

test_mail=[]

# adding spam mails in testing dataset
for message in read_file('Testing_Set/spam'):
    test_mail.append([message,'spam'])
    
# adding ham mails in testing dataset
for message in read_file('Testing_Set/ham'):
    test_mail.append([message,'ham'])
    
# converting test_mail to a numpy array
test_data=np.asarray(test_mail)

# Shows 260 mails with 2 columns (message,(spam/ham))
print (test_data.shape)

example_counts=vectorizer.transform(test_data[:,0])
predictions=classifer.predict(example_counts)

# Calculating accuracy of predicted labels by comparing with actual labels
x=0
for i in range(len(predictions)):
    if test_data[i][1]==predictions[i]:
        x+=1
print ("Accuracy: ", 100*x/len(predictions))

dataset link http://openclassroom.stanford.edu/MainFolder/DocumentPage.php?course=MachineLearning&doc=exercises/ex6/ex6.html
https://github.com/sarthakagarwal18/Spam-Classifier

== DECISION TREE ID3 ==

import pandas as pd
import numpy as np
import random

# Define the dataset
data = {
    'Weather': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy': [False, True, False, False, False, True, True, False, False, False, True, True, False, True],
    'Play Tennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy_val = -np.sum([(counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts)) for i in range(len(elements))])
    return entropy_val

def information_gain(data, split_attribute_name, target_name):
    total_entropy = entropy(data[target_name])
    vals, counts= np.unique(data[split_attribute_name], return_counts=True)
    weighted_entropy = np.sum([(counts[i] / np.sum(counts)) * entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) for i in range(len(vals))])
    information_gain_val = total_entropy - weighted_entropy
    return information_gain_val

def id3_algorithm(data, original_data, features, target_attribute_name, parent_node_class):
    # Base cases
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data) == 0:
        return np.unique(original_data[target_attribute_name])[np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])]
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        item_values = [information_gain(data, feature, target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]
        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = id3_algorithm(sub_data, data, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree
        return tree

def predict(query, tree, default = 1):
    for key in list(query.keys()):
        if key in list(tree.keys()):
            try:
                result = tree[key][query[key]]
            except:
                return default
            result = tree[key][query[key]]
            if isinstance(result, dict):
                return predict(query, result)
            else:
                return result

def train_test_split(df, test_size):
    if isinstance(test_size, float):
        test_size = round(test_size * len(df))
    indices = df.index.tolist()
    test_indices = random.sample(population=indices, k=test_size)
    test_df = df.loc[test_indices]
    train_df = df.drop(test_indices)
    return train_df, test_df

train_data, test_data = train_test_split(df, test_size=0.2)

def fit(df, target_attribute_name, features):
    return id3_algorithm(df, df, features, target_attribute_name, None)

def get_accuracy(df, tree):
    df["classification"] = df.apply(predict, axis=1, args=(tree, 'Yes'))
    df["classification_correct"] = df["classification"] == df["Play Tennis"]
    accuracy = df["classification_correct"].mean()
    return accuracy

tree = fit(train_data, 'Play Tennis', ['Weather', 'Temperature', 'Humidity', 'Windy'])
accuracy = get_accuracy(test_data, tree)
print("Decision Tree:")
print(tree)
print("Accuracy:", accuracy)


"""
