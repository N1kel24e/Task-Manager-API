terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.17.0"
    }
  }
}
provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "app" {
  ami = "ami-0bfa6d0ea0fe2c5a1"
  instance_type = "t3.micro"
  key_name = "docker-learning-key"
  vpc_security_group_ids = [aws_security_group.app_sg.id]

  tags = {
    Name = "task-manager"
  }
}

resource "aws_security_group" "app_sg" {
  name = "task-manager-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 8000
    to_port = 8000
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}