variable "project" {
  type        = string
  description = "Project name "
}

variable "region" {
  type        = string
  description = "Name of the AWS region all AWS resources will be provisioned in"
}

variable "environment" {
  type        = string
  description = "Name of the environment"
  default     = "dev"
}

variable "domain" {
  type        = string
  description = "The website domain"
}

variable "app_name" {
  type        = string
  description = "The name of the application"
}
