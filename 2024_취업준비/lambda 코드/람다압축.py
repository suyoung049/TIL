import json
import boto3
import os
import subprocess
import logging
import uuid
import urllib3
import urllib.parse


SLACK_WEBHOOK_URL = "https://api-lms-saas.sparta-devcamp.com/receive-compressed-url"
http = urllib3.PoolManager()

# 로깅 설정
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

s3 = boto3.client('s3')

def lambda_handler(event, context):
    logger.info('Lambda function started')
    try:
        clear_tmp_directory()
        
        # S3 이벤트로부터 버킷 이름과 객체 키를 가져옴
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        logger.info(f'Received event for bucket: {bucket_name}, key: {object_key}')
        
        # 객체 키를 URL 디코딩
        decoded_object_key = urllib.parse.unquote(object_key.replace('+', ' '))
        logger.info(f'Decoded object key: {decoded_object_key}')
        
        # S3 객체 메타데이터를 가져와 파일 크기를 확인
        try:
            head_object = s3.head_object(Bucket=bucket_name, Key=decoded_object_key)
            file_size = head_object['ContentLength']
            file_size_mb = file_size / (1024 * 1024)
            logger.info(f'File size: {file_size_mb:.2f} MB')
            
            # 파일 사이즈가 200MB 이하인 경우
            if file_size_mb <= 200:
                logger.info('File size is less than or equal to 300MB. Skipping compression.')
                return {
                    'statusCode': 200,
                    'body': f'File size is less than or equal to 300MB. No compression needed for {object_key}.'
                }
        except Exception as e:
            logger.error(f'Error getting file size from S3: {e}', exc_info=True)
            raise
    
        # 무한 루프 방지를 위해 'compressed/' 접두사를 가진 파일은 무시
        if decoded_object_key.startswith('compressed/'):
            logger.info('Ignored compressed file.')
            return {
                'statusCode': 200,
                'body': 'Ignored compressed file.'
            }
        
        
        # 고유한 파일 이름 생성
        unique_id = uuid.uuid4()
        download_path = f'/tmp/{unique_id}_{os.path.basename(decoded_object_key)}'
        compressed_path = f'/tmp/compressed_{unique_id}_{os.path.basename(decoded_object_key)}'
        
        # S3에서 파일 다운로드
        try:
            logger.info(f'Trying to download {decoded_object_key} from bucket {bucket_name}')
            with open(download_path, 'wb') as f:
                s3.download_fileobj(bucket_name, decoded_object_key, f)
            logger.info(f'File downloaded from S3 to {download_path}')
        except Exception as e:
            logger.error(f'Error downloading file from S3: {e}', exc_info=True)
            raise
        
        # 파일 압축
        compress_file_with_ffmpeg(download_path, compressed_path)
        logger.info(f'File compressed to {compressed_path}')
        
        # 압축된 파일 크기 확인
        compressed_file_size = os.path.getsize(compressed_path)
        compressed_file_size_mb = compressed_file_size / (1024 * 1024)
        logger.info(f'Compressed file size: {compressed_file_size_mb:.2f} MB')
        
        # 압축 파일 업로드
        try:
            compressed_key = f'compressed/{os.path.basename(compressed_path)}'
            s3.upload_file(compressed_path, bucket_name, compressed_key)
            logger.info(f'Compressed file uploaded to S3 with key {compressed_key}')
        except Exception as e:
            logger.error(f'Error uploading file to S3: {e}', exc_info=True)
            raise
        
        # 로컬 파일 삭제
        os.remove(download_path)
        os.remove(compressed_path)
        logger.info('Local files removed')
    
        compressed_file_url = f'https://{bucket_name}.s3.amazonaws.com/{compressed_key}'
        
        try:
            api_message = {
                'message': f'File successfully compressed and uploaded to S3.',
                'compressed_file_url': compressed_file_url
            }
            encoded_message = json.dumps(api_message).encode('utf-8')
            response = http.request(
                'POST',
                SLACK_WEBHOOK_URL,  # 이 URL은 지정한 API 서버로 전송됩니다
                body=encoded_message,
                headers={'Content-Type': 'application/json'}
            )
            logger.info(f'Notification sent to API, status: {response.status}')
        except Exception as e:
            logger.error(f'Error sending notification to API: {e}', exc_info=True)
            raise
        
        return {
            'statusCode': 200,
            'body': f'Successfully compressed {object_key}. Original size: {file_size_mb:.2f} MB, Compressed size: {compressed_file_size_mb:.2f} MB'
        }
    except Exception as e:
        logger.error(f'Error occurred: {e}', exc_info=True)
        return {
            'statusCode': 500,
            'body': str(e)
        }

def compress_file_with_ffmpeg(input_path, output_path):
    logger.info('Starting compression')
    logger.info(f'Input path: {input_path}, Output path: {output_path}')
    
    audio_bitrate = 128 * 1000  # 128kbps 오디오
    video_bitrate = 2500000  # 2,300kbps 비디오
    logger.info(f'Calculated video bitrate: {video_bitrate} bps, audio bitrate: {audio_bitrate} bps')

    ffmpeg_command = [
        '/opt/ffmpeg-7.0-amd64-static/ffmpeg',  # Lambda Layer에 포함된 ffmpeg 바이너리 경로
        '-i', input_path,
        '-b:v', str(video_bitrate),
        '-maxrate', str(video_bitrate),
        '-bufsize', str(video_bitrate // 2),
        '-b:a', str(audio_bitrate),
        '-threads', 'auto',
        '-preset', 'ultrafast',
        output_path
    ]
    result = subprocess.run(ffmpeg_command, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error(f"FFmpeg failed with error: {result.stderr}")
        raise Exception(f"FFmpeg failed with error: {result.stderr}")
    logger.info('Compression completed successfully')
    return result.stdout

def clear_tmp_directory():
    logger.info('Clearing /tmp directory')
    try:
        for root, dirs, files in os.walk('/tmp'):
            for file in files:
                os.remove(os.path.join(root, file))
        logger.info("Temporary directory cleared")
    except Exception as e:
        logger.error(f"Error clearing temporary directory: {e}", exc_info=True)
