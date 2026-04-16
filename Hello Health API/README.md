# 🏥 Hello Health API — Day 1 of 20

> **FastAPI + SQLite | Beginner Project**
> Learn: Routes · Request/Response · Status Codes · CRUD · Pydantic · SQLAlchemy

---

## 📁 Project Structure

```
hello-health-api/
├── app/
│   ├── __init__.py
│   ├── main.py          ← FastAPI app entry point
│   ├── database.py      ← SQLite connection + session
│   ├── models.py        ← SQLAlchemy table definitions
│   ├── schemas.py       ← Pydantic request/response models
│   └── routers/
│       ├── __init__.py
│       ├── health.py    ← GET /health — ping & status
│       └── patients.py  ← Full CRUD for patients
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### Option 1 — Run Locally

```bash
# 1. Clone / enter project folder
cd hello-health-api

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the server
uvicorn app.main:app --reload

# 5. Open in browser
# http://localhost:8000/docs     ← Swagger UI (interactive)
# http://localhost:8000/redoc    ← ReDoc UI
```

### Option 2 — Run with Docker

```bash
# Build and start
docker-compose up --build

# Stop
docker-compose down

# Rebuild after code changes
docker-compose up --build --force-recreate
```

---

## 📡 API Endpoints

### Health Check

| Method | Endpoint        | Description           | Status Code |
|--------|-----------------|-----------------------|-------------|
| GET    | `/`             | Welcome message       | 200         |
| GET    | `/health`       | API health status     | 200         |
| GET    | `/health/ping`  | Simple ping           | 200         |

### Patients (CRUD)

| Method | Endpoint            | Description             | Status Code |
|--------|---------------------|-------------------------|-------------|
| POST   | `/patients/`        | Register new patient    | 201         |
| GET    | `/patients/`        | List all patients       | 200         |
| GET    | `/patients/{id}`    | Get one patient         | 200 / 404   |
| PATCH  | `/patients/{id}`    | Update patient fields   | 200 / 404   |
| DELETE | `/patients/{id}`    | Delete patient          | 204 / 404   |

---

## 🧪 Test the API

### Using curl

```bash
# Create a patient
curl -X POST http://localhost:8000/patients/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "age": 42,
    "blood_type": "O+",
    "condition": "Diabetes"
  }'

# Get all patients
curl http://localhost:8000/patients/

# Get patient by ID
curl http://localhost:8000/patients/1

# Update a patient
curl -X PATCH http://localhost:8000/patients/1 \
  -H "Content-Type: application/json" \
  -d '{"condition": "Controlled Diabetes"}'

# Delete a patient
curl -X DELETE http://localhost:8000/patients/1
```

### Using Swagger UI
1. Go to `http://localhost:8000/docs`
2. Click any endpoint → **Try it out** → **Execute**
3. No setup needed — runs in the browser

---

## 🧠 What You Learn in This Project

| Concept | Where to find it |
|---|---|
| FastAPI app setup | `app/main.py` |
| SQLite + SQLAlchemy | `app/database.py` |
| Database models | `app/models.py` |
| Pydantic validation | `app/schemas.py` |
| Route + status codes | `app/routers/patients.py` |
| HTTP 201, 204, 404 | `app/routers/patients.py` |
| Dependency injection | `Depends(get_db)` |
| Docker containerization | `Dockerfile` + `docker-compose.yml` |

---

## 🔑 Key Concepts Explained

### Why Pydantic schemas?
Pydantic validates incoming data automatically. If someone sends `age: "hello"` — FastAPI rejects it with a clear error before it ever touches your database.

### Why SQLAlchemy?
It lets you write Python instead of raw SQL. `db.add(patient)` is cleaner and safer than writing `INSERT INTO patients ...` manually.

### Why `Depends(get_db)`?
FastAPI's dependency injection opens a DB session per request and closes it cleanly after — even if an error occurs.

### Status codes used
| Code | Meaning | When |
|------|---------|------|
| 200 | OK | Successful GET / PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 404 | Not Found | Patient ID doesn't exist |
| 422 | Unprocessable | Invalid request data (Pydantic) |

---

## ➡️ Next: Day 2

**Personal Todo API** — same stack, adds in-memory vs persistent storage comparison, and introduces query parameters for filtering.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `fastapi` | Web framework |
| `uvicorn` | ASGI server |
| `sqlalchemy` | ORM for SQLite |
| `pydantic` | Data validation |
