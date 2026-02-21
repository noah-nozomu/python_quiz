# data_frontend_advanced.py
quiz_list = [
    {
        "id": 301,
        "level": "応用",
        "category": "フロントエンド",
        "question": "スマホ対応（レスポンシブデザイン）にするために、HTMLの<head>内に書くべき必須のmetaタグは？",
        "choices": ["<meta name='viewport'>", "<meta name='mobile'>", "<meta name='responsive'>", "<meta name='screen'>"],
        "answer": "<meta name='viewport'>",
        "explanation": "デバイスの画面幅に合わせて表示を最適化するためのタグです。これがないとスマホでもPC用の広い画面が縮小表示されてしまいます。"
    },
    {
        "id": 302,
        "level": "応用",
        "category": "フロントエンド",
        "question": "CSSで、画面の幅に合わせてスタイルを切り替える（例：スマホの時だけ縦並びにする）機能は？",
        "choices": ["@media (メディアクエリ)", "@screen", "@mobile", "@responsive"],
        "answer": "@media (メディアクエリ)",
        "explanation": "「@media (max-width: 768px)」のように書くことで、画面幅が768px以下の時だけ適用されるCSSを作ることができます。"
    },
    {
        "id": 303,
        "level": "応用",
        "category": "フロントエンド",
        "question": "CSSで要素を特定の位置に絶対配置する「position: absolute;」を使う時、基準となる親要素に設定しておくべきプロパティは？",
        "choices": ["position: relative;", "position: fixed;", "position: static;", "position: sticky;"],
        "answer": "position: relative;",
        "explanation": "親要素にrelativeを指定しておかないと、画面全体（ブラウザの左上）を基準にして配置されてしまい、レイアウトが崩れる原因になります。"
    },
    {
        "id": 304,
        "level": "応用",
        "category": "フロントエンド",
        "question": "CSSのセレクタ（適用先の指定）で、最も優先順位が高い（スタイルが強力に適用される）のはどれ？",
        "choices": ["タグ名（例: div）", "クラス名（例: .btn）", "ID名（例: #header）", "全称セレクタ（例: *）"],
        "answer": "ID名（例: #header）",
        "explanation": "IDはページ内に1つしか存在しないため、優先順位が非常に高く設定されています（ID > クラス > タグ の順）。"
    },
    {
        "id": 305,
        "level": "応用",
        "category": "フロントエンド",
        "question": "JavaScriptで、HTMLの中にある特定のIDを持つ要素（タグ）を取得するメソッドは？",
        "choices": ["document.querySelector()", "document.getElementById()", "document.getClass()", "document.fetchId()"],
        "answer": "document.getElementById()",
        "explanation": "指定したID名を持つHTML要素をJavaScript側で操作したい時に使います。最近は汎用的な querySelector() もよく使われます。"
    },
    {
        "id": 306,
        "level": "応用",
        "category": "フロントエンド",
        "question": "JavaScriptで、ボタンがクリックされた時などに処理を実行させるための「イベントリスナー」を登録するメソッドは？",
        "choices": ["addEventListener()", "onClick()", "setEvent()", "listenEvent()"],
        "answer": "addEventListener()",
        "explanation": "element.addEventListener('click', 関数) のように書くことで、ユーザーの操作に反応してプログラムを動かせます。"
    },
    {
        "id": 307,
        "level": "応用",
        "category": "フロントエンド",
        "question": "JavaScriptで「等しいかどうか」を判定する時、「==」よりも厳密な「===」を使うべき理由は？",
        "choices": ["データ型まで一致しているかチェックするから", "処理速度が圧倒的に早いから", "文字数が多くて見やすいから", "古いブラウザでも動くから"],
        "answer": "データ型まで一致しているかチェックするから",
        "explanation": "「==」だと数字の 1 と文字列の '1' を同じと判定してしまいますが、「===」は型もチェックするためバグを防げます。"
    },
    {
        "id": 308,
        "level": "応用",
        "category": "フロントエンド",
        "question": "JavaScriptで、短く関数を書くことができる「アロー関数」の正しい構文は？",
        "choices": ["const func = () => {}", "const func -> () {}", "const func = () => []", "const func => () {}"],
        "answer": "const func = () => {}",
        "explanation": "「=>」という矢印のような記号を使うことで、従来の「function() {}」よりもスッキリと関数を定義できます。"
    },
    {
        "id": 309,
        "level": "応用",
        "category": "フロントエンド",
        "question": "JavaScriptの配列から、条件に合うデータだけを抽出して新しい配列を作るメソッドは？",
        "choices": ["map()", "filter()", "reduce()", "find()"],
        "answer": "filter()",
        "explanation": "例えば array.filter(num => num > 10) と書けば、10より大きい数字だけを集めた新しいリストが作れます。"
    },
    {
        "id": 310,
        "level": "応用",
        "category": "フロントエンド",
        "question": "JavaScriptで、バックエンド（サーバー）からデータを非同期で取得するためによく使われる関数は？",
        "choices": ["get()", "request()", "fetch()", "pull()"],
        "answer": "fetch()",
        "explanation": "fetch(URL) を使うことで、画面をリロードせずに裏側でAPIからデータを取ってくる（非同期通信）ことができます。"
    },
    {
        "id": 311,
        "level": "応用",
        "category": "フロントエンド",
        "question": "JavaScriptで非同期処理（データの取得待ちなど）を直感的に書きやすくするキーワードの組み合わせは？",
        "choices": ["try / catch", "async / await", "then / catch", "wait / done"],
        "answer": "async / await",
        "explanation": "関数の前に async を付け、待ちたい処理の前に await を付けることで、上から下へ順番に実行されるように分かりやすく書けます。"
    },
    {
        "id": 312,
        "level": "応用",
        "category": "フロントエンド",
        "question": "HTMLのフォームで、送信ボタン（submit）を押した時に画面が切り替わる（リロードされる）のを防ぐJavaScriptの命令は？",
        "choices": ["event.stop()", "event.preventDefault()", "event.cancel()", "event.halt()"],
        "answer": "event.preventDefault()",
        "explanation": "ブラウザが持っている「本来の動き（デフォルト動作）」をキャンセルする命令です。非同期でデータを送信する際によく使います。"
    },
    {
        "id": 313,
        "level": "応用",
        "category": "フロントエンド",
        "question": "ブラウザにデータを保存する仕組みのうち、ブラウザを閉じてもデータが消えずに残り続けるものは？",
        "choices": ["Cookie", "SessionStorage", "LocalStorage", "Cache"],
        "answer": "LocalStorage",
        "explanation": "LocalStorageに保存したデータは明示的に消さない限り残ります。逆にSessionStorageはタブを閉じると消えます。"
    },
    {
        "id": 314,
        "level": "応用",
        "category": "フロントエンド",
        "question": "HTML5から導入された、意味を持ったタグ（セマンティックタグ）のうち、ヘッダーやフッター以外の独立した記事・コンテンツを囲むタグは？",
        "choices": ["<section>", "<div>", "<article>", "<main>"],
        "answer": "<article>",
        "explanation": "「それ単体で内容が完結している情報」には<article>を使います。検索エンジンにもページ構造を正しく伝えることができます。"
    },
    {
        "id": 315,
        "level": "応用",
        "category": "フロントエンド",
        "question": "CSSで、要素を重ねて表示した時（z軸）、どの要素を上に持ってくるかを数字で指定するプロパティは？",
        "choices": ["z-index", "layer-index", "stack-order", "overlap"],
        "answer": "z-index",
        "explanation": "z-index: 100; のように数字が大きいほど手前（上）に表示されます。positionプロパティと一緒に使う必要があります。"
    }
]