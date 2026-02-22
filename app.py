import streamlit as st
import random
from quiz_data import question_bank

st.title("プログラミング クイズアプリ")

# 記憶箱（session_state）の準備
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "current_questions" not in st.session_state:
    st.session_state.current_questions = []
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "is_scored" not in st.session_state:
    st.session_state.is_scored = False
# ↓追加：間違えた問題リストと、復習画面にいるかどうかの判定
if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = []
if "is_reviewing" not in st.session_state:
    st.session_state.is_reviewing = False

# ----------------------------------------
# ① 【復習画面】
# ----------------------------------------
if st.session_state.is_reviewing:
    st.write("### 📝 復習画面")
    st.write("今回間違えた問題のリストです。しっかり確認しておきましょう！")
    
    # 間違えた問題をループで表示
    for i, q in enumerate(st.session_state.wrong_questions):
        st.write(f"**Q{i+1}. {q['question']}**")
        st.error(f"正解: {q['answer']}") # 正解を目立たせて表示
        if "example" in q:
            st.info("💡 【コード例】\n```\n" + q["example"] + "\n```")
        st.write("---")
        
    if st.button("トップ画面に戻る"):
        st.session_state.quiz_started = False
        st.session_state.is_scored = False
        st.session_state.is_reviewing = False
        st.rerun()

# ----------------------------------------
# ② 【スタート画面】
# ----------------------------------------
elif not st.session_state.quiz_started:
    st.write("ジャンルと難易度を選んでください。")

    selected_category = st.selectbox("ジャンル", ["HTML/CSS", "Pythonフロントエンド", "Pythonバックエンド"])
    selected_difficulty = st.selectbox("難易度", ["初級", "中級", "上級"])

    if st.button("クイズスタート！"):
        all_q = question_bank[selected_category][selected_difficulty]
        
        # 出題数を 15問 に変更しました！
        sample_size = min(15, len(all_q)) 

        if sample_size > 0:
            st.session_state.current_questions = random.sample(all_q, sample_size)
            st.session_state.quiz_started = True
            st.session_state.user_answers = {}
            st.session_state.is_scored = False
            st.session_state.wrong_questions = [] # クイズ開始時に間違えた問題リストをリセット
            st.session_state.is_reviewing = False
            st.rerun() 
        else:
            st.warning("このジャンル・難易度の問題はまだ準備中です！")

# ----------------------------------------
# ③ 【クイズ解答・結果画面】
# ----------------------------------------
else:
    st.write(f"### 問題 ({len(st.session_state.current_questions)}問)")

    questions = st.session_state.current_questions

    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}. {q['question']}**")
        
        if st.session_state.is_scored:
            user_ans = st.session_state.user_answers.get(i)
            st.radio(f"Q{i+1}の選択", q['choices'], key=f"q_{i}", index=q['choices'].index(user_ans) if user_ans in q['choices'] else None, disabled=True)
            
            if user_ans == q['answer']:
                st.success("正解！ ⭕")
            else:
                st.error(f"不正解 ❌ (正解は: {q['answer']})")
                
            if "example" in q:
                st.info("💡 【コード例】\n```\n" + q["example"] + "\n```")
            st.write("---")
            
        else:
            answer = st.radio(f"Q{i+1}の答えを選んでください", q['choices'], key=f"q_{i}", index=None)
            st.session_state.user_answers[i] = answer
            st.write("---")

    if not st.session_state.is_scored:
        if st.button("採点する"):
            st.session_state.is_scored = True
            
            # 採点と同時に、間違えた問題をリストに追加する処理
            st.session_state.wrong_questions = []
            for i, q in enumerate(questions):
                if st.session_state.user_answers.get(i) != q['answer']:
                    st.session_state.wrong_questions.append(q)
                    
            st.rerun()
            
    else:
        # 正解数の計算（全体の数 - 間違えた数）
        score = len(questions) - len(st.session_state.wrong_questions)
        st.write(f"### あなたの点数は {len(questions)}問中 【 {score}問 】 正解です！")
        
        # ボタンを横に2つ並べるためのレイアウト
        col1, col2 = st.columns(2)
        with col1:
            if st.button("トップ画面に戻る"):
                st.session_state.quiz_started = False
                st.session_state.is_scored = False
                st.session_state.is_reviewing = False
                st.rerun()
        with col2:
            # 間違えた問題が1問以上ある時だけ「復習ボタン」を表示する
            if len(st.session_state.wrong_questions) > 0:
                if st.button("間違えた問題を復習する"):
                    st.session_state.is_reviewing = True
                    st.rerun()