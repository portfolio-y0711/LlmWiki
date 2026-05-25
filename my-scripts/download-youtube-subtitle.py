import argparse
import math
import os
import re
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound


def extract_video_id(url: str) -> str:
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    raise ValueError(f"유효하지 않은 YouTube URL: {url}")


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
    parser.add_argument("--title", required=True, help="문서 제목")
    parser.add_argument("--output-dir", default="my-raws", help="출력 디렉토리 (기본값: my-raws)")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)
    print(f"자막 다운로드 중... (video_id: {video_id})")

    try:
        transcript_text = download_transcript(video_id)
    except NoTranscriptFound:
        raise SystemExit(f"자막을 찾을 수 없습니다: {video_id}")

    os.makedirs(args.output_dir, exist_ok=True)
    filepath = os.path.join(args.output_dir, sanitize_filename(args.title) + ".md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {args.title}\n\n")
        f.write(transcript_text)

    print(f"저장 완료: {filepath}")


if __name__ == "__main__":
    main()
