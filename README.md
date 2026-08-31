python -m venv .venv
.venv\Scripts\activate
uvicorn app.main:app --reload

Testing
pytest

Git
git status
git init
git branch -M main      Configura la rama principal:
git add .               Agrega archivos:
git status              Debes ver tus archivos preparados para commit.
git commit -m "Initial FastAPI application" 
git log --oneline
git add .gitignore
git commit -m "Add gitignore"