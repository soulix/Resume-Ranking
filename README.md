# resumeranking 

Extract the text from resume formats like docx,doc,rtf,txt and pdf

1. We are extracting experience from extract_exp.py.
2. Extract Emal, Phone no from ExtractEntities.py file.
3. Extract Skills and non technical skills from getCategory.py file.
4. Run app.py from CMD as it is an web app built on Flask Framework of Python.

We are giving weightage to each resume in 4 ways as mentioned below:

1. 40% weightage to Experience matching of Resume to JD
2. 40% Weightage of Skill in Resume to JD matching
3. 15% weightage of JD to Resume matching using Cosine Distance
4. 5% weightage of Non-Technical skill matching of Resume to JD

All above weightages can be easily changed from the coding. 
We can also seperately create a config file to make it more flexible.
