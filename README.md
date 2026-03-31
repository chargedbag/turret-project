# 🎯 Vision-Based Pan-Tilt Turret

A real-time object tracking turret using OpenCV and proportional control, communicating with an Arduino for servo actuation.

---

## 🧠 System Overview

Camera → Detection → Error → Control → Serial → Arduino → Servos

---

## ⚙️ Features

* Real-time face tracking
* Smooth servo control (P-control)
* Serial communication with Arduino
* Modular code structure

---

## 🚀 Run

```bash
pip install -r requirements.txt
python src/main.py
```

---

## 🔌 Hardware

* Arduino Nano
* MG996R servos (pan + tilt)
* External 5V power supply
* Webcam

---

## 🎥 Demo

See `/demo/demo.mp4`
