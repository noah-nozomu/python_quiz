# data_html_css.py

questions = {
    "初級": [
        {
            "question": "見出しを作るHTMLタグはどれ？", 
            "choices": ["<h1>", "<p>", "<div>", "<a>"], 
            "answer": "<h1>",
            "example": "<h1>これは一番大きな見出しです</h1>\n<h2>これは少し小さな見出しです</h2>"
        },
        {
            "question": "文字を太くするCSSは？", 
            "choices": ["font-weight", "text-align", "color", "margin"], 
            "answer": "font-weight",
            "example": ".bold-text {\n    font-weight: bold;\n}"
        }
    ],
    "中級": [
        {
            "question": "要素を横並びにするCSSプロパティは？", 
            "choices": ["display: flex;", "display: block;", "position: absolute;", "float: center;"], 
            "answer": "display: flex;",
            "example": ".container {\n    display: flex;\n    justify-content: space-between;\n}"
        }
    ],
    "上級": [
        {
            "question": "CSSアニメーションでキーフレームを定義する@ルールは？", 
            "choices": ["@keyframes", "@media", "@import", "@font-face"], 
            "answer": "@keyframes",
            "example": "@keyframes slide {\n    from { opacity: 0; }\n    to { opacity: 1; }\n}"
        }
    ]
}