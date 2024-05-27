#!/bin/bash

USER_NAME=$(whoami)

SERVICE_FILE=/etc/systemd/system/TechShadow.service

SERVICE_CONTENT="[Unit]
Description=TechShadow AUV Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/TechShadow/main.py
WorkingDirectory=/home/TechShadow
StandardOutput=inherit
StandardError=inherit
Restart=always
User=$USER_NAME

[Install]
WantedBy=multi-user.target"

if [ "$(id -u)" != "0" ]; then
   echo "Bu script'i sudo veya root olarak çalıştırmalısınız" 1>&2
   exit 1
fi

echo "$SERVICE_CONTENT" > $SERVICE_FILE

systemctl daemon-reload

systemctl enable TechShadow.service

systemctl start TechShadow.service

echo "TechShadow servisi başarıyla oluşturuldu ve başlatıldı."

