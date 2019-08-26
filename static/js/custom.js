$(document).ready(function(){
    
    $('#myCarousel').on('slide.bs.carousel');
    $('.collapse').collapse();
    $('#myModal').modal('toggle');
    
    $('#privacyPolicy').modal('show');
    
    $(function () {
      $('[data-toggle="tooltip"]').tooltip();
    });
    
     
/*------------------------------------------------------LEARNING FOR ADULTS QUIZ*/
    
    // Adults First Aid Questions
    var adultsQuiz = [
    {
        question: "1. How should you open the airway of an unconscious casualty?",

        answerChoices: {
            A: "Head tilt and chin lift",
            B: "Jaw thrust",
            C: "Head tilt and jaw thrust",
            D: "Lift the chin",
        },
        correctAnswer: 'A',
        
        solution: "The correct Answer is A. Check that their airway is open and clear by laying the person on their side, tilting the head back, lifting the chin to open the airway."
    },
    {
        question: "2. You are a lone first aider and have an unconscious non-breathing adult, what should you do first?",
        
        answerChoices: {
            A: "Start CPR with 30 chest compressions.",
            B: "Give five initial rescue breaths.",
            C: "Call 999 requesting AED (defibrillator) and ambulance.",
        	D: "Give two initial rescue breaths.",
        },
        correctAnswer: 'C',
        
        solution: "The correct Answer is C. Call or tell someone to call 911. Check the person's airway, breathing, and pulse frequently."
    },
    {
        question: "3. How long would you check to see if an unconscious casualty is breathing normally?",

        answerChoices: {
            A: "No more than 10 seconds",
            B: "Approximately 10 seconds",
            C: "Exactly 10 seconds",
        	D: "At least 10 seconds",
        },
        correctAnswer: 'A',
        
        solution: "The correct answer is A. To check if a person is still breathing: look to see if their chest is rising and falling. Listen over their mouth and nose for breathing sounds. Feel their breath against your cheek for no more than 10 seconds."
    },
    {
        question: "4. Which is the correct ratio of chest compressions to rescue breaths for use in CPR of an adult casualty?",
        
        image: "{% static 'images/chestcompressionsandrescuebreaths.jpg' %}",

        answerChoices: {
            A: "2 compressions : 30 rescue breaths",
            B: "5 compressions : 1 rescue breath",
            C: "15 compressions : 2 rescue breaths",
        	D: "30 compressions : 2 rescue breaths",
        },
        correctAnswer: 'D',
        
        solution: "The correct answer is D. Start CPR with 30 chest compressions before giving two rescue breaths."
    },
    {
        question: "5. Which of the following is the correct sequence for the chain of survival?",

        answerChoices: {
            A: "Call 999. CPR. Defibrillation. Advanced care.",
            B: "CPR. Defibrillation. Call 999. Advanced care.",
            C: "Defibrillation. CPR. Call 999. Advanced care.",
        	D: "Defibrillation. Call 999. CPR. Advanced care.",
        },
        correctAnswer: 'A',
        
        solution: "The correct answer is A. Activation of the emergency response system. Early cardiopulmonary resuscitation (CPR) with an emphasis on chest compressions. Rapid defibrillation. Basic and advanced emergency medical services."
    },
    {
        question: "6. What is the cause of angina?",

        answerChoices: {
            A: "Insufficient blood reaching the lungs",
            B: "Insufficient blood reaching the brain",
            C: "Insufficient blood reaching the heart muscle",
        	D: "Insufficient blood reaching the leg muscles",
        },
        correctAnswer: 'C',
        
        solution: "The correct answer is C. Angina is a type of chest pain caused by reduced blood flow to the heart with symptoms such as squeezing, pressure, heaviness, tightness or pain in your chest."
    },
    {
        question: "7. What should a casualty with a severe allergy carry at all times?",

        answerChoices: {
            A: "Insulin",
            B: "Acetaminophen (Paracetamol)",
            C: "Adrenaline (Epipen)",
        	D: "Aspirin",
        },
        correctAnswer: 'C',
        
        solution: "The correct answer is C."
    },
    {
        question: "8. Which test should you use if you suspect that a casualty has had a stroke?",

        answerChoices: {
            A: "Face, Arms, Speech, Test",
            B: "Alert, Voice, Pain, Unresponsive",
            C: "Response, Airway, Breathing, Circulation",
        	D: "Pulse, Respiratory Rate, Temperature",
        },
        correctAnswer: 'A',
        
        solution: "The correct answer is A. If you think someone is having a stroke, check the three main symptoms using the FAST test: Face ‒ look at their face and ask them to smile. Are they only able to smile on one side of their mouth? If yes, this is not normal. Arms ‒ ask them to raise both arms. Are they only able to lift one arm? If yes, this is not normal. Speech ‒ ask them to speak. Are they struggling to speak clearly? If yes, this is not normal. Time ‒ if the answer to any of these three questions is yes, then it is time to call 999 or 112 for medical help and say you think the casualty is having a stroke."
    },
    {
        question: "9. Which of the following can cause a stroke?",

        answerChoices: {
            A: "A blood clot in an artery in the brain",
            B: "A blood clot in an artery in the heart",
            C: "A blood clot in an artery in the leg",
        	D: "A blood clot in an artery in the lungs",
        },
        correctAnswer: 'A',
        
        solution: "The correct answer is A. A stroke happens when the flow of blood to part of the brain is cut off. This is normally due to a clot in a blood vessel or a rupture which stops the flow of blood getting to the brain."
    },
    {
        question: "10. What should your first action be when treating an electrical burn?",

        answerChoices: {
            A: "Ensure that the casualty is still breathing",
            B: "Wash the burn with cold water",
            C: "Check for danger and ensure that contact with the electrical source is broken",
        	D: "Check for level of response",
        },
        correctAnswer: 'C',
        
        solution: "The correct answer is C. Do not touch the 'electrified person' with your hands. Unplug the appliance or turn off the main power switch."
    },
    {
        question: "11. What is an open fracture?",

        answerChoices: {
            A: "A fracture in which the bone ends can move around",
            B: "A fracture in which the bone is exposed as the skin is broken",
            C: "A fracture which causes complications such as a punctured lung",
        	D: "A fracture in which the bone has bent and split",
        },
        correctAnswer: 'B',
        
        solution: "The correct answer is B. An open fracture, also called a compound fracture, is a fracture in which there is an open wound or break in the skin near the site of the broken bone."
    },
    {
        question: "12. Which medical condition will develop from severe blood loss?",

        answerChoices: {
            A: "Shock",
            B: "Hypoglycaemia",
            C: "Anaphylaxis",
        	D: "Hypothermia",
        },
        correctAnswer: 'A',
        
        solution: "The correct answer is A. Hypovolemic Shock is a life-threatening condition that results when you lose more than 20 percent (one-fifth) of your body's blood or fluid supply, making it impossible for the heart to pump a sufficient amount of blood to your body."
    },
    {
        question: "13. What names are given to the three different depths of burns?",

        answerChoices: {
            A: "Small, medium and large",
            B: "First, second and third degree",
            C: "Minor, medium and severe",
        	D: "Superficial, partial thickness, full thickness",
        },
        correctAnswer: 'D',
        
        solution: "The correct answer is D. Superficial burns-A first-degree burn is also called a superficial burn or wound. It's an injury that affects the first layer of your skin. First-degree burns are one of the mildest forms of skin injuries, and they usually don't require medical treatment. Partial-thickness burns are more serious than superficial (first-degree) burns because a deeper layer of skin is burned. They are more painful and they can get infected more easily. Full thickness burns destroy both layers of skin-(epidermis and dermis) and may penetrate more deeply into underlying structures. These burns have a dense white, waxy or even charred appearance."
    },
    {
        question: "14. What is a faint?",

        answerChoices: {
            A: "A response to fear",
            B: "An unexpected collapse",
            C: "A brief loss of consciousness",
        	D: "A sign of flu",
        },
        correctAnswer: 'C',
        
        solution: "The correct answer is C. Fainting, also called syncope (pronounced SIN-ko-pee), is a sudden, brief loss of consciousness and posture caused by decreased blood flow to the brain."
    },
    {
        question: "15. What steps would you take to control bleeding from a nosebleed?",

        answerChoices: {
            A: "Sit casualty down, lean forward and pinch soft part of nose",
            B: "Sit casualty down, lean backward and pinch soft part of nose",
            C: "Lie casualty down and pinch soft part of nose",
        	D: "Lie casualty down and pinch top of nose",
        },
        correctAnswer: 'A',
        
        solution: "The correct answer is A. You should sit casualty down, lean head forward and firmly pinch the soft part of your nose, just above your nostrils, for at least 10-15 minutes."
    }
    
    ];
    
    
    // Link to id = quiz in html template, will display main body of quiz
    var quizBody = document.getElementById('quizBody');
    
    // Link to button id = submit in html template, will activate results to display to user
    var submitAnswers = document.getElementById('submitAnswers');
    
    // Link to id = userScore in html template, will display the user's results from the quiz
    var userScore = document.getElementById('userScore');
    
    // Text variable for providing feedback to user on how they could improve their First Aid knowledge
    var text;
    
    // Loads the quiz interface immediately
    beginQuiz(adultsQuiz, quizBody, userScore, submitAnswers);
    
    function beginQuiz(questions, quizBody, userScore, submitAnswers){
    
        // Loads Quiz body with questions and choices
        function questionsLoaded(questions, quizBody){
            
            var quizLoad = [];
            var answerChoices;
            var letter;
            
            for(var i=0; i < questions.length; i++){
                
                answerChoices = [];
    
                /* Adds a HTML Radio button for all answer choices (4) for each question, rendering each
                answer choice on a separate line for better User Experience*/
                for(letter in questions[i].answerChoices){
    
                    answerChoices.push(
                        '<div>' + '<input type="radio" name="question'+i+'" value="'+letter+'">'+ ' ' + letter + ': '
                        + questions[i].answerChoices[letter] + '</div>'
                    );
                }
    
                // Loads questions with their answer choices and solutions(but hidden)
                quizLoad.push(
                    '<h4 class="padding-top">' + questions[i].question + '</h4>' + '<img src="' + questions[i].image + '" alt="quiz image">' 
                    + '<div class="answerChoices">' + answerChoices.join('') + '</div>' + '<div class="solution hide">' 
                    + questions[i].solution + '</div>'
                );
            }
    
            // Displays quiz on HTML page
            quizBody.innerHTML = quizLoad.join('');
        }
    
        // Loads User's score and feedback
        function scoreLoaded(questions, quizBody, userScore){
            
            // Collates answer choices
            var answerChoices = quizBody.querySelectorAll('.answerChoices');
            
            
            // Monitor for user's answers
            var userAnswer = '';
            var correctAnswers = 0;
            
            for (var i=0; i < questions.length; i++) {
    
                // Monitors user's selected answer from list of answer choices
                userAnswer = (answerChoices[i].querySelector('input[name=question'+i+']:checked')||{}).value;
                
                /* If a user's answer is correct, 1 will be added to the number of correct answers and
                highlights the answer choices for that question green, in order to clearly show the 
                user that they correctly answered that question*/
                
                if (userAnswer === questions[i].correctAnswer) {
                    
                    correctAnswers++;
                    
                    answerChoices[i].style.color = '#90ee90';
                }
                /* If a user's answer is incorrect, the answer choices for that question will be highlighted red, 
                in order to clearly show the user that they DID NOT correctly answer that question */
                
                else {
                    answerChoices[i].style.color = '#ff0000';
                }
            }
    
            /* Displays the number of correct answers out of total number of questions, to provide user with a better understanding
            of their performance.*/
            userScore.innerHTML = '<b>' + 'Your score is ' + correctAnswers + ' out of ' + questions.length + '</b>';
            if ( correctAnswers < 7) {
                text = "Oh dear, but don't worry we have got great learning material that can help boost your knowledge on First Aid.";
            } 
            else if (correctAnswers < 11) {
                text = "Not bad, you have some understanding of First Aid. Consider buying some of our manikins to put your First Aid knowledge into practise and grow your understanding.";
            }
            else if (correctAnswers < 15) {
                text = "Nearly there, practise makes perfect. Consider buying some of our books and CDs to perfect your knowledge!";
            }
            else {
                text = "Wow! You really know your stuff. Using First Aid Manikins are a great way to put your First Aid knowledge into practise and grow your understanding!";
            }
            document.getElementById("userFeedback").innerHTML = text;
        }
        
    
        // Reveals questions as soon as user presses the Begin Quiz button on Learning for Adults page (previous page)
        questionsLoaded(questions, quizBody);

        /* Reveals question solutions as soon as user presses the submit button to give user a detailed understanding
        of the correct answer and what to do in such situations*/
        function revealSolution() {
            $(".solution").removeClass("hide");
        }
        
        
        /* When user clicks the submit button at the end of the quiz page, their results appear below to give them feedback on their 
        and recommend Keep Learning First Aid Product Categories that will be useful in enhancing their knowledge to enhance UX. 
        The solutions for each question will also display below each question's list of answer choices*/
        submitAnswers.onclick = function() {
            scoreLoaded(questions, quizBody, userScore);
            revealSolution();
        };
    
    }

});