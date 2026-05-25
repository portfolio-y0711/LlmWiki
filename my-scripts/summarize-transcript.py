# /// script
# dependencies = ["anthropic"]
# ///

import argparse
import os
import re
import anthropic

AGENT_PROMPT_FILE = "my-agents/professional-video-content-structuring-agent.md"


def load_file(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def extract_from_code_block(text: str) -> str:
    """에이전트가 마크다운 코드 블록으로 감싸서 응답한 경우 내용만 추출합니다."""
    match = re.search(r"```(?:markdown)?\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()


def summarize(transcript: str) -> str:
    agent_prompt = load_file(AGENT_PROMPT_FILE)
    full_prompt = agent_prompt.replace("{사용자의 SRT 파일 내용}", transcript)

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        messages=[{"role": "user", "content": full_prompt}],
    )
    return extract_from_code_block(message.content[0].text)


def main():
    parser = argparse.ArgumentParser(description="영상 자막을 Claude로 구조화 요약")
    parser.add_argument("--file", required=True, help="자막 마크다운 파일 경로")
    parser.add_argument("--output", help="출력 파일 경로 (기본: 원본 파일에 _structured 접미사)")
    args = parser.parse_args()

    transcript = load_file(args.file)
    print("Claude API로 구조화 요약 중...")
    structured = summarize(transcript)

    output_path = args.output or os.path.splitext(args.file)[0] + "_structured.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(structured)

    print(f"구조화 완료: {output_path}")
    print(f"STRUCTURED_FILE={output_path}")


if __name__ == "__main__":
    main()
