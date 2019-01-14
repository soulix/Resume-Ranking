import nltk, re
from word2number import w2n
import pandas as pd

class ExtractExp:
    
    information=[]
    inputString = ''
    tokens = []
    lines = []
    sentences = []
    max_weightage = 40;
    min_variance = 5
    
    def get_features(self, text): 
        #TODO: Download below package only once
        #nltk.download('punkt')
        #nltk.download('averaged_perceptron_tagger')
        #nltk.download('maxent_ne_chunker')
        #nltk.download('words')
       
        self.preprocess_data(text)
        self.tokenize(text)
        return self.get_exp(text)
            
    def preprocess_data(self, document):
        
        try:
            # Try to get rid of special characters
            try:
                document = document.decode('ascii', 'ignore')
            except:
                #Pass as document not encoded
                pass
            # Newlines are one element of structure in the data
            # Helps limit the context and breaks up the data as is intended in resumes - i.e., into points
            lines = [el.strip() for el in re.split("\r|\n",document) if len(el) > 0]  # Splitting on the basis of newlines 
            lines = [nltk.word_tokenize(el) for el in lines]    # Tokenize the individual lines
            lines = [nltk.pos_tag(el) for el in lines]  # Tag them
            # Below approach is slightly different because it splits sentences not just on the basis of newlines, but also full stops 
            # - (barring abbreviations etc.)
            # But it fails miserably at predicting names, so currently using it only for tokenization of the whole document
            sentences = nltk.sent_tokenize(document)    # Split/Tokenize into sentences (List of strings)
            sentences = [nltk.word_tokenize(sent) for sent in sentences]    # Split/Tokenize sentences into words (List of lists of strings)
            tokens = sentences
            sentences = [nltk.pos_tag(sent) for sent in sentences]    # Tag the tokens - list of lists of tuples - each tuple is (<word>, <tag>)
            # Next 4 lines convert tokens from a list of list of strings to a list of strings; basically stitches them together
            dummy = []
            for el in tokens:
                dummy += el
            tokens = dummy
            # tokens - words extracted from the doc, lines - split only based on newlines (may have more than one sentence)
            # sentences - split on the basis of rules of grammar
            return tokens, lines, sentences
        except Exception as e:
            print(e)
    
    def tokenize(self, inputString):
        try:
            self.tokens, self.lines, self.sentences = self.preprocess_data(inputString)
            return self.tokens, self.lines, self.sentences
        except Exception as e:
            print(e)
    
    def get_exp(self,inputString):
        expMatchStrings = ['experience', 'exp ', 'exp.', 'exp:','experience:']
        #TODO need to calculate months also
        yearStrings = ['yrs', 'years', 'yr']
        experience = []
        experience_df=pd.DataFrame(columns=('Type', 'Years', 'Months', 'Location'))
        try:
            pos = 0
            for sentence in self.lines:#find the index of the sentence where the degree is find and then analyse that sentence
                pos = pos+1
                sen=" ".join([words[0].lower() for words in sentence]) #string of words in sentence
                if any(re.search(x,sen) for x in expMatchStrings) and any(re.search(x,sen) for x in yearStrings):
                    sen_tokenised= nltk.word_tokenize(sen)
                    tagged = nltk.pos_tag(sen_tokenised)
                    entities = nltk.chunk.ne_chunk(tagged)
                    for subtree in entities.subtrees():
                        for leaf in subtree.leaves():
                            if leaf[1]=='CD':
                                if re.search('total',sen):
                                    expType = 1
                                else: 
                                    if re.search('overall',sen):
                                        expType = 2
                                    else:
                                        expType = 3
                                        
                                expStr = leaf[0].strip('+').strip('\x07')
                                
                                for match in (expMatchStrings+yearStrings):
                                    expStr = expStr.replace(match,"")
                                    
                                    #If expStr contains only digit
                                    try:
                                        years = float(expStr)
                                    except:
                                        try:
                                            # If expStr is string which can be converted into number
                                            years = w2n.word_to_num(expStr)
                                        except:
                                            # try to remove all non-numeric characters from string except dot
                                            non_decimal = re.compile(r'[^\d.]+')
                                            expStr=non_decimal.sub("", expStr)
                                            try:
                                                years = float(expStr)
                                            except Exception as e:
                                                years = 0
                                                print(e)
                            
                                    if years>0 and years < 30:
                                        experience_df = experience_df.append({'Type': expType, 'Years': years, 'Months': 0, 'Location': pos},ignore_index=True)                                    
                                                                                
            if not experience_df.empty:
                #experience_df = experience_df.sort_values(['Type', 'Years','Location'], ascending=[True, False, True])
                experience_df = experience_df.sort_values(['Type', 'Years'], ascending=[True, False])
                experience = float(experience_df['Years'].iloc[0])
            else:
                experience = 0.0
                        
        except Exception as e:
            print (e)
            
        return experience

    def get_exp_weightage(self,jd_exp,resume_exp):
        
        score = 0
        resume_exp = int(round(resume_exp))
        #print(resume_exp)
        if jd_exp.find("-") == -1:
            jd_exp = "0-"+jd_exp[:]
            
        min_jd_exp =  int(jd_exp[0])
        max_jd_exp = int(jd_exp[2])
        
        if resume_exp == 0:
            score = 0
            
        elif resume_exp > min_jd_exp:
            if resume_exp > max_jd_exp:
                score = self.max_weightage - (self.min_variance*(resume_exp-max_jd_exp))
            else:
                score = self.max_weightage
                
        else:
            score = self.max_weightage - (self.min_variance*(min_jd_exp-resume_exp))
        
        if score < 0:
            score = 0
        return score 