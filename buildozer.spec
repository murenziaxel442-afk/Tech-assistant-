[app]
# (str) Title of your application
title = Jervis

# (str) Package name
package.name = jervisapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ganza

# (str) Source code where the main.py lives
source.dir = .

# (list) Application requirements
requirements = python3, kivy

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = RECORD_AUDIO, INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# Automatically accept the Android SDK License so the build doesn't freeze
android.accept_sdk_license = True