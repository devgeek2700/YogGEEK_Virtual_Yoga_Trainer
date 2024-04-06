
# Virtual Yoga Trainer Using openCV

Virtual yoga trainers have gained popularity as a convenient and accessible way to practice yoga from
any location at any time. This paper presents a virtual yoga trainer built with Python that uses machine
learning models, computer vision techniques, and other technologies to provide yoga routines and
real-time feedback to users. 

Additionally, the system can analyze the user's posture and movements during yoga practice to provide real-time feedback to help the user improve their form and avoid
injury. The virtual yoga trainer can make yoga more accessible to people who may not have access to
traditional yoga classes, promote regular yoga practice, and improve users' physical and mental wellbeing. The paper discusses the objectives of the virtual yoga trainer, the potential benefits for users,
and the evaluation metrics for measuring the effectiveness of the system.

It detects 18 yoga poses.
This project got 2nd position in VNPS Competition.
## Proccess

• GUI is created with the help of CSS, HTML and Java Script.

• The UI consists of different poses from which the user can select the desired pose.

• This will instigate the webcam which is done with the help of OpenCV library.

• Now with the help of MediaPipe library 32 key points will be detected in the body which will
be displayed in the screen.

• With the help of human pose estimation algorithm, the key points are detected of the arms and
the legs and are compared with that of MediaPipe.

• Then it will compare the live angles of the legs and the arms with the pre feeded angles.

• If the given live angle is equal or in range of the database's angle then it will show in webcam's
frame that the pose is accurate.

• If the given live angles are not equal or in range of the database's angles then it will show in
webcam's frame that the pose is inaccurate.

• After the completion of a pose (1 minute) there is a 30 second automated break after which
next pose will be automatically initiated. This flow will repeat till the last pose.


This was our Sem-4 mini project.
## Objectives

 - Offer real-time feedback: The system should be able to analyze the user's posture and movements during yoga practice and provide real-time feedback to help the user improve their form and avoid injury.

 - Make yoga more accessible: The virtual yoga trainer should make yoga more accessible to people who may not have access to traditional yoga classes or who feel intimidated by attending a physical yoga studio.


 - Improve physical and mental well-being: The virtual yoga trainer should promote regular yoga practice to improve users' physical and mental well-being, reduce stress and anxiety, and help them lead healthier lives

## Hardware

- OS: Windows 10 and 11

- Processor: i5 and 8th generation

- RAM 8GB

## Software
## Frontend

- HTML

- CSS

- JavaScript

## Backend

- Python
## Libraries used
- OpenCV
- Mediapipe
- Tensorflow
- Numpy
- Flask
- Time

## Database

- SQLite Database (Flask-SQLAlchemy)






## Register page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/output_1.1%20(1).png?raw=true)

## Login page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/output_1.2%20(1).png?raw=true)

## Home page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/output_1.3%20(1).png?raw=true)

## Select page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/output_1.4%20(1).png?raw=true)

## Tulorials page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/output1.5%20(1).png?raw=true)

## Tracks page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/OUTPUT1.6%20(1).png?raw=true)

## Level page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/OUTPUT1.7%20(1).png?raw=true)

## Practice page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/ouput1.8.jpeg?raw=true)


## Rest page

![App Screenshot](https://github.com/devgeek2700/YogGEEK_Virtual_Yoga_Trainer/blob/master/output/output_1.9%20(1).png?raw=true)






## Demo video

<!-- ![App Screenshot](https://github.com/devgeek2700/Myntra_Clone/blob/master/output/demo_myntra_gif.gif?raw=true) -->

## Team Members

| S.No. | Name                | Role                   | GitHub Username      |
|-------|---------------------|------------------------|----------------------|
| 1.    |  Neha Singh  | Full Stack Web Developer        | @devgeek2700         |
| 2.    | Shalaka Kadam      | Research and Designer   | @shalaka2603  |
| 3.    | Amulya Shetty      | Product Designer   | @AmulyaShetty11      |




## Limitations

- Shows results on the screen based on only one input images. No Dataset is used.
- No Showing Analysis of the overall exercise.


## 🛠 Skills
HTML, CSS,JavaScript, Python, openCV, Flask ....

