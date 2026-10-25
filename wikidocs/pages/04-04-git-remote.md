원격 저장소(remote)는 GitHub처럼 네트워크에 있는 저장소입니다. 내 로컬 저장소와 원격 저장소를 동기화하며 협업합니다.

## 복제 (clone)
```bash
git clone https://github.com/owner/repo.git        # HTTPS
git clone git@github.com:owner/repo.git            # SSH
git clone --depth 1 https://github.com/owner/repo  # 최신 커밋만 (빠름, 이력 없음)
gh repo clone owner/repo                           # GitHub CLI
```
`clone` 하면 원격 저장소가 자동으로 `origin` 이라는 이름으로 등록됩니다.

## 원격 저장소 관리
```bash
git remote -v                                   # 등록된 원격 저장소 목록
git remote add origin https://github.com/me/repo.git
git remote add upstream https://github.com/original/repo.git  # 포크한 원본
git remote set-url origin git@github.com:me/repo.git           # 주소 변경
git remote remove upstream
```

[[TIP("📝 origin 과 upstream")]]
오픈소스에 기여할 때는 보통 두 원격을 둡니다.

- `origin`: 내가 포크한 내 저장소 (push 가능)
- `upstream`: 원본 프로젝트 저장소 (읽기 전용으로 최신 변경을 받아옴)
[[/TIP]]
## 올리기 (push)
```bash
git push -u origin feature/login   # 처음 push: 원격 브랜치와 연결(-u)
git push                           # 이후에는 간단히
git push origin --delete feature/login   # 원격 브랜치 삭제
git push --tags                    # 태그 올리기
```

## 받아오기 (fetch, pull)
| 명령 | 동작 |
|---|---|
| `git fetch` | 원격의 새 커밋을 받아만 둠. 내 작업 브랜치는 그대로 |
| `git pull` | `fetch` + 현재 브랜치에 병합 (`merge`) |
| `git pull --rebase` | `fetch` + 내 커밋을 원격 커밋 위로 재배치 (이력이 깔끔) |

```bash
git fetch origin
git log --oneline main..origin/main   # 원격에 새로 생긴 커밋 확인
git pull
```

## 포크를 원본과 동기화
```bash
git fetch upstream
git switch main
git merge upstream/main     # 또는 git rebase upstream/main
git push origin main
```
GitHub 웹의 포크 저장소 화면에서 **Sync fork** 버튼으로도 할 수 있습니다.

## 강제 push 주의
```bash
git push --force-with-lease    # 원격이 내가 마지막으로 본 상태일 때만 덮어씀
```

[[TIP("⚠️ 주의")]]
`git push --force` 는 원격 이력을 덮어써 다른 사람의 작업을 지울 수 있습니다. 공유 브랜치(`main` 등)에는 쓰지 말고, 꼭 필요하면 내 PR 브랜치에서 `--force-with-lease` 를 쓰세요.
[[/TIP]]
