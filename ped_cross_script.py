# -*- coding: utf-8 -*-
"""Ped_cross_script.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YO073K3GpsyXgkeVBTn91LL3uXYVLv29
"""

int carRed = 12;
int carYellow = 11;
int carGreen = 10;
int pedRed = 9;
int pedGreen = 8;
int button = 2;
int crossTime = 5000;
unsigned long changeTime;

void setup() {
    Serial.begin(9600);
    pinMode(carRed, OUTPUT);
    pinMode(carYellow, OUTPUT);
    pinMode(carGreen, OUTPUT);
    pinMode(pedRed, OUTPUT);
    pinMode(pedGreen, OUTPUT);
    pinMode(button, INPUT);
    digitalWrite(carGreen, HIGH);
    digitalWrite(pedRed, HIGH);
}

void loop() {
    int state = digitalRead(button);
    if (state == HIGH && (millis() - changeTime) > 5000) {
        changeLights();
    }
}

void changeLights() {
    Serial.println("carGreen on");
    Serial.println("pedRed on");
    digitalWrite(carGreen, LOW);
    Serial.println("carGreen off");
    Serial.println("carYellow on");
    digitalWrite(carYellow, HIGH);
    delay(2000);
    digitalWrite(carYellow, LOW);
    Serial.println("carYellow off");
    digitalWrite(carRed, HIGH);
    Serial.println("carRed on");
    delay(1000);
    digitalWrite(pedRed, LOW);
    Serial.println("pedRed off");
    digitalWrite(pedGreen, HIGH);
    Serial.println("pedGreen on");
    delay(crossTime);

    for (int x = 0; x < 10; x++) {
        digitalWrite(pedGreen, HIGH);
        delay(250);
        digitalWrite(pedGreen, LOW);
        delay(250);
    }
    digitalWrite(pedRed, HIGH);
    Serial.println("pedRed on");
    delay(500);
    digitalWrite(carYellow, HIGH);
    Serial.println("carYellow on");
    digitalWrite(carRed, LOW);
    Serial.println("carRed off");
    delay(1000);
    digitalWrite(carGreen, HIGH);
    Serial.println("carGreen on");
    digitalWrite(carYellow, LOW);
    Serial.println("carYellow off");
    changeTime = millis();
}