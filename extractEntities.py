# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 20:57:57 2018

@author: saurabh.keshari
"""
#python -m spacy download en_core_web_sm
#mport spacy
import re
#from collections import Counter
#import en_core_web_sm


#Function to extract names from the string using spacy
def extract_name(resume):
   
   # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = en_core_web_sm.load()
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(resume)
    for ent in doc.ents:
        if(ent.label_ == 'PER'):
            print(ent.text)
            break 
    return ent.text                  

#Function to extract Phone Numbers from string using regular expressions
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers if len(number) >9]

#Function to extract Email address from a string using regular expressions
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

"""

resume = open("resumeSample.txt", "r")
resume_txt = resume.read()
#print(resume_txt)
#print(programmingScore(pdftotextmaybe.convert("Sample resumes/sample1.pdf"), jd_txt) )
#print(extract_name(resume_txt) )
print("Phone numbers are ",extract_phone_numbers(resume_txt) )
print("Email id is ",extract_email_addresses(resume_txt) )


 Code to Read skills from any file 
skills = open("skillDB.txt", "r")
skills = skills.read()
print(skills)
listOfSkills = skills.split(",")
print(listOfSkills)

"""
