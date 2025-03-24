# FastAPI

# Docker
```bash
docker-compose up -d
- `docker exec -it fastapi bash`
```

Pour afficher les logs des containers :
```bash
docker-compose logs -f -n10
```

# Python
## Installation des dépendances
```bash
poetry install --no-root
```

## Lancement du serveur
### Programme test
```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

### Swagger et documentation
```bash
http://127.0.0.1:3000/docs
http://127.0.0.1:3000/redoc
```

### Tests
```bash
curl -X POST "http://localhost:3000/persons" -H "Content-Type: application/json" -d '{"name": "Diane", "age": 28, "city": {"name": "Neuchâtel","npa": "2000"}}'
```