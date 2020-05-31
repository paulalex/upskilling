.PHONY: all

all: init plan-with-no-colour

init:
	@echo "Removing cached terraform modules."
	@echo "Deploying into environment ${CURRENT_STAGE}"
	@rm -Rf .terraform/modules
	@echo "Initialiasing terraform for ** HELLO WORLD EXAMPLE ** environment."
	@terraform init -reconfigure -backend-config="environments/${BUILD_ENV}/backend.conf" -no-color
	@echo "Validating terraform code."
	@terraform validate -no-color

validate:
	@echo "Validating terraform code."
	@terraform validate -no-color

plan: validate
	@echo "Running a terraform plan on ** HELLO WORLD EXAMPLE ** environment."
	@terraform plan -parallelism=30 -refresh=true -out=plan.out

plan-with-no-colour: validate
	@echo "Running a terraform plan on ** HELLO WORLD EXAMPLE ** environment."
	@terraform plan -parallelism=30 -no-color -refresh=true -out=plan.out

deploy: validate
	@echo "Deploying the infrastructure on ** HELLO WORLD EXAMPLE ** environment."
	@terraform apply -no-color -auto-approve

apply: validate deploy
	@echo "Validating the deployment on ** HELLO WORLD EXAMPLE ** environment."
	@terraform plan -no-color -refresh=true -detailed-exitcode
	@echo "Deployment is completed on ** HELLO WORLD EXAMPLE ** environment."