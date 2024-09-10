Non - Touch Virtual Keyboard using OpenCV




DESCRIPTION


The virtual keyboard is an application that enables users to interact with a virtual keyboard by moving their hand over the keys and making certain motions to enter a key in the textbox. It does this using computer vision and hand tracking techniques. The program makes use of a webcam to record the video feed, and computer vision is employed to identify the user's hand and fingers. The characters that the user types into the textbox and sees on the screen are the output.


Hand tracking and gesture recognition are well-established fields in computer vision that have been heavily utilized in a variety of fields, such as gaming, robotics, and human-computer interaction. Our group identified hands in the captured image and followed the fingertips using the HandTrackingModule. To simulate key presses, the algorithm maps the locations of the user's fingertips on the virtual keyboard. This algorithm can recognise hands with a high degree of accuracy because it has already been trained on a sizable collection of hand photos.


Our group developed a useful virtual keyboard that can be operated with hand gestures to give users an engaging and convenient experience. On the basis of the user's fingertips and the button's location on the screen, we also created the detection of selected buttons. Users can type without touching the keyboard because the text input box is updated with the chosen characters.


This algorithm's capability to recognize hands in a variety of illumination situations and hand positions enables real-time tracking of hand movements. However, one drawback is that it might not function correctly in a noisy setting and needs a powerful computer to execute in real-time.


Our team used the OpenCV and cvzone packages to construct the virtual keyboard, incorporating hand tracking and gesture recognition to identify the user's input. In order to draw the buttons on the virtual keyboard, we implemented the display_buttons() function, produced a list of Buttons objects using the key definitions for the virtual keyboard available in the dictionary qwerty_layout, and developed a Buttons class that defines the properties and methods of each button on the virtual keyboard.


Finally, our non-touch virtual keyboard serves as an excellent illustration of how computer vision and hand tracking methods may be used to develop creative and interactive apps. This project was created by our team with pride, and we hope that it will encourage others to investigate the potential of computer vision and gesture recognition.




INSTALL AND RUN PROJECT


You can download it using


    pip install -r requirements.txt


Navigate to the stored folder and run below commands on the terminal: 
    
    sh run.sh


PROJECT STRUCTURE




CVIP Project: directory for the virtual keyboard algorithm


virtual_keyboard.py :  contains code for implementing virtual keyboard using opencv    and cvzone along with integration of hand detection and gesture recognition.


 run.sh : to run the code