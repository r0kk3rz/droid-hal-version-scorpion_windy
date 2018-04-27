# rpm_device is the name of the ported device
%define rpm_device scorpion_windy
# rpm_vendor is used in the rpm space
%define rpm_vendor sony

# Manufacturer and device name to be shown in UI
%define vendor_pretty Sony
%define device_pretty Xperia Z3 Tablet Compact (WIFI)

# ../droid-hal-version/droid-hal-device.inc for similar macros
%define have_vibrator_native 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc
