# ChatBot BE

## プロジェクト概要

このプロジェクトは、社内手続き関連のPDFやWordファイルなどをアップロードし、その内容に基づいて質問応答が可能なチャットボットを構築するAPIです。

アップロードされたドキュメントは分割・Embeddingされ、ベクトルDB（FAISS）に格納されます。ユーザーからの質問に対してはRAGにより、根拠付きの自然な回答を提供します。

---


## 環境構築手順

### 1. リポジトリをクローン

```bash
git clone git@github.com:novel-muraguchi/chatbot-be.git
cd chatbot-be
```

---

### 2. `.env` ファイルを作成

プロジェクトルートに `.env` ファイルを作成し、以下を記載してください。

```env
ENVIRONMENT=local
PYTHONPATH=src/chatbot_be

DB_CONNECTION=mysql
DB_HOST=chatbot-be-db
DB_PORT=3306
DB_DATABASE=chatbot_be
DB_USERNAME=user
DB_PASSWORD=your_password
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