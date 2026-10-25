GitHub Actions는 push, PR, 이슈, 일정 같은 **이벤트**가 일어나면 정의한 **워크플로**를 GitHub의 서버(러너)에서 실행합니다. 공개 저장소는 GitHub 호스팅 러너를 무료로 쓸 수 있습니다.

## 구성 요소
| 요소 | 설명 |
|---|---|
| Workflow | `.github/workflows/*.yml` 파일 하나. 자동화 전체 정의 |
| Event (`on`) | 실행 조건: `push`, `pull_request`, `schedule`, `workflow_dispatch`(수동) 등 |
| Job | 같은 러너에서 실행되는 단계 묶음. 여러 Job은 기본적으로 병렬 |
| Step | 명령(`run`) 또는 미리 만든 액션(`uses`) 하나 |
| Runner | 실행 환경: `ubuntu-latest`, `windows-latest`, `macos-latest` |
| Action | 재사용 가능한 단계. [GitHub Marketplace](https://github.com/marketplace?type=actions)에서 검색 |

## 예: PR마다 테스트 실행 (CI)
```yaml
# .github/workflows/test.yml
name: Test
on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -r requirements.txt
      - run: pytest
```
`matrix` 로 여러 버전에서 동시에 테스트합니다. 결과는 PR 화면의 체크 표시로 나타나고, 브랜치 보호에서 "통과 필수"로 지정할 수 있습니다.

## 자주 쓰는 자동화
| 용도 | 예 |
|---|---|
| CI | 테스트, 린트, 빌드 |
| CD | 패키지 배포(PyPI, npm), 컨테이너 이미지 푸시, Pages 배포 |
| 릴리스 | 태그 push 시 릴리스 노트·바이너리 자동 생성 |
| 저장소 관리 | 신규 이슈 라벨링, 오래된 이슈 정리, 첫 기여자 환영 메시지 |
| 보안 | CodeQL 코드 스캔, 의존성 검토 |

## 비밀 값 사용
API 토큰 같은 값은 **Settings → Secrets and variables → Actions** 에 저장하고 `${{ secrets.이름 }}` 으로 씁니다. 로그에는 자동으로 가려집니다.

```yaml
      - run: ./deploy.sh
        env:
          API_TOKEN: ${{ secrets.API_TOKEN }}
```

## 보안 수칙
- 워크플로 최상단에 `permissions:` 로 `GITHUB_TOKEN` 권한을 최소한으로 줍니다.
- 외부 액션은 가능하면 **커밋 해시로 고정**합니다 (`uses: owner/action@<SHA>`). 태그는 바뀔 수 있습니다.
- 포크에서 온 PR에 비밀 값을 노출하는 `pull_request_target` 은 동작을 이해하고 신중히 씁니다.
- 공급망 공격은 CI를 노립니다 → [향후 방향: 보안과 공급망](https://goodhosup.github.io/opensource/future/trends/)
