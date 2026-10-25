# GitHub CLI (gh)

`gh` 는 GitHub를 터미널에서 다루는 공식 도구입니다. 웹 브라우저를 오가지 않고 저장소·이슈·PR·Actions를 관리합니다. 설치는 [cli.github.com](https://cli.github.com)을 참고합니다.

```bash
gh auth login            # 로그인 (Git HTTPS 인증도 함께 설정)
gh auth status
```

## 저장소
| 명령 | 설명 |
|---|---|
| `gh repo create 이름 --public --source=. --push` | 현재 폴더로 새 저장소 만들고 push |
| `gh repo clone owner/repo` | 복제 |
| `gh repo fork owner/repo --clone` | 포크하고 복제 |
| `gh repo view --web` | 브라우저로 열기 |
| `gh repo sync` | 포크를 원본과 동기화 |

## 이슈
| 명령 | 설명 |
|---|---|
| `gh issue list --label "good first issue"` | 목록 |
| `gh issue create --title "제목" --body "내용"` | 생성 |
| `gh issue view 123` | 보기 |
| `gh issue close 123` | 닫기 |

## 풀 리퀘스트
| 명령 | 설명 |
|---|---|
| `gh pr create --fill` | 커밋 내용으로 PR 생성 |
| `gh pr create --draft` | 초안 PR |
| `gh pr list` / `gh pr status` | 목록 / 내 PR 상태 |
| `gh pr checkout 45` | 다른 사람의 PR을 로컬로 받아 테스트 |
| `gh pr diff 45` | 변경 내용 |
| `gh pr review 45 --approve` | 승인 |
| `gh pr merge 45 --squash --delete-branch` | 스쿼시 병합 후 브랜치 삭제 |
| `gh pr checks` | CI 결과 확인 |

## Actions와 릴리스
| 명령 | 설명 |
|---|---|
| `gh run list` | 워크플로 실행 목록 |
| `gh run watch` | 실행 중인 워크플로 실시간 보기 |
| `gh run view --log-failed` | 실패한 단계 로그 |
| `gh workflow run deploy.yml` | 수동 실행 |
| `gh release create v1.0.0 --generate-notes` | 릴리스 생성 |
| `gh secret set API_TOKEN` | Actions 비밀 값 등록 |

## 하루 흐름 예
```bash
gh issue list --assignee @me                 # 오늘 할 일
git switch -c fix/42-login main
# ... 작업, 커밋 ...
git push -u origin fix/42-login
gh pr create --fill --reviewer teammate      # PR 생성, 리뷰 요청
gh pr checks --watch                         # CI 통과 기다리기
gh pr merge --squash --delete-branch         # 승인 후 병합
```
