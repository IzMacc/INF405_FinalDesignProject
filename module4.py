#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:22:57 2026

@author: gabriellab
"""

# Intro
label module4_intro:

    call screen module4_intro

label module4_start:

    call screen module4_start

    menu:
        "Continue to simulation":
            jump module4_simulation

#Simulation
label module4_simulation:

    scene bg living room

    show player normal at right
    show jake normal at left

    "You step through the front door to your house after a long day at your new internship, and see your little brother, Jake, laying on the couch, staring at his laptop."

    mod4_brother "Hey, [player_name], you’re back! How was your internship?"

    p "Hey, Jake, it’s been a super long day, but I learned a lot. I did a lot of research about ethics in AI."

    mod4_brother "AI ethics? I’ve never heard of that. I use AI all the time for my assignments and for fun. I’m actually using it right now. Isn’t AI just a regular tool?"

    p "Lots of people think that, but it’s not that simple. AI is trained on really large datasets, and its outputs aren’t always fair due to bias."
  
    jump module4_quiz



# -------------------------------------------------
# QUIZ SECTION
# Must get all 5 correct
# -------------------------------------------------

label module4_quiz:

    $ score = 0
    $ wrong_questions = []



# -------------------------------------------------
# QUESTION 1
# Correct = Choice 1
# -------------------------------------------------

    mod4_brother "What’s bias in AI?"

    p "SBias in AI is…"

    menu:

        "1. AI’s tendency to produce unfair results based on opinionated or unreliable training data":
            $ score += 1

        "2.	AI’s learning process over time":
            $ wrong_questions.append("Question 1")

        "3.	AI’s ability to create original content":
            $ score += 1

        "4.	AI’s capacity to learn faster than humans":
            $ wrong_questions.append("Question 1")

    mod4_brother "Huh… I’ve never thought about the training that goes into AI products. I didn’t know that it just learns patterns from other pieces of data."



# -------------------------------------------------
# QUESTION 2
# Correct = Choice 2
# -------------------------------------------------

    mod4_brother  "Does AI create any original content?"
    
    p "That's another topic I researched today, and..."

    menu:

        "2.	Yes, AI creates original content without any input from data or humans.":
            $ wrong_question.append("Question 2")

        "1.	it’s a growing debate. Since AI comes up with all of its outputs through existing works, it’s a complex question.":
            $ score += 1

        "3.	No, AI copies existing work without creating its own inferences":
            $ wrong_questions.append("Question 2")

        "4.	Yes, but only if prompted":
            $ wrong_questions.append("Question 2")

    mod4_brother "Wow, I never thought AI was so complicated. And AI being an author? That’s crazy."




# -------------------------------------------------
# QUESTION 3
# Correct = Choice 3
# -------------------------------------------------

    mod4_brother "I did see something online about AI collecting our data, but I don’t see how that’s a bad thing. Wouldn’t it just improve the user experience? How else can AI data collection affect us?"

    p "Even though data collection does improve the user experience, it also threatens to invade our privacy. Data collection affects us because…"

    menu:

        "1.	It solely introduces benefits by improving recommendations and keeping our society safe.":
            $ wrong_questions.append("Question 3")

        "2.	It doesn’t affect us because the data collected isn’t stored.":
            $ wrong_questions.append("Question 3")

        "3.	Though there are benefits, it can perform mass collection and surveillance without our knowledge, violating our rights.":
            $ score += 1

        "4.	It doesn’t affect us because we can always choose what data to share.                                                                                  ":
            $ wrong_questions.append("Question 3")





# -------------------------------------------------
# QUESTION 4
# Correct = Choice 4
# -------------------------------------------------

    p "AI doesn’t just collect written data, but it could also be used to track people. For example, AI can impact employees at work by…"

    menu:

        "1.	Tracking their locations":
            $ wrong_questions.append("Question 4")

        "2.	AI has no effect on professional environments":
            $ wrong_questions.append("Question 4")

        "3. Replacing all human workers"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ":
            $ wrong_questions.append("Question 4")

        "4.	Monitoring them through cameras, violating their autonomy":
            $ score += 1


    mod4_brother "I didn’t know that. Sometimes I share my personal information to get better results. I’ll keep that in mind next time…"

# -------------------------------------------------
# QUESTION 5
# Correct = Choice 1
# -------------------------------------------------

    mod4_brother "Hey, I’ve also been seeing a lot of AI generated videos online lately. Did you learn anything about that?"

    p "Yes, I did! AI videos can be entertaining, but sometimes people make them for the wrong reasons. One risk associated with the misuse of AI is…"

    menu:

        "1.	AI tools can be used to create deepfakes, scams, and propaganda":
            $ score += 1

        "2.	The misuse of AI doesn’t have risks because AI outputs aren’t realistic":
            $ wrong_questions.append("Question 5")

        "3.	AI only produces facts and improves online information":
            $ wrong_questions.append("Question 5")

        "4.	AI prevents deepfakes, scams, and propaganda":
            $ wrong_questions.append("Question 5")

    mod4_brother "That makes sense. AI is a really powerful tool, so when it gets into the wrong hands, it could harm people"

    p "Exactly, you’re learning a lot already!"


# -------------------------------------------------
# QUIZ RESULTS
# -------------------------------------------------

    if score == 5:
        jump module4_pass
    else:
        jump module4_fail



# -------------------------------------------------
# PASS ENDING
# -------------------------------------------------

label module4_pass:

    mod4_brother "Thanks for explaining all of that to me, I feel like I know a lot more about AI now than I did before. I can’t wait to hear about what you research tomorrow!"

    
# -------------------------------------------------
# FAIL ENDING
# -------------------------------------------------

label module4_fail:

    mod4_brother "Hmm... I understood some of what you said, but that was kind of confusing. I think I’m just going to continue using AI the way I always do.”"

    centered "You answered some questions incorrectly."

    "Incorrect Questions: [', '.join(wrong_questions)]"

    menu:

        "Retry Quiz":
            jump module4_quiz

        "Return to Menu":
            jump module_select
            return