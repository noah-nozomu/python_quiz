import streamlit as st
from quiz_data import quiz_list

# --- 状態管理 (Session State) ---
if "current_q_index" not in st.session_state:
    st.session_state.current_q_index = 0
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = []
if "show_explanation" not in st.session_state:
    st.session_state.show_explanation = False
if "selected_choice" not in st.session_state:
    st.session_state.selected_choice = None
if "review_mode" not in st.session_state:
    st.session_state.review_mode = False

# メニューを変更したときにクイズをリセットする関数
def reset_quiz():
    st.session_state.current_q_index = 0
    st.session_state.show_explanation = False
    st.session_state.selected_choice = None
    st.session_state.review_mode = False

st.title("Python & Web開発 クイズアプリ")

# --- サイドバー (設定メニュー) ---
st.sidebar.header("クイズの設定")
selected_level = st.sidebar.selectbox("レベルを選択", ["基礎", "応用"], on_change=reset_quiz)
selected_category = st.sidebar.selectbox("分野を選択", ["フロントエンド", "バックエンド"], on_change=reset_quiz)

# --- 問題の絞り込み ---
if st.session_state.review_mode:
    st.warning("🔥 復習モード実行中（間違えた問題のみ出題）")
    # 間違えた問題IDに一致するものだけを抽出
    filtered_quiz = [q for q in quiz_list if q['id'] in st.session_state.wrong_answers]
else:
    # 選択したレベルと分野に一致するものだけを抽出
    filtered_quiz = [q for q in quiz_list if q['level'] == selected_level and q['category'] == selected_category]

# 問題が1つもない場合の処理
if not filtered_quiz:
    st.info("この条件の問題はまだありません。追加をお待ちください！")
    st.stop()

# --- クイズのメイン処理 ---
# 全問終了したかチェック
if st.session_state.current_q_index >= len(filtered_quiz):
    st.success("全問終了しました！お疲れ様でした。")
    
    if st.session_state.review_mode:
        st.write("復習完了です！")
        if st.button("通常モードに戻る"):
            reset_quiz()
            st.rerun()
    else:
        if st.session_state.wrong_answers:
            st.warning(f"間違えた問題数: {len(st.session_state.wrong_answers)}問")
            if st.button("間違えた問題を復習する"):
                st.session_state.review_mode = True
                st.session_state.current_q_index = 0
                st.session_state.show_explanation = False
                st.rerun()
        else:
            st.balloons()
            st.write("全問正解です！素晴らしい！")
        
        if st.button("最初からやり直す"):
            reset_quiz()
            st.session_state.wrong_answers = []
            st.rerun()

else:
    # 現在の問題を取得
    q = filtered_quiz[st.session_state.current_q_index]
    
    st.subheader(f"第{st.session_state.current_q_index + 1}問 / 全{len(filtered_quiz)}問")
    st.write(q['question'])

    # --- 解説表示モード ---
    if st.session_state.show_explanation:
        if st.session_state.selected_choice == q['answer']:
            st.success("正解！🎉")
            # 復習モードで正解したら、間違えたリストから削除する
            if st.session_state.review_mode and q['id'] in st.session_state.wrong_answers:
                st.session_state.wrong_answers.remove(q['id'])
        else:
            st.error(f"不正解... (あなたの回答: {st.session_state.selected_choice})")
            if not st.session_state.review_mode and q['id'] not in st.session_state.wrong_answers:
                st.session_state.wrong_answers.append(q['id'])
        
        st.info(f"**【解説】**\n\n正解は **{q['answer']}** です。\n\n{q['explanation']}")
        
        if st.button("次の問題へ"):
            st.session_state.current_q_index += 1
            st.session_state.show_explanation = False
            st.rerun()

    # --- 問題出題モード (4択ボタン) ---
    else:
        col1, col2 = st.columns(2)
        for i, choice in enumerate(q['choices']):
            target_col = col1 if i % 2 == 0 else col2
            with target_col:
                if st.button(choice, use_container_width=True):
                    st.session_state.selected_choice = choice
                    st.session_state.show_explanation = True
                    st.rerun()