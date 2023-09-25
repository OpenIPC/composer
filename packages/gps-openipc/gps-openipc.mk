################################################################################
#
# gps-openipc | updated 2023.09.25
#
################################################################################

GPS_OPENIPC_LICENSE = MIT
GPS_OPENIPC_LICENSE_FILES = LICENSE

define GPS_OPENIPC_EXTRACT_CMDS
	cp -avr $(GPS_OPENIPC_PKGDIR)/src/* $(@D)/
endef

define GPS_OPENIPC_BUILD_CMDS
	(cd $(@D); $(TARGET_CC) -s gps-openipc.c -o gps-openipc)
endef

define GPS_OPENIPC_INSTALL_TARGET_CMDS
	install -m 0755 -D $(@D)/gps-openipc $(TARGET_DIR)/usr/sbin/gps-openipc
endef

$(eval $(generic-package))
