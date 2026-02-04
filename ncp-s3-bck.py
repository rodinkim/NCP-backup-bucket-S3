#!/usr/bin/env python3
import argparse
import datetime as dt
import os
import subprocess
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def build_backup_filename(source_dir: Path, date_str: str) -> Path:
    return source_dir / f"{date_str}_Backup.zip"


def zip_directory(source_dir: Path, backup_file: Path) -> None:
    with ZipFile(backup_file, "w", compression=ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            root_path = Path(root)
            for filename in files:
                file_path = root_path / filename
                if file_path == backup_file:
                    continue
                arcname = file_path.relative_to(source_dir)
                zipf.write(file_path, arcname)


def upload_to_s3(backup_file: Path, endpoint_url: str, s3_uri: str) -> None:
    subprocess.run(
        [
            "aws",
            f"--endpoint-url={endpoint_url}",
            "s3",
            "cp",
            str(backup_file),
            s3_uri,
        ],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Backup a directory and upload to S3.")
    parser.add_argument("--source-dir", required=True, help="Directory to back up")
    parser.add_argument("--endpoint-url", required=True, help="S3 endpoint URL")
    parser.add_argument("--s3-uri", required=True, help="S3 destination URI")
    args = parser.parse_args()

    source_dir = Path(args.source_dir).expanduser().resolve()
    if not source_dir.is_dir():
        raise SystemExit(f"Source directory does not exist: {source_dir}")

    date_str = dt.datetime.now().strftime("%Y%m%d")
    backup_file = build_backup_filename(source_dir, date_str)

    print("Creating backup archive...")
    zip_directory(source_dir, backup_file)

    print("Uploading backup to AWS S3...")
    upload_to_s3(backup_file, args.endpoint_url, args.s3_uri)

    print("Removing local backup archive...")
    backup_file.unlink()

    print("Backup and upload process completed.")


if __name__ == "__main__":
    main()
