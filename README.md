# Git - 研修1~5

# 研修1

## Git を使い始める（初期化）

```bash
git init
```

## GitHub のリポジトリと紐付ける

```jsx
git remote add origin https://github.com/hoso-jpn/athena-tech-onboarding.git
```

## .gitignoreを作る

```jsx
echo ".venv/" > .gitignore
```

## ファイルを保存してプッシュする

- プッシュ：手元のセーブデータを、共有のサーバーに反映させること。

```jsx
#すべての変更を保存対象(準備)
git add .

#特定のファイル(Ex introduction.py, .gitignore)
git add introduction.py .gitignore

#セーブ（コミット）する(記録)
git commit -m "メッセージ"

#GitHubに送る(共有)
#最初だけ「-u origin main」と書くことで、次から「git push」だけで済む
git push -u origin main

#注意
#「プッシュしたつもりが、コミットを忘れていた」を防ぐ
git status
```

## メッセージの作法

`feat: Python基礎コードの追加` のように、**[種別]: [内容]** という形式（Conventional Commitsと言う）で書く

| **種別 (Type)** | **内容** | **具体的な使用例** |
| --- | --- | --- |
| **`feat`** | **新機能の追加** (feature) | `feat: ログイン機能の実装` |
| **`fix`** | **バグの修正** | `fix: 入力フォームのバリデーションエラーを修正` |
| **`docs`** | **ドキュメントのみの修正** (documentation) | `docs: READMEに使用方法を追記` |
| **`style`** | **見た目の調整**（コードの動作に影響しない、空白やセミコロンなど） | `style: インデントを4スペースに統一` |
| **`refactor`** | **リファクタリング**（バグ修正でも新機能でもないコード整理） | `refactor: 重複していた計算処理を共通関数に統合` |
| **`test`** | **テストコードの追加・修正** | `test: ユーザー登録のユニットテストを追加` |
| **`chore`** | **雑用・ビルド構成の変更**（ソースコード以外、ライブラリの更新など） | `chore: termcolorライブラリを追加` |
