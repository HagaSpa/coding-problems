class Solution:
    def isValid(self, s: str) -> bool:
        token = []
        brackets = {')':'(', '}':'{', ']':'['}

        for v in s:
            # 閉じかっこの場合(bracketsのkeyに合致した場合)
            if v in brackets:
                # tokenにpushされた開きかっこを取得。今までで一番最後に出てきた閉じかっこ。
                # 「tokenが空 = 開きかっこの前に、閉じかっこが出てきた場合」つまりInvalid
                open_bracket = token.pop() if token else ""
                # 開きかっこと、出現した閉じかっこに対応した開きかっこが等しくないなら。ex: [)
                if open_bracket != brackets[v]:
                    return False
            # 開きかっこの場合
            else:
                token.append(v)

        if len(token) < 1:
            return True
        else:
            return False

