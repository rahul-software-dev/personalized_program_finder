# personalized_program_finder
Personalized Program Finder: This project implements a Django backend for Nbyula's platform, enabling users to receive tailored international study program recommendations based on detailed preferences. It utilizes advanced algorithms to match users with programs that align with their academic, career, and personal goals.

personalized_program_finder/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py          # Database models for users, preferences, programs
│   │   ├── serializers.py     # Serializers for data conversion (e.g., JSON)
│   │   ├── views.py           # API endpoints for program recommendations
│   │   ├── algorithms/       # Directory for recommendation algorithms
│   │   │   ├── __init__.py
│   │   │   ├── preference_matching.py # Algorithm for matching user preferences to programs
│   │   │   ├── career_alignment.py # Algorithm for aligning programs with career goals
│   │   │   ├── cultural_fit.py   # Algorithm for assessing cultural compatibility
│   │   │   └── teaching_style.py # Algorithm for matching teaching styles
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_models.py
│   │   │   ├── test_views.py
│   │   │   └── test_algorithms.py
│   │   ├── migrations/
│   │   │   # Django migrations files
│   │   ├── admin.py           # Django admin configurations
│   │   ├── urls.py            # API URL routing
│   │   └── utils.py           # Utility functions
│   ├── manage.py            # Django management script
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Optional: Dockerfile for containerization
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ProgramList.js     # Component to display program recommendations
│   │   │   ├── PreferenceForm.js   # Component for user preference input
│   │   │   ├── ProgramCard.js     # Individual program display component
│   │   │   └── LoadingSpinner.js # Component for loading states
│   │   ├── services/
│   │   │   ├── api.js           # API service for communication with backend
│   │   ├── App.js             # Main application component
│   │   ├── index.js           # Entry point for React application
│   │   ├── styles/
│   │   │   └── styles.css
│   │   └── utils/
│   │       └── helpers.js       # Utility functions for frontend
│   ├── package.json         # Node.js dependencies
│   ├── package-lock.json    # Lock file for Node.js dependencies
│   └── README.md            # Frontend README
├── database/
│   ├── mysql/               # Optional: MySQL configuration files
│   │   ├── init.sql
│   │   └── Dockerfile
│   ├── mongodb/             # Optional: MongoDB configuration files
│   │   ├── init.js
│   │   └── Dockerfile
├── docs/
│   └── API_documentation.md # API documentation using Markdown
├── tests/
│   └── integration/         # Integration tests
│       └── test_program_finder.py
├── .gitignore               # Git ignore file
└── README.md                # Project README