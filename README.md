# 🔍 Octopii PII Scanner

AI 기반 개인정보 식별 시스템 - 게시판 첨부파일에서 개인정보를 자동으로 감지하고 분류합니다.

## 📋 프로젝트 개요

이 프로젝트는 [Octopii](https://github.com/redhuntlabs/Octopii) 오픈소스를 기반으로 하여 게시판에서 파일을 첨부할 때 첨부파일 내의 개인정보(PII)를 자동으로 식별하고 분류하는 웹 애플리케이션입니다.

## ✨ 주요 기능

### 🔍 개인정보 감지
- **📧 이메일 주소**: 표준 형식 및 공백 포함 형식
- **📞 전화번호**: 한국, 미국, 국제 형식 지원
- **💳 금융 정보**: 신용카드, 계좌번호, 라우팅 번호, CVV/CVC
- **🆔 신분증/식별번호**: SSN, PAN, 운전면허, 주민등록번호, 여권번호
- **🏠 주소 정보**: 영어/한국어 키워드 매칭
- **🏥 의료 정보**: 환자 ID, 의료 기록 번호, 의료 키워드

### 📊 문서 타입 자동 분류
- 🚗 운전면허
- 🛂 여권
- 💳 신용카드
- 🏦 은행 거래내역
- 🏥 의료 기록
- 🆔 신분증

### 🌍 국가별 특화 감지
- 🇺🇸 미국: SSN, 라우팅 번호
- 🇰🇷 한국: 주민등록번호, 010- 전화번호
- 🇮🇳 인도: PAN, Aadhaar 번호
- 🇬🇧 영국: NI 번호
- 🇨🇦 캐나다: SIN 번호

## 🚀 빠른 시작

### 1. 서버 시작
```bash
python simple-server.py
```

### 2. 브라우저 접속
```
http://localhost:8000/test-debug.html
```

### 3. 테스트 진행
1. **파일 선택 테스트**: 파일 업로드 기능 확인
2. **파일 읽기 테스트**: 파일 내용 읽기 확인
3. **PII 스캔 테스트**: 개인정보 감지 및 분류 확인

## 📁 프로젝트 구조

```
octopii/
├── test-debug.html          # 메인 웹 애플리케이션
├── simple-server.py         # 로컬 HTTP 서버
├── favicon.ico             # 웹사이트 아이콘
├── definitions.json        # PII 정의 및 키워드
├── sample-files/           # 테스트용 샘플 파일들
│   ├── sample-pii.txt      # 개인정보 포함 샘플
│   ├── safe-document.txt   # 안전한 문서 샘플
│   └── mixed-document.txt  # 혼합 문서 샘플
└── README.md              # 프로젝트 문서
```

## 🛠️ 기술 스택

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python 3.x (HTTP Server)
- **PII Detection**: 정규식, 키워드 매칭, 패턴 인식
- **UI Framework**: CSS Grid, Flexbox
- **Browser Support**: Chrome, Firefox, Safari, Edge

## 📖 사용 방법

### 1. 파일 업로드
- 지원 형식: `.txt`, `.md`, `.log`, `.csv`, `.json`, `.xml`, `.pdf`
- 최대 크기: 10MB
- 드래그 앤 드롭 지원

### 2. PII 스캔 결과 확인
- 감지된 개인정보 유형별 분류
- 문서 타입 자동 분류
- 국가별 특화 감지 결과
- 신뢰도 점수 제공

### 3. 결과 해석
- **높은 신뢰도**: 명확한 개인정보 패턴 감지
- **중간 신뢰도**: 가능성 있는 개인정보 감지
- **낮은 신뢰도**: 의심스러운 패턴 감지

## 🔧 고급 설정

### 정규식 패턴 커스터마이징
`test-debug.html` 파일의 `scanForPII` 함수에서 정규식 패턴을 수정할 수 있습니다:

```javascript
// 이메일 패턴 예시
const emailPatterns = [
    /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g,
    /\b[A-Za-z0-9._%+-]+\s*@\s*[A-Za-z0-9.-]+\s*\.\s*[A-Z|a-z]{2,}\b/g
];
```

### 키워드 추가
`definitions.json` 파일에서 감지 키워드를 추가하거나 수정할 수 있습니다.

## 🧪 테스트

### 샘플 파일 테스트
1. `sample-files/sample-pii.txt`: 다양한 개인정보 포함
2. `sample-files/safe-document.txt`: 개인정보 없는 안전한 문서
3. `sample-files/mixed-document.txt`: 일부 개인정보 포함

### 자동 테스트
웹 페이지의 "PII 스캔 테스트" 버튼을 클릭하여 자동으로 샘플 데이터로 테스트할 수 있습니다.

## 🔒 보안 고려사항

- **로컬 처리**: 모든 PII 스캔은 클라이언트 사이드에서 처리
- **데이터 전송 없음**: 파일 내용이 서버로 전송되지 않음
- **임시 저장 없음**: 파일 내용이 디스크에 저장되지 않음

## 🐛 문제 해결

### CORS 오류
```
Access to fetch at 'file:///...' from origin 'null' has been blocked by CORS policy
```
**해결방법**: `simple-server.py`를 실행하여 HTTP 서버를 통해 접속

### 파일 읽기 실패
```
파일을 선택해주세요
```
**해결방법**: 
1. 파일이 올바르게 선택되었는지 확인
2. 지원되는 파일 형식인지 확인
3. 파일 크기가 10MB 이하인지 확인

### PII 감지 안됨
**해결방법**:
1. 정규식 패턴이 해당 형식과 일치하는지 확인
2. 키워드 매칭이 올바른지 확인
3. 파일 인코딩이 UTF-8인지 확인

## 📈 성능 최적화

- **대용량 파일**: 10MB 제한으로 브라우저 성능 보장
- **정규식 최적화**: 효율적인 패턴 매칭
- **메모리 관리**: 파일 처리 후 메모리 정리

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 🙏 감사의 말

- [Octopii](https://github.com/redhuntlabs/Octopii) - 원본 PII 감지 엔진
- [Supabase](https://supabase.com) - 데이터베이스 및 인증 서비스

## 📞 지원

문제가 발생하거나 질문이 있으시면 이슈를 생성해 주세요.

---

**⚠️ 주의사항**: 이 도구는 개발 및 테스트 목적으로 제작되었습니다. 실제 운영 환경에서 사용하기 전에 충분한 테스트를 거쳐 주세요.
