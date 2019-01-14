
def programmingScore(resume, jdTxt, progWords = None):
    skill_weightage = 40
    skill_threshold = 5
    fout = open("results.tex", "a")
    fout.write("\\textbf{Programming Languages:} \\\\\n")
    
    if(progWords == None):
        programming = ["assembly", "bash", " c " "c++", "c#", "coffeescript", "emacs lisp",
         "go!", "groovy", "haskell", "java", "javascript", "matlab", "max MSP", "objective c", 
         "perl", "php","html", "xml", "css", "processing", "python", "ruby", "sml", "swift", 
         "latex" "unity", "unix" "visual basic" "wolfram language", "xquery", "sql", "node.js", 
         "scala", "kdb", "jquery", "mongodb", "CMMI", "ISO", "finance", "Banking", "Finacle", "Oracle Flexcube", "Fiserv", 
         "TCS BaNcs", "FIS Profile"]
    else:
        programming = progWords
    programmingTotal = 0
    
    jdSkillCount = 0
    jdSkillMatched = []
    for i in range(len(programming)):
        if programming[i].lower() in jdTxt.lower() != -1:
            jdSkillCount += 1
            jdSkillMatched.append(programming[i].lower())
    #print("jdSkillCount", jdSkillCount)
    #for x in range(len(jdSkillMatched)): 
    #print("jd Skills matched are ",jdSkillMatched)
    #END 
    
    individualSkillWeightage = 0
    
    if( jdSkillCount > 0):
        individualSkillWeightage = skill_weightage/jdSkillCount
    
    ResumeProgrammingSkillsMatchedWithJD = []
    for i in range(len(jdSkillMatched)):
        if jdSkillMatched[i].lower() in resume.lower() != -1:
            programmingTotal += 1
            ResumeProgrammingSkillsMatchedWithJD.append(jdSkillMatched[i].lower())
            if not("#" in jdSkillMatched[i]):
                fout.write(jdSkillMatched[i]+", ")
    #print("Resume skills matched with JD are ", ResumeProgrammingSkillsMatchedWithJD)
    #print("programming total is ", programmingTotal)
    
   # My Code 
    resumeCorpus = resume.split()
    resumeCorpus = [x.lower() for x in resumeCorpus if isinstance(x, str)]
    jdSkillMatched = [x.lower() for x in jdSkillMatched if isinstance(x, str)]
    list1 = jdSkillMatched
    list2 = resumeCorpus
    results = {}
    for i in list1:
        results[i] = list2.count(i) 
    
    #print("Dictionary is ",results)
    
   #end of code
   
    constantValue = (individualSkillWeightage/skill_threshold)
    # Updating Dictionary
    results.update({n: constantValue * results[n] for n in results.keys()})
    #print("updated dict is ", results)

    TotalScore = sum(results.values())
    #print("Score is ", TotalScore)

    fout.close()

    #progScore = min(programmingTotal/10.0, 1) * 5.0


    return TotalScore

def NonTechnicalSkillScore(resume, jd_txt, progWords = None):
    skill_weightage = 5
    skill_threshold = 5
    fout = open("results.tex", "a")
    fout.write("\\textbf{Programming Languages:} \\\\\n")
    
    if(progWords == None):
        NonTechnicalSkill = ["Self-directed learning", "Collaboration", "Communication", "Resilience", "Big-picture mindset", "Prioritization ", "Creativity ",
         "creative", "Insight", "curiosity", "curious", "Openness", "Teamwork", "Time management", "Emotional intelligence", 
         "quick learner", "problem solver","Customer-service skills", "Planning and organizing", "innovative", "Thinking innovatively and creatively", "Resourceful", "Flexible", "Able to manage own time", "Having self-esteem", 
         "Innovation skills", "Enterprise skills", "Civic or citizenship knowledge and skills", "Sociability", "Self-management", "Integrity", "Honesty", "Human resources", 
         "Participates as a team member", "Works with diversity", "Exercises leadership", "leadership", "Exercises leadership", "Monitors and corrects performance", "Understands systems"]
    else:
        NonTechnicalSkill = progWords
    programmingTotal = 0
    
    # ADDED BY SAURABH for extracting JD skills is *WORKING* 
    jdSkillCount = 0
    jdSkillMatched = []
    for i in range(len(NonTechnicalSkill)):
        if NonTechnicalSkill[i].lower() in jd_txt.lower() != -1:
            jdSkillCount += 1
            jdSkillMatched.append(NonTechnicalSkill[i].lower())
    #print("jdSkillCount", jdSkillCount)
    #for x in range(len(jdSkillMatched)): 
    #print("jd Skills matched are ",jdSkillMatched)
    #END 
    if (jdSkillCount > 0):
        individualSkillWeightage = skill_weightage/jdSkillCount
    else :
        individualSkillWeightage = 0

    ResumeProgrammingSkillsMatchedWithJD = []
    for i in range(len(jdSkillMatched)):
        if jdSkillMatched[i].lower() in resume.lower() != -1:
            programmingTotal += 1
            ResumeProgrammingSkillsMatchedWithJD.append(jdSkillMatched[i].lower())
            if not("#" in jdSkillMatched[i]):
                fout.write(jdSkillMatched[i]+", ")
    #print("Resume skills matched with JD are ", ResumeProgrammingSkillsMatchedWithJD)
    #print("Non Technical skill total is ", programmingTotal)
    
   # My Code 
    resumeCorpus = resume.split()
    """ Modify below """
    resumeCorpus = resumeCorpus + ResumeProgrammingSkillsMatchedWithJD
    resumeCorpus = [x.lower() for x in resumeCorpus if isinstance(x, str)]
    jdSkillMatched = [x.lower() for x in jdSkillMatched if isinstance(x, str)]
    #print(type(resumeCorpus))
    print("jd skills matched in lower case",jdSkillMatched)
    list1 = jdSkillMatched
    list2 = resumeCorpus
    results = {}
    for i in list1:
        if list2.count(i) > skill_threshold:
           results[i] = skill_threshold
        else:
           results[i] = list2.count(i)
		
    #print("Relevant non-technical skills and their count in resume as per the JD are below")
    print("Dictionary from resume is ",results)
    #print(type(results))
   #end of code
   
    constantValue = (individualSkillWeightage/skill_threshold)
    # Updating Dictionary
    results.update({n: constantValue * results[n] for n in results.keys()})
    print("updated dict is ", results)

    TotalScore = sum(results.values())
    print("Score is ", TotalScore)

    fout.close()

    #progScore = min(programmingTotal/10.0, 1) * 5.0


    return TotalScore
