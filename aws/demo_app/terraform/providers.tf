provider "aws" {
  region  = var.region
  version = "~> 2.44.0"
}

# provider "aws" {
#   region = var.region
#   alias  = "primary"
#   assume_role {
#     role_arn = "arn:aws:iam::${var.primary_account_id}:role/${var.codebuild_role_name}"
#   }
# }

# provider "aws" {
#   region = var.region
#   alias  = "secondary"
#   assume_role {
#     role_arn = "arn:aws:iam::${var.secondary_account_id}:role/${var.codebuild_role_name}"
#   }
# }

