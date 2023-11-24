from src.serv import Service
from src.repo import Repo
from src.ui import Ui

repo = Repo()
serv = Service(repo)
ui = Ui(serv)

# ui.run()
ui.asg3()