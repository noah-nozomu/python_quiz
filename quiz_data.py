# quiz_data.py

# 作成した3つのファイルから問題データ（questions）を読み込む
from data_html_css import questions as html_css_q
from data_python_frontend import questions as frontend_q
from data_python_backend import questions as backend_q

# アプリで使うための大きな辞書にまとめる
question_bank = {
    "HTML/CSS": html_css_q,
    "Pythonフロントエンド": frontend_q,
    "Pythonバックエンド": backend_q
}