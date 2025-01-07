# inputs
#### Remove services
docker-compose -f infrastructure/docker/development/docker-compose.dev.yml down --volumes --remove-orphans

#### Start the services
docker-compose -f infrastructure/docker/development/docker-compose.dev.yml up -d --build

#### See logs
docker-compose -f infrastructure/docker/development/docker-compose.dev.yml logs -f inputs_firebase_dev

#### Execute pytest
docker-compose -f infrastructure/docker/development/docker-compose.dev.yml exec -u appuser inputs_mongodb_dev python -m pytest -v

#### Test the health endpoint
curl http://localhost:8005/api/v1/health

curl -X POST "http://localhost:8005/api/v1/health_db" \
  -H "Content-Type: application/json" \
  -d '{"name": "test_item"}'

curl http://localhost:8005/api/v1/health_db


### Trasnform to base64
base64 -w 0 infrastructure/docker/development/credentials/credentials.json > credentials_base64.txt

# Test health endpoint
curl http://localhost:8005/api/v1/health

# Create test item
curl -X POST "http://localhost:8005/api/v1/health_db" \
  -H "Content-Type: application/json" \
  -d '{"name": "test_item"}'

# Get all items
curl http://localhost:8005/api/v1/health_db
