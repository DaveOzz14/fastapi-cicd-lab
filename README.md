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
Crear repo en github
git remote add origin https://github.com/DaveOzz14/fastapi-cicd-lab.git
git remote -v
git push -u origin main    Aca se subio todo el codigo local -> GitHub

git checkout -b feature/add-endpoint    Creamos una rama (Local)
git branch
git add .
git commit -m "Add version endpoint"
git push -u origin feature/add-endpoint   Sube a GitHub