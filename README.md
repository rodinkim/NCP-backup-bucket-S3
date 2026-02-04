# NCP Bucket Backup Automation with AWS S3 API

네이버 클라우드에서 S3 API를 이용한 object bucket으로 백업 파일을 자동 업로드하는 작업입니다.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Script Overview](#script-overview)

## Prerequisites

Before running this script, ensure that the following tools are installed on your server:

- **AWS CLI**: Required to interact with NCP bucket using AWS S3 API. (AWS CLI v2)
- **Python 3**: Used to run the backup script.
- **zip**: Used to compress the backup files (via Python's zipfile module).

### AWS CLI Configuration

Configure the AWS CLI to work with NCP Object Storage by adding the endpoint URL and credentials:

```bash
aws configure
```

### Installation

sudo apt-get update
sudo apt-get install zip awscli

sudo yum install zip awscli

nano /root/script/ncp-s3-bck.py


### Script Overview

The ncp-s3-bck.py script performs the following steps:

Set up the environment variables.
Compress the target directory into a .zip file.
Upload the compressed file to the NCP bucket using AWS S3 API.
Remove the local backup file after upload.

```bash
python3 ncp-s3-bck.py \\
  --source-dir /path/to/source/ \\
  --endpoint-url http://kr.objectstorage.ncloud.com \\
  --s3-uri s3://path/to/s3/
```
