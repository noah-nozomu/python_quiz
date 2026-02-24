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
if "wrong_questions" not in st.session_state:
    st.session_state.wrong_questions = []
if "is_reviewing" not in st.session_state:
    st.session_state.is_reviewing = False

# 復習画面専用の記憶箱
if "review_answers" not in st.session_state:
    st.session_state.review_answers = {}
if "review_scored" not in st.session_state:
    st.session_state.review_scored = False

# ----------------------------------------
# ★追加機能：サイドバー（左メニュー）
# ----------------------------------------
# クイズ中または復習中なら、左側に「タイトルに戻る」ボタンを常に出す
if st.session_state.quiz_started:
    with st.sidebar:
        st.write("### メニュー")
        if st.button("🏠 タイトルに戻る"):
            # 全てリセットして再読み込み
            st.session_state.quiz_started = False
            st.session_state.is_scored = False
            st.session_state.is_reviewing = False
            st.session_state.wrong_questions = []
            st.session_state.review_scored = False
            st.session_state.review_answers = {}
            st.rerun()

# ----------------------------------------
# ① 【復習画面】
# ----------------------------------------
if st.session_state.is_reviewing:
    st.write("### 📝 復習画面")
    st.write("間違えた問題にもう一度挑戦してみましょう！")
    
    for i, q in enumerate(st.session_state.wrong_questions):
        st.write(f"**Q{i+1}. {q['question']}**")
        
        # 復習画面の採点後
        if st.session_state.review_scored:
            user_ans = st.session_state.review_answers.get(i)
            st.radio(f"Q{i+1}の選択", q['choices'], key=f"rev_q_{i}", index=q['choices'].index(user_ans) if user_ans in q['choices'] else None, disabled=True)
            
            if user_ans == q['answer']:
                st.success("正解！ ばっちりですね！ ⭕")
            else:
                st.error(f"不正解 ❌ (正解は: {q['answer']})")
                
            if "example" in q:
                st.info("💡 【コード例】\n```\n" + q["example"] + "\n```")
            st.write("---")
            
        # 復習画面の採点前
        else:
            answer = st.radio(f"Q{i+1}の答えを選んでください", q['choices'], key=f"rev_q_{i}", index=None)
            st.session_state.review_answers[i] = answer
            st.write("---")

    # ボタンの表示切り替え
    if not st.session_state.review_scored:
        if st.button("復習を採点する"):
            st.session_state.review_scored = True
            st.rerun()
    # ※サイドバーにあるので、ここには戻るボタン不要

# ----------------------------------------
# ② 【スタート画面】
# ----------------------------------------
elif not st.session_state.quiz_started:
    st.write("ジャンルと難易度を選んでください。")

    selected_category = st.selectbox("ジャンル", ["HTML/CSS", "Pythonフロントエンド", "Pythonバックエンド"])
    selected_difficulty = st.selectbox("難易度", ["初級", "中級", "上級"])

    if st.button("クイズスタート！"):
        all_q = question_bank[selected_category][selected_difficulty]
        sample_size = min(15, len(all_q)) 

        if sample_size > 0:
            st.session_state.current_questions = random.sample(all_q, sample_size)
            st.session_state.quiz_started = True
            st.session_state.user_answers = {}
            st.session_state.is_scored = False
            st.session_state.wrong_questions = []
            st.session_state.is_reviewing = False
            st.session_state.review_scored = False
            st.session_state.review_answers = {}
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
            
            st.session_state.wrong_questions = []
            for i, q in enumerate(questions):
                if st.session_state.user_answers.get(i) != q['answer']:
                    st.session_state.wrong_questions.append(q)
                    
            st.rerun()
            
    else:
        score = len(questions) - len(st.session_state.wrong_questions)
        st.write(f"### あなたの点数は {len(questions)}問中 【 {score}問 】 正解です！")
        
        # 採点結果画面には、わかりやすいよう画面下にもボタンを残しておきます
        col1, col2 = st.columns(2)
        with col1:
            if st.button("トップ画面に戻る", key="result_back_top"):
                st.session_state.quiz_started = False
                st.session_state.is_scored = False
                st.session_state.is_reviewing = False
                st.rerun()
        with col2:
            if len(st.session_state.wrong_questions) > 0:
                if st.button("間違えた問題を復習する"):
                    st.session_state.is_reviewing = True
                    st.session_state.review_scored = False
                    st.session_state.review_answers = {}
                    st.rerun()