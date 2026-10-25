공개 저장소는 대부분의 보안 기능을 무료로 쓸 수 있습니다. **Settings → Code security** (또는 Security) 에서 켭니다.

| 기능 | 하는 일 | 권장 |
|---|---|---|
| **Dependabot alerts** | 의존성에 알려진 취약점(CVE)이 있으면 알림 | 켜기 |
| **Dependabot security updates** | 취약한 의존성을 고치는 PR 자동 생성 | 켜기 |
| **Dependabot version updates** | `.github/dependabot.yml` 로 정기 업데이트 PR | 선택 |
| **Secret scanning** | 커밋된 토큰·키 탐지 | 켜기 |
| **Push protection** | 비밀이 포함된 push를 사전 차단 | 켜기 |
| **Code scanning (CodeQL)** | 소스 코드의 보안 취약 패턴 정적 분석 | 켜기 (Default setup) |
| **Private vulnerability reporting** | 취약점을 공개 이슈 대신 비공개로 신고받음 | 켜기 |
| **Security advisories** | 취약점 공지 작성, CVE 발급 요청 | 필요 시 |
| **Dependency graph / SBOM 내보내기** | 의존성 목록, SPDX 형식 SBOM 다운로드 | 확인 |

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

## 계정과 조직 보안
- 2단계 인증(2FA)과 패스키 사용
- 토큰은 fine-grained PAT로 권한·기간 최소화, 사용하지 않는 토큰과 SSH 키 정기 삭제
- 조직은 멤버 2FA 의무화, 외부 협업자 권한 정기 점검
- 커밋 서명으로 작성자 위장 방지

## SECURITY.md 예
```markdown
# 보안 정책

## 지원 버전
| 버전 | 지원 |
|---|---|
| 2.x | ✅ |
| 1.x | ❌ |

## 취약점 신고
공개 이슈로 올리지 말고, 저장소의 Security 탭 → "Report a vulnerability"로 비공개 신고해 주세요.
보통 7일 이내에 답변드립니다.
```

오픈소스 공급망 보안의 큰 흐름(SBOM, 국내 SW 공급망 보안 로드맵)은 [향후 방향](https://goodhosup.github.io/opensource/future/trends/)을 참고하세요.
