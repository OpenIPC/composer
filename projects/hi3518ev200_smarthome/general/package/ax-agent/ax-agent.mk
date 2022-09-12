################################################################################
#
# ax-agent | updated 2022.09.04
#
################################################################################

AX_AGENT_LICENSE = MIT
AX_AGENT_LICENSE_FILES = LICENSE

define AX_AGENT_EXTRACT_CMDS
	cp ../general/package/ax-agent/src/ax-agent.c $(@D)/
endef

define AX_AGENT_BUILD_CMDS
	(cd $(@D); $(TARGET_CC) -s ax-agent.c -o ax-agent)
endef

define AX_AGENT_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	cp ../general/package/ax-agent/files/S97agent $(TARGET_DIR)/etc/init.d

	install -m 0755 -D $(@D)/ax-agent $(TARGET_DIR)/usr/sbin/ax-agent
endef

$(eval $(generic-package))
