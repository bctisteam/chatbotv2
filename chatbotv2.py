import pygame
import sys
from pygame.locals import *
import os
import time
import playsound
import sounddevice #somehow hides alsa and jack errors
import speech_recognition as sr
from gtts import gTTS
import numpy
import datetime

#initialize components

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("ChatBot")
screen =  pygame.display.set_mode((1370,389),pygame.FULLSCREEN ,pygame.NOFRAME)
#screen =  pygame.display.set_mode((1370,589),0,32)

bfont = pygame.font.SysFont(None,200)
sfont = pygame.font.SysFont(None,50)
font = pygame.font.SysFont(None,90)

def draw_text(text, font, colour, surface, x, y):
    textobj = font.render(text ,font ,colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj,textrect)
    
def speak(text): #saving user input in wav audio file
        tts = gTTS(text=text, lang="en")
        filename = "voice.wav"
        tts.save(filename)
        playsound.playsound(filename)
    
click = False
def get_audio(): #getting user input
    said = ""
    try:
        r = sr.Recognizer()
        print("Microphone Active.") #indicate mic active
        with sr.Microphone() as source:
            # timeout is the number of seconds it will wait for you to say something before it stops listening
            # phrase_time_limit is the maximum number of seconds that a phrase can be
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            said = r.recognize_google(audio)
    except sr.WaitTimeoutError:
        print("You did not say anything or I could not hear you.")
    except Exception as e:
        print(e)
    finally:
        # This block of code will run no matter what,
        # whether an exception is thrown or not.
        print(f"Speech recorded: '{said}' ")
        # return the text that was heard in lowercase
        # as there might be rare occasions where the text is not in lowercase
        # such as "3D printing" instead of "3d printing"
    return said.lower()
    
def main_menu():
    click = False    
    while True:
        img = pygame.image.load('/home/kalremo/ai screen.jpg').convert()
        img = pygame.transform.smoothscale(img,screen.get_size())
        imgrect = img.get_rect()
        screen.blit(img, imgrect)
        draw_text("Introducing",bfont, (184,167,209),screen, 800,400)
        draw_text("ChatBot",bfont, (184,167,209),screen, 1100,550)
         
        
        mx, my = pygame.mouse.get_pos()
        
        settings_bttn = pygame.Rect(850, 750, 200, 50)
        devices_bttn = pygame.Rect(1150, 750, 200, 50)
        faq_bttn = pygame.Rect(1450, 750, 200, 50)
        
        if settings_bttn.collidepoint((mx,my)):
            if click:
                settings()
        if devices_bttn.collidepoint((mx,my)):
            if click:
                devices()
        if faq_bttn.collidepoint((mx,my)):
            if click:
                faq()
        
        pygame.draw.rect(screen, (161, 142, 191), settings_bttn)
        pygame.draw.rect(screen, (161, 142, 191), devices_bttn)
        pygame.draw.rect(screen, (161, 142, 191), faq_bttn)
        
        draw_text("Settings",sfont, (41,34,51),screen, 880,760)
        draw_text("Devices",sfont, (41,34,51),screen, 1185,760)
        draw_text("FAQs",sfont, (41,34,51),screen, 1505,760)
        
        click = False

        text = get_audio()
    
        if "chatbot" in text:
            start_listening = datetime.datetime.now()
            done_listening = start_listening + datetime.timedelta(seconds=10)
            while done_listening > datetime.datetime.now():
                draw_text("Say Something!",sfont, (184,167,209),screen, 830,700)
                commands()
    
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()
        mainClock.tick(60)
def settings():
    running = True
    click = False
    while running:
        screen.fill((211,206,219))
        draw_text("Settings",font, (41,34,51),screen, 840,80)
        
        mx, my = pygame.mouse.get_pos()
        
        back_bttn = pygame.Rect(1250, 850, 200, 50)
        
        if back_bttn.collidepoint((mx,my)):
            if click:
                running = False
                
        pygame.draw.rect(screen, (161, 142, 191), back_bttn)
        draw_text("Back",sfont, (41,34,51),screen, 1305,860)
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        pygame.display.update()
        mainClock.tick(60)
        
def devices():
    running = True
    click = False
    while running:
        screen.fill((211,206,219))
        draw_text("Devices",font, (41,34,51),screen, 830,80)
        mx, my = pygame.mouse.get_pos()
        
        back_bttn = pygame.Rect(1250, 850, 200, 50)
        
        if back_bttn.collidepoint((mx,my)):
            if click:
                running = False
                
        pygame.draw.rect(screen, (161, 142, 191), back_bttn)
        draw_text("Back",sfont, (41,34,51),screen, 1305,860)
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
          
        pygame.display.update()
        mainClock.tick(60)

def faq():
    running = True
    click = False
    while running:
        screen.fill((211,206,219))
        draw_text("Frequently Asked Questions",font, (41,34,51),screen, 560,80)
        mx, my = pygame.mouse.get_pos()
        
        back_bttn = pygame.Rect(1250, 850, 200, 50)
        
        if back_bttn.collidepoint((mx,my)):
            if click:
                running = False
                
        pygame.draw.rect(screen, (161, 142, 191), back_bttn)
        draw_text("Back",sfont, (41,34,51),screen, 1305,860)
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
          
        pygame.display.update()
        mainClock.tick(60)

