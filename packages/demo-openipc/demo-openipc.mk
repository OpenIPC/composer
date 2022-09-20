################################################################################
#
# demo-openipc | updated 2022.09.13
#
################################################################################

DEMO_OPENIPC_LICENSE = MIT
DEMO_OPENIPC_LICENSE_FILES = LICENSE

define DEMO_OPENIPC_EXTRACT_CMDS
	cp ../general/package/demo-openipc/src/* $(@D)/
endef

define DEMO_OPENIPC_BUILD_CMDS
	(cd $(@D); $(TARGET_CC) -s demo-openipc.c -o demo-openipc)
endef

define DEMO_OPENIPC_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	cp ../general/package/demo-openipc/files/S97demo $(TARGET_DIR)/etc/init.d

	install -m 0755 -D $(@D)/demo-openipc $(TARGET_DIR)/usr/sbin/demo-openipc
endef

$(eval $(generic-package))
