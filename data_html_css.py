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
    "中級": [
        {
            "question": "要素を横並びにする際によく使われる、レイアウト手法のCSSプロパティはどれ？", 
            "choices": ["display: block;", "display: inline;", "display: flex;", "display: none;"], 
            "answer": "display: flex;",
            "example": ".container {\n  display: flex;\n  /* 子要素が横並びになります */\n}"
        },
        {
            "question": "Flexboxで、子要素を「両端揃え」や「均等配置」にするプロパティはどれ？", 
            "choices": ["align-items", "justify-content", "flex-direction", "flex-wrap"], 
            "answer": "justify-content",
            "example": ".container {\n  display: flex;\n  justify-content: space-between;\n}"
        },
        {
            "question": "Flexboxで、子要素を「上下中央揃え」にするプロパティはどれ？", 
            "choices": ["justify-content", "align-items", "text-align", "vertical-align"], 
            "answer": "align-items",
            "example": ".container {\n  display: flex;\n  align-items: center;\n}"
        },
        {
            "question": "Flexboxで、要素が入りきらない場合に「折り返し」をさせるプロパティはどれ？", 
            "choices": ["flex-wrap", "flex-flow", "flex-direction", "overflow"], 
            "answer": "flex-wrap",
            "example": ".container {\n  display: flex;\n  flex-wrap: wrap;\n}"
        },
        {
            "question": "スマホとPCでデザインを変える時などに使う「メディアクエリ」の書き方はどれ？", 
            "choices": ["@media", "@screen", "@responsive", "@size"], 
            "answer": "@media",
            "example": "@media (max-width: 600px) {\n  body {\n    font-size: 14px;\n  }\n}"
        },
        {
            "question": "マウスカーソルが乗った時だけスタイルを適用する「擬似クラス」はどれ？", 
            "choices": [":active", ":focus", ":hover", ":visited"], 
            "answer": ":hover",
            "example": "button:hover {\n  background-color: blue;\n}"
        },
        {
            "question": "兄弟要素の中で「3番目の要素」だけを指定する擬似クラスはどれ？", 
            "choices": [":nth-child(3)", ":child(3)", ":eq(3)", ":third-child"], 
            "answer": ":nth-child(3)",
            "example": "li:nth-child(3) {\n  color: red;\n}"
        },
        {
            "question": "特定の要素の「直下にある子要素だけ」を指定する結合子はどれ？", 
            "choices": ["div + p", "div > p", "div p", "div ~ p"], 
            "answer": "div > p",
            "example": "div > p {\n  /* divの直下のpのみ適用 */\n  color: blue;\n}"
        },
        {
            "question": "要素の重なり順（手前か奥か）を指定するプロパティはどれ？", 
            "choices": ["z-index", "order", "layer", "stack"], 
            "answer": "z-index",
            "example": ".modal {\n  z-index: 100;\n  /* 数字が大きいほど手前にくる */\n}"
        },
        {
            "question": "要素の透明度を指定するプロパティはどれ？", 
            "choices": ["transparent", "visibility", "opacity", "filter"], 
            "answer": "opacity",
            "example": "img {\n  opacity: 0.5;\n  /* 50%透明になる */\n}"
        },
        {
            "question": "マウスカーソルの形を「指のマーク（リンク用）」にするプロパティはどれ？", 
            "choices": ["cursor: pointer;", "cursor: hand;", "cursor: click;", "cursor: finger;"], 
            "answer": "cursor: pointer;",
            "example": "button {\n  cursor: pointer;\n}"
        },
        {
            "question": "CSSでルート要素（html）のフォントサイズを基準にする単位はどれ？", 
            "choices": ["em", "px", "rem", "%"], 
            "answer": "rem",
            "example": "h1 {\n  font-size: 2rem;\n  /* ルートが16pxなら32pxになる */\n}"
        },
        {
            "question": "外部のCSSファイルをHTMLに読み込むためのタグはどれ？", 
            "choices": ["<style>", "<script>", "<link>", "<css>"], 
            "answer": "<link>",
            "example": "<link rel=\"stylesheet\" href=\"style.css\">"
        },
        {
            "question": "inputタグで、入力必須にするための属性はどれ？", 
            "choices": ["must", "required", "need", "validate"], 
            "answer": "required",
            "example": "<input type=\"text\" required>"
        },
        {
            "question": "要素を回転させたり拡大縮小させたりするプロパティはどれ？", 
            "choices": ["transition", "animation", "transform", "move"], 
            "answer": "transform",
            "example": "div {\n  transform: rotate(45deg);\n}"
        },
        {
            "question": "要素の角を丸くするCSSプロパティはどれ？", 
            "choices": ["border-radius", "border-circle", "corner-radius", "round"], 
            "answer": "border-radius",
            "example": "button {\n  border-radius: 5px;\n}"
        },
        {
            "question": "要素に影（ドロップシャドウ）をつけるCSSプロパティはどれ？", 
            "choices": ["text-shadow", "box-shadow", "drop-shadow", "shadow"], 
            "answer": "box-shadow",
            "example": "div {\n  box-shadow: 2px 2px 5px gray;\n}"
        },
        {
            "question": "paddingとborderを幅（width）に含める計算にするための、非常に重要なプロパティはどれ？", 
            "choices": ["box-sizing: content-box;", "box-sizing: border-box;", "box-model: fix;", "width: auto;"], 
            "answer": "box-sizing: border-box;",
            "example": "* {\n  box-sizing: border-box;\n  /* これでレイアウト崩れを防げます */\n}"
        },
        {
            "question": "親要素（relative）を基準に、自由な位置に配置する「絶対配置」のプロパティはどれ？", 
            "choices": ["position: absolute;", "position: fixed;", "position: static;", "position: sticky;"], 
            "answer": "position: absolute;",
            "example": ".parent { position: relative; }\n.child {\n  position: absolute;\n  top: 10px; right: 10px;\n}"
        },
        {
            "question": "スクロールしても画面の同じ位置に固定され続ける配置（ヘッダーなど）はどれ？", 
            "choices": ["position: absolute;", "position: fixed;", "position: sticky;", "display: fixed;"], 
            "answer": "position: fixed;",
            "example": "header {\n  position: fixed;\n  top: 0;\n  width: 100%;\n}"
        },
        {
            "question": "要素からはみ出した部分を「非表示」にするプロパティはどれ？", 
            "choices": ["overflow: hidden;", "overflow: scroll;", "display: none;", "visibility: hidden;"], 
            "answer": "overflow: hidden;",
            "example": "div {\n  width: 100px;\n  overflow: hidden;\n}"
        },
        {
            "question": "CSSで計算式（足し算や引き算など）を使うための関数はどれ？", 
            "choices": ["calc()", "math()", "sum()", "count()"], 
            "answer": "calc()",
            "example": "div {\n  width: calc(100% - 20px);\n}"
        },
        {
            "question": "画面の「高さ」の100%（画面いっぱい）を指定する単位はどれ？", 
            "choices": ["100%", "100vh", "100px", "100em"], 
            "answer": "100vh",
            "example": ".hero {\n  height: 100vh;\n}"
        },
        {
            "question": "背景色を「グラデーション」にするための関数はどれ？", 
            "choices": ["gradient()", "linear-gradient()", "color-mix()", "background-image()"], 
            "answer": "linear-gradient()",
            "example": "div {\n  background: linear-gradient(to right, red, blue);\n}"
        },
        {
            "question": "画像が縦横比を保ったまま、親要素いっぱいに埋まるようにする（切り取られる）プロパティはどれ？", 
            "choices": ["object-fit: cover;", "object-fit: contain;", "background-size: cover;", "width: 100%;"], 
            "answer": "object-fit: cover;",
            "example": "img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n}"
        },
        {
            "question": "要素のスタイル変化を、時間をかけて滑らかに変化させる（アニメーションの基礎）プロパティはどれ？", 
            "choices": ["animation", "transform", "transition", "change"], 
            "answer": "transition",
            "example": "button {\n  transition: all 0.3s;\n}"
        },
        {
            "question": "「もっとも優先度が高い」スタイル指定にするためのキーワードはどれ？", 
            "choices": ["!important", "!priority", "!top", "!override"], 
            "answer": "!important",
            "example": "p {\n  color: red !important;\n}"
        },
        {
            "question": "要素の前後に装飾的なコンテンツを追加する「擬似要素」はどれ？", 
            "choices": ["::before / ::after", ":first / :last", "::start / ::end", "::head / ::foot"], 
            "answer": "::before / ::after",
            "example": "h1::before {\n  content: '★';\n  color: gold;\n}"
        },
        {
            "question": "SEO的にも重要な、ページの「主要なナビゲーション」を表すHTMLタグはどれ？", 
            "choices": ["<div>", "<nav>", "<menu>", "<header>"], 
            "answer": "<nav>",
            "example": "<nav>\n  <ul><li>ホーム</li><li>記事一覧</li></ul>\n</nav>"
        },
        {
            "question": "フォームの部品（inputなど）と、そのラベル（文字）を紐付けるためのHTMLタグはどれ？", 
            "choices": ["<tag>", "<label>", "<name>", "<span>"], 
            "answer": "<label>",
            "example": "<label>\n  名前：<input type=\"text\">\n</label>"
        }
    ],
    "上級": [
        {
            "question": "要素を格子状（グリッド）に配置する、強力なレイアウト手法はどれ？", 
            "choices": ["display: grid;", "display: table;", "display: flex;", "display: lattice;"], 
            "answer": "display: grid;",
            "example": ".container {\n  display: grid;\n  /* Flexboxより複雑な配置が可能です */\n}"
        },
        {
            "question": "Gridレイアウトで、列（縦方向）のサイズと数を指定するプロパティはどれ？", 
            "choices": ["grid-template-rows", "grid-template-columns", "grid-column-gap", "grid-auto-flow"], 
            "answer": "grid-template-columns",
            "example": ".container {\n  grid-template-columns: 100px 1fr 200px;\n}"
        },
        {
            "question": "GridやFlexboxで、要素間の「隙間」を一括で指定するプロパティはどれ？", 
            "choices": ["margin", "padding", "gap", "space"], 
            "answer": "gap",
            "example": ".container {\n  gap: 20px;\n  /* 縦横の隙間が20pxになります */\n}"
        },
        {
            "question": "CSSで「変数（カスタムプロパティ）」を定義する時の正しい書き方はどれ？", 
            "choices": ["--main-color: blue;", "$main-color: blue;", "@main-color: blue;", "var-main-color: blue;"], 
            "answer": "--main-color: blue;",
            "example": ":root {\n  --main-color: #ff0000;\n}"
        },
        {
            "question": "CSSで定義した「変数」を呼び出して使う時の関数はどれ？", 
            "choices": ["call()", "use()", "var()", "$()"], 
            "answer": "var()",
            "example": "p {\n  color: var(--main-color);\n}"
        },
        {
            "question": "「ID（#id）」と「クラス（.class）」、スタイルの優先順位（詳細度）が高いのはどっち？", 
            "choices": ["IDの方が高い", "クラスの方が高い", "同じ（後から書いた方）", "同じ（先に書いた方）"], 
            "answer": "IDの方が高い",
            "example": "#title { color: red; } /* 勝つ */\n.title { color: blue; } /*負ける */"
        },
        {
            "question": "画面サイズに応じて画像を切り替える（レスポンシブ画像）ためのHTMLタグはどれ？", 
            "choices": ["<image>", "<switch>", "<picture>", "<photo>"], 
            "answer": "<picture>",
            "example": "<picture>\n  <source srcset=\"sp.jpg\" media=\"(max-width: 600px)\">\n  <img src=\"pc.jpg\">\n</picture>"
        },
        {
            "question": "要素を非表示にするが、レイアウト上のスペース（場所）は確保したままにするプロパティはどれ？", 
            "choices": ["display: none;", "visibility: hidden;", "opacity: 0;", "z-index: -1;"], 
            "answer": "visibility: hidden;",
            "example": ".hidden {\n  visibility: hidden;\n  /* 見えないけど、そこに透明な箱がある状態 */\n}"
        },
        {
            "question": "記事の内容が独立している（それだけで完結する）部分を表すセマンティックなHTMLタグはどれ？", 
            "choices": ["<section>", "<div>", "<article>", "<main>"], 
            "answer": "<article>",
            "example": "<article>\n  <h2>ブログ記事のタイトル</h2>\n  <p>記事の本文...</p>\n</article>"
        },
        {
            "question": "文書の一般的な「区切り」や「章」を表すセマンティックなHTMLタグはどれ？", 
            "choices": ["<article>", "<section>", "<div>", "<part>"], 
            "answer": "<section>",
            "example": "<section>\n  <h2>会社概要</h2>\n  <p>所在地など...</p>\n</section>"
        },
        {
            "question": "検索エンジン（Googleなど）にページの説明を伝えるためのメタタグはどれ？", 
            "choices": ["<meta name=\"description\">", "<meta name=\"keyword\">", "<title>", "<link>"], 
            "answer": "<meta name=\"description\">",
            "example": "<meta name=\"description\" content=\"このページはPythonの学習サイトです\">"
        },
        {
            "question": "視覚障害者などが使うスクリーンリーダー向けに、要素のラベル（説明）を提供する属性はどれ？", 
            "choices": ["alt", "title", "aria-label", "data-label"], 
            "answer": "aria-label",
            "example": "<button aria-label=\"閉じる\">X</button>"
        },
        {
            "question": "クリックなどのマウスイベントを無効化（反応しなくする）CSSプロパティはどれ？", 
            "choices": ["pointer-events: none;", "cursor: none;", "user-select: none;", "click: disable;"], 
            "answer": "pointer-events: none;",
            "example": ".overlay {\n  pointer-events: none;\n  /* クリックが貫通します */\n}"
        },
        {
            "question": "長い文章を「...」で省略して表示したい時に使うプロパティの組み合わせに含まれないのはどれ？", 
            "choices": ["white-space: nowrap;", "overflow: hidden;", "text-overflow: ellipsis;", "word-break: break-all;"], 
            "answer": "word-break: break-all;",
            "example": ".text {\n  white-space: nowrap;\n  overflow: hidden;\n  text-overflow: ellipsis;\n}"
        },
        {
            "question": "要素を円形や多角形に切り抜く（クリッピングする）プロパティはどれ？", 
            "choices": ["clip-path", "mask-image", "border-radius", "cut-out"], 
            "answer": "clip-path",
            "example": ".circle {\n  clip-path: circle(50%);\n}"
        },
        {
            "question": "要素の角を丸くするCSSプロパティはどれ？", 
            "choices": ["border-radius", "border-circle", "corner-radius", "round"], 
            "answer": "border-radius",
            "example": "button {\n  border-radius: 5px;\n}"
        },
        {
            "question": "要素に影（ドロップシャドウ）をつけるCSSプロパティはどれ？", 
            "choices": ["text-shadow", "box-shadow", "drop-shadow", "shadow"], 
            "answer": "box-shadow",
            "example": "div {\n  box-shadow: 2px 2px 5px gray;\n}"
        },
        {
            "question": "paddingとborderを幅（width）に含める計算にするための、非常に重要なプロパティはどれ？", 
            "choices": ["box-sizing: content-box;", "box-sizing: border-box;", "box-model: fix;", "width: auto;"], 
            "answer": "box-sizing: border-box;",
            "example": "* {\n  box-sizing: border-box;\n  /* これでレイアウト崩れを防げます */\n}"
        },
        {
            "question": "親要素（relative）を基準に、自由な位置に配置する「絶対配置」のプロパティはどれ？", 
            "choices": ["position: absolute;", "position: fixed;", "position: static;", "position: sticky;"], 
            "answer": "position: absolute;",
            "example": ".parent { position: relative; }\n.child {\n  position: absolute;\n  top: 10px; right: 10px;\n}"
        },
        {
            "question": "スクロールしても画面の同じ位置に固定され続ける配置（ヘッダーなど）はどれ？", 
            "choices": ["position: absolute;", "position: fixed;", "position: sticky;", "display: fixed;"], 
            "answer": "position: fixed;",
            "example": "header {\n  position: fixed;\n  top: 0;\n  width: 100%;\n}"
        },
        {
            "question": "要素からはみ出した部分を「非表示」にするプロパティはどれ？", 
            "choices": ["overflow: hidden;", "overflow: scroll;", "display: none;", "visibility: hidden;"], 
            "answer": "overflow: hidden;",
            "example": "div {\n  width: 100px;\n  overflow: hidden;\n}"
        },
        {
            "question": "CSSで計算式（足し算や引き算など）を使うための関数はどれ？", 
            "choices": ["calc()", "math()", "sum()", "count()"], 
            "answer": "calc()",
            "example": "div {\n  width: calc(100% - 20px);\n}"
        },
        {
            "question": "画面の「高さ」の100%（画面いっぱい）を指定する単位はどれ？", 
            "choices": ["100%", "100vh", "100px", "100em"], 
            "answer": "100vh",
            "example": ".hero {\n  height: 100vh;\n}"
        },
        {
            "question": "背景色を「グラデーション」にするための関数はどれ？", 
            "choices": ["gradient()", "linear-gradient()", "color-mix()", "background-image()"], 
            "answer": "linear-gradient()",
            "example": "div {\n  background: linear-gradient(to right, red, blue);\n}"
        },
        {
            "question": "画像が縦横比を保ったまま、親要素いっぱいに埋まるようにする（切り取られる）プロパティはどれ？", 
            "choices": ["object-fit: cover;", "object-fit: contain;", "background-size: cover;", "width: 100%;"], 
            "answer": "object-fit: cover;",
            "example": "img {\n  width: 100%;\n  height: 100%;\n  object-fit: cover;\n}"
        },
        {
            "question": "要素のスタイル変化を、時間をかけて滑らかに変化させる（アニメーションの基礎）プロパティはどれ？", 
            "choices": ["animation", "transform", "transition", "change"], 
            "answer": "transition",
            "example": "button {\n  transition: all 0.3s;\n}"
        },
        {
            "question": "「もっとも優先度が高い」スタイル指定にするためのキーワードはどれ？", 
            "choices": ["!important", "!priority", "!top", "!override"], 
            "answer": "!important",
            "example": "p {\n  color: red !important;\n}"
        },
        {
            "question": "要素の前後に装飾的なコンテンツを追加する「擬似要素」はどれ？", 
            "choices": ["::before / ::after", ":first / :last", "::start / ::end", "::head / ::foot"], 
            "answer": "::before / ::after",
            "example": "h1::before {\n  content: '★';\n  color: gold;\n}"
        },
        {
            "question": "SEO的にも重要な、ページの「主要なナビゲーション」を表すHTMLタグはどれ？", 
            "choices": ["<div>", "<nav>", "<menu>", "<header>"], 
            "answer": "<nav>",
            "example": "<nav>\n  <ul><li>ホーム</li><li>記事一覧</li></ul>\n</nav>"
        },
        {
            "question": "フォームの部品（inputなど）と、そのラベル（文字）を紐付けるためのHTMLタグはどれ？", 
            "choices": ["<tag>", "<label>", "<name>", "<span>"], 
            "answer": "<label>",
            "example": "<label>\n  名前：<input type=\"text\">\n</label>"
        }
    ],
}