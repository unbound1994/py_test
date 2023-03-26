from actions.actions import *
from actions.DBConnection import *

path = "../../.env"
read_env(path)


def test_login():
    comp_inn = '7725827190'
    trade_name = 'г. Москва, МКАД 14-й км, д. 2 стр. 45  / 100 фитнес (СО)'

    fast_login(os.environ.get('LOGIN'), os.environ.get('PASSWD'), comp_inn, trade_name)
