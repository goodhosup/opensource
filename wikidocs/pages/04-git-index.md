오픈소스에 참여하려면 **Git**을 다룰 줄 알아야 합니다. 거의 모든 오픈소스 프로젝트가 Git으로 코드와 변경 이력을 관리하고, GitHub·GitLab 같은 플랫폼에서 협업합니다.

[[TIP("📝 이 장에서 다루는 것")]]
- Git이 무엇이고 왜 쓰는지
- 설치와 처음 설정
- 매일 쓰는 기본 명령 (`add`, `commit`, `status`, `log`, `diff`)
- 브랜치와 병합
- 원격 저장소 (`clone`, `push`, `pull`, `fetch`)
- 실수 되돌리기 (`restore`, `reset`, `revert`, `stash`)
- 한 단계 더 (`rebase`, `cherry-pick`, `tag`)
- 자주 쓰는 명령 요약표
[[/TIP]]
## Git이란
Git은 2005년 리누스 토르발스가 리눅스 커널 개발을 위해 만든 **분산 버전 관리 시스템(DVCS)** 입니다. 그 자체로 GPL v2 라이선스의 오픈소스입니다.

- **버전 관리**: 파일이 언제, 누가, 왜 바뀌었는지 기록하고 언제든 과거 상태로 돌아갈 수 있습니다.
- **분산**: 모든 사람이 전체 이력을 가진 완전한 저장소 사본을 가집니다. 서버 없이도 커밋·브랜치·이력 조회가 가능합니다.
- **브랜치**: 작업을 갈래로 나눠 동시에 여러 기능을 개발하고 나중에 합칠 수 있습니다.

## Git의 세 영역
Git을 이해하는 핵심은 파일이 거치는 세 영역입니다.

| 영역 | 설명 | 이동 명령 |
|---|---|---|
| 작업 디렉터리 (Working Directory) | 실제로 파일을 편집하는 곳 | — |
| 스테이징 영역 (Staging Area, Index) | 다음 커밋에 넣을 변경을 골라 두는 곳 | `git add` |
| 저장소 (Repository, `.git`) | 커밋으로 확정된 이력이 저장되는 곳 | `git commit` |

```text
작업 디렉터리 --git add--> 스테이징 영역 --git commit--> 로컬 저장소 --git push--> 원격 저장소(GitHub)
                                                       <--git pull/fetch--
```

## Git과 GitHub의 차이
| 구분 | Git | GitHub |
|---|---|---|
| 정체 | 버전 관리 **도구** (프로그램) | Git 저장소를 호스팅하는 **서비스** |
| 실행 위치 | 내 컴퓨터 | 웹 (github.com) |
| 기능 | 커밋, 브랜치, 병합, 이력 | 저장소 공유, 이슈, 풀 리퀘스트, Actions, Pages |
| 대안 | — | GitLab, Bitbucket, Gitea, Codeberg |

GitHub 사용법은 다음 장 [GitHub 운용 방법](https://goodhosup.github.io/opensource/github/)에서 다룹니다.
