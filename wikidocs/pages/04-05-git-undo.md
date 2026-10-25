상황별로 어떤 명령을 쓰는지 정리합니다. 먼저 `git status` 로 지금 상태를 확인하는 습관이 가장 중요합니다.

## 상황별 요약
| 상황 | 명령 |
|---|---|
| 파일 수정을 취소하고 마지막 커밋 상태로 | `git restore 파일` |
| `git add` 를 취소 (변경은 유지) | `git restore --staged 파일` |
| 방금 한 커밋 메시지 수정 / 빠뜨린 파일 추가 | `git commit --amend` |
| 마지막 커밋 취소, 변경은 스테이징에 남김 | `git reset --soft HEAD~1` |
| 마지막 커밋 취소, 변경은 작업 디렉터리에 남김 | `git reset HEAD~1` (= `--mixed`) |
| 마지막 커밋과 변경을 모두 버림 | `git reset --hard HEAD~1` ⚠️ |
| 이미 push한 커밋을 되돌림 | `git revert <커밋>` |
| 작업 중인 변경을 잠시 치워 둠 | `git stash` |
| 실수로 지운 커밋·브랜치 찾기 | `git reflog` |

## reset 과 revert
| | `git reset` | `git revert` |
|---|---|---|
| 방식 | 브랜치를 과거 커밋으로 되돌림 (이력 삭제) | 변경을 취소하는 **새 커밋**을 만듦 (이력 보존) |
| 안전한 곳 | 아직 push 안 한 로컬 커밋 | 이미 push한 공유 브랜치 |

```bash
git revert a1b2c3d          # 해당 커밋의 변경을 거꾸로 적용한 커밋 생성
```

[[TIP("⚠️ `--hard` 는 되돌릴 수 없을 수 있습니다")]]
`git reset --hard` 와 `git restore` 는 커밋하지 않은 변경을 영구히 지웁니다. 실행 전에 `git stash` 로 백업해 두면 안전합니다.
[[/TIP]]
## stash: 작업 잠시 치우기
급한 버그를 고치러 다른 브랜치로 가야 하는데 지금 작업은 커밋하기 애매할 때 씁니다.

```bash
git stash push -m "로그인 화면 작업 중"   # 변경을 임시 저장
git stash list                          # 목록
git stash pop                           # 가장 최근 것을 꺼내 적용하고 목록에서 삭제
git stash apply stash@{1}               # 특정 항목 적용 (목록에 남김)
git stash drop stash@{0}                # 삭제
git stash -u                            # 추적되지 않은 새 파일까지 저장
```

## reflog: 마지막 구조 수단
Git은 `HEAD` 가 움직인 기록을 일정 기간(기본 90일) 보관합니다. `reset --hard` 로 날린 커밋도 여기서 찾을 수 있습니다.

```bash
git reflog
# a1b2c3d HEAD@{0}: reset: moving to HEAD~1
# 9f8e7d6 HEAD@{1}: commit: 로그인 기능   ← 되살리고 싶은 커밋
git reset --hard 9f8e7d6     # 또는 git switch -c rescue 9f8e7d6
```

## 비밀 정보를 커밋했다면
1. **즉시 해당 비밀(토큰, 비밀번호)을 폐기하고 새로 발급**합니다. 이력에서 지우는 것보다 이것이 먼저입니다.
2. 이력에서 지우려면 `git filter-repo` 나 BFG Repo-Cleaner를 쓰고 강제 push합니다.
3. GitHub의 **Secret scanning push protection** 을 켜 두면 비밀이 담긴 push를 미리 막아 줍니다 → [보안](https://goodhosup.github.io/opensource/github/security/)
