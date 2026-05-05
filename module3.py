#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:39:35 2026

@author: gabriellab
"""

# Intro
label module3_intro:

    call screen module3_intro

label module3_start:

    call screen module3_start

    menu:
        "Continue to simulation":
            jump module3_simulation

#Simulation
label module3_simulation:

    scene bg office

    show player normal at right
    show ryan normal at left

    " You are in your first meeting with your supervisor on your first day of your internship. "

    mod3_supervisor "Good morning, [player_name], congratulations on securing your internship position at GRIN! How is your first day going?"

    p "Great, Mr. Brown, thanks for asking. I brushed up on my technical terms and AI basics this week, so I’m ready for my first project."

    mod3_supervisor "Before we discuss specific projects, I want to pick your brain. At GRIN, we expect you to not only understand AI, but know when and how to use it based on different situations."

  
    jump module3_quiz



# -------------------------------------------------
# QUIZ SECTION
# Must get all 4 correct
# -------------------------------------------------

label module3_quiz:

    $ score = 0
    $ wrong_questions = []



# -------------------------------------------------
# QUESTION 1
# Correct = Choice 3
# -------------------------------------------------

    mod3_supervisor "I’ll start off with an easy question. Could you tell me what the relationship between Artificial Intelligence and machine learning is?”"

    p "Sure..."

    menu:

        "1.	Artificial intelligence is a subset of machine learning.":
            $ wrong_questions.append("Question 1")

        "2. Machine learning is the overall field of using computers to mimic human intelligence, artificial intelligence makes this possible":
            $ wrong_questions.append("Question 1")

        "3.	Machine learning is a subset of Artificial Intelligence":
            $ score += 1

        "4.	Machine learning is unrelated to Artificial Intelligence.":
            $ wrong_questions.append("Question 1")

    mod3_supervisor "Thank you."



# -------------------------------------------------
# QUESTION 2
# Correct = Choice 1
# -------------------------------------------------

    mod3_supervisor ". Now, tell me what the main goal of machine learning is."

    p "The main goal of machine learning is..."

    menu:

        "1.	To learn patterns from existing data and make inferences on new data":
            $ score += 1

        "2.	To store relevant data and automatically remove irrelevant data":
            $ wrong_questions.append("Question 2")

        "3.	To set rules for new data":
            $ wrong_questions.append("Question 2")

        "4.	To design computer hardware":
            $ wrong_questions.append("Question 2")

    mod3_supervisor "Alright..."



# -------------------------------------------------
# QUESTION 3
# Correct = Choice 2
# -------------------------------------------------

    mod3_supervisor "Next, I’ll ask a bit more of an advanced question. Tell me, what type of data is used in supervised learning?"

    p "Hmm..."

    menu:

        "1.	Unlabeled and unstructured data":
            $ wrong_questions.append("Question 3")

        "2.	Labeled and structured data":
            $ score += 1

        "3.	Numerical data":
            $ wrong_questions.append("Question 3")

        "4.	Random datasets":
            $ wrong_questions.append("Question 3")

    mod3_supervisor "*Nods*"



# -------------------------------------------------
# QUESTION 4
# Correct = Choice 4
# -------------------------------------------------

    mod3_supervisor "Just a couple more questions to test your foundation. What is the main idea behind reinforced learning?"

    p "The main idea behind reinforced learning is..."

    menu:

        "1.	Reinforced data groups data into unstructured clusters.":
            $ wrong_questions.append("Question 4")

        "2.	Reinforced learning groups data based similar words.":
            $ wrong_questions.append("Question 4")

        "3.	Reinforced learning learns from unlabeled data.":
            $ wrong_questions.append("Question 4")

        "Reinforced learning uses nested equations to map inputs to outputs.":
            $ score += 1


mod3_supervisor "Thank you."

# -------------------------------------------------
# QUESTION 5
# Correct = Choice 1
# -------------------------------------------------

    mod3_supervisor "Lastly, because our interns spend a lot of time on this, could you tell me what deep learning is?"

    p "Deep learning is..."

    menu:

        "a subset of machine learning that involves multilayered neural networks that are modeled after the structure of the human brain.":
            $ score += 1

        "the new version of machine learning with increased capabilities.":
            $ wrong_questions.append("Question 5")

        "a special type of artificial intelligence that is responsible for natural language processing and convolutional neural networks.":
            $ wrong_questions.append("Question 5")

        "a term used when thinking critically about ways to implement AI.":
            $ wrong_questions.append("Question 5")




# -------------------------------------------------
# QUIZ RESULTS
# -------------------------------------------------

    if score == 5:
        jump module3_pass
    else:
        jump module3_fail



# -------------------------------------------------
# PASS ENDING
# -------------------------------------------------

label module3_pass:

    mod3_supervisor "Great job, [player_name]. Lots of new interns get tripped up with those questions. It’s impressive that you took the time to sharpen your knowledge before your first day. I’ll keep you in mind if any opportunities come up!"

    p "Thank you so much!"

    
# -------------------------------------------------
# FAIL ENDING
# -------------------------------------------------

label module3_fail:

    mod3_supervisor "Unfortunately, those weren’t the answers I was looking for. I’d recommend sharpening your technical understanding a bit more before I introduce you to any new projects."

    "Mr. Brown leaves the office, disappointed."

    centered "You answered some questions incorrectly."

    "Incorrect Questions: [', '.join(wrong_questions)]"

    menu:

        "Retry Quiz":
            jump module3_quiz

        "Return to Menu":
            jump module_select
            return