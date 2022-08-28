################################################################################
#
# dbell-ina219 | updated 2022.08.26
#
################################################################################

DBELL_INA219_LICENSE = MIT
DBELL_INA219_LICENSE_FILES = LICENSE

define DBELL_INA219_EXTRACT_CMDS
	cp -av ../general/package/dbell-ina219/src/* $(@D)/
endef

define DBELL_INA219_BUILD_CMDS
	(cd $(@D); $(TARGET_CC) -s ina219.c -o ina219)
endef

define DBELL_INA219_INSTALL_TARGET_CMDS
	install -m 0755 -D $(@D)/ina219 $(TARGET_DIR)/usr/sbin/ina219
endef

$(eval $(generic-package))
