
    // 1. LOADING QUESTIONS AND VARIABLES:
    describe("Test selection of questions and respective variables", function(){
      var kidsQuiz = [
      {
        kidsQuestion: "1. What phone number should you call in an emergency?",
        
        image: "https://keeplearningfirstaid.s3.eu-west-2.amazonaws.com/media/images/Telephone.png",
  
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
        
        image: "https://keeplearningfirstaid.s3.eu-west-2.amazonaws.com/media/images/Kids_to_Adults.jpg",
        
        kidsAnswerChoices: {
            A: "Only ambulance staff",
            B: "Only adults",
            C: "Adults and children",
        },
        kidsCorrectAnswer: 'C',
        
        kidsSolution: "The correct Answer is C. First Aid treatment can be given by both Adults and Kids. We have a range of learning resources available in our online store, have a look!"
      }];
      
      it("selected the correct question to load on page", function() {
        expect(kidsQuiz[0].kidsQuestion).toEqual("1. What phone number should you call in an emergency?");
      });
      it("selected the correct image url to load on page", function() {
        expect(kidsQuiz[0].image).toEqual("https://keeplearningfirstaid.s3.eu-west-2.amazonaws.com/media/images/Telephone.png");
        expect(kidsQuiz[1].image).toEqual("https://keeplearningfirstaid.s3.eu-west-2.amazonaws.com/media/images/Kids_to_Adults.jpg");
      });
      it("reads correct answer to question", function() {
        expect(kidsQuiz[0].kidsCorrectAnswer).toEqual("C");
        expect(kidsQuiz[1].kidsCorrectAnswer).toEqual("C");
      });
    });
    