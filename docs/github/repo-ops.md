# 저장소 운영과 협업 설정

내 프로젝트를 오픈소스로 운영할 때 갖춰야 할 것들입니다.

## 커뮤니티 건강 파일
GitHub는 저장소의 **Insights → Community Standards** 에서 아래 파일이 갖춰졌는지 체크리스트로 보여 줍니다.

| 파일 | 역할 |
|---|---|
| `README.md` | 무엇을, 왜, 어떻게 설치·사용하는지 |
| `LICENSE` | 사용 조건 |
| `CONTRIBUTING.md` | 기여 방법, 개발 환경, 규칙 |
| `CODE_OF_CONDUCT.md` | 행동 강령 (보통 Contributor Covenant 사용) |
| `SECURITY.md` | 보안 취약점 비공개 신고 방법 |
| `SUPPORT.md` | 질문은 어디로 해야 하는지 |
| `.github/ISSUE_TEMPLATE/` | 이슈 양식 (버그, 기능 요청) |
| `.github/pull_request_template.md` | PR 설명 양식 |
| `.github/FUNDING.yml` | 후원 버튼 (GitHub Sponsors, Open Collective 등) |

조직 계정에 `.github` 라는 저장소를 만들고 이 파일들을 넣으면 조직의 모든 저장소에 기본값으로 적용됩니다.

### README에 담을 내용
1. 프로젝트 이름과 한 줄 설명, 배지(빌드 상태, 버전, 라이선스)
2. 무엇을 해결하는지, 스크린샷
3. 설치와 빠른 시작
4. 사용 예
5. 기여 방법 링크, 라이선스, 연락처

### 이슈 양식 예 (`.github/ISSUE_TEMPLATE/bug_report.yml`)
```yaml
name: 버그 리포트
description: 문제를 알려 주세요
labels: [bug, needs triage]
body:
  - type: textarea
    id: steps
    attributes:
      label: 재현 방법
      placeholder: "1. ... 2. ... 3. ..."
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: 버전
```

## 브랜치 보호
`main` 에 실수로 직접 push하거나 검증 안 된 코드가 병합되는 것을 막습니다. **Settings → Rules → Rulesets** (또는 Branches → Branch protection rules)에서 설정합니다.

| 규칙 | 효과 |
|---|---|
| Require a pull request before merging | PR 없이 직접 push 금지 |
| Required approvals | 최소 승인 인원 (예: 1명) |
| Require review from Code Owners | CODEOWNERS 승인 필수 |
| Require status checks to pass | CI 테스트 통과 필수 |
| Require conversation resolution | 리뷰 대화가 모두 해결돼야 병합 |
| Require signed commits | 서명된 커밋만 허용 |
| Block force pushes / deletions | 강제 push와 브랜치 삭제 금지 |

## 릴리스
1. 버전을 정하고 태그를 만듭니다: `git tag -a v1.2.0 -m "v1.2.0" && git push origin v1.2.0`
2. **Releases → Draft a new release** 에서 태그를 고르고 **Generate release notes** 로 PR 목록 기반 변경 내역을 자동 작성합니다.
3. 바이너리나 패키지 파일을 첨부합니다.

```bash
gh release create v1.2.0 --generate-notes ./dist/*.tar.gz
```

`CHANGELOG.md` 를 [Keep a Changelog](https://keepachangelog.com/ko/) 형식으로 함께 관리하면 사용자가 변경 사항을 쉽게 파악합니다.

## 메인테이너의 지속가능성
- 응답 기대치를 README에 밝힙니다 (예: "주말에만 확인합니다").
- 반복 질문은 문서·FAQ·Discussions로 돌립니다.
- 신뢰할 수 있는 기여자를 Triage → Write 권한의 공동 메인테이너로 키웁니다.
- 오래된 이슈 정리는 `actions/stale` 같은 자동화로 돕되, 사람의 판단을 대체하지 않게 합니다.
- GitHub Sponsors 등으로 후원을 받을 수 있습니다.
