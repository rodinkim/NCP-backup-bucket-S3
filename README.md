# NCP Bucket Backup Automation with AWS S3 API

네이버 클라우드에서 S3 API를 이용한 object bucket으로 백업 파일을 자동 업로드하는 작업입니다.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Script Overview](#script-overview)

## Prerequisites

Before running this script, ensure that the following tools are installed on your server:

- **AWS CLI**: Required to interact with NCP bucket using AWS S3 API. (AWS CLI v2)
- **zip**: Used to compress the backup files.

### AWS CLI Configuration

Configure the AWS CLI to work with NCP Object Storage by adding the endpoint URL and credentials:

```bash
aws configure

### Installation

sudo apt-get update
sudo apt-get install zip awscli

sudo yum install zip awscli

nano /root/script/backup.sh


### Script Overview

The backup.sh script performs the following steps:

Set up the environment variables.
Compress the target directory into a .zip file.
Upload the compressed file to the NCP bucket using AWS S3 API.
Remove the local backup file after upload.


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
