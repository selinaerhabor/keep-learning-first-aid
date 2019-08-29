# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Kidsquestion

class Kidsquestiontests(TestCase):

    def test_str(self):
        test_question = Kidsquestion(name='question')
        self.assertEqual(str(test_question), 'question')

"""
Example Test for Learning for Kids Quiz
"""
class Question:
    def __init__(self, ask, answer, solution):
        self.ask = ask
        self.answer = answer
        self.solution = solution
        
#Questions        
ask_kids = [
   'What phone number should you call in an emergency?\n(a)0800\n(b)100\n(c)999\n',
   'Who can give first aid treatment?\n(a)Only ambulance staff\n(b)Only adults\n(c)Adults and children\n',
   'If someone is choking, how can you help?\n(a)Hit them on the back\n(b)Lean them backwards\n(c)Lie them on their side\n',
   'What is the best thing to put on a burn at first?\n(a)Warm running water\n(b)Cold running water\n(c)Kitchen film\n',
   'Pressing on the wound is the treatment for what?\n(a)A broken bone\n(b)A bad bleed\n(c)A bee sting\n',
   'Which of these is the best way to treat a nose bleed?\n(a)Lean head forward, pinch soft part of the nose\n(b)Lean head forward, pinch hard part of the nose\n(c)Lean head backwards, pinch soft part of the nose\n',
   'Why might someone use an inhaler?\n(a)They get nosebleeds a lot\n(b)They have asthma\n(c)They fall over often\n',
   'If you find someone collapsed on the floor, what should you do first?\n(a)Put my jacket over them to keep them warm\n(b)Check if they are breathing\n(c)Run off to find an adult\n',
   'How would you help an unconscious person who is breathing?\n(a)Sit them up and make sure their head is facing forward\n(b)Turn them on their side, with their head back\n(c)Turn them on their side, with their head forward\n',
   'What is the best way to help a person with a broken leg?\n(a)Press on it\n(b)Pour cold water on it\n(c)Keep it still and support it\n',
]
        
        
#Kids Quiz Full Solutions
solution = [
    'UK Emergency Services: 999, US Emergency Services: 911. If you are in any doubt in an emergency situation, call the emergency services immediately.\n',
    'First Aid treatment can be given by both Adults and Kids. We have a range of learning resources available in our online store, have a look!\n',
    'If he/she cannot clear the object himself, support him/her with one hand while leaning them forwards. Give up to five back blows between shoulder blades.\n',
    'The first thing you should do when you get a minor burn is run cool (not cold) water over the burn area for about 20 minutes.\n',
    'Direct pressure slows blood flow at the site of the injury and might even stop it completely.\n',
    'Sit down, lean head forward and firmly pinch the soft part of your nose, just above your nostrils, for at least 10-15 minutes.\n',
    'An inhaler (puffer or pump) is a medical device used for delivering medication into the body via the lungs. It is mainly used in the treatment of asthma and chronic obstructive pulmonary disease.\n',
    'Put your face near their cheek to see if you can hear or feel breath, and look along their chest to see if it is rising and falling. If they are not breathing, then quickly call for help (or ask someone else to) and start CPR: cardiopulmonary resuscitation.\n',
    'Check that their airway is open and clear by laying the person on their side, tilting the head back, lifting the chin to open the airway.\n',
    'Avoid moving the broken leg as much as possible – keep it straight and put a cushion or clothing underneath to support it.\n',
]

#Kids Quiz Questions, Answers & Solution Index
kids_questions = [	
    Question(ask_kids [0], "c", solution [0]),
    Question(ask_kids [1], "c", solution [1]),
    Question(ask_kids [2], "a", solution [2]),
    Question(ask_kids [3], "b", solution [3]),
    Question(ask_kids [4], "b", solution [4]),
    Question(ask_kids [5], "a", solution [5]),
    Question(ask_kids [6], "b", solution [6]),
    Question(ask_kids [7], "b", solution [7]),
    Question(ask_kids [8], "b", solution [8]),
    Question(ask_kids [9], "c", solution [9]),
]

#Kids Quiz Score Feedback
def run_quiz(kids_questions):
    score = 0
    for kids_question in kids_questions:
        answer = input(kids_question.ask)
        if answer == kids_question.answer:
            print("Correct!", kids_question.solution)
            score += 1
        else:
            print("That's Incorrect.", kids_question.solution)
    print("Your score is", score, "out of", len(kids_questions))
    if 0 <= score <= 7:
        print("Oh dear, but don't worry we have got great learning material that can help boost your knowledge on First Aid.")
    elif 8 <= score <= 10:
        print("Not bad, you have some understanding of First Aid. Take a look at some of our books and CDs for kids to boost your knowledge.")
    elif 11 <= score <= 14:
        print("Nearly there, practise makes perfect. Consider some of our books and CDs for kids to perfect your knowledge!")
    else:
        print("Wow! You really know your stuff. Manikins are a great way to put your First Aid knowledge into practise and grow your understanding!")

run_quiz(kids_questions)