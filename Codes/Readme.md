
# Code Documentations
## Data and Data Pre-processing
we first set up the necessary libraries (nltk, pandas, numpy, re and string) and download the relevant packages ('stopwords',and 'punkt') to Google Colab. 

Then we uploaded the corpus file into Colab and get the column of tweets by applying pandas dataframe iloc function (however, later on this project realised that the indexed csv can just use loc to select the columns) and named this column tweets_pd_raw. We inspected the first five rows of the selected dataset so as to get a general idea of our data structure.

Before applying any machine learning models, our project first inspects the data and making sure that they are feasible for analysis. We relied mostly on the NLTK library for text preprocessing. We replaced the URLs, excessive white spaces and mentions with a single gap. Then we tokenized the text and remove punctuations and set to lowercase. After that, this project stemmed the tokenized text and pasted the preprocessed text back to the labelled dataset. Now the preprocessed dataset is renamed as df_tweets. Again we inspected the first five rows of the selected dataset to ensure that the preprocessing generate our desired output.

## Feature Generation and Initial Attempt to Build the RNN Classifier (LSTM)
In this section, we rely mainly on the sklearn and karas libraries to perform the deep learning model training. At this point, we have not encountered computing capacity problems but high chances are, the future training will be moved to other cloud GPU service such as the Amazon AWS. 

By the time of the midterm report, we complete the Tfidf vectorization with the sklearn library and also split the preprocessed dataset into training and testing. The testing accounts for 30% of the complete data. However, this project believe that for better tuning of the final model, it worth spliting the dataset further into at four: training, tuning, development and test. We will explore the feasibility of this data seperation in the post-midterm report period. 

Reference:
As a duplication work, this project would like to mention the code that it consulted. Code suggestion by Alison and Maximilian on our piazza forum give me great help in understanding csv input for NLP data cleaning. During the preprocessing, we modeled mostly the repository for "Automated Hate Speech Detection and the Problem of Offensive Language." by Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. When it comes to dataset spliting and 
RNN model construction, we looked at the repository by unnathi10. 
