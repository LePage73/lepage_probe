# # Добавляем путь к директории проекта в sys.path
import os
import sys
project_directory = os.path.abspath(os.path.join(os.path.dirname("alembic.ini"), ".."))
sys.path.append(project_directory)