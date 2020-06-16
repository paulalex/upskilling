.PHONY : start-dev test-dev

STAGE := "production"

test-dev: start-dev unit-test

start-dev: dev-up dev-schema dev-data

dev-up:
	@echo "[INFO] Starting development environment"
	@docker-compose up -d

dev-schema:
	@echo "[INFO] Creating database schema"
	@docker-compose run -e PGPASSWORD=mad_password database psql --host=database --dbname=mad_database -U mad_user -f /scripts/schema.sql
	@echo "[INFO] Database schema applied successfully"

dev-data:
	@echo "[INFO] Initialising development data"
	@docker-compose run -e PGPASSWORD=mad_password database psql --host=database --dbname=mad_database -U mad_user -f /scripts/test_data.sql
	@echo "[INFO] Development data applied to database successfully"

dev-clean:
	@echo "[INFO] Cleaning development environment"
	@docker-compose down -v
	@echo "[INFO] Successfully cleaned development environment, schema and test data deleted"

unit-test:
	@echo "[INFO] Running unit tests"
	@python -m  pytest -s --junitxml=result.xml app/test/unit/*.py

	


