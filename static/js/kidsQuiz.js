$(document).ready(function(){

    /*------------------------------------------------------LEARNING FOR KIDS QUIZ*/
    
    // Kids First Aid Questions
    var kidsQuiz = [
    {
        kidsQuestion: "1. What phone number should you call in an emergency?",
        
        image: "/static/images/telephone.png",

        kidsAnswerChoices: {
            A: "0800",
            B: "1000000000000",
            C: "999",
        },
        kidsCorrectAnswer: 'C',
        
        kidsSolution: "The correct Answer is C. The UK Emergency Services number is 999. If you are in any doubt in an emergency situation, call the emergency services immediately."
    },
    {
        kidsQuestion: "2. Who can give first aid treatment?",
        
        image: "",
        
        kidsAnswerChoices: {
            A: "Only ambulance staff",
            B: "Only adults",
            C: "Adults and children",
        },
        kidsCorrectAnswer: 'C',
        
        kidsSolution: "The correct Answer is C. First Aid treatment can be given by both Adults and Kids. We have a range of learning resources available in our online store, have a look!"
    },
    {
        kidsQuestion: "3. If someone is choking, how can you help?",
        
        image: "",

        kidsAnswerChoices: {
            A: "Hit them on the back",
            B: "Lean them backwards",
            C: "Lie them on their side",
        },
        kidsCorrectAnswer: 'A',
        
        kidsSolution: "The correct answer is A. If he/she cannot clear the object himself, support him/her with one hand while leaning them forwards. Give up to five back blows between shoulder blades."
    },
    {
        kidsQuestion: "4. What is the best thing to put on a burn at first?",
        
        image: "",

        kidsAnswerChoices: {
            A: "Warm running water",
            B: "Cold running water",
            C: "Kitchen film",
        },
        kidsCorrectAnswer: 'B',
        
        kidsSolution: "The correct answer is B. The first thing you should do when you get a minor burn is run cool (not cold) water over the burn area for about 20 minutes."
    },
    {
        kidsQuestion: "5. Pressing on the wound is the treatment for what?",
        
        image: "",

        kidsAnswerChoices: {
            A: "A broken bone",
            B: "A bad bleed",
            C: "A bee sting",
        },
        kidsCorrectAnswer: 'B',
        
        kidsSolution: "The correct answer is B. Direct pressure slows blood flow at the site of the injury and might even stop it completely."
    },
    {
        kidsQuestion: "6. 'Which of these is the best way to treat a nose bleed?",
        
        image: "",

        kidsAnswerChoices: {
            A: "Lean head forward, pinch soft part of the nose",
            B: "Lean head forward, pinch hard part of the nose",
            C: "Lean head backwards, pinch soft part of the nose",
        },
        kidsCorrectAnswer: 'A',
        
        kidsSolution: "The correct answer is A. Sit down, lean head forward and firmly pinch the soft part of your nose, just above your nostrils, for at least 10-15 minutes."
    },
    {
        kidsQuestion: "7. Why might someone use an inhaler?",
        
        image: "",

        kidsAnswerChoices: {
            A: "They get nosebleeds a lot",
            B: "They have asthma",
            C: "They fall over often",
        },
        kidsCorrectAnswer: 'B',
        
        kidsSolution: "The correct answer is B. An inhaler (puffer or pump) is a medical device used for delivering medication into the body via the lungs. It is mainly used in the treatment of asthma and chronic obstructive pulmonary disease."
    },
    {
        kidsQuestion: "8. If you find someone collapsed on the floor, what should you do first?",
        
        image: "",

        kidsAnswerChoices: {
            A: "Put my jacket over them to keep them warm",
            B: "Check if they are breathing",
            C: "Run off to find an adult",
        },
        kidsCorrectAnswer: 'B',
        
        kidsSolution: "The correct answer is B. Put your face near their cheek to see if you can hear or feel breath, and look along their chest to see if it is rising and falling. If they are not breathing, then quickly call for help (or ask someone else to) and start CPR: cardiopulmonary resuscitation."
    },
    {
        kidsQuestion: "9. How would you help an unconscious person who is breathing?",
        
        image: "",

        kidsAnswerChoices: {
            A: "Sit them up and make sure their head is facing forward",
            B: "Turn them on their side, with their head back",
            C: "Turn them on their side, with their head forward",
        },
        kidsCorrectAnswer: 'B',
        
        kidsSolution: "The correct answer is B. Check that their airway is open and clear by laying the person on their side, tilting the head back, lifting the chin to open the airway."
    },
    {
        kidsQuestion: "10. What is the best way to help a person with a broken leg?",
        
        image: "",

        kidsAnswerChoices: {
            A: "Press on it",
            B: "Pour cold water on it",
            C: "Keep it still and support it",
        },
        kidsCorrectAnswer: 'C',
        
        kidsSolution: "The correct answer is C. Avoid moving the broken leg as much as possible – keep it straight and put a cushion or clothing underneath to support it."
    }
    
    ];
    
    
    // Link to id = quiz in html template, will display main body of quiz
    var kidsQuizBody = document.getElementById('kidsQuizBody');
    
    // Link to button id = submit in html template, will activate results to display to user
    var kidsSubmitAnswers = document.getElementById('kidsSubmitAnswers');
    
    // Link to id = userScore in html template, will display the user's results from the quiz
    var kidsUserScore = document.getElementById('kidsUserScore');
    
    // Text variable for providing feedback to user on how they could improve their First Aid knowledge
    var scoreText;
    
    // Loads the quiz interface immediately
    beginKidsQuiz(kidsQuiz, kidsQuizBody, kidsUserScore, kidsSubmitAnswers);
    
    function beginKidsQuiz(kidsQuestions, kidsQuizBody, kidsUserScore, kidsSubmitAnswers){
    
        // Loads Quiz body with questions and choices
        function kidsQuestionsLoaded(kidsQuestions, kidsQuizBody){
            
            var kidsQuizLoad = [];
            var kidsAnswerChoices;
            var letter;
            
            for(var i=0; i < kidsQuestions.length; i++){
                
                kidsAnswerChoices = [];
    
                /* Adds a HTML Radio button for all answer choices (4) for each question, rendering each
                answer choice on a separate line for better User Experience*/
                for(letter in kidsQuestions[i].kidsAnswerChoices){
    
                    kidsAnswerChoices.push(
                        '<div>' + '<input type="radio" name="kidsQuestion'+i+'" value="'+letter+'">'+ ' ' + letter + ': '
                        + kidsQuestions[i].kidsAnswerChoices[letter] + '</div>'
                    );
                }
    
                // Loads questions with their answer choices and solutions(but hidden)
                kidsQuizLoad.push(
                    '<h4 class="padding-top">' + kidsQuestions[i].kidsQuestion + '</h4>' 
                    + '<div class="kidsAnswerChoices">' + kidsAnswerChoices.join('') + '</div>' + '<div class="kidsSolution hide">' 
                    + kidsQuestions[i].kidsSolution + '</div>'
                );
            }
    
            // Displays quiz on HTML page
            kidsQuizBody.innerHTML = kidsQuizLoad.join('');
        }
    
        // Loads User's score and feedback
        function kidsScoreLoaded(kidsQuestions, kidsQuizBody, kidsUserScore){
            
            // Collates answer choices
            var kidsAnswerChoices = kidsQuizBody.querySelectorAll('.kidsAnswerChoices');
            
            
            // Monitor for user's answers
            var userAnswer = '';
            var kidsCorrectAnswers = 0;
            
            for (var i=0; i < kidsQuestions.length; i++) {
    
                // Monitors user's selected answer from list of answer choices
                userAnswer = (kidsAnswerChoices[i].querySelector('input[name=kidsQuestion'+i+']:checked')||{}).value;
                
                /* If a user's answer is correct, 1 will be added to the number of correct answers and
                highlights the answer choices for that question green, in order to clearly show the 
                user that they correctly answered that question*/
                
                if (userAnswer === kidsQuestions[i].kidsCorrectAnswer) {
                    
                    kidsCorrectAnswers++;
                    
                    kidsAnswerChoices[i].style.color = '#90ee90';
                }
                /* If a user's answer is incorrect, the answer choices for that question will be highlighted red, 
                in order to clearly show the user that they DID NOT correctly answer that question */
                
                else {
                    kidsAnswerChoices[i].style.color = '#ff0000';
                }
            }
    
            /* Displays the number of correct answers out of total number of questions, to provide user with a better understanding
            of their performance.*/
            kidsUserScore.innerHTML = '<b>' + 'Your score is ' + kidsCorrectAnswers + ' out of ' + kidsQuestions.length + '</b>';
            if ( kidsCorrectAnswers < 5) {
                scoreText = "Oh dear, but don't worry we have got great learning material that can help boost your knowledge on First Aid.";
            } 
            else if (kidsCorrectAnswers < 7) {
                scoreText = "Not bad, you have some understanding of First Aid. Consider buying some of our books and CDs to perfect your knowledge!";
            }
            else if (kidsCorrectAnswers < 10) {
                scoreText = "Nearly there, practise makes perfect. Consider buying some of our books and CDs to perfect your knowledge!";
            }
            else {
                scoreText = "Wow! You really know your stuff. Using First Aid Manikins are a great way to put your First Aid knowledge into practise and grow your understanding!";
            }
            document.getElementById("kidsUserFeedback").innerHTML = scoreText;
        }
        
    
        // Reveals questions as soon as user presses the Begin Quiz button on Learning for Adults page (previous page)
        kidsQuestionsLoaded(kidsQuestions, kidsQuizBody);

        /* Reveals question solutions as soon as user presses the submit button to give user a detailed understanding
        of the correct answer and what to do in such situations*/
        function revealKidsSolution() {
            $(".kidsSolution").removeClass("hide");
        }
        
        
        /* When user clicks the submit button at the end of the quiz page, their results appear below to give them feedback on their 
        and recommend Keep Learning First Aid Product Categories that will be useful in enhancing their knowledge to enhance UX. 
        The solutions for each question will also display below each question's list of answer choices*/
        kidsSubmitAnswers.onclick = function() {
            kidsScoreLoaded(kidsQuestions, kidsQuizBody, kidsUserScore);
            revealKidsSolution();
        };
    
    }


});