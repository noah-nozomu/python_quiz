import streamlit as st
import random

# ① 問題データ（後でここにどんどん問題を書き足していきます）
question_bank = {
    "HTML/CSS": {
        "初級": [
            {"question": "見出しを作るHTMLタグはどれ？", "choices": ["<h1>", "<p>", "<div>", "<a>"], "answer": "<h1>"},
            {"question": "文字を太くするCSSプロパティは？", "choices": ["font-weight", "text-align", "color", "margin"], "answer": "font-weight"},
            {"question": "リンクを作るタグはどれ？", "choices": ["<a>", "<link>", "<href>", "<img>"], "answer": "<a>"},
            {"question": "段落を作るタグはどれ？", "choices": ["<p>", "<br>", "<span>", "<div>"], "answer": "<p>"},
            {"question": "背景色を変えるCSSは？", "choices": ["background-color", "color", "bg-color", "border"], "answer": "background-color"}
        ],
        "中級": [],
        "上級": []
    },
    "Pythonフロントエンド": {
        "初級": [], "中級": [], "上級": []
    },
    "Pythonバックエンド": {
        "初級": [], "中級": [], "上級": []
    }
}

st.title("プログラミング クイズアプリ")

# ② 記憶箱（session_state）の準備
# Streamlitはボタンを押すたびに最初から読み込み直す性質があるため、
# 「今クイズ中かどうか」「ランダムに選んだ問題」を記憶させておく必要があります。
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "current_questions" not in st.session_state:
    st.session_state.current_questions = []
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# ③ 画面の切り替え
if not st.session_state.quiz_started:
    # 【スタート画面】
    st.write("ジャンルと難易度を選んでください。")

    selected_category = st.selectbox("ジャンル", ["HTML/CSS", "Pythonフロントエンド", "Pythonバックエンド"])
    selected_difficulty = st.selectbox("難易度", ["初級", "中級", "上級"])

    if st.button("クイズスタート！"):
        # 選ばれたジャンル・難易度の問題を全部持ってくる
        all_q = question_bank[selected_category][selected_difficulty]

        # ※今はテスト用に「3問」ランダムに選ぶ設定にしています。
        # 問題数が充実したら、ここを 15 に変更します。
        sample_size = min(3, len(all_q)) 

        if sample_size > 0:
            # ランダムに選んで記憶箱に保存
            st.session_state.current_questions = random.sample(all_q, sample_size)
            st.session_state.quiz_started = True
            st.session_state.user_answers = {}
            st.rerun() # 画面を更新してクイズ解答画面へ
        else:
            st.warning("このジャンル・難易度の問題はまだ準備中です！")

else:
    # 【クイズ解答画面】
    st.write(f"### 問題 ({len(st.session_state.current_questions)}問)")

    questions = st.session_state.current_questions

    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}. {q['question']}**")
        # 選択肢をシャッフルして表示したい場合はもう少し工夫できますが、まずはシンプルに表示します
        answer = st.radio(f"Q{i+1}の答えを選んでください", q['choices'], key=f"q_{i}", index=None)
        st.session_state.user_answers[i] = answer
        st.write("---")

    if st.button("採点する"):
        score = 0
        for i, q in enumerate(questions):
            # 選んだ答えと、正解が一致しているかチェック
            if st.session_state.user_answers.get(i) == q['answer']:
                score += 1

        st.success(f"あなたの点数は {len(questions)}問中 【 {score}問 】 正解です！")

        if st.button("トップ画面に戻る"):
            # 記憶箱をリセットしてスタート画面に戻る
            st.session_state.quiz_started = False
            st.rerun()