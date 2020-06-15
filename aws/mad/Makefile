STAGE := "production"

dev-up:
	@echo "[INFO] Initialising development environment"
	@echo "[INFO] Cleaning docker environment and restarting docker compose"
	@docker-compose down -v
	@docker-compose up -d
	@echo "[INFO] Initialising development data"
	@docker-compose run -e PGPASSWORD=mad_password database psql --host=database --dbname=mad_database -U mad_user -f /scripts/mad.sql
	@echo "[INFO] Development environment initialised, test data built and postgres is now running"

dev-data:
	@echo "[INFO] Initialising development data"
	@docker-compose run -e PGPASSWORD=mad_password database psql --host=database --dbname=mad_database -U mad_user -f /scripts/mad.sql
	@echo "[INFO] Development data applied to database successfully"
