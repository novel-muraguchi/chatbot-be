# ChatBot BE

## プロジェクト概要

このプロジェクトは、社内手続き関連のPDFやWordファイルなどをアップロードし、その内容に基づいて質問応答が可能なチャットボットを構築するAPIです。

アップロードされたドキュメントは分割・Embeddingされ、ベクトルDB（FAISS）に格納されます。ユーザーからの質問に対してはRAGにより、根拠付きの自然な回答を提供します。

---


## 環境構築手順

### 1. リポジトリをクローン

以下は **SSH を使用した場合の例** です。HTTPS を使用する場合は GitHub 上でリポジトリのクローン用 URL を変更してください。

```bash
git clone git@github.com:novel-muraguchi/chatbot-be.git
cd chatbot-be
```

---

### 2. `.env` ファイルを作成

ルートディレクトリに `.env` ファイルを作成してください。
`.env.example` を用意していますので、以下のコマンドでコピーしてから必要に応じて値を編集してください。

```bash
cp .env.example .env
```

---

### 3. Docker 環境を構築・起動

```bash
docker compose up -d
```

---

### 4. FastAPI のドキュメントを確認

ブラウザで以下のURLにアクセスし、Swagger UI が表示されることを確認します。

```
http://localhost:8000/docs
```