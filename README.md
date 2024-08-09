# IoT-Enabled Pedestrian Traffic Light Control System
## Overview
An IoT-enabled pedestrian traffic light control system using an Arduino developed as a part of University Project. This system aims to improve pedestrian safety and traffic management at crossings. It utilizes an Arduino board to control LEDs which represent the traffic and pedestrian lights, and a push button to trigger the crossing sequence.

## Features
- Arduino Controlled: Utilizes Arduino UNO for easy replication and modification.
- LED Traffic Signals: Red, yellow, and green LEDs for car traffic, and red and green LEDs for pedestrian signals.
- Push Button Operation: Allows pedestrians to control when they cross based on traffic flow.
- Software Debouncing: Ensures the system handles button presses accurately.
- Scalable: Code and design can be adapted for multiple intersections or more complex scenarios.
  
## Components Needed
- Arduino UNO , Breadboard and connecting wires, LEDs (2 red, 1 yellow, 1 green for traffic, 1 red and 1 green for pedestrians), Resistor 220 ohms for each LED, Push button, USB cable to connect Arduino to PC, Circuit Diagram.
- Please refer to the CircuitDiagram.png in this repository to see how to connect the LEDs, button, and Arduino.

## Note :
- Make sure to replace the placeholder for setting changeTime with changeTime = millis(); at the end of the changeLights() function to update the timing correctly. This ensures the timing mechanism resets properly after each cycle.
