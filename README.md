# 課程管理系統

這是一個使用 Django 框架開發的課程管理網站，提供課程瀏覽、管理等功能。

## 功能介紹

- 課程瀏覽與搜尋
- 課程詳細資料查看
- 課程管理（新增、編輯、刪除）
- 使用者帳號管理

## 本地開發環境設置

### 系統需求

- Python 3.8+
- pip
- Git

### 步驟 1: 複製專案

```bash
git clone [your-repository-url]
cd Coding-Project
```

### 步驟 2: 建立並啟用虛擬環境

#### Windows

```bash
# 建立虛擬環境
python -m venv venv

# 啟用虛擬環境
venv\Scripts\activate
```

#### macOS/Linux

```bash
# 建立虛擬環境
python3 -m venv venv

# 啟用虛擬環境
source venv/bin/activate
```

### 步驟 3: 安裝相依套件

```bash
pip install -r requirements.txt
```

如果您尚未創建 requirements.txt 文件，可以使用以下命令生成：

```bash
pip freeze > requirements.txt
```

### 步驟 4: 設定環境變數

建立 `.env` 檔案並填入必要的環境變數：

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 步驟 5: 資料庫遷移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 步驟 6: 創建超級使用者

```bash
python manage.py createsuperuser
```

## 執行應用程式

```bash
python manage.py runserver
```

應用程式將在 http://127.0.0.1:8000/ 啟動

## 部署至 Azure

### 前置準備

1. 註冊 Azure 帳號或使用現有帳號
2. 安裝 Azure CLI: [https://docs.microsoft.com/cli/azure/install-azure-cli](https://docs.microsoft.com/cli/azure/install-azure-cli)

### 步驟 1: 登入 Azure

```bash
az login
```

### 步驟 2: 創建資源群組

```bash
az group create --name myResourceGroup --location eastasia
```

### 步驟 3: 創建 App Service 計劃

```bash
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux
```

### 步驟 4: 創建 Web App

```bash
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name your-app-name --runtime "PYTHON|3.8" --deployment-local-git
```

### 步驟 5: 設定環境變數

```bash
az webapp config appsettings set --resource-group myResourceGroup --name your-app-name --settings \
    SECRET_KEY="your_production_secret_key" \
    DEBUG="False" \
    ALLOWED_HOSTS="your-app-name.azurewebsites.net" \
    DATABASE_URL="your_database_connection_string"
```

### 步驟 6: 設定部署來源

```bash
az webapp deployment source config-local-git --name your-app-name --resource-group myResourceGroup
```

### 步驟 7: 部署應用程式

```bash
# 添加 Azure remote
git remote add azure <git-url-from-previous-command>

# 部署
git push azure main
```

### 步驟 8: 配置資料庫（選用 Azure Database for PostgreSQL）

```bash
# 創建 PostgreSQL 服務器
az postgres server create --resource-group myResourceGroup --name your-db-server --location eastasia --admin-user adminuser --admin-password yourPassword --sku-name GP_Gen5_2

# 配置防火牆規則
az postgres server firewall-rule create --resource-group myResourceGroup --server your-db-server --name AllowAllIPs --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255

# 創建資料庫
az postgres db create --resource-group myResourceGroup --server-name your-db-server --name yourdbname
```

更新 Web App 的環境變數，加入 PostgreSQL 連接字串：

```bash
az webapp config appsettings set --resource-group myResourceGroup --name your-app-name --settings \
    DATABASE_URL="postgres://adminuser:yourPassword@your-db-server.postgres.database.azure.com:5432/yourdbname"
```

### 步驟 9: 配置靜態檔案（使用 Azure Storage）

建議使用 Azure Storage 來存放靜態檔案，並更新 Django 設置來使用這些檔案。

## 專案結構

```
Coding-Project/
├── manage.py
├── README.md
├── requirements.txt
├── static/
│   ├── css/
│   ├── images/
│   └── js/
├── templates/
│   ├── base.html
│   └── course/
│       ├── course_list.html
│       └── course_detail.html
└── [Django應用程式]/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    └── urls.py
```

## 使用技術

- **後端框架**: Django
- **前端技術**: HTML, CSS, JavaScript, jQuery, Bootstrap
- **資料庫**: SQLite (開發), PostgreSQL (生產環境)
- **部署**: Azure App Service
- **靜態檔案存儲**: Azure Storage
- **版本控制**: Git
```
