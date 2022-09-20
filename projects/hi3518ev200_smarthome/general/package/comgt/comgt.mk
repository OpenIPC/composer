################################################################################
#
# comgt | updated 2022.09.13
#
################################################################################

COMGT_LICENSE = GPL
COMGT_LICENSE_FILES = LICENSE

define COMGT_EXTRACT_CMDS
	cp ../general/package/demo-openipc/src/* $(@D)/
endef

define COMGT_BUILD_CMDS
	(cd $(@D); $(TARGET_CC) -s comgt.c -o comgt)
endef

define COMGT_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/usr/sbin
	install -m 0755 -D $(@D)/comgt $(TARGET_DIR)/usr/sbin/comgt
endef

$(eval $(generic-package))
