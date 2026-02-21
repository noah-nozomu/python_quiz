from data_backend_basic import quiz_list as backend_basic
from data_frontend_basic import quiz_list as frontend_basic
from data_backend_advanced import quiz_list as backend_advanced
from data_frontend_advanced import quiz_list as frontend_advanced

# 4つのリストを足し算して1つの大きなリストにする
quiz_list = backend_basic + frontend_basic + backend_advanced + frontend_advanced