def commands():
    
    #GREETINGS
    text = get_audio()
    if "hello" in text:
        speak("Hello there human. How may I help you?")
    

    if ("introduce yourself" in text) or ("who are you" in text) or ("what are you" in text):
        speak("Hello, my name is Chatbot. I am an AI robot created by STEAM members in 2024. You can ask me questions about the BCTI. ")
    

    if ("bye" in text) or ("they are leaving" in text):
        speak("Good-bye human. It was nice talking to you")

    
    #IMPORTANT LOCATIONS WITH DESCRIPTIONS 
    if ("steam lab" in text) or ("Steam" in text): 
        speak("The STEAM Lab is located on the second floor at CTI 215. There are other projects there like PuzzleBot, DrawBot, BuzzMe, and the MPS station") 

    if ("3d printing" in text) or ("additive" in text) or ("javelin" in text): 
        speak("the javelin additive manufacturing lab is located on the second floor at cti 216. you can see that there are 3d printed models, 3d printers, and a laser cutting machine.") 

    if ("c p factory" in text) or ("festo" in text): 
        speak("the cp factory is located on the first floor at cti 117. there, automated guided vehicles are occasionally driving across the room to aid .") 

    if ("magna" in text) or ("skills" in text) or ("mechatronics" in text): 
        speak("the magna mechatronics skills training room is located on the second floor at cti 210. here students are able to learn to program and build small scale versions of industrial factories.") 

    if ("atrium" in text) or ("demonstration" in text) or ("event" in text): 
        speak("the Main Atrium is located on the first floor at CTI 107 and the demonstration room is located CTI 108. Many event are held in these areas.") 

    if "prototyping" in text: 
        speak("The Product Prototyping Facility is located in the machine shop at CTI 110. This facility contains specialized and traditional machining equipment that will enable users to bring ideas and concepts to life by transforming digital files into tangible models, prototypes and proof-of-concepts.") 

    if "gaming" in text: 
        speak("The Gaming zone is located on the second floor at CTI 209. here the humber esports team train") 

    if "indigenous" in text: 
        speak("The Indigenous Cultural Marker is located on the second floor. This sculpture is a representation of our entire life and the central piece that links this life is symbolic of the spirit.") 

    if ("kuka" in text) or ("automation" in text): 
        speak("The Kuka Advanced Automation Lab is located in the fourth floor at CTI 409. This lab is equipped with robotics technology dedicated to the collaboration of industry, faculty members and students on robotics systems integration applications.") 

    if ("s e w" in text) or ("eurodrive" in text): 
        speak("The S E W-Eurodrive Innovation Lab is located in the second floor at CTI 221 where it demonstrates how humans, technology, and machines collaborate on the production line. The laboratory focuses on Automated Guided Vehicles for assembly, production and distribution logistics. ") 

    if ("capstone" in text) or ("projects" in text): 
        speak("the capstone projects room is located on the fourth floor at CTI 215 and CTI 216. these rooms are for students to complete their industrial capstone projects.") 

    if "sick" in text: 
        speak("the Sick sensor lab is located on the third floor at CTI 316 A. this lab is used to deliver training on SICK Vison Sensor Technologies. ") 

    if ("cisco" in text) or ("digital" in text): 
        speak("The Cisco Digital Transformation Zone is located on the fourth floor at CTI 410. The data centre provides critical services to support a wide range of projects and innovation activities in the capacity of Internet of Things (IoT), and digital transformation. It allows for end-user project connectivity for capstone projects, applied research, and industry activities.")

    
    #JOKES 
    if "tell me a joke" in text:
        jokes = [
                "Why was Cinderella so bad at soccer? She kept running away from the ball!",
                "What do you call a well-balanced horse? Stable.",
                "Why did the bicycle fall over? Because it was two-tired!",
                "What did the triangle say to the circle? You are pointless.",
                "Why are balloons so expensive? Inflation!",
                "What did the ocean say to the beach? Nothing, it just waved.",
                "Why did the programmer quit their job? Because they didn't get arrays",
                "Why do programmers prefer dark mode? Because light attracts bugs.",
                "How does the moon cut its hair? Eclipse it.",
                "Why can't you trust an atom? Because they make everything up.",
                "What did one wall say to the other? I'll meet you at the corner.",
                "What do you call a poor Santa Claus? Saint Nickel-less",
                "What is the most used language in programming? Profanity.",
                "Why did the robot go to the shoe shop? To get re-booted.",
                "Binary: It's as easy as 01, 10, 11",

                #Add more jokes here (don't forget the comma at the end of each joke! )
            ]
        joke_choice = numpy.random.randint(0, len(jokes))
        speak(jokes[joke_choice]) 

#FUN FACTS
    if ("fact" in text) or ("tell me a fact" in text) or ("fun fact" in text):
        facts =  [
            "A single ant can carry fifty time its own body weight.",
            "The Earth's core is as hot as the surface of the Sun.",
            "Dolphins sleep with one eye open.",
            "The shortest war in history lasted only 38 minutes.",
            "The human brain takes in 11 million bits of information every second but is aware only of 40.",
             #Add more fun facts here (don't forget the comma at the end of each fun fact! )
            ]
        fact_choice = numpy.random.randint(0, len(facts))
        speak(facts[fact_choice])
main_menu()

