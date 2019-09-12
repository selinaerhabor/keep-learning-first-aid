# Keep Learning First Aid – First Aid Learning Equipment and Resources Website

[![Build Status](https://travis-ci.org/selinaerhabor/keep-learning-first-aid.svg?branch=master)](https://travis-ci.org/selinaerhabor/keep-learning-first-aid)

### **Only 5% of adults have the skills and confidence to provide first aid in emergency situations.**
Keep Learning First Aid aim to be UK’s number one first aid learning equipment and resources provider. The website displays First Aid tip of the week, multiple-choice quizzes for children and for adults, first aid learning materials and products for both kids and adults which can be purchased and collection of some frequently asked questions. The products available on the website for purchase include First Aid Books, E-books, Manikins, Posters, DVDs/ CDs and Extras. The aim of the website is to make learning first aid easy and interesting for all ages and make first aid learning resources readily available in order to combat the lack of skills and confidence in providing first aid in emergency situations.
Keep Learning First Aid Website can be accessed [here].

## List of Contents
1. [**User Experience Design (UX)**](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#1-user-experience-design-ux)
      
    1.1	[User Stories](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#11-user-stories)
    
    1.2 [Django App Structure](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#11-user-stories)
    

2. [**Features**](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#2-features)
      
    2.1 [Existing Features](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#21-existing-features)

    2.1.1 [Home Page and Standard Features](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#211-home-page-and-standard-features)

    2.1.2 [First Aid Tip of the Week](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#212-first-aid-tip-of-the-week)

    2.1.3 [Learning for Kids](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#213-learning-for-kids)

    2.1.4 [Learning for Adults](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#214-learning-for-adults)
      
    2.1.5 [FAQs](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#215-faqs)
    
    2.1.6 [Products](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#216-products)
    
    2.1.7 [Login/Register](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#217-loginregister)
    
    2.1.8 [Cart](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#218-cart)
    
    2.1.9 [Order Checkout](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#219-order-checkout)
    
    2.2 [Potential Features to Implement](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#22-potential-features-to-implement-in-the-future)

3. [**Technologies used**](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#3-technologies-used)

4. [**Testing**](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#4-testing)
      
    4.1 [Process of Testing Features](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#41-process-of-testing-features)

    4.2 [HTML and CSS Validation](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#42-html-and-css-validation-results)
    
    4.3 [Jasmine Test Results](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#43-jasmine-tests-results)
    
    4.4 [Device Screen Size and Browser Compatibility Test Results](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#44-device-screen-size-and-browser-compatibility-test-results)
    
    4.5 [Responses from users who visited the web application](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#45-responses-from-users-who-visited-the-keep-learning-first-aid-website-application)
    
    4.6 [Interesting bugs or problems discovered during testing](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#46-interesting-bugs-or-problems-discovered-during-testing)

5. [**Deployment**](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#5-deployment)
      
    5.1 [Deployment Process](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#51-deployment-process)

    5.2 [Running the code locally](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#52-running-the-code-locally)
    
    5.3 [Discussion on the differences between the development code and the deployed Code Version](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#53-discussion-on-the-differences-between-the-development-code-and-the-deployed-code-version)

6. [**Credits**](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#6-credits)
      
    6.1 [Content/Media](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#61-contentmedia)

    6.2 [Acknowledgements](https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/README.md#62-acknowledgements)


## 1. User Experience Design (UX)

Keep Learning First Aid website aims to explain to users the importance of First Aid in our lives and to those around us. The website includes First Aid Tips with a new one appearing every week, first aid quizzes for both children and adults to test their knowledge and a wide range of useful learning resources and first aid items for all ages on the products page which can be purchased. The contents of this website aim to deliver an interactive user experience and inspire people to invest more in learning first aid. 

Main Requirements for the Website: 
* Web application must fulfil some actual (or imagined) real-world need.
* Should allow users to easily navigate through the website
* Application user interface must be responsive to allow good user experience (UX) across various device screen sizes.
* Website should connect to a database.
* App should include use of JavaScript logic to enhance UX.
* Website should contain e-commerce functionality using Stripe.
* Website should include an authentication mechanism.

## 1.1 User Stories
I collected opinions from what users would like in the first aid learning provider website. From a display of clear and easy to understand first aid steps to ease in purchasing products available for sale on the website. I collected feedback from users who discussed potential features they wished to be taken into consideration prior to building the website:

> "Certified first aid courses available to be purchased on the website"

> "Nice clear images of products available, with good descriptions and well organised on the page"

> "Maybe some form of free online learning experience to give people a heads up on what they should know on first aid"

> "Should be engaging, interactive and secure"

> "Website should have a creative and unique style"

> "Application should look professional to encourage users to buy products"

> "Neat and easy to read layout to cater for all ages"


The wireframes were based on meeting the project's requirements and inspired from the user stories listed above. Wireframes focused on each of the main pages of the website from the home page to the products page. These are available in this folder: [Initial Ideas - Wireframes].

## 1.2 Django App Structure
For the Keep Learning First Aid (KLFA) website, the web application is connected to a Postgres database. The Postgres database stores information on users who create an account, first aid tips of the week, products and order information. AWS S3 Storage Bucket has been used for media and static data storages.


There are 10 apps in total as follows:-
* **Accounts** – this app allows the user to login to their account, view their profile, logout from their account and create an account/register.
* **Cart** – this app provides control for the user to add products to their shopping cart, view their cart, adjust their cart and empty the shopping cart. 
* **Firstaidtipoftheweek** – this app is linked to 52 first aid tips stored via Django ORM and displays one first aid tip
* **Home** – this app contains urls for home/index page where there are four featured best-selling products filtered from the back end database, frequently asked questions page and thanks for subscribing page.
* **Keeplearningfirstaid** – this app contains settings and urls that power the web application.
* **Learningforadults** – this app contains filtered learning products for adults and a first aid quiz for adults.
* **Learningforkids** - this app contains filtered learning products for kids and a first aid quiz for kids.
* **Order** – this app contains the payment form and order form to allow user to purchase their items using Stripe and store the order information in the back end
* **Products** – this app provides display of all products currently available with pagination, users can view products by specific category and users can also view products individually to find out more information
* **Search** – this app allows the user to make a search via search input bar at the top of the page and feeds users results from that search

For screenshots of First Aid Tips of the Week and Products data see database-screenshots folder

## 2. Features
Keep Learning First Aid website combines professionalism and user-friendliness to provide a website which showcases the products and services offered by the First Aid learning and training provider. The overall aesthetics for the web application are clean and consistent from the website navigation layout to the interactive multiple choice quiz the user stories have been taken into account when building the website’s features and components. I have chosen green and white as the main colour code to match the key colours in first aid and give the website a neat layout.

## 2.1 Existing Features 
### 2.1.1 Home Page and Standard Features
* **Brand Logo** - the elongated first aid cross as the brand logo is intended to demonstrate a focus of continuing to learn and grow knowledge in first aid. Keep Learning First Aid brand logo was designed using Adobe Photoshop.
* **Website Icon** - uses the Keep Learning First Aid brand logo as this image is unique enough to symbolise the tab/window of the website. 
* **Collapsed Navigation Bar (Mobile view)** - available on extra small and small screens, displays username, cart, search bar and the different pages on the website to make it easy to navigate through the web app.
* **Footer** - Available on all screen sizes, includes a mock email subscription form to sign up to Keep Learning First Aid newsletter. Underneath input box, there are privacy policy, terms & conditions and contact us links to provide users with some information on data protection in accordance with addressing recent changes to General Data Protection Regulation (GDPR).
* **Colour Scheme** - Includes Green, White and Blue which are bright colours that work well with each other. The combination of these colours on the page provides a neat and clean layout as intended.

### 2.1.2 First Aid Tip of the Week
The First Aid Tip of the Week displays featured first aid topic every week. The card uses animation to gain the user’s interest and focus once they click on the First Aid Tip of the Week tab. By default the first aid tip of the week is loaded in the card displayed on the page, but the user can access past First Aid Tips of the week in case they are not up-to-date with the latest post. This gives users the opportunity to actually absorb the information provided on the page and hopes to encourage users to remain in tune with the posts.

### 2.1.3 Learning for Kids
Learning for Kids page displays a link to a quiz for Kids to test their first aid knowledge. This link uses animate.css animation class called ‘heartBeat’ to allow the link to pulse when the Learning for Kids page is loading. Using animation here, aims to grab the attention of users and encourage them or their children to take the quiz.

The Learning for Kids quiz, consists of 10 multiple choice questions with each question having three answer options (A, B or C). There is only one correct answer for each of the 10 questions. The logic for this quiz has been designed using JavaScript, functions include loading the questions with their respective images and answer options with radio buttons, allowing the user to select one radio button per question, verify whether the user’s answers are correct, display user’s score and provide feedback on how they can improve their knowledge. For every correctly answered question, the user will receive one point, but receives no points for an incorrectly answered question. When the user clicks the submit button to mark their answers, the user’s score is calculated and feedback is provided for the user.

Below the link to the quiz, there are three featured products popular for Kids displayed on the page. Users can click on the featured products to be redirected to the filtered list of products where they can proceed to checkout and purchase products.

### 2.1.4 Learning for Adults
Learning for Adults page displays a link to a quiz for Adults to test their first aid knowledge. This link uses animate.css animation class called ‘heartBeat’ to allow the link to pulse when the Learning for Adults page is loading. Using animation here, aims to grab the attention of users and encourage them or their children to take the quiz. 

The Learning for Adults quiz, consists of 15 multiple choice questions with each question having four answer options (A, B, C or D). There is only one correct answer for each of the 15 questions. The addition of quizzes for both kids and adults on the page raises awareness on some of the key areas people should be aware of regarding First Aid. Whilst the quiz does not cover all first aid knowledge, feedback given at the end of the quiz advices users to purchase products that can help them grow their first aid knowledge and be confident in an emergency to provide first aid. 

Below the link to the quiz, there are three featured products popular for Adults displayed on the page. Users can click on the featured products to be redirected to the filtered list of products where they can proceed to checkout and purchase products.

### 2.1.5 FAQs
This page presents answers to frequently asked questions (FAQs) by users to provide all users with better understanding of the application, its products and services in order to enhance the user experience.

Bootstrap Accordion style has been used as the presentation style for this page to organise frequently asked questions (FAQs) and their answers. The accordion style allows one FAQ card to be opened at a time, to keep a neat display of content and prevent overwhelming users with information hence ensuring good readability. The first FAQ card has been left expanded in order for the user to clearly understand the presentation style used (i.e. a user must click on the question card to reveal the answer below.)

### 2.1.6 Products
Card layout has been used to present each product information with titles using `text-truncate` class. Input bar for adding quantity amount joined with Add/Amend buttons. The products page uses pagination to display 9 products per page in order for users not to feel overwhelmed with all products being displayed on one page and long scrolling.

The products list can be filtered by category using dropdown list at the top of the page. Categories currently include Books, Courses, First Aid Kits, Posters, CDs & DVDs, Mankins and Extras. When a user has filtered the products list by a specific category, the name of the category will be displayed by the title. For example if a user selected the Books category, the title of page will change from Products to Products: Books to signal to the user that they are viewing a filtered number of products.

### 2.1.7 Login/Register

The login and register forms use the jumbotron bootstrap class which positions items in the centre and makes text stand out hence providing a clear and formatted form input interface for users when they choose to create accounts/login. 

Each of the forms have links for the user to switch to register/sign in forms. For example, if a user is prompted to the login page when trying to complete checkout but has not created an account. The user can click the register link on the login page to be redirected to the registration form.

### 2.1.8 Cart

The cart display items in card form. Each cart displays the product’s name (truncated text if longer than one line), product image and price.

When the cart is empty, the ‘Your cart is empty’ message will display on the page along with the ‘continue shopping’ button, which redirects users to the products/sale page.  As the cart is empty, the ‘empty cart’ button is hidden and the ‘continue to checkout’ button becomes disabled.

However, when there are items in the cart, the products and quantity you added to your cart will be displayed in card form. The Empty Your Cart and Continue to Checkout buttons are enabled 

### 2.1.9 Order Checkout

The Order Checkout form reads the items displayed in a cart into a table which calculates the total price of all items and their quantities in order to present to the user a final price for purchase. Users will then have to complete the form below to make payment. The forms include information for users to fill in their contact details (name, telephone and address) and their payment information (card number, CVV - 3 digits at the back, card expiry month and year). In order to enhance presentation of forms mentioned Django Crispy Forms package has been used (added in Installed Apps in settings.py file).


## 2.2 Potential Features to implement in the future: 

The addition of a section to allow users to post their experiences on how the website’s resources are helping people to gain confidence in delivering First Aid. These stories are likely to encourage others to take learning First Aid more seriously and raise awareness of the company Keep Learning First Aid and its products and services offered. Users’ experiences could be posted on the Learning for Kids and Learning for Adults pages. 

Another feature to implement is completing functionality to allow users to reset their password in the case of forgetting and receive temporary password via email/telephone from which they can create a new password and get access back to their account and create interfaces for the process of resetting passwords. This includes interface for user to type in email, where a temporary password/ link to reset password will be sent. After this, users will be redirected to another interface where they will have to type in and confirm their new password.



## 3. Technologies Used
* [AWS Cloud 9] - The Integrated Development Environment (IDE) used for building the website.
*	[HTML] - Used for the structure and format of the entire website.
*	[CSS] - For styling the website and maintaining its responsiveness across various screen sizes.
*	[Bootstrap 4.0] - Used for grid form and assistance in styling.
*	[JQuery] - Used for the interactive features of the online cookbook to enhance user experience.
*	[Font Awesome] - Used for displaying the social logos and vector icons present on the website.
*	[Django] – Used for creating apps, superuser and configuring settings to control the web application’s urls and content. Also used for testing. The Django Crispy Forms package assists in rendering forms in a very neat and organised manner to make them easier for the user to understand and complete.
*	[Travis CI] – Used to build and test software project from web application code hosted at GitHub.
* [Browsershots] - For checking browser compatibility and cross platform browser testing.
*	[W3C HTML Validator] - Used to check that no errors were present in the HTML code before final deployment.
*	[W3C CSS Validator] - Used to check that no errors were present in the CSS code before final deployment.
*	[JSHint] - Used to check code quality of JavaScript code.
* [Jasmine Testing] – Used to test some key aspects of the Learning for Kids and Learning for Adults quizzes.

## 4. Testing
This section discusses the testing process for key features of the KLFA website and documents test results on various device screen sizes and browsers to ensure the application is responsive as set out as a main requirement.

## 4.1 Process of Testing Features:

**Register – Create an account on the website**

* Opened the website application and directed to the home page, clicked login/register tab on Navigation bar.
* Redirected to login page, clicked register link
* Chose a username, typed in email, typed in password and confirmed password.
* Submitted registration details and was redirected to home page with alert telling me that I have successfully logged in.
* Account with dropdown options to view profile or logout now appearing where login/register tab was alongside Cart icon and search bar at top of the page.


**Login – Access your registered account**

* Opened the website application and directed to the home page, clicked sign in
* Typed in username/email and password.
* Clicked login and was redirected to home page with alert telling me that I have successfully logged in.
* Account, Search, Cart options appear at top of the page



**Logout**

* Clicked logout from dropdown list on username
* Redirected to home page with alert appearing inside navigation bar that I have successfully logged out.
* Login/Register, Search, Cart icons appear at top of the page in navigation bar.



**First Aid Tip of the Week – Test a new First Aid Tip Appears for each week**

* Logged into superuser account via django admin and clicked First Aid Tip Model.
* Set two first aid tips for start date: 2019/09/10 and end date: 2019/09/17 (YYYY/MM/DD).
* Two First Aid Tips appeared on the page. 
* Changed one First Aid Tip to a different week range and only one first aid tip is appearing on the page for the selected start date and end date above.

**Cart**

* Clicked the Cart Icon in navigation bar
* Redirected to the view cart page
* Message 'Your Cart is empty' displayed and continue to checkout button disabled
* Clicked continue shopping added an item to cart
* Clicked on the cart symbol again, item appears in cart, empty cart button appears and checkout button enabled
* Clicked empty cart and item has now been removed from cart, cart is now empty.

**Order Checkout**

* Placed an item in the cart
* Clicked the continue to checkout button 
* Redirected to the Order Checkout page with item details in table
* Total price of items to be purchased stated below the table with an Amend Cart button on the side
* Completed Order form my details 
* Completed Payment details form
* Clicked Submit and payment successful


**Products**

* Clicked the Products Tab on the lower navigation bar
* Redirected to the products page
* Used dropdown filter and selected each category
* Correctly directed to a filtered view of each category with title adjusting to filtered title
* On the dropdown filter there is a Show All option to return to the full list of products
* All filtered view categories are organised by lowest price first
* Pagination at bottom of page is working well, page number displayed at top of the page is in sync

**FAQs**

* Clicked the FAQs Tab on the lower navigation bar
* Redirected to the FAQs page with one FAQ card expanded to user
* Clicked on the FAQ card and it toggles between hide and show collapse style
* All other FAQs on the page follow the same format


**Score commentary**

* Clicked Kids Quiz, clicked submit button
* Score feedback has selected the correct commentary for score of 0
Oh dear, but don't worry we have got great learning material that can help boost your knowledge on First Aid.
* Clicked 5 correct answers, clicked submit button
* Score feedback has selected the correct commentary for score of 5
Not bad, you have some understanding of First Aid. Consider buying some of our books and CDs to perfect your knowledge!
* Clicked all correct answers
* Score feedback has selected correct commentary
Wow! You really know your stuff. Using First Aid Manikins are a great way to put your First Aid knowledge into practise and grow your understanding!
 

**Search**

* Typed 'books' in search bar at the top of the page
* Products filtered list of books returned below
* Typed 'li' in search bar
* No results returned, return to home page button displayed along with products dropdown filter



## 4.2 HTML and CSS Validation Results:
The HTML and CSS code for the Keep Learning First Aid website has been tested using official validators.

**HTML code**
* No major application errors returned for HTML code for Keep Learning First Aid Web application.

**CSS Code**
* No major application errors returned for CSS code for Keep Learning First Aid Web application.


## 4.3 Jasmine Tests Results: 
The Jasmine tests were carried out for the JS Quiz that is available on both the Learning for Kids and Learning For Adults pages. As both quizzes are built on similar structure in JavaScript, I decided to use the Kids Quiz format for testing which contains images besides each question.

**Loading Questions and Variables:** 
* This test demonstrated whether questions from the kidsQuiz function were correctly being called and loaded. For this test, I declared an 
example array of questions and the respective question’s image url, answer choices, correct answer and solution and used Jasmine matchers to 
ensure the correct variables were being selected.

An example of a check used during testing used is below:
`expect(kidsQuiz[0].kidsCorrectAnswer).toEqual("C");`


Overall, the results from testing the application shows that variables are being correctly selected. 
Screenshot of the [Jasmine Test Results Page] and the script for the main JavaScript code (kidsQuiz.js) had no major issues appear in JSHint Quality tool.


## 4.4 Device Screen Size and Browser Compatibility Test Results:
The website has been tested on various browsers including Firefox, Opera and Google Chrome at the various screen sizes using [Browsershots].
* The below screen size tests were carried out assessing performance of all pages of the website using Google Chrome 74.0 (Windows):

Device | Screen Size (Width x Height) | Keep Learning First Aid
---- | ---- | ---- | 
Galaxy S5 | 360 x 640 | ✓ | 
Pixel 2 | 411 x 731 | ✓ |
Pixel 2 XL | 411 x 823 | ✓ |  
iPhone 5 SE | 320 x 568 | ✓ | 
iPhone 6/7/8 | 375 x 667 | ✓ | 
iPhone 6/7/8 Plus | 414 x 736 | ✓ | 
iPhone X | 375 x 812 | ✓ | 
iPad | 768 x 1024 | ✓ | 
iPad Pro | 1024 x 1366 | ✓ | 
Sony Bravia Television 4K |5280 width (55")|✓ | 


* Below are the test results of the website deployed on GitHub pages when tested on Browsershots.org on various browsers. 
Key screenshots of the Browser Test results can be found in the `browser-tests` under the `tests` folder.
* Key: ✓ - Application loads successfully

Operating System | Browser | Keep Learning First Aid
---- | ---- | ---- | 
Windows | Chrome 73.0 | ✓ |
Windows | Opera 58.0 |  ✓ |
Linux | Firefox 61.0 | ✓  | 

Overall, the results of the tests documented in this chapter and feedback from users suggests that the application works very well across key operating system browsers and various screen sizes with the application layout and structure adjusting responsively. The Keep Learning First Aid Website Application should therefore be reliable and easy to use. 


## 4.5 Responses from users who visited the Keep Learning First Aid Website Application:
I asked a group of people to visit the Keep Learning First Aid Website Application and provide feedback on their experience. They were given the opportunity to explore the web application in its entirety. Below are some of the feedback received from the users:

> "Very satisfactory and informative website with detailed products advertisement." (Eric)

> "Very engaging with the Kids quiz and Adults quiz and opportunity to purchase courses to put into practise what I’ve learnt" (Abbie)

> "It has a variety of products suitable for different age groups" (Tinya)

> "The website is simple and easy to use" (Sunny)
 
> "An excellent website for proactive learning and purchasing of materials" (Osas)

> "Provides opportunity to purchase learning material which provide an in depth understanding of First Aid" (Jess)

The responses from users regarding the web application demonstrated success in meeting both user and project requirements initially set out in the design brief and discussed in the user stories (see 1.1 User Stories).



## 4.6 Interesting bugs or problems discovered during testing:

For the First Aid Tip of the Week app, previous model configured in the models.py used `published_date` as the variable which will be called to display one first aid tip from the database. However, in order to ensure only one First Aid Tip appears on the page every week, I amended the FirstAidTip model adding startdate and enddate fields to state when I would like the post to begin displaying on the page and when it should no longer be displaying. I ensured that the view filtered First Aid Tips which had a start date less than or equal to (lte) today’s date, but end date was greater than (gt) today’s date. The addition of these fields have been successful and I have now been able to set start and end dates for all 52 First Aid Tips, each of the 52 has been assigned to a week between  3rd September 2019 – 1st September 2020.
The view used for displaying a different First Aid Tip each week is below:
```sh
firstaidtips = Firstaidtip.objects.filter(startdate__lte = today, enddate__gt = today)
```
`gt` has been used instead of `gte` , so that no end date will coincide with another First Aid Tip’s start date.


Initially, for the quizzes checkboxes were to be used, but checkboxes were allowing the selection of more than one answer. For both quizzes, all questions have only one correct answer so radio buttons were used for the quiz instead as only one selection for each question could take place.




## 5. Deployment
## 5.1 Deployment Process:
For deploying the Keep Learning First Aid (KLFA) Website to Heroku:
* Ensure git has been initialised `git init`
* Use `git remote add` command with github repository url in order to push code to GitHub
* Type into AWS Cloud 9 terminal the command `pip freeze > requirements.txt` to create a requirements.txt file. 
* Then, type into AWS Cloud9 terminal the command `echo web: python app.py > Procfile` to create a Procfile. 
* Use commands - `git add` and then `git commit` to apply the changes to the application, then use `git push` to push the project to GitHub.
* Create a new app where this application will be deployed on the Heroku website by clicking on the button called "New" in your Heroku dashboard. 
* Set the app-name and the region to your respective region. 
* Next, click on Settings > Reveal Config Vars. Set the C9 HOSTNAME, DATABASE URL, DISABLE_COLLECTSTATIC, HOSTNAME and SECRET_KEY config vars in Heroku:


KEY | VALUE
--- | --- 
**C9 HOSTNAME** | <your-id>.vfs.cloud9.<your-region>.amazonaws.com
**DATABASE_URL**  | postgres://xxxxxxxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@<app-instance>-XX-XXX-X-XX.<app-region>.compute.amazonaws.com:XXXX/XXXXXXXXX
**DISABLE_COLLECTSTATIC ** | 1
**HOSTNAME ** | <app-name>.herokuapp.com
**SECRET_KEY** | <secret key goes here>

* Run python3 manage.py makemigrations and python3 manage.py migrate.
* Create a Procfile and add web: gunicorn tracker.wsgi:application
* import env should be commented out and set DEBUG = False in settings.py file in Django project.
* Type in the command below to log into your Heroku account via AWS Cloud9 terminal
```sh
$ heroku login
```
* Type in your Heroku credentials
* After changes have been pushed to GitHub, type in command ` git push heroku master` to push the updated code to Heroku.
* Add the Herokuapp link to ALLOWED_HOSTS in settings.py.
* Verify whether application has been correctly built by clicking on More > View Logs. 
* Application should now be up and running at https://app-name.herokuapp.com/

## 5.2 Running the code locally:
The repository for this website can be cloned using the command below in AWS Cloud 9 workspace terminal:

```sh
$ git clone https://github.com/selinaerhabor/keep-learning-first-aid.git
```
* Install requirements using command `pip install -r requirements.txt`
* 
* If changes are made to the cloned version of code, make a git commit and push changes to GitHub using the by typing the below commands in your AWS Cloud9 terminal:
```sh
$ git add .
$ git commit -am "type reason for changes to your code here"
$ git push
```
* Type in the command `python3 manage.py runserver 0.0.0.0:8080` in AWS Cloud9 terminal and click on the link that appears after running the command to load the Keep Learning First Aid Website in a new tab.

## 5.3 Discussion on the differences between the development code and the deployed Code Version:

The arrangement of navigation bar links on medium/large screens is slightly different. Originally, account, cart and search icons were to all be situated to the right side of the navigation bar. However due to the poor responsiveness of original layout on smaller screens, I have opted to use a Bootstrap 4 navigation bar layout to ensure responsiveness across a variety of screen sizes in order for the web application to be more user friendly.

The Frequently Asked Questions page was to simply display all questions and answers on the page, but as other pages are aesthetically pleasing I decided to add accordion styling to present the FAQs to users in an interactive and well organised way. I also ensured that the styling complemented text on the page and worked well with the page background and the rest of the website’s layout.

For the Products page, the provided filter by options is a dropdown filter for the different categories of products available. Each category when viewed displays products in order of lowest to highest price, whilst the full products list order all products by name. This simple filter replaces input price range slider and the use of checkboxes. The dropdown feature aims to make shopping experience on the Keep Learning First Aid Website easy and appealing.

The first aid advice cards which were to appear below the featured products on the Learning for Kids and Learning for Adults pages have been removed as First Aid Tip of the Week page will be covering this information. In addition, the quiz buttons have been brought to the top of the page rather than being situated below so that users can clearly see the link to the quiz and access it.

For the homepage, the best-selling products shop now link has been removed. Each of the best-selling product cards will be links to the detailed view of the selected product. This makes it easier for users to find out more information about a specific product rather than having to find the product themselves from a variety of products.

There are no longer first aid tips of the week as potential users raised concerns of the information being too overwhelming. Instead one first aid tip will appear each week to build people’s confidence in administering first aid making it easier for users to absorb the information and be encouraged to keep up to date with the weekly posts.

## 6. Credits
## 6.1 Content/Media:
**Sources**:
* Bootstrap 4.0 Documentation - https://getbootstrap.com/docs/4.0/getting-started/introduction/
* Authentication Mechanism and e-commerce Mechanism inspired from Code Institute lessons and tailored to better suit the nature of the Keep Learning First Aid website application with own additions of form values. New ideas added to the e-commerce mechanism include user friendly templates which also render messages when cart is empty to enhance user experience, amend cart and empty cart links.
* JavaScript Quiz has been inspired from https://www.youtube.com/watch?v=49pYIMygIcU . The quiz layout and design has been tailored to ensure it matches aesthetics of website application and is responsive on the page.

## 6.2 Acknowledgements:

I would like to thank my mentor Aaron and all the tutors at Code Institute for taking time to explain good coding practices in building Django projects, tackling bugs during deployment and ensuring good presentation of code with python code meeting PEP 8 standards. 

[Return to top](https://github.com/selinaerhabor/keep-learning-first-aid#keep-learning-first-aid--first-aid-learning-equipment-and-resources-website)

[//]: # (Below are the reference links used in the body of the README file)
[here]: <https://keeplearningfirstaid.herokuapp.com/>
[HTML]: <https://html.com/> 
[CSS]: <https://https://en.wikipedia.org/wiki/Cascading_Style_Sheets> 
[AWS Cloud 9]: <https://aws.amazon.com/cloud9/>
[Browsershots]: <http://browsershots.org/>
[Bootstrap 4.0]: <https://getbootstrap.com/docs/4.0/getting-started/introduction/>
[Font Awesome]: <https://fontawesome.com/icons?d=gallery>
[Django]: <https://www.djangoproject.com/>
[Travis CI]: <https://travis-ci.org/>
[JQuery]: <https://jquery.com/download/>
[W3C HTML Validator]: <https://validator.w3.org/>
[W3C CSS Validator]: <http://jigsaw.w3.org/css-validator/>
[Jasmine Test Results Page]: <https://github.com/selinaerhabor/keep-learning-first-aid/blob/master/tests/Jasmine%20Test%20Results.jpg>
[Initial Ideas - Wireframes]: <https://github.com/selinaerhabor/keep-learning-first-aid/tree/master/wireframes>
[JSHint]: <https://jshint.com/>
[Jasmine Testing]: <https://en.wikipedia.org/wiki/Jasmine_(JavaScript_testing_framework)>
