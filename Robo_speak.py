import os

if __name__ == '__main__':
    print("Welcome to robo speaker 1.1. Created by Akash Rathod..")
    while True:
        x = input("Enter what you want to speak: ")
        if x == 'o':
            command = f'''powershell -Command "Add-Type -AssemblyName System.Speech; \
        (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{"bye bye my dear freind"}')"'''
            os.system(command) # for windows
          # command = f"say bye bye my dear freind" # for mac os
            break
        command = f'''powershell -Command "Add-Type -AssemblyName System.Speech; \
        (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"'''
        
        # command = f"say {x}" for mac os
        os.system(command)
