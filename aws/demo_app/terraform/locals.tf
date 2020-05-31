locals {
  website_domain      = var.environment =="prod" ? "www.${var.domain}" : "www-${var.environment}.${var.domain}"
  site_bucket_name    = "${var.app_name}-site-${var.environment}"
  content_bucket_name = "${var.app_name}-content-${var.environment}"
  # ssm_site_bucket     = "/${local.app_name}/site-bucket/${var.environment}"
  # ssm_content_bucket  = "/${local.app_name}/content-bucket/${var.environment}"
  # ssm_cf_distro       = "/${local.app_name}/cf_distro/${var.environment}"
  ssm_api_id          = "/${var.app_name}/hello_api_id/${var.environment}"
  ssm_api_base        = "/${var.app_name}/hello_api_base/${var.environment}"

  tags = {
    PRODUCT = var.app_name
    STAGE = var.environment
  }
}