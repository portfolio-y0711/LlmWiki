# /// script
# dependencies = ["youtube-transcript-api", "requests"]
# ///

import argparse
import os
import re
import requests
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound


def extract_video_id(url: str) -> str:
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    raise ValueError(f"유효하지 않은 YouTube URL: {url}")


def fetch_youtube_title(url: str) -> str:
    oembed_url = f"https://www.youtube.com/oembed?url={url}&format=json"
    response = requests.get(oembed_url, timeout=10)
    response.raise_for_status()
    return response.json()["title"]


def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()


def download_transcript(video_id: str, languages=("ko", "en")) -> str:
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.list(video_id)
    transcript_obj = transcript_list.find_transcript(list(languages))
    transcript_data = transcript_obj.fetch()
    return "\n".join(entry.text for entry in transcript_data)


def main():
    parser = argparse.ArgumentParser(description="YouTube 자막 다운로드 후 마크다운 저장")
    parser.add_argument("--url", required=True, help="YouTube 영상 URL")
    parser.add_argument("--title", help="문서 제목 (미입력 시 YouTube 제목 자동 사용)")
    parser.add_argument("--output-dir", default="my-raws", help="출력 디렉토리 (기본값: my-raws)")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)
    print(f"자막 다운로드 중... (video_id: {video_id})")

    if args.title:
        title = args.title
    else:
        print("YouTube 제목 조회 중...")
        title = fetch_youtube_title(args.url)

    print(f"영상 제목: {title}")

    try:
        transcript_text = download_transcript(video_id)
    except NoTranscriptFound:
        raise SystemExit(f"자막을 찾을 수 없습니다: {video_id}")

    os.makedirs(args.output_dir, exist_ok=True)
    safe_title = sanitize_filename(title)
    filepath = os.path.join(args.output_dir, safe_title + ".md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(transcript_text)

    print(f"저장 완료: {filepath}")
    print(f"YOUTUBE_TITLE={title}")
    print(f"OUTPUT_FILE={filepath}")


if __name__ == "__main__":
    main()
