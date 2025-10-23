#!/usr/bin/env python3
"""
간단한 HTTP 서버 - Python 3.13 호환
CORS 문제 해결을 위한 로컬 서버
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # CORS 헤더 추가
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        # OPTIONS 요청 처리 (CORS preflight)
        self.send_response(200)
        self.end_headers()

def run_server(port=8000):
    """서버 실행"""
    # 현재 디렉토리를 서버 루트로 설정
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", port), CORSHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("🚀 PII 스캐너 로컬 서버가 시작되었습니다!")
        print("=" * 60)
        print(f"📱 브라우저에서 다음 주소로 접속하세요:")
        print(f"   http://localhost:{port}")
        print(f"   또는")
        print(f"   http://127.0.0.1:{port}")
        print("=" * 60)
        print("⏹️  서버를 중지하려면 Ctrl+C를 누르세요")
        print("=" * 60)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 서버를 종료합니다.")

if __name__ == "__main__":
    # 포트 번호 확인
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ 잘못된 포트 번호입니다. 기본값 8000을 사용합니다.")
    
    run_server(port)
