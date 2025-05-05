```
python -m venv venv
venv/Scripts/activate
```

```
pip install -r requirements.txt
```

```
http://127.0.0.1:8000/api/sensor/?value=45
```

```commandline
daphne core.asgi:application
```
