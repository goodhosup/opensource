## rebase: 이력 다시 쌓기
내 브랜치의 커밋을 다른 브랜치의 최신 커밋 위로 옮겨 다시 적용합니다. 병합 커밋 없이 이력을 일직선으로 만듭니다.

```bash
git switch feature/login
git rebase main              # feature 커밋들을 main 최신 위로 재배치
# 충돌 시: 해결 → git add → git rebase --continue  (포기: git rebase --abort)
```

### 인터랙티브 rebase: 커밋 정리
PR을 올리기 전에 지저분한 커밋을 정리할 때 씁니다.

```bash
git rebase -i HEAD~3         # 최근 3개 커밋 편집
```

| 명령 | 효과 |
|---|---|
| `pick` | 그대로 둠 |
| `reword` | 메시지만 수정 |
| `squash` | 이전 커밋과 합치고 메시지도 합침 |
| `fixup` | 이전 커밋과 합치고 이 커밋 메시지는 버림 |
| `drop` | 커밋 삭제 |

[[TIP("⚠️ rebase 의 황금률")]]
**다른 사람과 공유한(push한) 브랜치는 rebase 하지 마세요.** 커밋 해시가 바뀌어 다른 사람의 이력과 어긋납니다. 내 PR 브랜치처럼 혼자 쓰는 브랜치에서만 쓰고, 이후 `git push --force-with-lease` 로 올립니다.
[[/TIP]]
## cherry-pick: 특정 커밋만 가져오기
```bash
git cherry-pick a1b2c3d          # 다른 브랜치의 커밋 하나를 현재 브랜치에 적용
git cherry-pick a1b2c3d..f6e5d4c # 범위 (a1b2c3d 다음부터 f6e5d4c까지)
```
버그 수정 커밋을 릴리스 브랜치에도 반영할 때(백포트) 자주 씁니다.

## tag: 릴리스 표시
```bash
git tag                          # 목록
git tag -a v1.0.0 -m "첫 릴리스"   # 주석 태그 (작성자·날짜·메시지 포함, 권장)
git tag v1.0.0-rc1               # 가벼운 태그
git push origin v1.0.0           # 태그 올리기
git tag -d v1.0.0                # 로컬 태그 삭제
```

오픈소스는 보통 **유의적 버전(SemVer)** 을 씁니다: `MAJOR.MINOR.PATCH`

| 올리는 자리 | 언제 | 예 |
|---|---|---|
| MAJOR | 호환되지 않는 API 변경 | 1.4.2 → 2.0.0 |
| MINOR | 호환되는 기능 추가 | 1.4.2 → 1.5.0 |
| PATCH | 호환되는 버그 수정 | 1.4.2 → 1.4.3 |

## 그 밖에 알아 두면 좋은 기능
| 기능 | 명령 | 용도 |
|---|---|---|
| bisect | `git bisect start` → `good`/`bad` 표시 | 버그를 만든 커밋을 이진 탐색으로 찾기 |
| worktree | `git worktree add ../hotfix hotfix` | 한 저장소에서 여러 브랜치를 동시에 다른 폴더로 체크아웃 |
| submodule | `git submodule add <url>` | 다른 저장소를 하위 폴더로 포함 |
| 서명 커밋 | `git commit -S` | GPG/SSH 키로 커밋 작성자 증명 (GitHub에 Verified 표시) |
| alias | `git config --global alias.lg "log --oneline --graph --all"` | 긴 명령 줄여 쓰기 |
| Git LFS | `git lfs track "*.psd"` | 대용량 파일을 별도 저장 |
