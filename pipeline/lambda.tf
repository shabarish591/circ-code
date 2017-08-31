provider "aws" {
	region = "us-west-2"
}

resource "aws_lambda_function" "ngp_automation_switchboard" {
  filename         = "~/ngp_automation_switchboard.zip"
  function_name    = "ngp_automation_switchboard"
  role             = "arn:aws:iam::309048944729:role/lambda_exec_role"
  handler          = "switchboard.handler"
  source_code_hash = "${base64sha256(file("~/ngp_automation_switchboard.zip"))}"
  runtime          = "python2.7",
	timeout	    = 60,
	vpc_config {
       subnet_ids = [
			 	"subnet-168a7e60",
			 	"subnet-58b1623c"
			 ]
  }
}
