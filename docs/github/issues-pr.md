# 이슈, 풀 리퀘스트, 코드 리뷰

## 이슈 운영
### 좋은 버그 리포트의 구성
1. **요약**: 무엇이 문제인지 한 줄로
2. **재현 방법**: 단계별로
3. **기대 결과와 실제 결과**
4. **환경**: OS, 버전, 브라우저 등
5. 로그, 스크린샷, 최소 재현 코드

### 라벨 체계 예
| 라벨 | 의미 |
|---|---|
| `bug`, `enhancement`, `documentation`, `question` | 종류 |
| `good first issue`, `help wanted` | 신규 기여자 환영 |
| `priority: high` | 우선순위 |
| `needs triage`, `needs reproduction` | 분류·재현 필요 |
| `wontfix`, `duplicate`, `invalid` | 처리하지 않음 |

### 이슈 관리 도구
- **Assignees**: 담당자 지정
- **Milestones**: 릴리스 단위로 묶기 (예: v1.2.0)
- **Projects**: 칸반 보드나 표로 진행 상황 관리, 사용자 정의 필드(우선순위, 예상 규모)
- **Sub-issues / Issue types**: 큰 작업을 하위 이슈로 쪼개고 유형(Bug, Feature, Task) 구분
- **Discussions**: 질문·아이디어처럼 "해결"보다 "대화"가 필요한 주제는 이슈 대신 여기로

## 풀 리퀘스트
### PR 상태
| 상태 | 의미 |
|---|---|
| Draft | 작업 중. 리뷰 요청 전 의견을 미리 받고 싶을 때 |
| Open (Ready for review) | 리뷰 준비 완료 |
| Approved / Changes requested | 리뷰 결과 |
| Merged / Closed | 병합됨 / 병합 없이 닫힘 |

### 병합 방식 (저장소 설정에서 허용 방식 선택)
| 방식 | 결과 | 장단점 |
|---|---|---|
| **Create a merge commit** | 브랜치 커밋 전부 + 병합 커밋 | 이력이 정확하지만 복잡해짐 |
| **Squash and merge** | PR 전체를 커밋 하나로 | 이력이 깔끔, 오픈소스에서 많이 씀 |
| **Rebase and merge** | 커밋들을 일직선으로 재배치 | 병합 커밋 없이 개별 커밋 유지 |

## 코드 리뷰
### 리뷰어로서
- **Comment**(의견), **Approve**(승인), **Request changes**(수정 요청) 중 하나로 제출합니다.
- **Suggestion** 기능으로 고칠 코드를 직접 제안하면 작성자가 버튼 하나로 반영할 수 있습니다.
- 사람이 아니라 코드를 이야기하고, 필수 수정과 취향(nit)을 구분해 표시합니다.
- 칭찬도 리뷰입니다. 첫 기여자에게는 특히 중요합니다.

### 작성자로서
- PR은 작게(수백 줄 이내) 유지하면 리뷰가 빠르고 정확해집니다.
- 리뷰 코멘트마다 반영했는지, 왜 반영하지 않는지 답합니다.
- 해결된 대화는 **Resolve conversation** 으로 닫습니다.

### CODEOWNERS
`.github/CODEOWNERS` 파일로 경로별 담당 리뷰어를 지정하면 해당 파일이 바뀐 PR에 자동으로 리뷰가 요청됩니다.

```text
# 경로                  담당자
*                      @org/maintainers
/docs/                 @docs-team
*.py                   @python-reviewer
```
