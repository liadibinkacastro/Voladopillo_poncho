[app]
title = Volado pillo Poncho
package.name = voladopilloponcho
package.domain = com.lia.voladopillo
source.dir =.
source.include_exts = py,png,jpg,jpeg
version = 1.0
icon.filename = %(source.dir)s/icono.png
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
p4a.branch = master
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.2
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.sdk_dir = /usr/local/lib/android/sdk
p4a.sdk_dir = /usr/local/lib/android/sdk

[buildozer]
log_level = 2
warn_on_root = 1
