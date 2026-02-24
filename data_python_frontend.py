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
    "中級": [
        {
            "question": "Streamlitアプリのページタイトルやアイコン（favicon）を設定する関数はどれ？（※必ずコードの最初に書く必要があります）", 
            "choices": ["st.set_page_config()", "st.page_settings()", "st.config()", "st.title_config()"], 
            "answer": "st.set_page_config()",
            "example": "st.set_page_config(\n    page_title=\"私のアプリ\",\n    page_icon=\"😎\",\n    layout=\"wide\"\n)"
        },
        {
            "question": "データの読み込みなど、重い処理の結果を保存して高速化する（キャッシュする）ためのデコレータはどれ？", 
            "choices": ["@st.cache_data", "@st.memo", "@st.save", "@st.fast"], 
            "answer": "@st.cache_data",
            "example": "@st.cache_data\ndef load_data():\n    return pd.read_csv('data.csv')"
        },
        {
            "question": "データベース接続など、ハッシュ化できないオブジェクト（接続情報など）をキャッシュするためのデコレータはどれ？", 
            "choices": ["@st.cache_resource", "@st.cache_object", "@st.connect", "@st.store"], 
            "answer": "@st.cache_resource",
            "example": "@st.cache_resource\ndef init_connection():\n    return create_engine(\"...\")"
        },
        {
            "question": "画面の一部を後から書き換えるために場所を確保しておく「空のコンテナ（プレースホルダー）」を作る関数はどれ？", 
            "choices": ["st.empty()", "st.place()", "st.container()", "st.blank()"], 
            "answer": "st.empty()",
            "example": "placeholder = st.empty()\nif st.button('更新'):\n    placeholder.write('書き換えました！')"
        },
        {
            "question": "ボタンを押しても変数がリセットされないように、データを保存しておく辞書型の機能はどれ？", 
            "choices": ["st.session_state", "st.state", "st.memory", "st.storage"], 
            "answer": "st.session_state",
            "example": "if 'count' not in st.session_state:\n    st.session_state.count = 0"
        },
        {
            "question": "アプリの実行を途中で強制的に停止する（以降のコードを実行しない）関数はどれ？", 
            "choices": ["st.stop()", "st.break()", "st.end()", "st.exit()"], 
            "answer": "st.stop()",
            "example": "if not user_name:\n    st.warning('名前を入力してください')\n    st.stop()"
        },
        {
            "question": "Markdown形式のテキストをそのまま表示するための関数はどれ？", 
            "choices": ["st.markdown()", "st.md()", "st.text()", "st.write()"], 
            "answer": "st.markdown()",
            "example": "st.markdown(\"**太字**や*イタリック*が使えます\")"
        },
        {
            "question": "JSONデータを見やすく折りたたみ可能な形式で表示する関数はどれ？", 
            "choices": ["st.json()", "st.dict()", "st.data()", "st.show_json()"], 
            "answer": "st.json()",
            "example": "data = {'a': 1, 'b': [1, 2, 3]}\nst.json(data)"
        },
        {
            "question": "数値データの推移などを「折れ線グラフ」で簡易的に表示する関数はどれ？", 
            "choices": ["st.line_chart()", "st.plot()", "st.chart()", "st.graph()"], 
            "answer": "st.line_chart()",
            "example": "st.line_chart([10, 20, 15, 25, 30])"
        },
        {
            "question": "数値データの分布などを「棒グラフ」で簡易的に表示する関数はどれ？", 
            "choices": ["st.bar_chart()", "st.bar()", "st.histogram()", "st.column_chart()"], 
            "answer": "st.bar_chart()",
            "example": "st.bar_chart({'data1': 50, 'data2': 80})"
        },
        {
            "question": "地図上にポイントを表示する「マップ」を簡易的に表示する関数はどれ？", 
            "choices": ["st.map()", "st.geo()", "st.location()", "st.world()"], 
            "answer": "st.map()",
            "example": "# 緯度経度のデータフレームを渡すだけで地図が表示されます\nst.map(df)"
        },
        {
            "question": "複数の要素をグループ化して枠線などをつけることができるコンテナはどれ？", 
            "choices": ["st.container()", "st.group()", "st.area()", "st.box()"], 
            "answer": "st.container()",
            "example": "with st.container():\n    st.write('ここはグループ化されています')\n    st.bar_chart(data)"
        },
        {
            "question": "アップロードされたファイルを扱うためのウィジェットはどれ？", 
            "choices": ["st.file_uploader()", "st.upload()", "st.file_input()", "st.import()"], 
            "answer": "st.file_uploader()",
            "example": "file = st.file_uploader('CSVファイルを選択', type='csv')"
        },
        {
            "question": "ファイルをダウンロードするためのボタンを表示する関数はどれ？", 
            "choices": ["st.download_button()", "st.save_button()", "st.export()", "st.file_download()"], 
            "answer": "st.download_button()",
            "example": "st.download_button('CSVをダウンロード', data=csv_text, file_name='data.csv')"
        },
        {
            "question": "カメラを使って写真を撮影するための入力ウィジェットはどれ？", 
            "choices": ["st.camera_input()", "st.photo_input()", "st.webcam()", "st.camera()"], 
            "answer": "st.camera_input()",
            "example": "img = st.camera_input('写真を撮る')\nif img:\n    st.image(img)"
        },
        {
            "question": "処理の進捗状況をバーで表示する関数はどれ？", 
            "choices": ["st.progress()", "st.bar()", "st.loading_bar()", "st.process()"], 
            "answer": "st.progress()",
            "example": "my_bar = st.progress(0)\nfor percent_complete in range(100):\n    my_bar.progress(percent_complete + 1)"
        },
        {
            "question": "画面の右下にひょっこり現れて、数秒で消える通知メッセージ（トースト）を表示する関数はどれ？", 
            "choices": ["st.toast()", "st.notification()", "st.popup()", "st.message()"], 
            "answer": "st.toast()",
            "example": "if st.button('保存'):\n    st.toast('保存しました！', icon='✅')"
        },
        {
            "question": "KPIなどの重要な数値を、前日比（デルタ）付きで大きく表示する関数はどれ？", 
            "choices": ["st.metric()", "st.kpi()", "st.stat()", "st.score()"], 
            "answer": "st.metric()",
            "example": "st.metric(label=\"気温\", value=\"24°C\", delta=\"1.2°C\")"
        },
        {
            "question": "ユーザーが表（データフレーム）の中身を直接編集できる関数はどれ？", 
            "choices": ["st.data_editor()", "st.edit_dataframe()", "st.table_editor()", "st.input_table()"], 
            "answer": "st.data_editor()",
            "example": "edited_df = st.data_editor(df)\n# 編集後のデータがedited_dfに入ります"
        },
        {
            "question": "ユーザーに「色」を選んでもらうカラーピッカーを表示する関数はどれ？", 
            "choices": ["st.color_picker()", "st.select_color()", "st.palette()", "st.color_input()"], 
            "answer": "st.color_picker()",
            "example": "color = st.color_picker('背景色を選択', '#00f900')"
        },
        {
            "question": "Matplotlibで作成したグラフを表示するための関数はどれ？", 
            "choices": ["st.pyplot()", "st.matplotlib()", "st.plot()", "st.figure()"], 
            "answer": "st.pyplot()",
            "example": "import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\nax.plot([1, 2, 3])\nst.pyplot(fig)"
        },
        {
            "question": "Plotlyで作成したインタラクティブな（動かせる）グラフを表示する関数はどれ？", 
            "choices": ["st.plotly_chart()", "st.interactive_chart()", "st.plotly()", "st.graph_object()"], 
            "answer": "st.plotly_chart()",
            "example": "st.plotly_chart(fig, use_container_width=True)"
        },
        {
            "question": "パスワードやAPIキーなどの機密情報を安全に管理するためのStreamlitの機能はどれ？", 
            "choices": ["st.secrets", "st.env", "st.passwords", "st.keys"], 
            "answer": "st.secrets",
            "example": "# .streamlit/secrets.toml に保存した情報を読み込む\napi_key = st.secrets[\"api_key\"]"
        },
        {
            "question": "URLのクエリパラメータ（?id=123など）を取得したり設定したりする関数はどれ？", 
            "choices": ["st.query_params", "st.get_url()", "st.params", "st.request_args"], 
            "answer": "st.query_params",
            "example": "# ?name=taro にアクセスした場合\nname = st.query_params[\"name\"]"
        },
        {
            "question": "ボタンや入力欄で、操作が行われた瞬間に特定の関数を実行する（コールバック）ための引数はどれ？", 
            "choices": ["on_change / on_click", "callback", "run_function", "trigger"], 
            "answer": "on_change / on_click",
            "example": "def my_func():\n    print('実行！')\n\nst.button('送信', on_click=my_func)"
        },
        {
            "question": "ソースコードを表示しつつ、そのコードを実際に実行した結果も表示する（解説記事などで使う）関数はどれ？", 
            "choices": ["st.echo()", "st.show_code()", "st.run_and_show()", "st.display_source()"], 
            "answer": "st.echo()",
            "example": "with st.echo():\n    st.write('このコードが表示され、かつ実行されます')"
        },
        {
            "question": "数式（LaTeX形式）を綺麗にレンダリングして表示する関数はどれ？", 
            "choices": ["st.latex()", "st.math()", "st.equation()", "st.formula()"], 
            "answer": "st.latex()",
            "example": "st.latex(r''' e^{i\pi} + 1 = 0 ''')"
        },
        {
            "question": "クリックすると別のWebサイトに飛ぶリンクボタンを作成する関数はどれ？", 
            "choices": ["st.link_button()", "st.url_button()", "st.href()", "st.a_tag()"], 
            "answer": "st.link_button()",
            "example": "st.link_button(\"Googleを開く\", \"https://google.com\")"
        },
        {
            "question": "ウィジェットの右上に「？」マークを表示し、ホバー時に説明文を表示する引数はどれ？", 
            "choices": ["help", "tooltip", "description", "info"], 
            "answer": "help",
            "example": "st.text_input('名前', help='ここにフルネームを入力してください')"
        },
        {
            "question": "コードの途中で、アプリ全体を強制的に「再読み込み（リロード）」させる関数はどれ？", 
            "choices": ["st.rerun()", "st.reload()", "st.refresh()", "st.restart()"], 
            "answer": "st.rerun()",
            "example": "if st.button('リセット'):\n    st.session_state.clear()\n    st.rerun()"
        }
    ],
    "上級": [
        {
            "question": "Streamlitの標準機能では実現できない、Reactなどで作った独自の部品を組み込む機能を何と呼ぶ？", 
            "choices": ["Custom Components", "Extensions", "Add-ons", "Widgets"], 
            "answer": "Custom Components",
            "example": "import streamlit.components.v1 as components\n# 自作のHTML/JSを表示\ncomponents.html(\"<h1>Hello</h1>\")"
        },
        {
            "question": "Streamlitアプリをマルチページ対応（複数ページ）にするために、ページごとのPythonファイルを置くフォルダ名は？", 
            "choices": ["pages", "views", "screens", "routes"], 
            "answer": "pages",
            "example": "# pages/page1.py に書いたコードが自動でサイドバーのメニューに追加されます"
        },
        {
            "question": "Streamlitアプリの起動時に一度だけ実行され、セッションごとに共有されるリソース（DB接続など）を管理する新しいキャッシュデコレータは？", 
            "choices": ["@st.cache_resource", "@st.cache_global", "@st.singleton", "@st.share"], 
            "answer": "@st.cache_resource",
            "example": "@st.cache_resource\ndef init_db():\n    return database.connect()"
        },
        {
            "question": "データフレームなどの計算結果をキャッシュし、パラメータが変わった時だけ再計算させる新しいキャッシュデコレータは？", 
            "choices": ["@st.cache_data", "@st.memo", "@st.compute", "@st.calc"], 
            "answer": "@st.cache_data",
            "example": "@st.cache_data\ndef long_computation(x):\n    return x * x"
        },
        {
            "question": "キャッシュデータの有効期限（TTL）を設定する引数はどれ？", 
            "choices": ["ttl", "expire", "timeout", "limit"], 
            "answer": "ttl",
            "example": "@st.cache_data(ttl=3600)  # 1時間後にキャッシュ切れ"
        },
        {
            "question": "Streamlit Cloudなどにデプロイする際、必要なライブラリの一覧を記述するファイル名は？", 
            "choices": ["requirements.txt", "package.json", "setup.py", "Pipfile"], 
            "answer": "requirements.txt",
            "example": "streamlit\npandas\nnumpy"
        },
        {
            "question": "Streamlitのテーマ（色やフォント）をカスタマイズするために設定を記述するファイル名は？", 
            "choices": [".streamlit/config.toml", "settings.json", "theme.yaml", "style.css"], 
            "answer": ".streamlit/config.toml",
            "example": "[theme]\nprimaryColor=\"#F63366\""
        },
        {
            "question": "ファイルのアップロードサイズの上限を変更するために、config.tomlの[server]セクションで設定する項目は？", 
            "choices": ["maxUploadSize", "uploadLimit", "fileSize", "limitMB"], 
            "answer": "maxUploadSize",
            "example": "[server]\nmaxUploadSize=200"
        },
        {
            "question": "セッション状態（session_state）を、ページリロード後も保持し続けるために使う外部ライブラリとして有名なものは？", 
            "choices": ["streamlit-session", "streamlit-cookies", "streamlit-local-storage", "Extra-streamlit-components"], 
            "answer": "Extra-streamlit-components",
            "example": "import extra_streamlit_components as stx\n# CookieManagerを使ってブラウザにデータを保存"
        },
        {
            "question": "ユーザー認証（ログイン機能）を簡単に実装するためのライブラリとして有名なものは？", 
            "choices": ["Streamlit-Authenticator", "Streamlit-Login", "Streamlit-Auth", "Streamlit-User"], 
            "answer": "Streamlit-Authenticator",
            "example": "import streamlit_authenticator as stauth"
        },
        {
            "question": "StreamlitアプリのURL末尾に `?embed=true` をつけるとどうなる？", 
            "choices": ["ヘッダーやフッターが消えて埋め込みモードになる", "デバッグモードになる", "管理者モードになる", "ダークモードになる"], 
            "answer": "ヘッダーやフッターが消えて埋め込みモードになる",
            "example": "https://myapp.streamlit.app/?embed=true"
        },
        {
            "question": "アプリ内で発生した例外（エラー）の詳細を、ユーザーに見せずにログにだけ出力するための設定は？", 
            "choices": ["client.showErrorDetails=false", "server.debug=false", "app.error=hide", "log.only=true"], 
            "answer": "client.showErrorDetails=false",
            "example": "# .streamlit/config.toml\n[client]\nshowErrorDetails=false"
        },
        {
            "question": "Streamlitの実行ポート（デフォルトは8501）を変更するためのコマンドライン引数は？", 
            "choices": ["--server.port", "--port", "-p", "--address"], 
            "answer": "--server.port",
            "example": "streamlit run app.py --server.port 8080"
        },
        {
            "question": "StreamlitアプリをDockerコンテナで動かす際、外部からアクセス可能にするために設定すべきアドレスは？", 
            "choices": ["--server.address 0.0.0.0", "--server.address localhost", "--server.address 127.0.0.1", "--host public"], 
            "answer": "--server.address 0.0.0.0",
            "example": "CMD streamlit run app.py --server.port 8501 --server.address 0.0.0.0"
        },
        {
            "question": "Streamlitのexperimental機能（実験的機能）を使う際に、インポートするモジュールは？（現在は多くが本採用されています）", 
            "choices": ["streamlit.experimental", "streamlit.beta", "streamlit.lab", "streamlit.test"], 
            "answer": "streamlit.experimental",
            "example": "from streamlit.experimental import data_editor # 古い書き方"
        },
        {
            "question": "SQLデータベースやGoogle Sheetsなどに簡単に接続するための、新しい接続機能は？", 
            "choices": ["st.connection()", "st.connect()", "st.db()", "st.sql()"], 
            "answer": "st.connection()",
            "example": "conn = st.connection(\"my_database\")\ndf = conn.query(\"select * from table\")"
        },
        {
            "question": "データフレーム（st.dataframe）内の画像URLを実際の画像として表示したり、数値をバーで表示したりするための設定機能は？", 
            "choices": ["st.column_config", "st.table_config", "st.df_style", "st.format"], 
            "answer": "st.column_config",
            "example": "st.dataframe(df, column_config={\"img\": st.column_config.ImageColumn()})"
        },
        {
            "question": "ChatGPTのような「チャット画面（吹き出し）」を簡単に作るための関数は？", 
            "choices": ["st.chat_message()", "st.message()", "st.bubble()", "st.talk()"], 
            "answer": "st.chat_message()",
            "example": "with st.chat_message(\"user\"):\n    st.write(\"こんにちは\")"
        },
        {
            "question": "チャットアプリ用の「入力欄（送信ボタン付き）」を画面下部に固定して表示する関数は？", 
            "choices": ["st.chat_input()", "st.text_area_chat()", "st.message_input()", "st.send_box()"], 
            "answer": "st.chat_input()",
            "example": "prompt = st.chat_input(\"何か入力してください\")\nif prompt:\n    st.write(f\"あなた: {prompt}\")"
        },
        {
            "question": "処理の進行状況を表示し、完了後に折りたたまれる「ステータスコンテナ」を表示する関数は？", 
            "choices": ["st.status()", "st.process_container()", "st.loading_box()", "st.step()"], 
            "answer": "st.status()",
            "example": "with st.status(\"データをダウンロード中...\"):\n    time.sleep(1)\n    st.write(\"完了！\")"
        },
        {
            "question": "ON/OFFを切り替える「トグルスイッチ」を表示するウィジェットは？", 
            "choices": ["st.toggle()", "st.switch()", "st.checkbox_slide()", "st.bool_input()"], 
            "answer": "st.toggle()",
            "example": "on = st.toggle(\"ダークモードを有効にする\")"
        },
        {
            "question": "アプリの一部だけを再実行（リラン）して高速化する、新しい「フラグメント（部分更新）」機能は？", 
            "choices": ["@st.fragment", "@st.partial", "@st.part", "@st.rerun_scope"], 
            "answer": "@st.fragment",
            "example": "@st.fragment\ndef update_chart():\n    # この関数内のボタンを押しても、ここだけしか再実行されない\n    st.button(\"更新\")"
        },
        {
            "question": "画面の中央にポップアップ（モーダルウィンドウ）を表示する関数は？", 
            "choices": ["@st.dialog", "st.modal()", "st.popup()", "st.window()"], 
            "answer": "@st.dialog",
            "example": "@st.dialog(\"警告\")\ndef show_warning():\n    st.write(\"本当に削除しますか？\")"
        },
        {
            "question": "HTMLタグ（<script>などを含む）を直接埋め込んで実行するための、セキュリティリスクを伴う引数は？", 
            "choices": ["unsafe_allow_html=True", "allow_html=True", "render_html=True", "exec_html=True"], 
            "answer": "unsafe_allow_html=True",
            "example": "st.markdown(\"<script>alert('Hello')</script>\", unsafe_allow_html=True)"
        },
        {
            "question": "Altairを使って、高度でインタラクティブなグラフを表示する関数は？", 
            "choices": ["st.altair_chart()", "st.vega_lite()", "st.chart_altair()", "st.advanced_chart()"], 
            "answer": "st.altair_chart()",
            "example": "st.altair_chart(altair_chart, use_container_width=True)"
        },
        {
            "question": "3Dの地図（HexagonLayerなど）を表示するためのライブラリPyDeckを表示する関数は？", 
            "choices": ["st.pydeck_chart()", "st.deck_gl()", "st.3d_map()", "st.map_3d()"], 
            "answer": "st.pydeck_chart()",
            "example": "st.pydeck_chart(pdk.Deck(...))"
        },
        {
            "question": "Graphvizを使って、フローチャートやネットワーク図を描画する関数は？", 
            "choices": ["st.graphviz_chart()", "st.diagram()", "st.flowchart()", "st.network()"], 
            "answer": "st.graphviz_chart()",
            "example": "st.graphviz_chart('digraph { A -> B }')"
        },
        {
            "question": "Streamlit Cloud上で、現在ログインしているユーザーのメールアドレスなどを取得する（実験的）機能は？", 
            "choices": ["st.experimental_user", "st.user_info", "st.login_user", "st.auth_user"], 
            "answer": "st.experimental_user",
            "example": "st.write(f\"ようこそ {st.experimental_user.email} さん\")"
        },
        {
            "question": "サイドバーの左上に表示される「アプリのロゴ画像」を設定する関数は？", 
            "choices": ["st.logo()", "st.sidebar_image()", "st.brand()", "st.icon()"], 
            "answer": "st.logo()",
            "example": "st.logo(\"my_logo.png\")"
        },
        {
            "question": "Streamlitアプリのソースコードが変更された際、ブラウザをリロードせずに自動で反映させる開発モードの設定は？", 
            "choices": ["Run on save", "Auto reload", "Hot reload", "Live edit"], 
            "answer": "Run on save",
            "example": "※設定画面で「Run on save」にチェックを入れると開発が楽になります"
        }
    ]
}
