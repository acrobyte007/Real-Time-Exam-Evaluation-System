```bash
exam_system/
│
├── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py         # JWT auth routes (login, register, refresh)
│   │   │   ├── exams.py        # Exam related routes
│   │   │   ├── questions.py   # Question CRUD (admin)
│   │   │   ├── submissions.py # Start exam, submit exam, status, result
│   │   │   ├── admin.py        # Admin-only endpoints
│   │   │   └── websocket.py   # Optional: real-time progress updates
│
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Environment variables, settings
│   │   ├── security.py        # JWT creation, validation, password hashing
│   │   ├── logger.py          # Logging setup
│   │   └── dependencies.py   # Common Depends() functions
│
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py         # Async SQLAlchemy engine & session
│   │   ├── base.py            # Declarative Base
│   │   └── schema.py       # SQLAlchemy models
│      
│
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py            # Pydantic models for auth
│   │   ├── exam.py
│   │   ├── question.py
│   │   ├── submission.py
│   │   └── result.py
│
│   ├── services/
│   │   ├── __init__.py
│   │   ├── exam_service.py    # Business logic for exams
│   │   ├── evaluation.py      # Async + concurrent evaluation logic
│   │   └── auth_service.py    # Auth-related logic
│
│   ├── workers/
│   │   ├── __init__.py
│   │   └── evaluator.py       # Parallel processing using ProcessPoolExecutor
│
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│
│   └── middleware/
│       ├── __init__.py
│       └── request_timer.py   # Optional: measure API performance
│
├── migrations/                # Alembic migrations
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_exam.py
│   ├── test_submission.py
│   └── test_evaluation.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── .env
├── requirements.txt
├── README.md
└── alembic.ini
