[app]
title = Suba 2.0
package.name = suba
package.domain = org.suba
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 2.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

# Aucune permission nécessaire : les données sont dans le dossier privé de l'appli
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
