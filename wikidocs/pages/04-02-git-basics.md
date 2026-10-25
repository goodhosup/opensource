## 저장소 만들기
```bash
mkdir my-project && cd my-project
git init                 # 현재 폴더를 Git 저장소로 만듦 (.git 폴더 생성)
```
이미 있는 원격 저장소를 받아올 때는 `git clone` 을 씁니다 → [원격 저장소](https://goodhosup.github.io/opensource/git/remote/)

## 기본 흐름: 수정 → 스테이징 → 커밋
```bash
git status               # 어떤 파일이 바뀌었는지 확인
git add README.md        # 특정 파일 스테이징
git add .                # 현재 폴더의 모든 변경 스테이징
git commit -m "README 추가"   # 스테이징된 변경을 커밋
```

[[TIP("💡 `git add -p`")]]
파일의 변경을 덩어리(hunk) 단위로 보여 주며 하나씩 골라 스테이징합니다. 한 파일에 섞인 여러 작업을 나눠 커밋할 때 유용합니다.
[[/TIP]]
## 상태와 차이 확인
| 명령 | 설명 |
|---|---|
| `git status` | 변경·스테이징·추적되지 않은 파일 목록 |
| `git status -s` | 짧은 형식 |
| `git diff` | 작업 디렉터리 vs 스테이징 영역 (아직 add 안 한 변경) |
| `git diff --staged` | 스테이징 영역 vs 마지막 커밋 (커밋될 변경) |
| `git diff main..feature` | 두 브랜치 비교 |

## 이력 보기
```bash
git log                          # 전체 이력
git log --oneline                # 한 줄 요약
git log --oneline --graph --all  # 모든 브랜치를 그래프로
git log -p README.md             # 특정 파일의 변경 내용까지
git log --author="홍길동"          # 작성자로 필터
git show <커밋해시>                # 특정 커밋 상세
git blame README.md              # 각 줄을 마지막으로 바꾼 커밋과 작성자
```

## 파일 삭제와 이름 변경
```bash
git rm old.txt                # 삭제하고 스테이징
git rm --cached secret.env    # Git 추적만 중단 (파일은 남김)
git mv old.md new.md          # 이름 변경
```

## .gitignore
커밋하지 않을 파일을 지정합니다. 저장소 최상위에 `.gitignore` 파일을 만듭니다.

```gitignore
# 빌드 결과물
build/
dist/
*.log

# 환경 설정과 비밀 정보
.env
*.pem

# 운영체제·편집기 파일
.DS_Store
.vscode/
```

[[TIP("💡 팁")]]
[github/gitignore](https://github.com/github/gitignore) 저장소에 언어·프레임워크별 템플릿이 있습니다. GitHub에서 새 저장소를 만들 때 고를 수도 있습니다.
[[/TIP]]
## 좋은 커밋 메시지
```text
로그인 실패 시 오류 메시지 표시          ← 제목: 50자 안팎, 무엇을 했는지

비밀번호가 틀렸을 때 아무 반응이 없어       ← 본문: 왜 바꿨는지
사용자가 혼란스러워하던 문제를 고친다.

Fixes #42                              ← 관련 이슈
```

많은 오픈소스 프로젝트가 **Conventional Commits** 규칙을 씁니다.

| 접두어 | 의미 | 예 |
|---|---|---|
| `feat:` | 새 기능 | `feat: 다크 모드 추가` |
| `fix:` | 버그 수정 | `fix: 한글 파일명 깨짐 수정` |
| `docs:` | 문서 | `docs: 설치 방법 보완` |
| `refactor:` | 동작 변화 없는 코드 정리 | `refactor: 인증 모듈 분리` |
| `test:` | 테스트 | `test: 로그인 테스트 추가` |
| `chore:` | 빌드·설정 등 잡무 | `chore: 의존성 업데이트` |

기여하기 전에 프로젝트의 `CONTRIBUTING.md` 에서 커밋 규칙을 먼저 확인하세요.
