questions = {
    "初級": [
        {
            "question": "HTMLで「一番大きな見出し」を作るタグはどれ？", 
            "choices": ["<head>", "<h1>", "<title>", "<top>"], 
            "answer": "<h1>",
            "explanation": "見出しタグはh1からh6まであり、h1が最も重要な大見出しを表します。<head>はページの設定を書く場所です。",
            "example": "<h1>ここが大見出し</h1>"
        },
        {
            "question": "HTMLで「段落（文章のまとまり）」を作るタグはどれ？", 
            "choices": ["<p>", "<text>", "<br>", "<group>"], 
            "answer": "<p>",
            "explanation": "Paragraph（パラグラフ）の略で、文章のひとかたまりを表します。<br>は改行を行うタグです。",
            "example": "<p>これがひとつの段落です。</p>"
        },
        {
            "question": "HTMLで「改行」をするためのタグはどれ？", 
            "choices": ["<lb>", "<br>", "<break>", "<n>"], 
            "answer": "<br>",
            "explanation": "Breakの略です。終了タグ（</br>）は不要で、単独で使います。",
            "example": "行の途中で<br>改行します"
        },
        {
            "question": "箇条書きリスト（順序なし・黒丸）を作るHTMLタグはどれ？", 
            "choices": ["<ol>", "<li>", "<ul>", "<list>"], 
            "answer": "<ul>",
            "explanation": "Unordered Listの略です。順序のあるリスト（番号付き）を作りたい場合は<ol>を使います。",
            "example": "<ul>\n  <li>リスト1</li>\n  <li>リスト2</li>\n</ul>"
        },
        {
            "question": "箇条書きリスト（順序あり・番号付き）を作るHTMLタグはどれ？", 
            "choices": ["<ul>", "<ol>", "<dl>", "<bl>"], 
            "answer": "<ol>",
            "explanation": "Ordered Listの略です。自動的に1, 2, 3...と番号が振られます。",
            "example": "<ol>\n  <li>手順1</li>\n  <li>手順2</li>\n</ol>"
        },
        {
            "question": "リストの中の「各項目」を作るタグはどれ？", 
            "choices": ["<ul>", "<ol>", "<li>", "<item>"], 
            "answer": "<li>",
            "explanation": "List Itemの略です。<ul>や<ol>の中に書いて使います。",
            "example": "<ul>\n  <li>ここが項目です</li>\n</ul>"
        },
        {
            "question": "文字を「太字」にするためのタグはどれ？", 
            "choices": ["<b>", "<bold>", "<big>", "<stronger>"], 
            "answer": "<b>",
            "explanation": "Boldの略です。重要性を強調したい場合は<strong>を使うことが推奨されています。",
            "example": "ここを<b>太字</b>にします"
        },
        {
            "question": "文字の色を変えたりする時に使う、特に意味を持たない汎用的なタグ（インライン要素）はどれ？", 
            "choices": ["<div>", "<p>", "<span>", "<style>"], 
            "answer": "<span>",
            "explanation": "文章の一部だけ色を変えたい時などにCSSと組み合わせて使います。ブロック単位で囲む場合は<div>を使います。",
            "example": "<span style=\"color: red;\">ここだけ赤色</span>"
        },
        {
            "question": "CSSで文字の「色」を変えるプロパティはどれ？", 
            "choices": ["font-color", "text-color", "color", "background-color"], 
            "answer": "color",
            "explanation": "文字色はシンプルに`color`プロパティを使います。`font-color`というプロパティはありません。",
            "example": "p {\n  color: red;\n}"
        },
        {
            "question": "CSSで文字の「大きさ」を変えるプロパティはどれ？", 
            "choices": ["text-size", "font-size", "size", "font-style"], 
            "answer": "font-size",
            "explanation": "単位にはpx, rem, em, %などが使えます。",
            "example": "h1 {\n  font-size: 24px;\n}"
        },
        {
            "question": "CSSで文字を「中央揃え」にするプロパティはどれ？", 
            "choices": ["text-align: center;", "align: center;", "font-align: center;", "center: true;"], 
            "answer": "text-align: center;",
            "explanation": "ブロック要素の中にあるテキストや画像を中央に寄せます。左揃えは`left`、右揃えは`right`です。",
            "example": "div {\n  text-align: center;\n}"
        },
        {
            "question": "CSSで背景の色を変えるプロパティはどれ？", 
            "choices": ["color", "bg-color", "background-color", "area-color"], 
            "answer": "background-color",
            "explanation": "要素の背景色を指定します。単に`background`と書くこともできます。",
            "example": "body {\n  background-color: #f0f0f0;\n}"
        },
        {
            "question": "HTML要素に「クラス名」をつけるための属性はどれ？", 
            "choices": ["id", "class", "name", "style"], 
            "answer": "class",
            "explanation": "CSSで`.クラス名`としてスタイルを適用するために使います。同じクラス名を複数の要素に使えます。",
            "example": "<div class=\"box\">内容</div>"
        },
        {
            "question": "HTML要素に「ID（固有の名前）」をつけるための属性はどれ？", 
            "choices": ["class", "id", "tag", "key"], 
            "answer": "id",
            "explanation": "ページ内で一度しか使えない固有の名前を付けます。CSSでは`#ID名`として指定します。",
            "example": "<div id=\"header\">ヘッダー</div>"
        },
        {
            "question": "要素の「外側」の余白を指定するCSSプロパティはどれ？", 
            "choices": ["padding", "margin", "border", "space"], 
            "answer": "margin",
            "explanation": "要素の外側の隙間はmargin、内側の隙間はpaddingです。ここを混同しやすいので注意しましょう。",
            "example": "div {\n  margin: 20px;\n}"
        },
        {
            "question": "要素の「内側」の余白を指定するCSSプロパティはどれ？", 
            "choices": ["margin", "padding", "border", "spacing"], 
            "answer": "padding",
            "explanation": "枠線（border）の内側に余白を作ります。",
            "example": "div {\n  padding: 10px;\n}"
        },
        {
            "question": "要素に枠線（ボーダー）をつけるCSSプロパティはどれ？", 
            "choices": ["line", "stroke", "border", "outline"], 
            "answer": "border",
            "explanation": "太さ、種類（solid/dottedなど）、色をまとめて指定できます。",
            "example": "div {\n  border: 1px solid black;\n}"
        },
        {
            "question": "要素の「縦幅（高さ）」を指定するCSSプロパティはどれ？", 
            "choices": ["width", "height", "length", "size"], 
            "answer": "height",
            "explanation": "横幅はwidth、高さはheightです。",
            "example": "div {\n  height: 200px;\n}"
        },
        {
            "question": "リンクの下線を消すなど、テキストの装飾を指定するCSSプロパティはどれ？", 
            "choices": ["text-style", "font-decoration", "text-decoration", "line-style"], 
            "answer": "text-decoration",
            "explanation": "リンク（aタグ）の下線を消す際によく使われます。",
            "example": "a {\n  text-decoration: none;\n}"
        },
        {
            "question": "箇条書きの先頭の黒丸（・）などを消すCSSプロパティはどれ？", 
            "choices": ["list-type", "list-style", "ul-style", "bullet-none"], 
            "answer": "list-style",
            "explanation": "`none`を指定するとマーカーが消えます。",
            "example": "ul {\n  list-style: none;\n}"
        },
        {
            "question": "クリックできる「ボタン」を作るHTMLタグはどれ？", 
            "choices": ["<btn>", "<click>", "<button>", "<input>"], 
            "answer": "<button>",
            "explanation": "フォームの送信やJavaScriptのトリガーとして使われます。",
            "example": "<button type=\"button\">送信する</button>"
        },
        {
            "question": "ユーザーが文字を入力できる「テキストボックス」を作るHTMLタグはどれ？", 
            "choices": ["<text>", "<input>", "<form>", "<box>"], 
            "answer": "<input>",
            "explanation": "type属性を変えることで、パスワード入力やチェックボックスなど様々な用途に使えます。",
            "example": "<input type=\"text\" placeholder=\"名前を入力\">"
        },
        {
            "question": "表（テーブル）の全体を囲むHTMLタグはどれ？", 
            "choices": ["<grid>", "<form>", "<table>", "<list>"], 
            "answer": "<table>",
            "explanation": "表作成の基本となるタグです。",
            "example": "<table>\n  \n</table>"
        },
        {
            "question": "表（テーブル）の「行（横の並び）」を作るHTMLタグはどれ？", 
            "choices": ["<td>", "<tr>", "<th>", "<row>"], 
            "answer": "<tr>",
            "explanation": "Table Rowの略です。",
            "example": "<tr>\n  <td>データ1</td>\n  <td>データ2</td>\n</tr>"
        },
        {
            "question": "表（テーブル）の「セル（データを入れる箱）」を作るHTMLタグはどれ？", 
            "choices": ["<tr>", "<th>", "<td>", "<cell>"], 
            "answer": "<td>",
            "explanation": "Table Dataの略です。見出しセルには<th>を使います。",
            "example": "<tr>\n  <td>ここの部分です</td>\n</tr>"
        },
        {
            "question": "HTMLでブラウザには表示されない「コメントアウト（メモ）」を書く時の書き方はどれ？", 
            "choices": ["/* コメント */", "// コメント //", "", "# コメント"], 
            "answer": "",
            "explanation": "CSSやJavaScriptとは書き方が違うので注意しましょう。",
            "example": "\n<p>表示されるテキスト</p>"
        },
        {
            "question": "CSSで「コメントアウト（メモ）」を書く時の書き方はどれ？", 
            "choices": ["", "// コメント", "/* コメント */", "# コメント"], 
            "answer": "/* コメント */",
            "explanation": "複数行にわたって書くこともできます。",
            "example": "/* 背景色をグレーにする */\nbody {\n  background-color: gray;\n}"
        },
        {
            "question": "<a>タグで、リンク先のURLを指定するための「属性」はどれ？", 
            "choices": ["src", "link", "url", "href"], 
            "answer": "href",
            "explanation": "Hypertext REFerenceの略です。",
            "example": "<a href=\"https://example.com\">ここをクリック</a>"
        },
        {
            "question": "<img>タグで、表示したい画像のファイル名やURLを指定するための「属性」はどれ？", 
            "choices": ["href", "src", "file", "img"], 
            "answer": "src",
            "explanation": "SouRCeの略です。画像が表示できない時のためにalt属性も設定しましょう。",
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
            "question": "ユーザーがスマホなどを「ダークモード」にしているかどうかを検知するメディアクエリはどれ？", 
            "choices": ["prefers-color-scheme", "prefers-dark-mode", "color-mode", "theme-mode"], 
            "answer": "prefers-color-scheme",
            "example": "@media (prefers-color-scheme: dark) {\n  body { background: black; color: white; }\n}"
        },
        {
            "question": "Gridレイアウトで、エリアに名前をつけて視覚的に配置を決めるプロパティはどれ？", 
            "choices": ["grid-template-areas", "grid-area-map", "grid-layout-name", "grid-position"], 
            "answer": "grid-template-areas",
            "example": ".container {\n  grid-template-areas:\n    \"header header\"\n    \"sidebar main\";\n}"
        },
        {
            "question": "画像の「縦横比（アスペクト比）」を維持したままレスポンシブにする、モダンなプロパティはどれ？", 
            "choices": ["ratio", "aspect-ratio", "keep-ratio", "size-ratio"], 
            "answer": "aspect-ratio",
            "example": ".video {\n  aspect-ratio: 16 / 9;\n  width: 100%;\n}"
        },
        {
            "question": "すりガラスのような「背景のぼかし効果」を作るプロパティはどれ？", 
            "choices": ["filter: blur();", "backdrop-filter: blur();", "background-blur", "opacity-blur"], 
            "answer": "backdrop-filter: blur();",
            "example": ".glass {\n  background: rgba(255, 255, 255, 0.5);\n  backdrop-filter: blur(10px);\n}"
        },
        {
            "question": "ページ内リンクをクリックした時に、スルスルっと滑らかに移動させるプロパティはどれ？", 
            "choices": ["scroll-behavior: smooth;", "transition: scroll;", "animation: slide;", "move: smooth;"], 
            "answer": "scroll-behavior: smooth;",
            "example": "html {\n  scroll-behavior: smooth;\n}"
        },
        {
            "question": "フォントサイズなどを「最小値」「推奨値」「最大値」の範囲で可変させる便利な関数はどれ？", 
            "choices": ["clamp()", "minmax()", "range()", "calc()"], 
            "answer": "clamp()",
            "example": "h1 {\n  font-size: clamp(16px, 5vw, 32px);\n  /* 16px〜32pxの間で画面幅に合わせて伸縮 */\n}"
        },
        {
            "question": "キーボード操作（Tabキー）の時だけフォーカス枠を表示し、マウス操作時は消すアクセシビリティ対応の擬似クラスはどれ？", 
            "choices": [":focus-visible", ":focus-within", ":active", ":target"], 
            "answer": ":focus-visible",
            "example": "button:focus-visible {\n  outline: 2px solid blue;\n}"
        },
        {
            "question": "「0（ゼロ）」という文字の幅を基準にした、等幅フォントでの文字数指定に便利な単位はどれ？", 
            "choices": ["em", "rem", "ch", "ex"], 
            "answer": "ch",
            "example": "p {\n  max-width: 60ch;\n  /* 1行を約60文字以内に制限して読みやすくする */\n}"
        },
        {
            "question": "入力フォームの「カーソル（点滅する棒）」の色を変えるプロパティはどれ？", 
            "choices": ["cursor-color", "caret-color", "input-color", "text-cursor"], 
            "answer": "caret-color",
            "example": "input {\n  caret-color: red;\n}"
        },
        {
            "question": "画像とそのキャプション（説明文）をセットで扱うためのセマンティックなタグの組み合わせはどれ？", 
            "choices": ["<figure> と <figcaption>", "<img> と <span>", "<image-box> と <text>", "<div> と <p>"], 
            "answer": "<figure> と <figcaption>",
            "example": "<figure>\n  <img src=\"cat.jpg\">\n  <figcaption>かわいい猫</figcaption>\n</figure>"
        },
        {
            "question": "JavaScriptなしで、クリックで開閉できる「アコーディオン（詳細）」を作るタグはどれ？", 
            "choices": ["<details> と <summary>", "<accordion> と <item>", "<open> と <close>", "<toggle>"], 
            "answer": "<details> と <summary>",
            "example": "<details>\n  <summary>詳しく見る</summary>\n  <p>隠れていた内容...</p>\n</details>"
        },
        {
            "question": "「特定の要素以外」を指定する、否定の擬似クラスはどれ？", 
            "choices": [":not()", ":except()", ":no()", ":without()"], 
            "answer": ":not()",
            "example": "li:not(.special) {\n  color: gray;\n  /* .specialクラスがついていないliだけグレーにする */\n}"
        },
        {
            "question": "「特定の子要素を持っている親要素」を指定できる、CSSの新しい強力な擬似クラス（親セレクタ）はどれ？", 
            "choices": [":has()", ":parent()", ":contains()", ":owner()"], 
            "answer": ":has()",
            "example": "div:has(img) {\n  border: 1px solid red;\n  /* imgを中に持っているdivだけ赤枠にする */\n}"
        },
        {
            "question": "object-fitで切り取られる画像の位置（どこ中心で切り取るか）を調整するプロパティはどれ？", 
            "choices": ["object-position", "background-position", "image-align", "fit-position"], 
            "answer": "object-position",
            "example": "img {\n  object-fit: cover;\n  object-position: top center;\n}"
        },
        {
            "question": "これから変化するプロパティをブラウザに事前に伝えて、アニメーションのカクつきを防ぐプロパティはどれ？", 
            "choices": ["will-change", "render-ahead", "gpu-accelerate", "optimize"], 
            "answer": "will-change",
            "example": ".box {\n  will-change: transform, opacity;\n}"
        }
    ]
}