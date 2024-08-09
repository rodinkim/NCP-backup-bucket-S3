#!/bin/bash

# 'cron'에서 환경 변수 제한 방지
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 현재 날짜를 형식에 맞게 가져오기
DATE=$(date +"%Y%m%d")

# 압축할 파일 경로와 압축 파일명 정의
SOURCE_DIR="/path/to/source/"
BACKUP_FILE="/path/to/source/${DATE}_Backup.zip"

# 압축 파일 생성
echo "Creating backup archive..."
zip -r "$BACKUP_FILE" "$SOURCE_DIR"

# AWS S3에 업로드
echo "Uploading backup to AWS S3..."
aws --endpoint-url=http://kr.objectstorage.ncloud.com s3 cp "$BACKUP_FILE" s3://path/to/s3/

# 압축 파일 삭제
echo "Removing local backup archive..."
rm -rf "$BACKUP_FILE"

echo "Backup and upload process completed."
