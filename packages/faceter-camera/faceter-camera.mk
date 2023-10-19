################################################################################
#
# faceter-camera
#
################################################################################

FACETER_CAMERA_VERSION = 1.0.0
FACETER_CAMERA_SITE = https://github.com/openipc/faceter/archive
FACETER_CAMERA_SOURCE = master.tar.gz

FACETER_CAMERA_LICENSE = PROPRIETARY
FACETER_CAMERA_LICENSE_FILES = LICENSE

FACETER_CAMERA_PLACE = mips_ingenic_t31

FACETER_CAMERA_DEPENDENCIES = \
	json-c-openipc libcurl-openipc libyaml
	
define FACETER_CAMERA_INSTALL_TARGET_CMDS
	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc
	$(INSTALL) -m 644 -t $(TARGET_DIR)/etc $(@D)/$(FACETER_CAMERA_PLACE)/configs/faceter-client-settings.json

	$(INSTALL) -m 755 -d $(TARGET_DIR)/etc/init.d
	$(INSTALL) -m 755 -t $(TARGET_DIR)/etc/init.d $(@D)/$(FACETER_CAMERA_PLACE)/configs//S96faceter-camera

	$(INSTALL) -m 755 -d $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 755 -t $(TARGET_DIR)/usr/bin $(@D)/$(FACETER_CAMERA_PLACE)/faceter-camera
	
	$(INSTALL) -m 755 -d $(TARGET_DIR)/opt/faceter-camera
	$(INSTALL) -m 644 -t $(TARGET_DIR)/opt/faceter-camera $(@D)/$(FACETER_CAMERA_PLACE)/audio/*.pcm
endef

$(eval $(generic-package))