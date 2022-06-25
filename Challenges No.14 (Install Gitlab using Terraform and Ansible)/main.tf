terraform {
  required_version = ">=0.12"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>2.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  skip_provider_registration = "true"
  features {}
}

# Create A Resources Group - In Sandbox already have one when we use it, so this part is excluded
# resource "azurerm_resource_group" "vmss" {
#  name     = var.resource_group_name
#  location = var.location
#  tags     = var.tags
# }

resource "azurerm_virtual_network" "gitlab" {
  name                = "gitlab-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = var.resource_group_name
  tags                = var.tags
}

resource "azurerm_subnet" "gitlab" {
  name                 = "gitlab-subnet"
  resource_group_name  = var.resource_group_name
  virtual_network_name = azurerm_virtual_network.gitlab.name
  address_prefixes     = ["10.0.0.0/24"]
}

resource "azurerm_public_ip" "gitlab" {
  name                = "gitlab-public-ip"
  location            = var.location
  resource_group_name = var.resource_group_name
  allocation_method   = "Static"
  domain_name_label   = var.domain_name
  sku                 = "Standard"
  tags                = var.tags
}

resource "azurerm_network_interface" "gitlab" {
  name                = "gitlab-nic"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.gitlab.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.gitlab.id 
  }
}

resource "azurerm_network_security_group" "gitlab" {
  name                = "gitlab-nsg"
  location            = var.location
  resource_group_name = var.resource_group_name
  tags = var.tags

  security_rule {
    name                       = "HTTP"
    priority                   = 101
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "80"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "HTTPS"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "443"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  security_rule {
    name                       = "SSH"
    priority                   = 102
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
  
}

resource "azurerm_subnet_network_security_group_association" "example" {
  subnet_id                 = azurerm_subnet.gitlab.id
  network_security_group_id = azurerm_network_security_group.gitlab.id
}

resource "azurerm_availability_set" "gitlab" {
  name                = "gitlab-availabilityset"
  location            = var.location
  resource_group_name = var.resource_group_name
  tags                = var.tags
}

resource "azurerm_virtual_machine" "gitlab" {
  name                = "gitlab-vm"
  resource_group_name = var.resource_group_name
  location            = var.location
  vm_size                = "Standard_DS1_v2"
  tags                = var.tags
  network_interface_ids = [
    azurerm_network_interface.gitlab.id,
  ]

  storage_image_reference {
    publisher = "bitnami"
    offer     = "gitlab"
    sku       = "8-5"
    version   = "latest"
  }

  plan {
    name      = "8-5"
    product   = "gitlab"
    publisher = "bitnami"

  }

  storage_os_disk {
    name              = "gitlabdisk"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Premium_LRS"
  }

  os_profile {
    computer_name  = "git-hostname"
    admin_username = var.admin_user
    admin_password = var.admin_password
  }
  
  os_profile_linux_config {
    disable_password_authentication = false
  }
  
}

#----------output file to repo--------------
resource "local_file" "publicip" {
  content         = azurerm_public_ip.gitlab.ip_address
  filename        = "./publicip"
  file_permission = "0644"
}

resource "local_file" "DNS" {
  content         = azurerm_public_ip.gitlab.fqdn
  filename        = "./DNS"
  file_permission = "0644"
}

resource "local_file" "password" {
  content         = var.admin_password
  filename        = "./password"
  file_permission = "0644"
}