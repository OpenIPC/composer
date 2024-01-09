################################################################################
#
# webui
#
################################################################################

WEBUI_SITE_METHOD = git
WEBUI_SITE = https://github.com/openipc/webui
WEBUI_VERSION = bbb49c57695c116a17219d0898dc11cc696261df

WEBUI_LICENSE = MIT
WEBUI_LICENSE_FILES = LICENSE

define WEBUI_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc
	cp $(WEBUI_PKGDIR)/files/httpd.conf $(TARGET_DIR)/etc

	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	cp $(WEBUI_PKGDIR)/files/S50httpd $(TARGET_DIR)/etc/init.d
	cp -rv $(@D)/files/etc/init.d/* $(TARGET_DIR)/etc/init.d

	$(INSTALL) -m 755 -d $(TARGET_DIR)/usr
	cp -rv $(@D)/files/usr/sbin $(TARGET_DIR)/usr

	$(INSTALL) -m 755 -d $(TARGET_DIR)/var
	cp -rv $(@D)/files/var/www $(TARGET_DIR)/var
endef

$(eval $(generic-package))
