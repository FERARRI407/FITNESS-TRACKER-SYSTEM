from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Fitness Tracker System"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple working endpoints
@app.get("/")
def home():
    return {"message": "Fitness Tracker API Running Successfully"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# Mock Auth Endpoints
@app.post("/register")
def register():
    return {"message": "User registered successfully"}

@app.post("/login")
def login():
    return {"access_token": "mock-token", "token_type": "bearer"}

# Mock User Endpoints
@app.get("/users")
def get_users():
    return [{"user_id": 1, "username": "john_doe", "email": "john@example.com"}]

# Mock Goals Endpoints
@app.get("/goals")
def get_goals():
    return [{"goal_id": 1, "target_weight": 75.0, "target_calories": 2500.0}]

# Mock Dashboard Endpoint
@app.get("/dashboard")
def dashboard():
    return {
        "users": 1,
        "workouts": 5,
        "goals": 2,
        "progress": 10,
        "meals": 15
    }

# Mock Workouts Endpoints
@app.get("/workouts")
def get_workouts():
    return [{"workout_id": 1, "workout_type": "Running", "duration": 30, "calories_burned": 300.0}]

@app.post("/workouts")
def create_workout():
    return {"message": "Workout created successfully"}

# Mock Progress Endpoints
@app.post("/progress")
def add_progress():
    return {"message": "Progress recorded successfully"}

# Mock Meals Endpoints
@app.post("/meals")
def create_meal():
    return {"message": "Meal created successfully"}

# --- Additional endpoints matching spec (mocked stores) ---
from typing import Optional
from fastapi import Body

# In-memory stores (mock)
USERS = [{"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30, "weight": 80}]
WORKOUTS = [{"workout_id": 1, "user_id": 1, "workout_type": "Running", "duration_minutes": 30, "calories_burned": 300, "workout_date": "2026-06-01"}]
GOALS = [{"goal_id": 1, "user_id": 1, "goal_name": "Lose Weight", "target_value": 75, "current_progress": 80, "deadline": "2026-12-31"}]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in USERS:
        if u["id"] == user_id:
            return u
    return {"detail": "User not found"}


@app.put("/users/{user_id}")
def update_user(user_id: int, payload: dict = Body(...)):
    for u in USERS:
        if u["id"] == user_id:
            u.update(payload)
            return {"message": "User updated", "user": u}
    return {"detail": "User not found"}


@app.get("/workouts/{workout_id}")
def get_workout(workout_id: int):
    for w in WORKOUTS:
        if w["workout_id"] == workout_id:
            return w
    return {"detail": "Workout not found"}


@app.put("/workouts/{workout_id}")
def update_workout(workout_id: int, payload: dict = Body(...)):
    for w in WORKOUTS:
        if w["workout_id"] == workout_id:
            w.update(payload)
            return {"message": "Workout updated", "workout": w}
    return {"detail": "Workout not found"}


@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    for i, w in enumerate(WORKOUTS):
        if w["workout_id"] == workout_id:
            WORKOUTS.pop(i)
            return {"message": "Workout deleted"}
    return {"detail": "Workout not found"}


@app.post("/goals")
def create_goal(payload: dict = Body(...)):
    new_id = max([g["goal_id"] for g in GOALS] or [0]) + 1
    payload["goal_id"] = new_id
    GOALS.append(payload)
    return payload


@app.put("/goals/{goal_id}")
def update_goal(goal_id: int, payload: dict = Body(...)):
    for g in GOALS:
        if g["goal_id"] == goal_id:
            g.update(payload)
            return {"message": "Goal updated", "goal": g}
    return {"detail": "Goal not found"}


@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int):
    for i, g in enumerate(GOALS):
        if g["goal_id"] == goal_id:
            GOALS.pop(i)
            return {"message": "Goal deleted"}
    return {"detail": "Goal not found"}


@app.get("/dashboard/stats")
def dashboard_stats():
    return {
        "total_users": len(USERS),
        "total_workouts": len(WORKOUTS),
        "total_goals": len(GOALS)
    }


@app.get("/workouts/search")
def search_workouts(q: Optional[str] = None):
    if not q:
        return WORKOUTS
    return [w for w in WORKOUTS if q.lower() in w.get("workout_type", "").lower()]


@app.get("/workouts/filter")
def filter_workouts(user_id: Optional[int] = None, workout_type: Optional[str] = None):
    results = WORKOUTS
    if user_id:
        results = [w for w in results if w.get("user_id") == user_id]
    if workout_type:
        results = [w for w in results if w.get("workout_type") == workout_type]
    return results

