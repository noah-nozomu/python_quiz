# data_html_css.py

questions = {
    "初級": [
        {
            "question": "一番大きな見出しを作るHTMLタグはどれ？", 
            "choices": ["<h1>", "<p>", "<div>", "<a>"], 
            "answer": "<h1>",
            "example": "<h1>これは大見出しです</h1>"
        },
        {
            "question": "段落（文章のまとまり）を作るHTMLタグはどれ？", 
            "choices": ["<br>", "<span>", "<p>", "<div>"], 
            "answer": "<p>",
            "example": "<p>ここからここまでが一つの段落になります。</p>"
        },
        {
            "question": "別のページへのリンクを作るHTMLタグはどれ？", 
            "choices": ["<link>", "<a>", "<href>", "<img>"], 
            "answer": "<a>",
            "example": "<a href=\"https://google.com\">Googleへ移動</a>"
        },
        {
            "question": "画像を表示するためのHTMLタグはどれ？", 
            "choices": ["<image>", "<pic>", "<src>", "<img>"], 
            "answer": "<img>",
            "example": "<img src=\"sample.jpg\" alt=\"サンプルの画像\">"
        },
        {
            "question": "文章を途中で改行するためのHTMLタグはどれ？", 
            "choices": ["<enter>", "<break>", "<br>", "<hr>"], 
            "answer": "<br>",
            "example": "あいうえお<br>かきくけこ"
        },
        {
            "question": "順序のない箇条書き（リスト）全体を囲むHTMLタグはどれ？", 
            "choices": ["<ol>", "<ul>", "<li>", "<list>"], 
            "answer": "<ul>",
            "example": "<ul>\n  <li>りんご</li>\n  <li>みかん</li>\n</ul>"
        },
        {
            "question": "箇条書き（リスト）の各項目を作るHTMLタグはどれ？", 
            "choices": ["<ul>", "<ol>", "<item>", "<li>"], 
            "answer": "<li>",
            "example": "<ul>\n  <li>この部分がリストの項目です</li>\n</ul>"
        },
        {
            "question": "複数の要素をグループ化する、ブロック要素のタグはどれ？", 
            "choices": ["<span>", "<div>", "<group>", "<box>"], 
            "answer": "<div>",
            "example": "<div class=\"container\">\n  <p>グループ化された要素</p>\n</div>"
        },
        {
            "question": "文章の一部だけ色を変えたい時などに使う、インライン要素のタグはどれ？", 
            "choices": ["<div>", "<p>", "<span>", "<text>"], 
            "answer": "<span>",
            "example": "ここは普通の文字。<span style=\"color: red;\">ここだけ赤い文字。</span>"
        },
        {
            "question": "文字の色を変えるCSSプロパティはどれ？", 
            "choices": ["color", "font-color", "text-color", "background-color"], 
            "answer": "color",
            "example": "p {\n  color: blue;\n}"
        },
        {
            "question": "背景色を変えるCSSプロパティはどれ？", 
            "choices": ["color", "bg-color", "background-color", "back-color"], 
            "answer": "background-color",
            "example": "div {\n  background-color: #f0f0f0;\n}"
        },
        {
            "question": "文字の大きさを変えるCSSプロパティはどれ？", 
            "choices": ["text-size", "font-size", "size", "font-weight"], 
            "answer": "font-size",
            "example": "h1 {\n  font-size: 24px;\n}"
        },
        {
            "question": "文字の太さを変えるCSSプロパティはどれ？", 
            "choices": ["font-bold", "text-weight", "font-weight", "bold"], 
            "answer": "font-weight",
            "example": "p {\n  font-weight: bold;\n}"
        },
        {
            "question": "文字を中央揃えや右揃えにするCSSプロパティはどれ？", 
            "choices": ["align-items", "text-align", "justify-content", "position"], 
            "answer": "text-align",
            "example": "h2 {\n  text-align: center;\n}"
        },
        {
            "question": "要素の横幅を指定するCSSプロパティはどれ？", 
            "choices": ["height", "size", "width", "length"], 
            "answer": "width",
            "example": "img {\n  width: 100%;\n}"
        },
        {
            "question": "要素の「外側」の余白を指定するCSSプロパティはどれ？", 
            "choices": ["padding", "margin", "border", "space"], 
            "answer": "margin",
            "example": "div {\n  margin: 20px;\n}"
        },
        {
            "question": "要素の「内側」の余白を指定するCSSプロパティはどれ？", 
            "choices": ["margin", "padding", "border", "spacing"], 
            "answer": "padding",
            "example": "div {\n  padding: 10px;\n}"
        },
        {
            "question": "要素に枠線（ボーダー）をつけるCSSプロパティはどれ？", 
            "choices": ["line", "stroke", "border", "outline"], 
            "answer": "border",
            "example": "div {\n  border: 1px solid black;\n}"
        },
        {
            "question": "要素の「縦幅（高さ）」を指定するCSSプロパティはどれ？", 
            "choices": ["width", "height", "length", "size"], 
            "answer": "height",
            "example": "div {\n  height: 200px;\n}"
        },
        {
            "question": "リンクの下線を消すなど、テキストの装飾を指定するCSSプロパティはどれ？", 
            "choices": ["text-style", "font-decoration", "text-decoration", "line-style"], 
            "answer": "text-decoration",
            "example": "a {\n  text-decoration: none;\n}"
        },
        {
            "question": "箇条書きの先頭の黒丸（・）などを消すCSSプロパティはどれ？", 
            "choices": ["list-type", "list-style", "ul-style", "bullet-none"], 
            "answer": "list-style",
            "example": "ul {\n  list-style: none;\n}"
        },
        {
            "question": "クリックできる「ボタン」を作るHTMLタグはどれ？", 
            "choices": ["<btn>", "<click>", "<button>", "<input>"], 
            "answer": "<button>",
            "example": "<button type=\"button\">送信する</button>"
        },
        {
            "question": "ユーザーが文字を入力できる「テキストボックス」を作るHTMLタグはどれ？", 
            "choices": ["<text>", "<input>", "<form>", "<box>"], 
            "answer": "<input>",
            "example": "<input type=\"text\" placeholder=\"名前を入力\">"
        },
        {
            "question": "表（テーブル）の全体を囲むHTMLタグはどれ？", 
            "choices": ["<grid>", "<form>", "<table>", "<list>"], 
            "answer": "<table>",
            "example": "<table>\n  \n</table>"
        },
        {
            "question": "表（テーブル）の「行（横の並び）」を作るHTMLタグはどれ？", 
            "choices": ["<td>", "<tr>", "<th>", "<row>"], 
            "answer": "<tr>",
            "example": "<tr>\n  <td>データ1</td>\n  <td>データ2</td>\n</tr>"
        },
        {
            "question": "表（テーブル）の「セル（データを入れる箱）」を作るHTMLタグはどれ？", 
            "choices": ["<tr>", "<th>", "<td>", "<cell>"], 
            "answer": "<td>",
            "example": "<tr>\n  <td>ここの部分です</td>\n</tr>"
        },
        {
            "question": "HTMLでブラウザには表示されない「コメントアウト（メモ）」を書く時の書き方はどれ？", 
            "choices": ["/* コメント */", "// コメント //", "", "# コメント"], 
            "answer": "",
            "example": "\n<p>表示されるテキスト</p>"
        },
        {
            "question": "CSSで「コメントアウト（メモ）」を書く時の書き方はどれ？", 
            "choices": ["", "// コメント", "/* コメント */", "# コメント"], 
            "answer": "/* コメント */",
            "example": "/* 背景色をグレーにする */\nbody {\n  background-color: gray;\n}"
        },
        {
            "question": "<a>タグで、リンク先のURLを指定するための「属性」はどれ？", 
            "choices": ["src", "link", "url", "href"], 
            "answer": "href",
            "example": "<a href=\"https://example.com\">ここをクリック</a>"
        },
        {
            "question": "<img>タグで、表示したい画像のファイル名やURLを指定するための「属性」はどれ？", 
            "choices": ["href", "src", "file", "img"], 
            "answer": "src",
            "example": "<img src=\"logo.png\">"
        }
    ],
    "中級": [],
    "上級": []
}