# data_python_frontend.py

questions = {
    "初級": [
        {
            "question": "Streamlitで一番大きなタイトルを表示する関数はどれ？", 
            "choices": ["st.title()", "st.header()", "st.write()", "st.text()"], 
            "answer": "st.title()",
            "example": "st.title('私のアプリ')"
        },
        {
            "question": "Streamlitで文字やデータなど、いろいろなものを自動で良い感じに表示してくれる便利な関数はどれ？", 
            "choices": ["st.print()", "st.show()", "st.display()", "st.write()"], 
            "answer": "st.write()",
            "example": "st.write('こんにちは！', 100)"
        },
        {
            "question": "Streamlitで中くらいの見出し（ヘッダー）を表示する関数はどれ？", 
            "choices": ["st.title()", "st.header()", "st.subheader()", "st.caption()"], 
            "answer": "st.header()",
            "example": "st.header('ここから設定画面です')"
        },
        {
            "question": "Streamlitで小さな見出し（サブヘッダー）を表示する関数はどれ？", 
            "choices": ["st.title()", "st.header()", "st.subheader()", "st.small()"], 
            "answer": "st.subheader()",
            "example": "st.subheader('詳細情報')"
        },
        {
            "question": "Streamlitでクリックできる「ボタン」を作る関数はどれ？", 
            "choices": ["st.click()", "st.submit()", "st.button()", "st.btn()"], 
            "answer": "st.button()",
            "example": "if st.button('送信する'):\n    st.write('ボタンが押されました！')"
        },
        {
            "question": "Streamlitでチェックを付け外しできる「チェックボックス」を作る関数はどれ？", 
            "choices": ["st.checkbox()", "st.check()", "st.box()", "st.tick()"], 
            "answer": "st.checkbox()",
            "example": "agree = st.checkbox('利用規約に同意する')\nif agree:\n    st.write('ありがとうございます！')"
        },
        {
            "question": "Streamlitで複数の選択肢から1つだけ選ぶ「ラジオボタン」を作る関数はどれ？", 
            "choices": ["st.select()", "st.radio()", "st.choice()", "st.option()"], 
            "answer": "st.radio()",
            "example": "color = st.radio('好きな色は？', ['赤', '青', '緑'])"
        },
        {
            "question": "Streamlitでプルダウンメニューから1つ選ぶ「セレクトボックス」を作る関数はどれ？", 
            "choices": ["st.dropdown()", "st.pulldown()", "st.selectbox()", "st.list()"], 
            "answer": "st.selectbox()",
            "example": "contact = st.selectbox('連絡方法', ['メール', '電話', 'LINE'])"
        },
        {
            "question": "Streamlitで複数の選択肢から複数選べる「マルチセレクト」を作る関数はどれ？", 
            "choices": ["st.multiselect()", "st.select_many()", "st.checkboxes()", "st.choices()"], 
            "answer": "st.multiselect()",
            "example": "fruits = st.multiselect('好きな果物は？', ['りんご', 'ばなな', 'みかん'])"
        },
        {
            "question": "Streamlitでユーザーに1行の短い文字を入力してもらう「テキストボックス」を作る関数はどれ？", 
            "choices": ["st.input()", "st.text_input()", "st.text_box()", "st.string_input()"], 
            "answer": "st.text_input()",
            "example": "name = st.text_input('あなたの名前は？')"
        },
        {
            "question": "Streamlitでユーザーに数値（数字）を入力してもらう関数はどれ？", 
            "choices": ["st.int_input()", "st.number_input()", "st.math_input()", "st.digit_input()"], 
            "answer": "st.number_input()",
            "example": "age = st.number_input('年齢は？', min_value=0, max_value=120)"
        },
        {
            "question": "Streamlitでつまみを左右に動かして数値を選ぶ「スライダー」を作る関数はどれ？", 
            "choices": ["st.bar()", "st.range()", "st.slider()", "st.scroll()"], 
            "answer": "st.slider()",
            "example": "volume = st.slider('音量を設定', 0, 100, 50)"
        },
        {
            "question": "Streamlitで緑色の背景で「成功」のメッセージを表示する関数はどれ？", 
            "choices": ["st.ok()", "st.good()", "st.success()", "st.clear()"], 
            "answer": "st.success()",
            "example": "st.success('データの保存が完了しました！')"
        },
        {
            "question": "Streamlitで赤色の背景で「エラー」のメッセージを表示する関数はどれ？", 
            "choices": ["st.error()", "st.warning()", "st.fail()", "st.bad()"], 
            "answer": "st.error()",
            "example": "st.error('パスワードが間違っています。')"
        },
        {
            "question": "Streamlitで黄色の背景で「警告（注意）」のメッセージを表示する関数はどれ？", 
            "choices": ["st.caution()", "st.warning()", "st.notice()", "st.alert()"], 
            "answer": "st.warning()",
            "example": "st.warning('まだ入力されていない項目があります。')"
        },
        {
            "question": "Streamlitで画像を表示する関数はどれ？", 
            "choices": ["st.image()", "st.picture()", "st.photo()", "st.img()"], 
            "answer": "st.image()",
            "example": "st.image('sample.jpg', caption='サンプルの画像です')"
        },
        {
            "question": "Streamlitで動画を表示する関数はどれ？", 
            "choices": ["st.movie()", "st.video()", "st.play()", "st.mp4()"], 
            "answer": "st.video()",
            "example": "st.video('sample.mp4')"
        },
        {
            "question": "Streamlitで音声を再生するプレーヤーを表示する関数はどれ？", 
            "choices": ["st.sound()", "st.music()", "st.audio()", "st.voice()"], 
            "answer": "st.audio()",
            "example": "st.audio('bgm.mp3')"
        },
        {
            "question": "Streamlitで画面を左右に分割して、要素を横並びにする関数はどれ？", 
            "choices": ["st.split()", "st.divide()", "st.columns()", "st.row()"], 
            "answer": "st.columns()",
            "example": "col1, col2 = st.columns(2)\nwith col1:\n    st.write('左側')\nwith col2:\n    st.write('右側')"
        },
        {
            "question": "Streamlitで画面の左側にメニュー（サイドバー）を作る関数はどれ？", 
            "choices": ["st.menu()", "st.side()", "st.left()", "st.sidebar()"], 
            "answer": "st.sidebar()",
            "example": "st.sidebar.title('メニュー')\nst.sidebar.button('設定へ')"
        },
        {
            "question": "Streamlitで、クリックするとパカッと開く「折りたたみメニュー」を作る関数はどれ？", 
            "choices": ["st.accordion()", "st.fold()", "st.expander()", "st.open()"], 
            "answer": "st.expander()",
            "example": "with st.expander('詳細を見る'):\n    st.write('ここは隠れている文章です。')"
        },
        {
            "question": "Streamlitで画面を切り替える「タブ」を作る関数はどれ？", 
            "choices": ["st.pages()", "st.tabs()", "st.menus()", "st.switch()"], 
            "answer": "st.tabs()",
            "example": "tab1, tab2 = st.tabs(['ホーム', '設定'])\nwith tab1:\n    st.write('ここはホーム画面です')"
        },
        {
            "question": "Streamlitで複数の入力項目をグループ化して、まとめて送信する「フォーム」を作る関数はどれ？", 
            "choices": ["st.form()", "st.group()", "st.box()", "st.submit_area()"], 
            "answer": "st.form()",
            "example": "with st.form('my_form'):\n    name = st.text_input('名前')\n    submit = st.form_submit_button('送信')"
        },
        {
            "question": "Streamlitのフォーム（st.form）の中で使う、専用の送信ボタンを作る関数はどれ？", 
            "choices": ["st.button()", "st.send_button()", "st.form_submit_button()", "st.submit()"], 
            "answer": "st.form_submit_button()",
            "example": "submit_btn = st.form_submit_button('登録する')"
        },
        {
            "question": "Streamlitで処理に時間がかかっている時に、ぐるぐる回る「ローディング（読み込み中）」を表示する関数はどれ？", 
            "choices": ["st.loading()", "st.wait()", "st.spinner()", "st.circle()"], 
            "answer": "st.spinner()",
            "example": "with st.spinner('処理中...'):\n    # ここに時間がかかる処理を書く\nst.success('完了しました！')"
        },
        {
            "question": "Streamlitで画面に「風船」を飛ばして祝うアニメーションを出す関数はどれ？", 
            "choices": ["st.party()", "st.balloons()", "st.celebrate()", "st.fly()"], 
            "answer": "st.balloons()",
            "example": "if st.button('正解！'):\n    st.balloons()"
        },
        {
            "question": "Streamlitで画面に「雪」を降らせるアニメーションを出す関数はどれ？", 
            "choices": ["st.snow()", "st.winter()", "st.ice()", "st.freeze()"], 
            "answer": "st.snow()",
            "example": "if st.button('メリークリスマス'):\n    st.snow()"
        },
        {
            "question": "Streamlitで画面に横線を引いて区切る（ディバイダー）関数はどれ？", 
            "choices": ["st.line()", "st.hr()", "st.divider()", "st.border()"], 
            "answer": "st.divider()",
            "example": "st.write('上の段落')\nst.divider()\nst.write('下の段落')"
        },
        {
            "question": "Streamlitで装飾のないシンプルなテキスト（文字）を表示する関数はどれ？", 
            "choices": ["st.text()", "st.string()", "st.word()", "st.letter()"], 
            "answer": "st.text()",
            "example": "st.text('これはシンプルなテキストです。')"
        },
        {
            "question": "Streamlitで、プログラムのコードを色付きで綺麗に表示する関数はどれ？", 
            "choices": ["st.program()", "st.code()", "st.script()", "st.highlight()"], 
            "answer": "st.code()",
            "example": "st.code('print(\"Hello World\")', language='python')"
        }
    ],
    "中級": [],
    "上級": []
}