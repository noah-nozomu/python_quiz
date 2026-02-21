# data_frontend_basic.py
quiz_list = [
    {
        "id": 101,  # IDが被らないように100番台にしています
        "level": "基礎",
        "category": "フロントエンド",
        "question": "HTMLで別のページへのリンク（ハイパーリンク）を作るタグはどれ？",
        "choices": ["<link>", "<a>", "<href>", "<url>"],
        "answer": "<a>",
        "explanation": "<a>タグ（アンカータグ）を使います。href属性でリンク先のURLを指定します。"
    },
    {
        "id": 102,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "HTMLで画像を表示するためのタグはどれ？",
        "choices": ["<image>", "<pic>", "<img>", "<src>"],
        "answer": "<img>",
        "explanation": "<img>タグを使います。閉じタグがない（空要素）のが特徴で、src属性で画像の場所を指定します。"
    },
    {
        "id": 103,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "CSSで文字の色を変更するプロパティは？",
        "choices": ["text-color", "font-color", "color", "background-color"],
        "answer": "color",
        "explanation": "文字色は単に「color」を使います。背景色は「background-color」です。"
    },
    {
        "id": 104,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "CSSで特定の「クラス名」にスタイルを当てるとき、名前の先頭につける記号は？",
        "choices": ["#", ".", "@", "&"],
        "answer": ".",
        "explanation": "クラス名には「.（ドット）」、ID名には「#（ハッシュ）」をつけます。"
    },
    {
        "id": 105,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "JavaScriptで、ブラウザの開発者ツール（コンソール）にメッセージを表示させる命令は？",
        "choices": ["print()", "console.log()", "document.write()", "alert()"],
        "answer": "console.log()",
        "explanation": "エラーの確認やデータのチェックなど、開発中のデバッグで最もよく使う命令です。"
    },
    {
        "id": 106,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "JavaScriptで、後から中身を変更できない「定数」を宣言するキーワードは？",
        "choices": ["let", "var", "const", "static"],
        "answer": "const",
        "explanation": "constで宣言した値は上書きできないため、安全なコードを書くためによく使われます。変更可能な変数はletを使います。"
    },
    {
        "id": 107,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "HTMLの入力フォームで、パスワードを見えないように（●●●のように）入力させるタイプは？",
        "choices": ["type='hidden'", "type='password'", "type='secret'", "type='text'"],
        "answer": "type='password'",
        "explanation": "<input type='password'> とすることで、入力文字が伏せ字になります。"
    },
    {
        "id": 108,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "要素を横並びにしたり、中央揃えにしたりするのに便利なCSSのレイアウト機能は？",
        "choices": ["display: block;", "display: grid;", "display: flex;", "display: inline;"],
        "answer": "display: flex;",
        "explanation": "Flexbox（フレックスボックス）と呼ばれ、現代のWebデザインで最も頻繁に使われるレイアウト手法です。"
    },
    {
        "id": 109,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "Webページのデザインを整えるために使われる言語「CSS」は何の略？",
        "choices": ["Cascading Style Sheets", "Creative Style System", "Computer Styling Sheets", "Colorful Style Sheets"],
        "answer": "Cascading Style Sheets",
        "explanation": "Cascading（滝のように連なる）という意味があり、複数のスタイルが優先順位に従って適用される仕組みを表しています。"
    },
    {
        "id": 110,
        "level": "基礎",
        "category": "フロントエンド",
        "question": "HTMLのリスト作成で、順番（1, 2, 3...）が自動でつくリストのタグは？",
        "choices": ["<ul>", "<ol>", "<li>", "<dl>"],
        "answer": "<ol>",
        "explanation": "<ol>はOrdered List（順序ありリスト）の略です。順番がない・（黒丸）のリストは<ul>を使います。"
    }
]