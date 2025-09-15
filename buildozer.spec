[app]
title = Violão com Ed (Testes)
package.name = violaocomed
package.domain = org.ed
source.dir = .
source.include_exts = py,png,jpg,kv,mp3,mp4,mpeg,ttf
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.1.1
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png
orientation = portrait

[android]
permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
api = 31
minapi = 21
archs = arm64-v8a, armeabi-v7a
apptheme = "@android:style/Theme.NoTitleBar"
add_assets = assets/

[buildozer]
log_level = 2
warn_on_root = 1