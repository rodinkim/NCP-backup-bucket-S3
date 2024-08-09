# NCP Bucket Backup Automation with AWS S3 API

This project provides a script that automates the backup of a directory and uploads it to an NCP (Naver Cloud Platform) bucket using the AWS S3 API. The script is scheduled to run every Friday at 9 AM using `cron`.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Script Overview](#script-overview)
- [Setting Up the Cron Job](#setting-up-the-cron-job)
- [Logging and Troubleshooting](#logging-and-troubleshooting)
- [License](#license)

## Prerequisites

Before running this script, ensure that the following tools are installed on your server:

- **AWS CLI**: Required to interact with NCP bucket using AWS S3 API.
- **zip**: Used to compress the backup files.
- **cron**: To schedule the script execution.

### AWS CLI Configuration

Configure the AWS CLI to work with NCP Object Storage by adding the endpoint URL and credentials:

```bash
aws configure
