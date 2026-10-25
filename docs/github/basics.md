# 계정과 저장소

## 계정 만들기와 보안
1. [github.com](https://github.com)에서 가입합니다. 아이디는 프로필 주소(`github.com/아이디`)가 되므로 신중히 고릅니다.
2. **2단계 인증(2FA)** 을 켭니다. GitHub는 코드를 기여하는 계정에 2FA를 의무화했습니다. 인증 앱, 패스키, 보안 키를 쓸 수 있습니다.
3. 프로필에 이름, 소개, 관심 분야를 적어 두면 기여 이력과 함께 포트폴리오가 됩니다. 아이디와 같은 이름의 저장소(`아이디/아이디`)를 만들고 `README.md` 를 쓰면 프로필 상단에 표시됩니다.

## 저장소 만들기
웹에서 **New repository** 를 누르거나 GitHub CLI를 씁니다.

| 항목 | 권장 |
|---|---|
| 이름 | 짧고 소문자, 하이픈으로 구분 (`my-awesome-tool`) |
| 공개 범위 | 오픈소스는 **Public** |
| README | 체크 (프로젝트 첫 화면) |
| .gitignore | 사용하는 언어 템플릿 선택 |
| License | 반드시 선택 → [라이선스](../license/licenses.md) |

```bash
# 로컬 프로젝트를 새 GitHub 저장소로 올리기 (GitHub CLI)
gh repo create my-awesome-tool --public --source=. --push
```

```bash
# 웹에서 빈 저장소를 만든 뒤 로컬과 연결
git remote add origin https://github.com/아이디/my-awesome-tool.git
git branch -M main
git push -u origin main
```

!!! warning "라이선스가 없으면 오픈소스가 아닙니다"
    코드를 공개해도 `LICENSE` 파일이 없으면 저작권법상 다른 사람은 사용·수정·배포할 권리가 없습니다. [choosealicense.com](https://choosealicense.com)에서 고르고, GitHub의 **Add file → Create new file → `LICENSE`** 를 입력하면 템플릿을 고를 수 있습니다.

## 공개 범위
| 종류 | 볼 수 있는 사람 |
|---|---|
| Public | 누구나 (오픈소스) |
| Private | 초대된 사람만 |
| Internal | 같은 기업(Enterprise) 구성원만 |

## 권한 수준 (협업자·팀)
| 역할 | 할 수 있는 일 |
|---|---|
| Read | 보기, 클론, 이슈 작성 |
| Triage | 이슈·PR 라벨, 담당자 지정, 닫기 (코드 쓰기 불가) |
| Write | push, PR 병합 |
| Maintain | 저장소 설정 일부 관리 (위험한 설정 제외) |
| Admin | 모든 설정, 삭제, 권한 관리 |

최소 권한 원칙에 따라 필요한 만큼만 줍니다. 커뮤니티 도우미에게는 **Triage** 가 적당합니다.
