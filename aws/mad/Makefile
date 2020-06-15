.PHONY: all

STAGE := "production"

all: dev-init

dev-init:
	@echo "[INFO] Initialising development environment"
	@docker-compose down -v
	@docker-compose up -d
	@docker-compose run -e PGPASSWORD=mad_password database psql --host=database --dbname=mad_database -U mad_user -f /scripts/mad.sql
	@echo "[INFO] Development environment initialised, test data built and postgres is now running"