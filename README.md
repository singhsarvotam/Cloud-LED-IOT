# Car-IoT-and-Smart-Home-Devices
Design a simulation for Car IoT service which controls various smart home devices based on real time GPS location from a smart phone


Project Description:
---------------------
1. Wrote a script which ran as demon on Raspberry Pi for generating GPS information using real time location from a smart phone.
2. Wrote another script which ran on Raspberry Pi to generate RPM information and Air Flow Rate information.
3. A demon on Raspberry Pi that gathers GPS, RPM, and Air Flow Rate information and sends status reports to cloud platform periodically.
4. A demon on our cloud IoT system storing the status reports and sending GPS information to Raspberry Pi. 
5. A demon on Raspberry Pi that turns on/off LED lights when GPS information is close to certain point.


Project Environment:
---------------------
Python 2.7, Ubuntu 16.04 (Xenial), Apache Flask, MySql, MQTT Protocol, Mosquitto message broker, HTML, CSS, CanaKit Raspberry Pi 3 Kit (32 GB), Amazon EC2, a smart phone
