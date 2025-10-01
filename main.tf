terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=4.1.0"
    }
  }
}
provider "azurerm" {
  features {}
}

terraform {
  backend "azurerm" {
    resource_group_name  = "rg-06"
    storage_account_name = "user983285"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

resource "azurerm_service_plan" "example" {
  name                = "example-app-service-plan223"
  location            = "westeurope"
  resource_group_name = "rg-06"
  os_type             = "Linux"
  sku_name            = "P0v3"
}


resource "azurerm_linux_web_app" "example" {
  name                = "example-webapp-123123i95u8fhwfdsewdwsa223"
  location            = "westeurope" 
  resource_group_name = "rg-06"
  service_plan_id     = azurerm_service_plan.example.id
  site_config {}
  provisioner "local-exec" {
    command = <<EOT
      az webapp deployment source config-zip \
        --resource-group ${self.resource_group_name} \
        --name ${self.name} \
        --src pong.zip
    EOT
  }
}
resource "null_resource" "zip_pong" {
  provisioner "local-exec" {
    command = "zip -j pong.zip pong.html"
  }
}
