import cv2
import cvzone.HandTrackingModule as handTracking
import math

#Detection Constants
DETECTION_CONFIDENCE = 0.8
NO_OF_HANDS = 1

#Colour Constants
TEXT_COLOUR = (255,255,255)
PURPLE = (255, 0, 255)
GREEN = (0,255,0)
NAVY_BLUE = (175,0,175)

#Font Constants
HORIZONTAL_OFFSET = 20
VERTICAL_OFFSET = 65
FONT_SIZE = 4
BUTTON_SIZE = [85, 85]
TEXT_BOX_FONT = 5
BOX_COOR = [(50,350), (700,450), (60,425)]
Resolution_w, Resolution_h = 1280, 720

#Video Input
video_feed = cv2.VideoCapture(0)
video_feed.set(3, Resolution_w)
video_feed.set(4, Resolution_h)

#defining detector
handDetector = handTracking.HandDetector(detectionCon=DETECTION_CONFIDENCE, maxHands=NO_OF_HANDS)
list_buttons=[]

#Keyboard Layout
qwerty_layout = {
    "1": ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    "2": ["A", "S", "D", "F", "G", "H", "J", "K", "L",";"],
    "3": ["Z", "X", "C", "V", "B", "N", "M", ",", ".","/","<"]
                 }
querty_keyboard=[qwerty_layout["1"], qwerty_layout["2"], qwerty_layout["3"]]
textbox_string=""

def display_buttons(image,list_buttons):
    
    #starting a loop to go through each button in the list
    i = 0
    while i < len(list_buttons):
        b = list_buttons[i] #get the current button from the list
        horizontal,vertical=b.location #get horizontal and vertical coordinates of the buttons
        width,height=b.size #get width and height of the image
        cv2.rectangle(image,b.location,(horizontal+width, vertical+height), PURPLE, cv2.FILLED) #drawing rectangle around buttons
        cv2.putText(image,b.data,(horizontal+HORIZONTAL_OFFSET,vertical+VERTICAL_OFFSET), cv2.FONT_HERSHEY_PLAIN, FONT_SIZE, TEXT_COLOUR, FONT_SIZE) #Add text of button to the image
        i += 1 #move to next button
    return image #return the modified image with buttons

class Buttons():
    def __init__(self, position, txt, size=BUTTON_SIZE):
        self.size=size #initialize size
        self.location=position #initialize location
        
        self.data=txt #initialize data

x = 0
while x < len(querty_keyboard): 
    j = 0
    while j < len(querty_keyboard[x]): #loop through keys in current row.
        key = querty_keyboard[x][j] #get current key
        list_buttons.append(Buttons([100*j+50, 100*x+50], key)) #Create button object with location and key on it and append it to list of buttons
        j += 1 #increment column counter
    x += 1 #increment row counter

while True:

    #check if the user has pressed q key to exit the loop
    #reference https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
    if cv2.waitKey(25) & 0xFF == ord('q') or cv2.waitKey(25) & 0xFF == ord('Q'): 
        break
    image = video_feed.read()[1] #read frame from video feed
    image=cv2.flip(image,1) #flip the frame horizontally
    
    hands,bbox_Info = handDetector.findHands(image, draw=True) #hand detector to detect hands
    
    image=display_buttons(image,list_buttons) #display buttons of image
    
    if hands:
        hand=hands[0]
        lm_List= hand["lmList"]
        for b in list_buttons:
            horizontal,vertical=b.location
            width,height=b.size
            #check if the index finger is over the button
            if horizontal<lm_List[8][0]<horizontal+width and vertical<lm_List[8][1]<vertical+height:

                #highlight the button
                cv2.rectangle(image,b.location,(horizontal+width,vertical+height), NAVY_BLUE,cv2.FILLED)
                cv2.putText(image,b.data,(horizontal+HORIZONTAL_OFFSET,vertical+VERTICAL_OFFSET),cv2.FONT_HERSHEY_PLAIN, FONT_SIZE, TEXT_COLOUR, FONT_SIZE)
                
                l=math.hypot(lm_List[8][0]-lm_List[12][0], lm_List[8][1]-lm_List[12][1])
                #check if the distance between index finger and middle finger is less than the threhold
                if l<35:
                    cv2.rectangle(image, b.location,(horizontal+width,vertical+height), GREEN,cv2.FILLED)
                    cv2.putText(image,b.data,(horizontal+HORIZONTAL_OFFSET,vertical+VERTICAL_OFFSET),cv2.FONT_HERSHEY_PLAIN, FONT_SIZE, TEXT_COLOUR, FONT_SIZE)
                    
                    textbox_string+=b.data #add text to the textbox

        #get the position of fingertips
        fingertips=[]
        for h in hands:
            for i, l in enumerate(h["lmList"]):

                if i in [4,12,8,20,16]:
                    fingertips.append(l)
        
        
        
        
        # Draw circles at the positions of the fingertips
        for tip in fingertips:
            cv2.circle(image,tip[:2],10, (0, 255, 0), cv2.FILLED)
    #display textbox on the image    
    cv2.rectangle(image, BOX_COOR[0], BOX_COOR[1],NAVY_BLUE,cv2.FILLED)
    cv2.putText(image,textbox_string, BOX_COOR[2],cv2.FONT_HERSHEY_PLAIN, TEXT_BOX_FONT, TEXT_COLOUR, TEXT_BOX_FONT)
    cv2.imshow("Output Image",image)
    cv2.waitKey(1)

#Release Camera Resources
video_feed.release()
cv2.destroyAllWindows()

'''
References
Cvzone Hand Tracking Module - https://github.com/cvzone/handTrackingModule
Qwerty keyboard - https://en.wikipedia.org/wiki/QWERTY
OpenCV - https://opencv.org/
Python math - https://docs.python.org/3/library/math.html
Numpy - https://numpy.org/
'''