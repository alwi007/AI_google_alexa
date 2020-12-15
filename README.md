# alwi007-ai_google_alexa
I tried to create a home AI protype with both Google Assistant &amp; ALexa intelligence.

Design of the System

For the Home Automation:

We required a fully functional Raspberry Pi 3 with Raspbian OS installed on it. The main reason which I selected Google Assistant for the Home Automation is we can control all the Home Appliances from anywhere around the world using our Smartphone just with the ease of a click.

Install the following software & necessary library:

    Thorny Python IDE

    Adafruit_IO Library

    Google Assistant on Smartphone

    IFTTT Mobile App (Optional)

Interfacing of Google Voice Assistant with Adafruit_IO :

Google voice Assistant has been interfaced with Adafruit_IO using the cloud service – IFTTT (If This Then That). IFTTT is the cloud service which helps to continuously monitor the IoT devices. If it receives any command from the user via services or devices like Google voice assistant, Alexa Voice services etc, they provide the triggering command to MQTT services like Adafruit_IO to do the task.

MQTT Settings in Adafruit_IO

I have used Adafruit_IO as the MQTT service for the monitoring & data exchange medium. Toggle blocks needs to be setup in Adafruit_IO for the trigger & monitoring purposes. After all the setup Adafruit will be communicating to the Raspberry Pi through the Python code for triggering (ON/OFF function) the devices inside home.

After successful installation of every software & library. Shutdown the raspberry pi 3 and connect the LED’s, Resistors as shown in fig.2. Then open the Thonny Python IDE & import required libraries.

Setting up of the circuit:

Devices which should be controlled needs to be connected to Raspberry Pi through Relays.

Note : For giving commands to Raspberry Pi, Google voice assistant needs to be installed in the smartphone & there should be an active data service on the smartphone.

For the Voice Assistant at home:

Alexa Voice Service (AVS) Device SDK has been implemented as the voice assistant on the Raspberry Pi. Same can be done by:

Register your device with Amazon.

Install and configure dependencies for the AVS Device SDK on your Raspberry Pi.
Build the SDK and run the sample app on your Raspberry Pi. Once the Raspberry Pi has been registered & created the security profile, a Json configuration file (CONFIG.JSON) can be downloaded which contains client ID and client secret code. This can be used for the authenticate the Raspberry Pi to interact with Alexa services.

Required components:

    USB microphone

    Speaker

Once the AVS Device SDK has been implemented in Raspberry Pi following the instructions, the next step is to launch the sample App using the command:

    ‘cd /home/pi/ sudo bash startsample.s’

The App can be activated with the wake word ‘Alexa’ & can start asking the questions.

Useful Links
Adafruit IO - https://io.adafruit.com
IFTTT - https://ifttt.com
Amazon Voice Service - https://developer.amazon.com/docs/alexa-voice-service/launch-sample-app.html
