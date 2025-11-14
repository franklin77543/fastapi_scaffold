# FastAPI Scaffold

一個簡單的 FastAPI 後端項目框架，包含分層架構和 User CRUD 功能。

## 架構層次

```
app/
├── core/           # 配置和全局設置
├── db/             # 數據庫連接和會話管理
├── models/         # SQLAlchemy ORM 模型
├── schemas/        # Pydantic 驗證模型
├── repositories/   # 數據持久層
├── services/       # 業務邏輯層
└── api/
    └── v1/
        └── endpoints/  # API 路由層
```

## 快速開始

### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

### 2. 運行服務器

```bash
uvicorn app.main:app --reload
```

服務器會運行在 `http://localhost:8000`

### 3. 訪問 API 文檔

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API 端點

### User CRUD 操作

- **POST** `/api/v1/users` - 創建用戶
- **GET** `/api/v1/users` - 獲取所有用戶
- **GET** `/api/v1/users/{user_id}` - 根據 ID 獲取用戶
- **PUT** `/api/v1/users/{user_id}` - 更新用戶
- **DELETE** `/api/v1/users/{user_id}` - 刪除用戶

## 項目結構說明

### Core
配置文件和應用設置

### DB
SQLAlchemy 引擎、會話管理和數據庫連接

### Models
ORM 模型定義（例如 User）

### Schemas
Pydantic 模型用於請求/響應驗證

### Repositories
數據訪問層，直接與數據庫交互

### Services
業務邏輯層，協調存儲庫操作

### API/Endpoints
路由定義和 API 端點

## 修改數據庫

默認使用 SQLite。要修改數據庫，編輯 `.env` 文件中的 `DATABASE_URL`。

例如，要使用 PostgreSQL：
```
DATABASE_URL=postgresql://user:password@localhost/dbname
```
