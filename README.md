# django_plotly
Django Plotly example

---

# 構築手順

## 準備

1. ソースコードをクローン
2. 仮想環境作成
3. django と plotly をインストール
4. django プロジェクトを新規作成

```
$ git clone https://github.com/HideKobayashi/django_plotly.git
$ cd django_plotly
$ python -m venv venv
$ pip install plotly django
$ django-admin startproject mysite
```

## Django プロジェクトにアプリを追加

```
cd mysite
python manage.py startapp app
```

`mysite/settings.py` にアプリを追加


