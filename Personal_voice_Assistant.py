import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import pywhatkit as kit
import os
import cv2
import datetime
import random
import pyjokes
import keyboard
import string
from googletrans import Translator
import qrcode

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id) 
engine.setProperty('rate',130)
engine.setProperty('volum',10.0)

 # text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    #To convert in to text :                                                                                                                  
def takecommand():

    recognizer =  sr.Recognizer()
    with sr.Microphone() as source:
        print("listeing.....")
        print("  ")
        print("Speak Now")

        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, timeout=100000,phrase_time_limit=5)


        try:

            print("processing....")
            query = recognizer.recognize_google(audio,language='en-in')
            print(f"you said :-{query}")

        except Exception as e:
                print("Say again...")
                return"none"
        return query

# Function to search anything in Google    
def search_in_google(query):
 kit.search(query)
# Main function
def google_Search():
    while True:
            speak("Searching on Google...")
            print("Searching Google for:", query)
            search_in_google(query)
            break
# Calling the main function # function to open the camera 
def open_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            speak("Failed to open camera.")
            break

        cv2.imshow("Camera", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main function
def main_camera():
    while True:
        speak("Opening camera")
        open_camera()
        break

def track_faces():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the frame
        cv2.imshow("Face Tracking", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main function
def main_track():
    while True:
         speak("Ok sir tracking face")
         track_faces()
         break

# Function to track movement
def track_movement():
    cap = cv2.VideoCapture(0)
    _, frame1 = cap.read()
    _, frame2 = cap.read()

    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 700:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Movement Tracking", frame1)
        frame1 = frame2
        _, frame2 = cap.read()

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main function
def main_movement():
    while True:
            speak("Ok sir tracking Movement")
            track_movement()
            break

def music():
        speak("Tell me the name of the song")         
        music = takecommand()
        if "hjjhv" in music:
         os.startfile("C:\\Users\\subha\\Music\\Darkside.mp3")
        else:
            pywhatkit.playonyt(music)
            speak("your song has been started")
            speak("Enjoy sir !") 

# Function to take a photo
def take_photo():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    # Check if the webcam is opened successfully
    
    if not cap.isOpened():
        speak("Error: Failed to open webcam.")
        return

    # Capture a photo
    ret, frame = cap.read()

    # Release the webcam
    cap.release()

    # Save the photo
    if ret:
        cv2.imwrite("C:\\Users\\subha\\photo\\photo.jpg", frame)
        os.startfile("C:\\Users\\subha\\photo\\photo.jpg")
        speak("Photo saved as 'photo.jpg'")
    else:
        speak("Error: Failed to capture photo.")

# Main function
def take_a_photo():
    while True:
        
        take_photo()
        break

# Function to create a folder
def create_folder():
    while True:
        speak("Ok sir.")
        speak("what should your folder query ?")
        folder_name = takecommand()

        if folder_name:
            folder_path = ("C:\\Users\\subha\\Desktop\\" + folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                speak(f"Folder '{folder_name}' created successfully at '{folder_path}'")
                break
            else:
                speak(f"Folder '{folder_name}' already exists. Please choose a different query.")

# Main function
def create_a_folder():
    while True:
       
            create_folder()
            break

# Function to generate a strong password
def generate_password():
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password with 12 characters
    password = ''.join(random.choice(characters) for i in range(12))

    print("Generated password:", password)

# Main function
def Password():
    while True:
       
            generate_password()
            break

       
fun_facts = [
    "Did you know that dolphins have names for each other?",
    "The shortest war in history lasted only 38 minutes.",
    "Bananas are berries, but strawberries aren't.",
    "Octopuses have three hearts.",
    "The Earth has traveled more than 5,000 miles in the past 5 minutes.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "Cows have best friends and can become stressed when they are separated.",
    "The average person spends six months of their lifetime waiting for red lights to turn green.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "The shortest war in history was between Zanzibar and England in 1896. Zanzibar surrendered after 38 minutes.",
    "The oldest known 'your mom' joke was discovered on a 3,500-year-old Babylonian tablet.",
    "A small child could swim through the veins of a blue whale.",
    "An octopus has three hearts.",
    "Bees can recognize human faces.",
    "Hippo milk is pink.",
    "Giraffes have no vocal cords.",
    "Polar bears are left-handed.",
    "The surface area of Russia is slightly larger than the surface area of Pluto.",
    "The human brain takes in 11 million bits of information every second but is aware of only 40 bits.",
    "The average person will spend six months of their life waiting for red lights to turn green.",
    "Honey never spoils.",
    "Dogs sniff good smells with their left nostril.",
    "In the 16th century, Turkish women could initiate a divorce if their husbands didn't pour coffee for them.",
    "An ostrich's eye is bigger than its brain.",
    "A group of flamingos is called a flamboyance.",
    "A single strand of spaghetti is called a spaghetto.",
    "The longest English word is 'pneumonoultramicroscopicsilicovolcanoconiosis' – a type of lung disease caused by inhaling ash and sand dust.",
    "Bananas are berries, but strawberries aren't.",
    "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion."
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "The average person will spend six months of their life waiting for red lights to turn green.",
    "Honey never spoils.",
    "Dogs sniff good smells with their left nostril.",
    "In the 16th century, Turkish women could initiate a divorce if their husbands didn't pour coffee for them.",
    "An ostrich's eye is bigger than its brain.",
    "A group of flamingos is called a flamboyance.",
    "A single strand of spaghetti is called a spaghetto.",
    "The longest English word is 'pneumonoultramicroscopicsilicovolcanoconiosis' – a type of lung disease caused by inhaling ash and sand dust.",
    "The surface area of Russia is slightly larger than the surface area of Pluto.",
    "The human brain takes in 11 million bits of information every second but is aware of only 40 bits.",
    "The average person will spend six months of their life waiting for red lights to turn green.",
    "Honey never spoils.",
    "Dogs sniff good smells with their left nostril.",
    "In the 16th century, Turkish women could initiate a divorce if their husbands didn't pour coffee for them.",
    "An ostrich's eye is bigger than its brain.",
    "A group of flamingos is called a flamboyance.",
    "A single strand of spaghetti is called a spaghetto.",
    "The longest English word is 'pneumonoultramicroscopicsilicovolcanoconiosis' – a type of lung disease caused by inhaling ash and sand dust.",
    "The surface area of Russia is slightly larger than the surface area of Pluto.",
    "The human brain takes in 11 million bits of information every second but is aware of only 40 bits.",
    "The average person will spend six months of their life waiting for red lights to turn green.",
    "Honey never spoils.",
    "Dogs sniff good smells with their left nostril.",
    "In the 16th century, Turkish women could initiate a divorce if their husbands didn't pour coffee for them.",
    "An ostrich's eye is bigger than its brain.",
    "A group of flamingos is called a flamboyance.",
    "A single strand of spaghetti is called a spaghetto.",
    "The longest English word is 'pneumonoultramicroscopicsilicovolcanoconiosis' – a type of lung disease caused by inhaling ash and sand dust.",
    "The surface area of Russia is slightly larger than the surface area of Pluto.",
    "The human brain takes in 11 million bits of information every second but is aware of only 40 bits.",
    "The average person will spend six months of their life waiting for red lights to turn green.",
    "Honey never spoils.",
    "Dogs sniff good smells with their left nostril.",
    "In the 16th century, Turkish women could initiate a divorce if their husbands didn't pour coffee for them.",
    "An ostrich's eye is bigger than its brain.",
    "A group of flamingos is called a flamboyance.",
    "A single strand of spaghetti is called a spaghetto.",
    "The longest English word is 'pneumonoultramicroscopicsilicovolcanoconiosis' – a type of lung disease caused by inhaling ash and sand dust.",
    "The surface area of Russia is slightly larger than the surface area of Pluto.",
    "The human brain takes in 11 million bits of information every second but is aware of only 40 bits.",
    "The average person will spend six months of their life waiting for red lights to turn green.",
    "Honey never spoils.",
    "Dogs sniff good smells with their left nostril.",
    "In the 16th century, Turkish women could initiate a divorce if their husbands didn't pour coffee for them.",
    "An ostrich's eye is bigger than its brain.",
    "A group of flamingos is called a flamboyance.",
    "A single strand of spaghetti is called a spaghetto.",
    "The longest English word is 'pneumonoultramicroscopicsilicovolcanoconiosis' – a type of lung disease caused by inhaling ash and sand dust.",
    "The surface area of Russia is slightly larger than the surface area of Pluto.",
    "The human brain takes in 11 million bits of information every second but is aware of only 40 bits."
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes.",
    "The probability of being killed by a vending machine is higher than the probability of being bitten by a shark.",
    "Honeybees can recognize human faces.",
    "A cat has been mayor of Talkeetna, Alaska, for over 20 years.",
    "The longest wedding veil was longer than 63 football fields.",
    "The first oranges weren't orange.",
    "A baby puffin is called a 'puffling'.",
    "Cows have best friends.",
    "Banging your head against a wall for one hour burns 150 calories.",
    "Pirates wore earrings because they believed it improved their eyesight.",
    "The oldest known 'yo mama' joke is from 3,500 years ago.",
    "Bananas are berries, but strawberries are not.",
    "The unicorn is the national animal of Scotland.",
    "Polar bears could eat as many as 86 penguins in a single sitting if they didn't get full.",
    "A group of flamingos is called a 'flamboyance'.",
    "A shrimp's heart is in its head.",
    "A giraffe can clean its ears with its 21-inch tongue.",
    "The world's largest snowflake was 15 inches wide.",
    "The tongue of a blue whale weighs more than most elephants.",
    "It takes about 8 minutes and 20 seconds for sunlight to reach Earth.",
    "The average person will spend 6 months of their life waiting for red lights to turn green.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes.",
    "The dot over the letter 'i' is called a tittle.",
    "Octopuses have three hearts.",
    "The pineapple is a symbol of hospitality.",
    "The 'Windy City' name for Chicago has nothing to do with its weather.",
    "The only letter that doesn't appear on the periodic table is 'J'.",
    "The dot over the letter 'i' is called a tittle.",
    "Oxford University is older than the Aztec Empire.",
    "The 'Windy City' name for Chicago has nothing to do with its weather.",
    "The elephant is the only mammal that can't jump.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes.",
    "The unicorn is the national animal of Scotland.",
    "Polar bears could eat as many as 86 penguins in a single sitting if they didn't get full.",
    "Bananas are berries, but strawberries are not.",
    "The tongue of a blue whale weighs more than most elephants.",
    "Octopuses have three hearts.",
    "The pineapple is a symbol of hospitality.",
    "Oxford University is older than the Aztec Empire.",
    "The 'Windy City' name for Chicago has nothing to do with its weather.",
    "The elephant is the only mammal that can't jump.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes.",
    "The unicorn is the national animal of Scotland.",
    "Polar bears could eat as many as 86 penguins in a single sitting if they didn't get full.",
    "Bananas are berries, but strawberries are not.",
    "The tongue of a blue whale weighs more than most elephants.",
    "Octopuses have three hearts.",
    "The pineapple is a symbol of hospitality.",
    "Oxford University is older than the Aztec Empire.",
    "The 'Windy City' name for Chicago has nothing to do with its weather.",
    "The elephant is the only mammal that can't jump.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted only 38 minutes.",
    "The unicorn is the national animal of Scotland.",
    "Polar bears could eat as many as 86 penguins in a single sitting if they didn't get full.",
    "Bananas are berries, but strawberries are not.",
    "The tongue of a blue whale weighs more than most elephants.",
    "Octopuses have three hearts.",
    "The pineapple is a symbol of hospitality.",
    "Oxford University is older than the Aztec Empire.",
    "The 'Windy City' name for Chicago has nothing to do with its weather.",
    "The elephant is the only mammal that can't jump.",
]
# Function to tell a fun fact
def tell_fun_fact():
    fun_fact = random.choice(fun_facts)
    speak("Sure")
    print(fun_fact)
    speak(fun_fact)

# Main function
def fun_fact():
    while True:
        
        tell_fun_fact()
        break

def translate_to_hindi(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='hi')
    speak("tack a look")
    print("Translated in Hindi:", translated_text.text)
# Main function
def translate():
    while True:
        speak("Please say you want to translate to Hindi:")
        command = takecommand()

        if command:
            translate_to_hindi(command)
            break


# Function to create QR code
def create_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("C:\\Users\\subha\\QR code\\"+ filename +".png")
    speak(f"QR code saved as '{filename}.png'")
    os.startfile("C:\\Users\\subha\\QR code\\" + filename + ".png")

# Main function
def QRcode():
    speak("Please provide the data you want to include in the QR code:")
    
    speak("What's the main text you want to encode in the QR code?")
    text = takecommand()
    
    additional_data = {}
    
    while True:
        speak("Do you want to add more data? (yes/no)")
        choice = takecommand()
        
        if choice.lower() == "no":
            break
        elif choice.lower() == "yes":
            speak("What's the key for the additional data?")
            key = takecommand()
            speak(f"What's the value for the key '{key}'?")
            value = takecommand()
            additional_data[key] = value
        else:
            speak("Invalid choice. Please say 'yes' or 'no'.")

    # Constructing the final data string
    data = f"Main text: {text}\n"
    for key, value in additional_data.items():
        data += f"{key}: {value}\n"

    # Ask for the file name
    speak("Please specify the file name for the QR code (without extension):")
    filename = takecommand()
    if not filename:
        filename = "qr_code"

    create_qr_code(data, filename)


# Function to lock Windows
def lock_windows():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    speak("Windows locked.")

# Main function
def LOCK_WINDOWS():
    while True:
            lock_windows()
            break


# Function to put Windows to sleep
def sleep_windows():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# Main function
def SLEEP_WINDOW():
    
    while True:
        
            sleep_windows()
            break  

# Function to shut down Windows
def shutdown_windows():
    os.system("shutdown /s /t 1")  # Shutdown command with a delay of 1 second

# Main function
def SHUTDOWN():
    
    while True:
       
            shutdown_windows()
            break  

# Function to restart Windows
def restart_windows():
    os.system("shutdown /r /t 0")

# Main function
def RESTART():

    while True:
    
            restart_windows()
            break

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<=11:
        speak("Good Morning ")
        speak("How can I help you today !")
    elif hour>=12 and hour<=18:
        speak("Good aftenoon ")
        speak("How can I help you today !")
    elif hour>=18 and hour<=20:
        speak("Good Evening ")
        speak("How can I help you today !")

    else:
           speak("middle of the night ")
           speak("How can I help you today !")

# Load Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces and count them
def detect_faces(gray):
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return faces, len(faces)

# Function to draw rectangles around detected faces
def draw_faces(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Function to display the count of detected faces on the frame
def display_face_count(frame, num_faces):
    cv2.putText(frame, f"Faces Detected: {num_faces}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Function to detect and recognize faces
def detect_and_recognize_faces():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces and count them
        faces, num_faces = detect_faces(gray)

        # Draw rectangles around detected faces
        draw_faces(frame, faces)

        # Display the count of detected faces
        display_face_count(frame, num_faces)

        cv2.imshow('Face Authentication', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
   
# Main function
def detect():
    detect_and_recognize_faces()
    
        
if __name__ == "__main__":
    
    wish()
    
    while True:
        query = takecommand().lower()
            
        if "hello" in query:
            speak("Hello sir !. How can I help you today ")  
        elif "hey siri" in query:
            speak("How can I help")         
        elif "stop listening" in query:
            speak("Stopping listening...")
            break

        elif "what is your name" in query:
            speak("My name is siri.")
            speak("I am your virtual personal Assistant")
        elif "what can you do" in query:
            speak("I can help you with a variety of tasks, such as searching the web, setting reminders,Track movement, playing music, and more. Just ask!")
        elif "what about you" in query:
            speak("I am your personal Assistant that takes your commands and turn them into actions. It also allows you to create and train new skills")   
        elif "where are you from" in query:
            speak("I am a virtual assistant created by Subham, so I don't have a physical location.")
        elif "tell me about yourself" in query:
            speak("I am an AI-powered virtual assistant designed to assist you with various tasks. I'm constantly learning and improving to better serve you.")
        elif "can you sing" in query:
            speak("I'm not programmed to sing, but I can play music for you!")
        elif "i have a question" in query:
            speak("Go for it !") 
        elif "bye" in query:
            speak("bye sir")
            break  
        elif"tata" in query:
            break

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")        
            speak(f"The current time is {strTime}")        
         
        elif "date" in query:  
            dateTimeObj = datetime.datetime.now()
            strDate = dateTimeObj.strftime("%m/%d/%Y")                
            speak(f"Today’s date is {strDate}")  
          
        elif "convert temperature" in query:        
            speak('What is the temperature you want to convert?') 
            temp = takecommand()   
            try:
                temp_float = float(temp)
                speak('Which unit do you want to convert it to? Celsius or Fahrenheit?')
                unit = takecommand().lower()    
                if 'celsius' in unit:
                    celsius = (temp_float - 32) * 5/9
                    speak(f"{temp} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
                elif 'fahrenheit' in unit:
                    fahreinheit = temp_float + 32
                    speak(f"{temp} degrees Celsius is equal to {fahreinheit} degrees Fahrenheit.")                            
            except:
                speak("Sorry, I didn't get that. Can you please say the temperature again?")              
                
        elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)            
        elif 'launch a website' in query or "launch" in query or "swow me a website" in query:
            speak("Tell me the query of website you want to launch.")
            query = takecommand()
            web = 'https://www.'+query+'.com'
            webbrowser.open(web)
            speak("lunching...")             
        elif "what" in query or "who" in query or "when" in query  or "how" in query or "which" in query or "where" in query or "whether" in query or "however" in query or "why" in query or "can you tell me" in query or "search" in query or "tell about" in query:
            google_Search()   
            
        elif "screenshot" in query or "tack a screenshot" in query: #tack a screenshort
            speak("Ok sir !")
            pywhatkit.take_screenshot("screenshot")
            speak("Here...take a look")
            
        elif "time kata hela" in query:
             strTime = datetime.datetime.now().strftime("%H:%M")    
             speak(f"Sir, the time is {strTime}")    
            
        elif "i am so tired" in query:      #this code is used when user
            speak("I bet you have working hard.")
            speak("I have some playing your favorite song for you")
            a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
            b = random.choice(a)
            if b==1:
               webbrowser.open("https://www.youtube.com/watch?v=SCFy_kBs4Qo&list=RDMMSCFy_kBs4Qo&start_radio=1")
            elif b==2:
                webbrowser.open("https://www.youtube.com/watch?v=3djI8Q6Y-kg&list=RDMMSCFy_kBs4Qo&index=11")
            elif b==3:
                webbrowser.open("https://www.youtube.com/watch?v=MG43EkoxfTQ&list=RDMMSCFy_kBs4Qo&index=14")
        
        elif'tell me a joke' in query:
            get = pyjokes.get_joke()
            speak(get)

         #repitation my word !!!                        
        elif 'repeat my word' in query:
            speak("Speak sir !")
            repeat = takecommand()
            speak(f"You said :-{repeat}")   
            
        elif "open camera" in query: 
            main_camera()     
        elif "track face" in query:
            main_track()
        elif "track movement" in query or "tracking movement" in query:
            main_movement()
        elif "take a photo" in query:
            take_a_photo()  
        elif "create a folder" in query:
            create_a_folder() 
        elif "generate password" in query or "create a strong password" in query:
            Password()    
        elif "tell me some fun" in query or "tell me some fun fact" in query:
            fun_fact() 
        elif "translate" in query:
            translate() 
        elif "create a qr code" in query:
            QRcode()              
        elif "play song" in query or "play music" in query:
            music()
        elif "lock window" in query or "lock" in query:
            LOCK_WINDOWS()
        elif "remember that" in query:       #Juts ask for remember the thing which you want to say and it will save into txt file
            rememberMgs = query.replace("remember that","")
            speak("you tell me that remind that:"+rememberMgs)
            remember = open('C:\\Users\\subha\\Documents\\remember.txt','w')
            os.startfile("C:\\Users\\subha\\Documents\\remember.txt")
            remember.write(rememberMgs)
            remember.close()
        elif "what do you remember" in query:    #ask for the what you have remembered
            remember = open('C:\\Users\\subha\\Documents\\remember.txt','r')
            os.startfile("C:\\Users\\subha\\Documents\\remember.txt")
            speak("You tell me that" + remember.read())
        elif "sleep windows" in query:
            SLEEP_WINDOW()
        elif "shutdown window" in query:
            SHUTDOWN()
        elif  "restart window" in query:
            RESTART()
        elif "count face" in query or "couting face" in query:
            detect()    
        #open function in webbrowser
        
        elif "open google" in query:
            speak("ok sir")
            webbrowser.open("google.com")  
            speak("Opening Google") 
        elif "open youtube" in query:
            speak("ok sir")
            webbrowser.open("youtube.com") 
            speak("Opening YouTube") 
        elif "open instagram" in query:
            speak("ok sir")
            webbrowser.open("instagram.com")
            speak("Opening Instagram") 
        elif "open facebook" in query:
            speak("ok sir")
            webbrowser.open("facebook.com")
            speak("Opening Facebook") 
        elif "open netflix" in query:
            speak("Ok sir")
            webbrowser.open("Netflix.com")
            speak("Opening Netflix") 
        elif "open flipkart" in query:
            speak("Ok sir")
            webbrowser.open("Flipkart.com")
            speak("Opening Flipkart") 
        elif "open amazon" in query:
            speak("Ok sir")
            webbrowser.open("Amazon.com")
            speak("Opening Amazon") 
        elif "open spotify" in query:
            speak("Ok sir")
            webbrowser.open("Spotify.com")
            speak("Opening Spotify")
        elif "open whatsapp" in query:
            speak("Ok sir")
            webbrowser.open("WhatsApp.com")
            speak("Opening WhatsApp")        
        elif "open tradingview" in query:
            speak("ok sir")
            webbrowser.open("Tradingview.com")    
        elif "show my insta profile" in query:
            speak("ok sir")
            webbrowser.open("https://www.instagram.com/lucifer__0.5")    
        elif "where i am" in query or "can you tell me my current location" in query:
            webbrowser.open("https://www.google.co.in/maps/@21.7953725,87.279096,15z?entry=ttu")
            speak("Here the your current location")  
        elif "check weather" in query:
            speak('Searching...')
            webbrowser.open("https://www.msn.com/en-us/weather/forecast/in-Jaleswar,Odisha?loc=eyJsIjoiSmFsZXN3YXIiLCJyIjoiT2Rpc2hhIiwicjIiOiJCYWxlc3dhciIsImMiOiJJbmRpYSIsImkiOiJJTiIsImciOiJlbi11cyIsIngiOiI4Ny4yODQiLCJ5IjoiMjEuNzk0In0%3D&ocid=ansmsnweather&weadegreetype=F")
            speak("tack a look...")
            
        
        # open the system file 
                        
        if "open notepad" in query:
            npath = "C:\\Users\\subha\\Documents\\event.txt"
            speak("ok sir")
            os.startfile(npath)   
        elif "open word" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            speak("ok sir")
            os.startfile(npath)
        elif "open powerpoint" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            speak("ok sir")
            os.startfile(npath) 
        elif "open one note" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote.lnk"
            speak("ok sir")
            os.startfile(npath) 
        elif "open excel" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            speak("ok sir")
            os.startfile(npath)
        elif "open Wordpad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\WordPad.lnk"
            speak("ok sir")
            os.startfile(npath)        
        elif "open document" in query:
            npath = "C:\\Users\\subha\\OneDrive\\Documents"
            speak("ok sir")
            os.startfile(npath)
        elif "open download" in query:
            npath ="C:\\Users\\subha\\Downloads"
            speak("ok sir")
            os.startfile(npath)
        elif "open music" in query:
            npath ="C:\\Users\\subha\\Music"
            speak("ok sir")
            os.startfile(npath)  
        elif "open video" in query:
            npath = "C:\\Users\\subha\\Videos"
            speak("ok sir")
            os.startfile(npath)        
        elif "open Recroder" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Steps Recorder.lnk"
            speak("ok sir")
            os.startfile(npath) 
        elif "open recorder" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Steps Recorder.lnk"
            speak("ok sir")
            os.startfile(npath)           
        elif "open cmd" in query:
            npath = "C:\\Users\\subha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"   
            speak("ok sir")
            os.startfile(npath)
        elif "open command prompt" in query:
            npath = "C:\\Users\\subha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"   
            speak("ok sir")
            os.startfile(npath)    
        elif "open on screen keyboard" in query:
            npath = "C:\\Users\\subha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessibility\\On-Screen Keyboard.lnk"
            speak("ok sir")
            os.startfile(npath)
        elif "open keyboard" in query:
            npath = "C:\\Users\\subha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessibility\\On-Screen Keyboard.lnk"
            speak("ok sir")
            os.startfile(npath)    
            
        #YouTube control command
          
        elif "stop" in query:
         keyboard.press('k')
         
        elif "pause" in query:
         keyboard.press('k')
         
        elif "restart" in query:
         keyboard.press('0')
         
        elif "mute" in query:
         keyboard.press('m') 
                               
        elif "full screen" in query:
         keyboard.press('f')
                 
        elif "Mini player" in query:
         keyboard.press('i')
                 
        elif "Expand" in query:
         keyboard.press('i')
                 
        elif "cinema mode" in query:
         keyboard.press('t')
                                        
        elif "close Subtitles" in query:
         keyboard.press('c')
                 
        elif "exit full scereen" in query:
         keyboard.press('Esc')   
              
        elif "play" in query:
         keyboard.press('k')   
              
        elif "Previous video" in query:
         keyboard.press_and_release('shift+ p') 
                
        elif "next video" in query or "play next video" in query:
         keyboard.press_and_release('shift + n')        
     
        #control MS-Woerd
        
        elif "copy" in query or "copy the selected the text" in query:
            keyboard.press_and_release('ctrl + c') 
            speak("copied!") 
            
        elif "paste" in query or  "Paste the text" in query:
            keyboard.press_and_release('ctrl + v')  
            speak("Done")
            
        elif "save" in query or  "Save the file" in query:
            keyboard.press_and_release('ctrl + s')
            speak("File Saved ")
          
        elif "cut" in query or  "Cut the selected text" in query:
            keyboard.press_and_release('ctrl + x')
            speak("Done")
           
        elif "undo" in query:
            keyboard.press_and_release('ctrl +z')
            speak("Done")
            
        elif "redo" in query:
            keyboard.press_and_release('ctrl + Y')
            speak("Done") 
         
        elif "print" in query or "print the document" in query:
            keyboard.press_and_release('ctrl + p')
            speak("Ok sir")
            speak("Would you like to print then click the print button Please")           
        
        elif "new file" in query or "create a new file" in query:
            speak("creating a new file")
            keyboard.press_and_release('ctrl + n')
            speak("Done")
            
        elif "selected all text" in query or "select all texted" in query:
            keyboard.press_and_release('ctrl + a')
            speak("Done")
        
        elif "paste and save" in query:
            keyboard.press_and_release('ctrl + v')
            keyboard.press_and_release('ctrl + s')
            speak("Done sir")  
            
        elif "close" in query:
            keyboard.press_and_release('alt + f4')           
          
     
        elif "voice type" in query or "voice typing" in query:
            keyboard.press_and_release('win + h')
            
        elif "open setting" in query:
            speak ("opening") 
            keyboard.press_and_release('win + u') 
            
        elif "hide desktop" in query:
            keyboard.press_and_release('win + d')
            
        elif "open game bar" in query:
            speak("Ok sir")
            keyboard.press_and_release('win + g')   
             