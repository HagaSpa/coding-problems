# word-ladder
## 問題
`beginWord`が `endWord`になるまでに必要な最短変換回数を返却する。
変換時のルールとして必ず一回につき1文字のみ変換できる。
また変換後のWordは`wordList`に含まれていなくてはならない。

e.g..

`beginWord=hit`

`endWord=cog`

`wordList=["hot","dot","dog","lot","log","cog"]`

の場合hit->hot->dot->dog->cog で`5`が求めるべき数字となる。


## 考え方
例えばhitを例にとると、hitは以下の3種類の中間文字列に変換可能と定義できる。
```
*it
h*t
hi*
```

またhotも上記3種類の中間文字列に変換可能である。(h*tに合致するため)

上記定義により`wordList`に含まれる単語について、中間文字列とその単語のマッピングを行い、中間文字列を探索した時にそれに合致する単語を取得できるようにする。

```main.py
for word in wordList:
    for i in range(l):
        d[word[:i] + "*" + word[i+1:]].append(word)

// print(d)
{
    '*ot': ['hot', 'dot', 'lot'], 
    'h*t': ['hot'], 
    'ho*': ['hot'], 
    'd*t': ['dot'], 
    'do*': ['dot', 'dog'], 
    '*og': ['dog', 'log', 'cog'], 
    'd*g': ['dog'], 
    'l*t': ['lot'], 
    'lo*': ['lot', 'log'], 
    'l*g': ['log'], 
    'c*g': ['cog'], 
    'co*': ['cog']
}
```

今回は最短経路（回数）を求めたいので、幅優先探索で実装する。
そのためキューを用意し、最初の要素として`beginWord`と回数の初期値である`1`をタプルで追加する。

※タプルのがpythonの実装上、popした時に2値取れるから使いやすいだけ。dictやlistでもいい。

また`d`を見るとわかるが、1つの単語は3つの中間文字列に紐づくため、重複カウントを防ぐために`chk`というdictを用意し、そこでチェック済みかどうかを管理する。

```
q = deque()
q.append((beginWord, 1))
chked = {beginWord: True}
```

キューから先頭の単語を取得し、その単語から生成可能な中間文字列を全て作る。

中間文字列をkeyにして`d`から単語の取得を行い、それが`endWord`かどうかの判定を行う。

`endWord`なら処理を中断し現在の変換回数を返却する。

そうじゃなければその単語を`chk`と`q`に追加し、次のループの対象とする。

キューがなくなるまでループを行う。

```
while q:
    k,v = q.popleft()
    for i in range(l):
        w = k[:i] + "*" + k[i+1:]
        for word in d[w]:
            if word == endWord:
                return v+1
            if word not in chked:
                chked[word] = True
                q.append((word, v+1))
```

## 最短経路問題に関する参考資料
- https://www.amazon.co.jp/dp/B01N14WBX3
    - 6章