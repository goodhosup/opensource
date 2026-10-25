## 시작
| 명령 | 설명 |
|---|---|
| `git config --global user.name "이름"` | 작성자 이름 설정 |
| `git config --global user.email "메일"` | 작성자 이메일 설정 |
| `git init` | 새 저장소 만들기 |
| `git clone <주소>` | 원격 저장소 복제 |

## 매일 쓰는 명령
| 명령 | 설명 |
|---|---|
| `git status` | 상태 확인 |
| `git add <파일>` / `git add .` | 스테이징 |
| `git commit -m "메시지"` | 커밋 |
| `git diff` / `git diff --staged` | 변경 내용 비교 |
| `git log --oneline --graph` | 이력 보기 |
| `git pull` | 원격 변경 받아와 병합 |
| `git push` | 원격에 올리기 |

## 브랜치
| 명령 | 설명 |
|---|---|
| `git branch` | 목록 |
| `git switch -c <브랜치>` | 만들고 이동 |
| `git switch <브랜치>` | 이동 |
| `git merge <브랜치>` | 현재 브랜치에 병합 |
| `git rebase <브랜치>` | 현재 브랜치를 대상 위로 재배치 |
| `git branch -d <브랜치>` | 삭제 |

## 원격
| 명령 | 설명 |
|---|---|
| `git remote -v` | 원격 목록 |
| `git remote add upstream <주소>` | 원본 저장소 등록 |
| `git fetch upstream` | 원본 변경 받아오기 |
| `git push -u origin <브랜치>` | 새 브랜치 첫 push |
| `git push --force-with-lease` | 내 브랜치 안전하게 덮어쓰기 |

## 되돌리기
| 명령 | 설명 |
|---|---|
| `git restore <파일>` | 수정 취소 |
| `git restore --staged <파일>` | 스테이징 취소 |
| `git commit --amend` | 마지막 커밋 수정 |
| `git reset --soft HEAD~1` | 마지막 커밋 취소 (변경 유지) |
| `git revert <커밋>` | 취소 커밋 만들기 (push 후) |
| `git stash` / `git stash pop` | 작업 임시 저장 / 복원 |
| `git reflog` | HEAD 이동 기록 (복구용) |

## 더 배우기
- [Pro Git (한국어판, 무료)](https://git-scm.com/book/ko/v2)
- [Git 공식 문서](https://git-scm.com/docs)
- [Learn Git Branching (브랜치 시각화 연습)](https://learngitbranching.js.org/?locale=ko)
- [GitHub Skills (실습 과정)](https://skills.github.com)
