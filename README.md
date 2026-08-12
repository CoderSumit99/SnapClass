# SnapClass

**An AI-powered attendance management system using face and voice recognition**

Automate classroom attendance with dual biometric identification — built with Python, Streamlit, and Supabase.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/github/license/CoderSumit99/SnapClass?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/CoderSumit99/SnapClass?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/CoderSumit99/SnapClass?style=flat-square)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Application Workflow](#application-workflow)
- [Face Recognition](#face-recognition)
- [SVM Classification](#svm-classification)
- [Voice Recognition](#voice-recognition)
- [Bulk Audio Processing](#bulk-audio-processing)
- [Password Security](#password-security)
- [Database](#database)
- [Attendance Workflow](#attendance-workflow)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Main Dependencies](#main-dependencies)
- [Roadmap](#roadmap)
- [Key Learnings](#key-learnings)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

**SnapClass** is an AI-powered attendance management system built using Python and Streamlit. It enables teachers to manage classes and automate student attendance through **face recognition** and **voice recognition** pipelines.

The project was developed to demonstrate practical experience in Python application development, machine learning, biometric recognition systems, database integration, authentication, session management, and AI-based automation.

---

## Features

| Category | Capabilities |
|---|---|
| User Roles | Separate teacher and student workflows |
| Authentication | Secure login with bcrypt-based password hashing |
| Class Management | Teacher-side class creation and student enrollment |
| Enrollment | Join-code based and QR-code based class enrollment |
| Face Recognition | Face detection, embedding generation, and SVM-based classification |
| Voice Recognition | Speaker identification via voice embeddings |
| Attendance | Automated attendance workflow from face or voice input |
| Database | Supabase integration for persistent data storage |
| Interface | Streamlit-based web UI with session-managed login |

---

## Tech Stack

**Application:** Python, Streamlit

**Database:** Supabase

**Face Recognition:** dlib, face_recognition_models, Scikit-learn, SVM

**Voice Recognition:** Librosa, Resemblyzer

**Data Processing:** NumPy, Pandas, Pillow

**Security & Utilities:** bcrypt, Segno

---

## Architecture

SnapClass follows a **layered architecture** with separate AI pipelines for face and voice recognition.

```text
                         User
                    /           \
               Teacher         Student
                  │               │
                  └───────┬───────┘
                          │
                          ▼
                    Streamlit App
                          │
                          ▼
                 Application Logic
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
       Authentication   Face AI      Voice AI
             │            │            │
             │        Embedding    Embedding
             │            │            │
             └────────────┼────────────┘
                          │
                          ▼
                       Supabase
```

**Face recognition flow:**

```text
Classroom Image → Face Detection → Face Embedding → SVM Classifier → Student Identification → Attendance
```

**Voice recognition flow:**

```text
Classroom Audio → Audio Processing → Speech Segmentation → Voice Embedding → Similarity Comparison → Speaker Identification → Attendance
```

---

## Application Workflow

### User Authentication

SnapClass provides separate workflows for teachers and students. After login, Streamlit session state maintains the user's login type and renders the corresponding dashboard.

```text
User → Login → Authentication → Session State → Teacher Dashboard / Student Dashboard
```

### Class Enrollment

Teachers create classes and share a join code; students use this code to enroll. The application also reads join codes directly from URL query parameters.

```text
Teacher → Create Class → Join Code → Share Code / Link → Student → Join Class
```

Example:

```text
?join_code=ABC123
```

The application detects the join code from the URL and initiates the enrollment process automatically.

---

## Face Recognition

Face recognition is one of SnapClass's core AI components, using dlib-based models to detect faces and generate numerical embeddings.

```text
Student Face → Face Detection → Face Embedding → SVM Classifier → Student Identification
```

**Face embeddings:** A face embedding is a numerical representation of a person's face. Each detected face is converted into a 128-dimensional embedding vector.

```text
Face → Face Recognition Model → [0.23, 0.78, -0.41, ...]
```

These embeddings are used as input features for the machine learning classifier that identifies students.

---

## SVM Classification

SnapClass uses a **Support Vector Machine (SVM)** for face classification.

**Training:** Registered student face embeddings serve as features, with corresponding student identities as labels.

```text
Registered Student Faces → Face Embeddings → SVM Training → SVM Model
```

**Inference (attendance):**

```text
New Face → Face Embedding → SVM Model → Student Prediction
```

An embedding-distance threshold is applied to reject weak or incorrect matches, improving classification reliability.

---

## Voice Recognition

SnapClass includes a complementary voice recognition pipeline built with:

- **Librosa** for audio processing
- **Resemblyzer** for generating voice embeddings

```text
Audio Recording → Librosa Processing → Speech Segmentation → Voice Embedding → Similarity Comparison → Speaker Identification
```

**Voice embeddings:** A voice embedding is a numerical representation of a person's voice, generated using Resemblyzer's `VoiceEncoder`.

```text
Voice → Resemblyzer → Voice Embedding → Compare With Stored Embeddings → Speaker Identification
```

The generated embedding is compared against stored embeddings using a similarity score to identify the speaker.

---

## Bulk Audio Processing

SnapClass can process longer classroom recordings by segmenting audio into individual speech clips, enabling multi-speaker identification from a single recording.

```text
Classroom Audio → Speech Segmentation → Audio Segments → Voice Embeddings → Speaker Matching → Identified Students
```

---

## Password Security

User passwords are secured using **bcrypt** hashing rather than being stored in plain text.

```text
Password → bcrypt → Password Hash → Database
```

---

## Database

**Supabase** serves as the database and backend service for SnapClass, storing data related to:

- Students
- Teachers
- Classes
- Attendance records
- Face recognition data
- Voice recognition data

---

## Attendance Workflow

**Face-based attendance:**

```text
Teacher → Classroom Image → Face Detection → Face Embedding → SVM Classification → Student Identification → Attendance
```

**Voice-based attendance:**

```text
Teacher → Classroom Audio → Speech Segmentation → Voice Embedding → Similarity Matching → Speaker Identification → Attendance
```

---

## Project Structure

```text
SnapClass/
├── src/                  Core application modules
├── app.py                Main Streamlit entry point
├── requirements.txt      Python dependencies
├── runtime.txt           Runtime configuration
└── .gitignore
```

---

## Installation

**Prerequisites:** Python 3.x and a Supabase project with the required credentials.

```bash
# 1. Clone the repository
git clone https://github.com/CoderSumit99/SnapClass.git
cd SnapClass

# 2. Create a virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# Set up the required Supabase and application credentials
# according to your project configuration.

# 5. Start the application
streamlit run app.py
```

**Security note:** Do not commit API keys, passwords, database credentials, or other secrets to version control.

---

## Main Dependencies

| Package | Purpose |
|---|---|
| Streamlit | Web application interface |
| Supabase | Database and backend service |
| bcrypt | Password hashing |
| dlib | Face detection and recognition |
| face_recognition_models | Pretrained face recognition models |
| Scikit-learn | Machine learning and SVM classification |
| Librosa | Audio processing |
| Resemblyzer | Voice embedding generation |
| NumPy | Numerical processing |
| Pandas | Data processing |
| Pillow | Image processing |
| Segno | QR code generation |

---

## Roadmap

- [ ] Real-time classroom face recognition
- [ ] Improved recognition under varying lighting conditions
- [ ] Better handling of partially visible faces
- [ ] More robust voice recognition in noisy classrooms
- [ ] Attendance analytics and reports
- [ ] Student attendance history view
- [ ] Teacher analytics dashboard
- [ ] Improved scalability for larger classrooms
- [ ] Real-time attendance via live classroom cameras

---

## Key Learnings

This project provided hands-on experience with:

- Python application development and Streamlit
- Supabase integration for backend and database services
- Authentication and session management
- Face recognition and face embedding generation
- Machine learning with Support Vector Machines
- Audio processing and voice embedding generation
- Speaker identification techniques
- AI-based attendance automation
- End-to-end database integration

---

## Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

**Sumit**
GitHub: [@CoderSumit99](https://github.com/CoderSumit99)

---

*An AI-focused attendance management project built to gain practical experience with Python, Streamlit, machine learning, face recognition, voice recognition, Supabase, and AI-based automation.*
