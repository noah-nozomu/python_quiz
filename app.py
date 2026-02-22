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
    st.session_state.is_scored = False # 新しく「採点済みかどうか」を記憶させます

if not st.session_state.quiz_started:
    # 【スタート画面】
    st.write("ジャンルと難易度を選んでください。")

    selected_category = st.selectbox("ジャンル", ["HTML/CSS", "Pythonフロントエンド", "Pythonバックエンド"])
    selected_difficulty = st.selectbox("難易度", ["初級", "中級", "上級"])

    if st.button("クイズスタート！"):
        all_q = question_bank[selected_category][selected_difficulty]
        sample_size = min(3, len(all_q)) # 今はテスト用に3問にしています

        if sample_size > 0:
            st.session_state.current_questions = random.sample(all_q, sample_size)
            st.session_state.quiz_started = True
            st.session_state.user_answers = {}
            st.session_state.is_scored = False
            st.rerun() 
        else:
            st.warning("このジャンル・難易度の問題はまだ準備中です！")

else:
    # 【クイズ解答・結果画面】
    st.write(f"### 問題 ({len(st.session_state.current_questions)}問)")

    questions = st.session_state.current_questions

    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}. {q['question']}**")
        
        # 採点前と採点後で動きを変えます
        if st.session_state.is_scored:
            # --- 採点後の表示 ---
            user_ans = st.session_state.user_answers.get(i)
            # 選択肢をいじれないようにします（disabled=True）
            st.radio(f"Q{i+1}の選択", q['choices'], key=f"q_{i}", index=q['choices'].index(user_ans) if user_ans in q['choices'] else None, disabled=True)
            
            # 正解・不正解の表示
            if user_ans == q['answer']:
                st.success("正解！ ⭕")
            else:
                st.error(f"不正解 ❌ (正解は: {q['answer']})")
                
            # ここが追加部分：例文（解説）を表示！
            if "example" in q:
                st.info("💡 【コード例】\n```\n" + q["example"] + "\n```")
            st.write("---")
            
        else:
            # --- 採点前の表示 ---
            answer = st.radio(f"Q{i+1}の答えを選んでください", q['choices'], key=f"q_{i}", index=None)
            st.session_state.user_answers[i] = answer
            st.write("---")

    # ボタンの表示も切り替えます
    if not st.session_state.is_scored:
        if st.button("採点する"):
            st.session_state.is_scored = True
            st.rerun() # 画面を更新して結果画面へ
    else:
        # 採点結果の合計点
        score = sum([1 for i, q in enumerate(questions) if st.session_state.user_answers.get(i) == q['answer']])
        st.write(f"### あなたの点数は {len(questions)}問中 【 {score}問 】 正解です！")
        
        if st.button("トップ画面に戻る"):
            st.session_state.quiz_started = False
            st.session_state.is_scored = False
            st.rerun()