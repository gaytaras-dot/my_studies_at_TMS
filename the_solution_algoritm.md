Использовал алгоритм:
1. в обычном терминале ОС:
- pyenv install 3.12.0 - установил нужную версию питона
- mkdir ...... создал папку
- pyenv local 3.12.0 создал локальный питон в папке
2. перешел в терминал vsc
- python -m venv venv создал изолированную среду
- source /venv/bin/activate активировал ее
- pip install django
- pip freeeze > requirements.txt
- создал main.py
- обновил pip freeeze > requirements.txt
вне задачи все выложил на github и поделился с коллегами