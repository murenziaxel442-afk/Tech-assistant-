[app]
# App Details
title = Jervis
package.name = jervisapp
package.domain = org.ganza

# Source Code Settings
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Application Requirements
# Added plyer (for Android system features like vibration, notifications, battery)
requirements = python3, kivy, requests, urllib3, plyer, android

# UI & Display Setup
orientation = portrait
fullscreen = 0

# Android Permissions for Jervis Capabilities
android.permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS, CAMERA, ACCESS_NETWORK_STATE, VIBRATE, WAKE_LOCK

# Hardware Features
android.features = android.hardware.microphone, android.hardware.camera

# Target Android API Levels
android.api = 33
android.minapi = 21
android.ndk_api = 21

# Automation Settings
android.accept_sdk_license = True