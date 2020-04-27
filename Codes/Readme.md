
# Code Documentations (brief)

## 1. Setting up

I installed Pytorch as well as some other useful libraries in preparation for the coming preprocessing, model construction and results visualization

Those libraaies could be categorized into four corresponding groups.

---

## 2. Load the corpus file form Google Drive into Colab

Since the LSTM classifier is operated in the Colab environment, I uploaded the dataset "labeled_data.csv" into drive folder and open it with pandas as a dataframe. Then I inspected the un-preprocessed text to get a sense of what to expect after the preprocessing. In the meanwhile, I also check the distribution of labels to see if the dataset is very biased towards "hate speech" or not.

---

##3. Preprocessing: 

**replace, tokenize sentences and words, remove stopwords, & lemmatizer**

With the re library, I removed mentions, punctuations, numbers, excessive white space.

Then I converted the tweets into lowercase and split sentences

After that, the tweets were lemmatized keeping only nones, adjectives, verbs and adverbs using the spacy library.

Onwards, I defined a remove_stopwords function which filtered out all stopwords contained in the nltk library. 

After finishing the text preprocessing, I printed out again the ten first row of the csv file to inspect the outcome. 

The following code consulted the article *Build Your First Text Classification model using PyTorch* by Aravind Pai (source:https://www.analyticsvidhya.com/blog/2020/01/first-text-classification-in-pytorch/)  

**Preparing input and output sequences**

I built the vocabulary for the text and converted them into integer sequences （embedding). Vocabulary contained the unique words in the entire text. Each unique word is assigned an index. 

Then we created an interator using in the BucketIterator form to format the embeddings into mini batches and paded them into the same length.  

---
# 4. Constructing a LSTM Model

Basic Steps of LSTM:

1. Create LSTM model with
2. Instantiate Model
3. Instantiate Loss Function
4. Instantiate Optimizer
5. Training the Model

---
## 5. Analysing the Model

In the training part, we already print out the training loss and training accuracy for each epoch.

In the validation stage, I first loaded the best model and define the inference function  that accepts the user defined input and **make predictions**. 

---

## 6. Model Comparison

In a the codebook Baseline Model.ipynb, one can fine the code for constructing the baseline model using the Naive Bayer. 
