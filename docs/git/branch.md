# 브랜치와 병합

브랜치는 독립된 작업 공간입니다. `main` 은 항상 안정된 상태로 두고, 기능 개발이나 버그 수정은 브랜치에서 한 뒤 합칩니다.

## 브랜치 다루기
```bash
git branch                    # 로컬 브랜치 목록 (* 가 현재 브랜치)
git branch -a                 # 원격 브랜치까지
git switch -c feature/login   # 새 브랜치를 만들고 이동
git switch main               # 기존 브랜치로 이동
git branch -d feature/login   # 병합된 브랜치 삭제
git branch -D feature/login   # 병합 여부와 상관없이 강제 삭제
git branch -m old-name new-name  # 이름 변경
```

!!! note "`checkout` 과 `switch`"
    예전에는 `git checkout` 하나로 브랜치 이동과 파일 복원을 모두 했습니다. Git 2.23(2019)부터 역할을 나눠 **브랜치 이동은 `git switch`**, **파일 복원은 `git restore`** 를 권장합니다. `git checkout -b 새브랜치` 는 `git switch -c 새브랜치` 와 같습니다.

## 병합 (merge)
```bash
git switch main
git merge feature/login       # feature/login 을 main 에 합침
```

| 병합 방식 | 언제 | 결과 |
|---|---|---|
| Fast-forward | main 이 그사이 바뀌지 않았을 때 | 포인터만 앞으로 이동, 병합 커밋 없음 |
| 3-way merge | 양쪽 모두 새 커밋이 있을 때 | 병합 커밋 생성 |
| `--no-ff` | 항상 병합 커밋을 남기고 싶을 때 | 브랜치 흔적이 이력에 남음 |
| `--squash` | 브랜치의 커밋을 하나로 합치고 싶을 때 | 변경만 스테이징, 직접 커밋 |

## 충돌 해결
같은 파일의 같은 부분을 양쪽에서 고치면 **충돌(conflict)** 이 납니다.

```text
<<<<<<< HEAD
환영합니다!
=======
어서 오세요!
>>>>>>> feature/greeting
```

1. `git status` 로 충돌난 파일을 확인합니다.
2. 파일을 열어 `<<<<<<<`, `=======`, `>>>>>>>` 표시를 지우고 원하는 내용으로 고칩니다.
3. `git add 파일` 로 해결했다고 표시합니다.
4. `git commit` (rebase 중이면 `git rebase --continue`) 으로 마무리합니다.

병합을 포기하려면 `git merge --abort` 를 씁니다.

## 브랜치 전략
| 전략 | 특징 | 어울리는 곳 |
|---|---|---|
| **GitHub Flow** | `main` + 짧은 기능 브랜치, PR로 병합, 병합 즉시 배포 가능 | 대부분의 오픈소스, 웹 서비스 |
| **Git Flow** | `main`, `develop`, `feature/*`, `release/*`, `hotfix/*` | 정기 릴리스가 있는 제품 |
| **트렁크 기반 개발** | 모두 `main` 에 자주(하루 여러 번) 통합, 기능 플래그 활용 | CI/CD가 성숙한 팀 |

오픈소스 기여는 보통 **GitHub Flow**를 따릅니다 → [기여 워크플로](../github/contribute.md)

## 브랜치 이름 관례
`feature/로그인`, `fix/42-한글-깨짐`, `docs/설치-가이드` 처럼 **종류/내용** 형태로 짓고, 이슈 번호를 넣으면 추적이 쉽습니다. (실무에서는 영문 소문자와 하이픈을 주로 씁니다.)
