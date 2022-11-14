################################################################################
#
# i2c-gpio-custom | updated 2022.11.14
#
################################################################################

I2C_GPIO_CUSTOM_LICENSE = GPL-2.0
I2C_GPIO_CUSTOM_LICENSE_FILES = COPYING

define I2C_GPIO_CUSTOM_EXTRACT_CMDS
	cp ../general/package/i2c-gpio-custom/src/* $(@D)/
endef

I2C_GPIO_CUSTOM_MODULE_MAKE_OPTS = CONFIG_I2C_GPIO_CUSTOM=m \
	KVER=$(LINUX_VERSION_PROBED) \
	KSRC=$(LINUX_DIR)

$(eval $(kernel-module))
$(eval $(generic-package))
