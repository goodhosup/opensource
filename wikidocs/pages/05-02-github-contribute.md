쓰기 권한이 없는 프로젝트에 기여하는 표준 방법은 **포크 → 브랜치 → 커밋 → PR** 입니다.

```text
원본 저장소 (upstream)  ──fork──▶  내 저장소 (origin)  ──clone──▶  내 컴퓨터
        ▲                                   ▲                         │
        └──────── Pull Request ─────────────┴──────── git push ───────┘
```

## 0. 기여할 곳 찾기
- 평소 쓰는 도구나 라이브러리부터 시작하면 동기와 이해도가 높습니다.
- `good first issue`, `help wanted` 라벨이 붙은 이슈를 찾습니다. ([github.com/topics/good-first-issue](https://github.com/topics/good-first-issue), [goodfirstissue.dev](https://goodfirstissue.dev))
- 코드가 아니어도 됩니다: **문서 오타·번역, 버그 재현, 테스트 추가, 이슈 정리**도 훌륭한 기여입니다.
- 국내에서는 컨트리뷰션 아카데미에서 멘토와 함께 시작할 수 있습니다 → [대회와 커뮤니티](https://goodhosup.github.io/opensource/ecosystem/community/)

## 1. 규칙 읽기
기여 전에 저장소의 다음 파일을 확인합니다.

| 파일 | 내용 |
|---|---|
| `README.md` | 프로젝트 소개, 설치, 사용법 |
| `CONTRIBUTING.md` | 기여 방법, 개발 환경, 커밋·PR 규칙 |
| `CODE_OF_CONDUCT.md` | 행동 강령 |
| `LICENSE` | 내 기여도 이 라이선스로 배포됨 |
| 이슈·PR 템플릿 | 작성해야 할 항목 |

큰 변경은 코드를 쓰기 전에 **이슈로 먼저 제안**하고 메인테이너의 의견을 받는 것이 예의이자 시간 절약입니다.

## 2. 포크하고 복제
```bash
gh repo fork owner/project --clone     # 포크 + 클론 + upstream 등록을 한 번에
# 또는 웹에서 Fork 버튼 → 아래 명령
git clone https://github.com/내아이디/project.git
cd project
git remote add upstream https://github.com/owner/project.git
```

## 3. 브랜치 만들어 작업
```bash
git fetch upstream
git switch -c fix/typo-in-readme upstream/main   # 원본 최신 main 에서 브랜치 시작
# ... 수정 ...
git add README.md
git commit -m "docs: README 설치 명령 오타 수정"
```

- 브랜치 하나에 **한 가지 주제**만 담습니다.
- 프로젝트의 테스트·린트를 로컬에서 먼저 돌립니다.
- 프로젝트가 요구하면 커밋에 서명(`git commit -s`, DCO)하거나 CLA에 동의합니다.

## 4. push 하고 PR 만들기
```bash
git push -u origin fix/typo-in-readme
gh pr create --repo owner/project --fill   # 또는 웹에서 "Compare & pull request"
```

좋은 PR 설명:

```markdown
## 무엇을 바꿨나요
README의 설치 명령에서 패키지 이름 오타(`pyhton`)를 고쳤습니다.

## 왜
그대로 복사하면 설치가 실패합니다.

## 확인 방법
수정한 명령으로 새 가상환경에서 설치되는 것을 확인했습니다.

Closes #123
```

[[TIP("💡 자동으로 이슈 닫기")]]
PR 설명에 `Closes #123`, `Fixes #123`, `Resolves #123` 을 쓰면 PR이 기본 브랜치에 병합될 때 해당 이슈가 자동으로 닫힙니다.
[[/TIP]]
## 5. 리뷰 대응
- 리뷰어의 요청을 반영해 같은 브랜치에 커밋하고 push하면 PR에 자동으로 추가됩니다.
- 원본이 그사이 바뀌어 충돌이 나면 `git fetch upstream && git rebase upstream/main` 후 `git push --force-with-lease` 합니다. (프로젝트가 merge를 선호하면 merge로)
- 의견이 다르면 이유를 들어 정중히 설명합니다. 메인테이너도 대부분 자원봉사자입니다.
- 한동안 반응이 없으면 1~2주 뒤 정중하게 한 번 확인을 요청합니다.

## 6. 병합 후 정리
```bash
git switch main
git pull upstream main
git push origin main
git branch -d fix/typo-in-readme
git push origin --delete fix/typo-in-readme
```

## 기여 예절 정리
| 하면 좋은 것 | 피할 것 |
|---|---|
| 이슈에 "제가 해 볼게요"라고 먼저 알리기 | 아무 말 없이 큰 PR 보내기 |
| 작고 집중된 PR | 여러 주제를 섞은 거대한 PR |
| 재현 방법·환경을 적은 버그 리포트 | "안 돼요"만 적은 이슈 |
| 직접 검증한 내용만 제출 | 검증하지 않은 AI 생성 코드·리포트 제출 → [AI가 미치는 영향](https://goodhosup.github.io/opensource/future/ai/) |
| 기존 논의 먼저 검색 | 중복 이슈 |
