"""

import pandas as pd
 import numpy as np
import matplotlib.pyplot as plt
import random

data = []
for i in range(0, 20): 
n = random.randint(1, 10)
 data.append(n)
data

outliers = []
mean = np.mean(data)
std = np.std(data)
print(mean,std)

for x in data :
z_score = (x-mean)/std
if (np.abs(z_score)>3):
outliers.append(x)
outliers

data = sorted(data)
q1 = np.percentile(data, 25) 
q3 = np.percentile(data, 75)
print(q1,q3)
IQR = q1 - q3

outliers_iqr = []
lv = q1-(1.5*IQR)
uv = q3 +(1.5*IQR)
for x in data:
if ( x < lv or x>uv):
outliers_iqr.append(x)
outliers_iqr



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


# Necessary Imports
import random

class Sorting:


    # Bubble Sort
    def bubbleSort(self,arr):
        n = len(arr) 
        # Traverse through all array elements 
        for i in range(n): 
        # Last i elements are already in place 
            for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    # Selection Sort

    def selectionSort(self,arr):

        for i in range(len(arr)): 
        # Find the minimum element in remaining  
        # unsorted array 
            min_idx = i 
            for j in range(i+1, len(arr)): 
                if arr[min_idx] > arr[j]: 
                    min_idx = j 
            # Swap the found minimum element with  
            # the first element         
            arr[i], arr[min_idx] = arr[min_idx], arr[i] 

        return arr

    # Insertion Sort

    def insertionSort(self,arr):

        # Traverse through 1 to len(arr) 
        for i in range(1, len(arr)): 
            key = arr[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
            j = i-1
            while j >= 0 and key < arr[j] : 
                    arr[j + 1] = arr[j] 
                    j -= 1
            arr[j + 1] = key
        return arr
    
    # Shell Sort

    def shellSort(self,arr):
            # Start with a big gap, then reduce the gap 
        n = len(arr) 
        gap = n//2
        # Do a gapped insertion sort for this gap size. 
        # The first gap elements a[0..gap-1] are already in gapped  
        # order keep adding one more element until the entire array 
        # is gap sorted 
        while gap > 0: 
  
            for i in range(gap,n): 
    
                # add a[i] to the elements that have been gap sorted 
                # save a[i] in temp and make a hole at position i 
                temp = arr[i] 
    
                # shift earlier gap-sorted elements up until the correct 
                # location for a[i] is found 
                j = i 
                while  j >= gap and arr[j-gap] >temp: 
                    arr[j] = arr[j-gap] 
                    j -= gap 
    
                # put temp (the original a[i]) in its correct location 
                arr[j] = temp 
            gap //= 2

        return arr
    
    # Pegion Hole Sort

    def pigeonHoleSort(self,arr):
            # size of range of values in the list  
            # (ie, number of pigeonholes we need) 
        my_min = min(arr) 
        my_max = max(arr) 
        size = my_max - my_min + 1
  
        # our list of pigeonholes 
        holes = [0] * size 
    
        # Populate the pigeonholes. 
        for x in arr: 
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1
    
        # Put the elements back into the array in order. 
        i = 0
        for count in range(size): 
            while holes[count] > 0: 
                holes[count] -= 1
                arr[i] = count + my_min 
                i += 1
        return arr
    
    # Heap Sort

    def heapify(self,arr, n, i): 
        largest = i # Initialize largest as root 
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 
    
        # See if left child of root exists and is 
        # greater than root 
        if l < n and arr[i] < arr[l]: 
            largest = l 
    
        # See if right child of root exists and is 
        # greater than root 
        if r < n and arr[largest] < arr[r]: 
            largest = r 
    
        # Change root, if needed 
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] # swap 
    
            # Heapify the root. 
            self.heapify(arr, n, largest) 
    
    # The main function to sort an array of given size 
    def heapSort(self,arr): 
        n = len(arr) 
    
        # Build a maxheap. 
        for i in range(n, -1, -1): 
            self.heapify(arr, n, i) 
    
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i] # swap 
            self.heapify(arr, i, 0) 
        # Returning the Result
        return arr

    # Gnome Sort

    def gnomeSort(self, arr): 
        index = 0
        n = len(arr)
        while index < n: 
            if index == 0: 
                index = index + 1
            if arr[index] >= arr[index - 1]: 
                index = index + 1
            else: 
                arr[index], arr[index-1] = arr[index-1], arr[index] 
                index = index - 1
  
        return arr

    # Stooage Sort
    def stoogeSort(self,arr,l,h): 
        
        if l >= h: 
            return
    
        # If first element is smaller 
        # than last, swap them 
        if arr[l]>arr[h]: 
            t = arr[l] 
            arr[l] = arr[h] 
            arr[h] = t 
    
        # If there are more than 2 elements in 
        # the array 
        if h-l + 1 > 2: 
            t = (int)((h-l + 1)/3) 
    
            # Recursively sort first 2 / 3 elements 
            self.stoogeSort(arr, l, (h-t)) 
    
            # Recursively sort last 2 / 3 elements 
            self.stoogeSort(arr, l + t, (h)) 
    
            # Recursively sort first 2 / 3 elements 
            # again to confirm 
            self.stoogeSort(arr, l, (h-t))
        return arr

    # Pancake Sorting

    # Reverses arr[0..i]  
    def flip(self,arr, i): 
        start = 0
        while start < i: 
            temp = arr[start] 
            arr[start] = arr[i] 
            arr[i] = temp 
            start += 1
            i -= 1
    
    # Returns index of the maximum 
    # element in arr[0..n-1] */ 
    def findMax(self,arr, n): 
        mi = 0
        for i in range(0,n): 
            if arr[i] > arr[mi]: 
                mi = i 
        return mi 
    
    # The main function that  
    # sorts given array  
    # using flip operations 
    def pancakeSort(self,arr): 
        
        # Start from the complete 
        # array and one by one 
        # reduce current size 
        # by one 
        curr_size = len(arr)
        while curr_size > 1: 
            # Find index of the maximum 
            # element in  
            # arr[0..curr_size-1] 
            mi = self.findMax(arr, curr_size) 
    
            # Move the maximum element 
            # to end of current array 
            # if it's not already at  
            # the end 
            if mi != curr_size-1: 
                # To move at the end,  
                # first move maximum  
                # number to beginning  
                self.flip(arr, mi) 
    
                # Now move the maximum  
                # number to end by 
                # reversing current array 
                self.flip(arr, curr_size-1) 
            curr_size -= 1
        return arr

    # Bogo (OR) Permutation Sort
    # Sorts array a[0..n-1] using Bogo sort 
    def bogoSort(self,arr): 
        n = len(arr) 
        while (self.is_sorted(arr)== False): 
            self.shuffle(arr) 
        return arr

    
    # To check if array is sorted or not 
    def is_sorted(self,arr): 
        n = len(arr) 
        for i in range(0, n-1): 
            if (arr[i] > arr[i+1] ): 
                return False
        return True
    
    # To generate permuatation of the array 
    def shuffle(self,arr): 
        n = len(arr) 
        for i in range (0,n): 
            r = random.randint(0,n-1) 
            arr[i], arr[r] = arr[r], arr[i]
    
    # Merge Sort

    def mergeSort(self,arr): 
        if len(arr) >1: 
            mid = len(arr)//2 #Finding the mid of the array 
            L = arr[:mid] # Dividing the array elements  
            R = arr[mid:] # into 2 halves 
    
            self.mergeSort(L) # Sorting the first half 
            self.mergeSort(R) # Sorting the second half 
    
            i = j = k = 0
            
            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1
            
            # Checking if any element was left 
            while i < len(L): 
                arr[k] = L[i] 
                i+=1
                k+=1
            
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1
        return arr

    # Quick Sort
    def partition(self,arr, low, high): 
        i = (low - 1)         # index of smaller element 
        pivot = arr[high]     # pivot 
    
        for j in range(low, high): 
    
            # If current element is smaller  
            # than or equal to pivot 
            if arr[j] <= pivot: 
            
                # increment index of 
                # smaller element 
                i += 1
                arr[i], arr[j] = arr[j], arr[i] 
    
        arr[i + 1], arr[high] = arr[high], arr[i + 1] 
        return (i + 1) 
    
    # The main function that implements QuickSort 
    # arr[] --> Array to be sorted, 
    # low --> Starting index, 
    # high --> Ending index 
    
    # Function to do Quick sort 
    def quickSort(self,arr, low, high): 
        if low < high: 
    
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.partition(arr, low, high) 
    
            # Separately sort elements before 
            # partition and after partition 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi + 1, high)
        return arr
    
    # Cocktail Sort

    def cocktailSort(self,arr): 
        n = len(arr) 
        swapped = True
        start = 0
        end = n-1
        while (swapped == True): 
    
            # reset the swapped flag on entering the loop, 
            # because it might be true from a previous 
            # iteration. 
            swapped = False
    
            # loop from left to right same as the bubble 
            # sort 
            for i in range (start, end): 
                if (arr[i] > arr[i + 1]) : 
                    arr[i], arr[i + 1]= arr[i + 1], arr[i] 
                    swapped = True
    
            # if nothing moved, then array is sorted. 
            if (swapped == False): 
                break
    
            # otherwise, reset the swapped flag so that it 
            # can be used in the next stage 
            swapped = False
    
            # move the end point back by one, because 
            # item at the end is in its rightful spot 
            end = end-1
    
            # from right to left, doing the same 
            # comparison as in the previous stage 
            for i in range(end-1, start-1, -1): 
                if (arr[i] > arr[i + 1]): 
                    arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                    swapped = True
    
            # increase the starting point, because 
            # the last stage would have moved the next 
            # smallest number to its rightful spot. 
            start = start + 1

        return arr
    
    # Brick Sort
    def brickSort(self,arr): 
        # Initially array is unsorted 
        isSorted = 0
        n = len(arr)
        while isSorted == 0: 
            isSorted = 1
            temp = 0
            for i in range(1, n-1, 2): 
                if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i] 
                    isSorted = 0
                    
            for i in range(0, n-1, 2): 
                if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i] 
                    isSorted = 0
        return arr

    # Radix Sort

    def counting(self, arr, exp1): 
  
        n = len(arr) 
    
        # The output array elements that will have sorted arr 
        output = [0] * (n) 
    
        # initialize count array as 0 
        count = [0] * (10) 
    
        # Store count of occurrences in count[] 
        for i in range(0, n): 
            index = (arr[i]//exp1) 
            count[ int((index)%10) ] += 1
    
        # Change count[i] so that count[i] now contains actual 
        #  position of this digit in output array 
        for i in range(1,10): 
            count[i] += count[i-1] 
    
        # Build the output array 
        i = n-1
        while i>=0: 
            index = (arr[i]/exp1) 
            output[ count[ int((index)%10) ] - 1] = arr[i] 
            count[ int((index)%10) ] -= 1
            i -= 1
    
        # Copying the output array to arr[], 
        # so that arr now contains sorted numbers 
        i = 0
        for i in range(0,len(arr)): 
            arr[i] = output[i] 
    
    # Method to do Radix Sort 
    def radixSort(self,arr): 
    
        # Find the maximum number to know number of digits 
        max1 = max(arr) 
    
        # Do counting sort for every digit. Note that instead 
        # of passing digit number, exp is passed. exp is 10^i 
        # where i is current digit number 
        exp = 1
        while max1/exp > 0: 
            self.counting(arr,exp) 
            exp *= 10
        
        return arr
