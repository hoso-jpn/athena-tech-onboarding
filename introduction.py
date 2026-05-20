"""
athena tech オンボーディング：Python基礎学習まとめ
作成者：hoso
内容：コレクション、関数、オブジェクト指向、制御構文、ライブラリの基本
"""

import datetime  # 1. ライブラリのインポートは一番上
from termcolor import colored

# ==========================================
# 1. コレクション (Collections)
# ==========================================
def study_collections():
    print("--- 1. Collections ---")
    
    # リスト：順序あり、変更可能
    members = ["山田", "田中", "佐藤"]
    members.append("鈴木")
    
    # タプル：順序あり、変更不可
    colors = ("Red", "Green", "Blue")
    
    # 辞書：キーと値のペア
    user_info = {"name": "hoso", "role": "engineer"}
    print(f"User Name: {user_info['name']}")
    
    # 集合：重複なし
    unique_numbers = {1, 2, 2, 3}
    print(f"Unique Set: {unique_numbers}")


# ==========================================
# 2. 関数 (Functions)
# ==========================================
def greet(name: str) -> str:
    """
    挨拶メッセージを生成する関数
    引数 name: str (文字列)
    戻り値: str (文字列)
    """
    return f"エンジニアの{name}です、よろしく！"


# ==========================================
# 3. オブジェクト指向 (OOP)
# ==========================================
class Engineer:
    """エンジニアを表現するクラス"""
    
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"私は{self.role}の{self.name}です。よろしくお願いします！")


# ==========================================
# 4. 制御構文 (Control Flow)
# ==========================================
def study_loops():
    print("\n--- 2. Nested Loops with Break ---")
    # 内側のループを抜けるパターン
    for i in range(4):
        for j in range(3):
            print(i, j)
            if j == 1:
                break
        print("====")

    print("\n--- 3. Outer Loop Break ---")
    # 外側のループを抜けるパターン
    for i in range(4):
        if i == 2:
            break
        for j in range(3):
            print(i, j)


# ==========================================
# メイン処理（実行部分）
# ==========================================
if __name__ == "__main__":
    # 時刻の表示
    now = datetime.datetime.now()
    print(colored(f"実行時刻: {now}", "cyan"))

    # 各セクションの実行
    study_collections()
    
    greeting = greet("hoso")
    print(f"\nFunction result: {greeting}")
    
    me = Engineer("hoso", "エンジニア初学者")
    me.introduce()
    
    study_loops()
    
    print(colored("\nPythonの基礎学習、完了！", "green", attrs=["bold"]))
