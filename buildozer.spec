[app]
title = Volado pillo Poncho
package.name = voladopilloponcho
package.domain = com.lia.voladopillo

source.dir =.
source.include_exts = py,png,jpg,jpeg

version = 1.0
requirements = python3,kivy==2.2.0,pillow

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True

[buildozer]
log_level = 2
warn_on_root = 1
