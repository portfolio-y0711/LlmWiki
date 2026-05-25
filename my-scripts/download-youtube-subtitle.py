# 필요한 라이브러리 설치
import math
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound # YouTubeTranscriptApi 클래스 import

def format_time(seconds):
    """초를 SRT 시간 형식(HH:MM:SS,ms)으로 변환합니다."""
    # 초의 정수부와 소수부를 분리합니다.
    frac_seconds, int_seconds = math.modf(seconds)
    int_seconds = int(int_seconds)

    milliseconds = int(frac_seconds * 1000)

    # 초를 시, 분, 초로 변환합니다.
    minutes, seconds_part = divmod(int_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    # SRT 형식에 맞게 HH:MM:SS,ms로 포맷팅합니다.
    return f"{hours:02d}:{minutes:02d}:{seconds_part:02d},{milliseconds:03d}"

def generate_srt_from_youtube(video_id, filename="subtitle.srt", languages=['ko', 'en']):
    """YouTube 동영상 ID를 받아 SRT 형식의 자막을 생성하고 파일에 저장합니다."""
    try:
        # YouTubeTranscriptApi 객체 생성
        ytt_api = YouTubeTranscriptApi()

        # 사용 가능한 자막 리스트 가져오기
        transcript_list_obj = ytt_api.list(video_id)

        # 요청한 언어로 자막 찾기
        # find_transcript는 Transcript 객체를 반환하며, fetch()를 호출해야 실제 데이터를 가져옴
        transcript_obj = transcript_list_obj.find_transcript(languages)
        transcript_data = transcript_obj.fetch()

        with open(filename, 'w', encoding='utf-8') as f:
            # 각 자막 세그먼트를 순회하며 SRT 형식으로 파일에 씁니다.
            for i, entry in enumerate(transcript_data, 1):
                start_time = entry.start # Fixed: Access as attribute
                end_time = start_time + entry.duration # Fixed: Access as attribute
                text = entry.text # Fixed: Access as attribute

                # SRT 블록 작성
                f.write(f"{i}\n")
                f.write(f"{format_time(start_time)} --> {format_time(end_time)}\n")
                f.write(f"{text}\n")
                f.write("\n") # 블록 간 빈 줄 추가
        print(f"자막이 '{filename}' 파일로 성공적으로 저장되었습니다.")

    except NoTranscriptFound:
        print(f"'{video_id}' 영상에 요청한 언어({', '.join(languages)})의 자막을 찾을 수 없습니다.")
        print("- 다른 언어를 시도하거나 동영상 자막 제공 여부를 확인해 주세요.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
        print(f"'{video_id}' 영상의 자막을 가져올 수 없습니다. 다음을 확인해 주세요:")
        print("- 동영상이 존재하지 않거나 비공개일 수 있습니다.")
        print("- 요청한 언어의 자막이 없을 수 있습니다.")

# 제공된 URL에서 비디오 ID 추출
video_url = "https://www.youtube.com/watch?v=VmIUXVlt7_I"
video_id = video_url.split("v=")[1].split("&")[0]

# SRT 자막 생성 함수 호출 및 파일 저장
generate_srt_from_youtube(video_id, filename="youtube_subtitle.srt")