import unittest
from LSTM_Classifer import remove_stopwords

class TestRemove_stopwords(unittest.TestCase):
    def setUp(self):
        self.remove_stopwords = remove_stopwords()
    
    from nltk.corpus import stopwords
    top = stopwords.words('english')
    tokens = ['this','is','my','pleasure']
    
    def remove_stopwords(tokens):
        filtered_list =[]
        for it in tokens:
            temp = []
        for word in it:
            if(word not in STOP_WORDS):
                temp.append(word)
        filtered_list.append(temp)
        temp=[] 
    return filtered_list

    tokens.assertEqual(filtered_list,tokens)

        
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()