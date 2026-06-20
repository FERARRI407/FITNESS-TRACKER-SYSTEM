<<<<<<< HEAD
﻿# Fitness Tracker System

FastAPI backend with SQLAlchemy models and basic frontend skeleton.

Run:

pip install -r requirements.txt
uvicorn backend.app:app --reload

Set DATABASE_URL and SECRET_KEY via environment variables for production.

---

Project Specification
=====================

1. Project Title

Fitness Tracker System

2. Problem Statement

Many people want to maintain a healthy lifestyle, but they struggle to consistently track workouts, monitor progress, manage fitness goals, and analyze their performance over time. Traditional methods such as notebooks or spreadsheets are inefficient and lack analytical insights.

The Fitness Tracker System provides a centralized platform where users can record workouts, monitor fitness activities, track calories burned, set goals, and visualize progress through dashboards and reports.

3. Project Objective

- Help users track daily fitness activities.
- Store workout and health-related data securely.
- Provide progress monitoring and performance analysis.
- Allow users to set and manage fitness goals.
- Offer a user-friendly web interface for managing fitness records.
- Generate fitness statistics through dashboards.

4. Target Users

1. Fitness Enthusiasts
2. Gym Members
3. Personal Trainers
4. Health-Conscious Individuals
5. Beginners Starting Their Fitness Journey

5. Main Features

User Management
- User Registration
- User Login
- User Profile Management

Workout Management
- Add Workout
- View Workouts
- Edit Workout
- Delete Workout

Goal Tracking
- Set Fitness Goals
- Update Goals
- Track Goal Progress

Dashboard & Analytics
- Daily Activity Summary
- Weekly Progress Reports
- Calories Burned Statistics
- Workout History

Search & Filter
- Search Workouts
- Filter by Date
- Filter by Workout Type

6. Frontend Pages

1. Home Page — Introduce the system and features
2. About Page — Explain project details
3. Register/Login Page — User registration and authentication
4. Dashboard Page — Statistics and goals
5. Workout Management Page — Add/view/edit/delete workouts
6. Goal Tracking Page — Set and track goals
7. Profile Page — Manage user information

7. Backend API Endpoints

Authentication APIs
- POST /register — Register new user
- POST /login — User login

User APIs
- GET /users/{id} — View user profile
- PUT /users/{id} — Update profile

Workout APIs
- POST /workouts — Add workout
- GET /workouts — View all workouts
- GET /workouts/{id} — View single workout
- PUT /workouts/{id} — Update workout
- DELETE /workouts/{id} — Delete workout

Goal APIs
- POST /goals — Create goal
- GET /goals — View goals
- PUT /goals/{id} — Update goal
- DELETE /goals/{id} — Delete goal

Analytics APIs
- GET /dashboard/stats — Dashboard statistics
- GET /workouts/search — Search workouts
- GET /workouts/filter — Filter workouts

Total APIs: 15+

8. Database Choice

Recommended: PostgreSQL. For local development we support SQLite.

9. Database Tables

Users (id, name, email, password, age, weight, created_at)
Workouts (workout_id, user_id, workout_type, duration_minutes, calories_burned, workout_date)
Goals (goal_id, user_id, goal_name, target_value, current_progress, deadline)

10. Technology Stack

Frontend: HTML5, CSS3, JavaScript
Backend: FastAPI, Python
Database: PostgreSQL (SQLite for local)
ORM: SQLAlchemy
Auth: JWT

11. Deployment Plan

Frontend: Netlify
Backend: Render
Database: Supabase/Postgres

12. Expected Output

- Register/login securely
- Add/manage workouts
- Set personal fitness goals
- Track calories and durations
- View dashboard statistics

13. Future Enhancements

- BMI Calculator, Water Intake, Sleep Monitoring, AI recommendations, Mobile app

---

If you want this README adjusted (shorter/longer or converted to markdown sections), tell me which parts to keep or remove.
=======
# FITNESS-TRACKER-SYSTEM
>>>>>>> 7e32ba1f2047a37392938815b18ee1ed59fda26e
