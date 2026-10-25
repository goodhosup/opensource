# 설치와 처음 설정

## 설치
| 운영체제 | 방법 |
|---|---|
| Windows | [git-scm.com](https://git-scm.com)에서 Git for Windows 설치 (Git Bash 포함) 또는 `winget install --id Git.Git` |
| macOS | `xcode-select --install` 또는 `brew install git` |
| Ubuntu/Debian | `sudo apt install git` |
| Fedora | `sudo dnf install git` |

설치 확인:

```bash
git --version
```

## 사용자 정보 설정
커밋에는 작성자 이름과 이메일이 기록됩니다. 처음 한 번만 설정하면 됩니다.

```bash
git config --global user.name "홍길동"
git config --global user.email "you@example.com"
```

!!! tip "이메일 공개가 걱정된다면"
    GitHub의 **Settings → Emails**에서 제공하는 `아이디@users.noreply.github.com` 형식의 주소를 쓰면 실제 이메일을 공개하지 않고 커밋할 수 있습니다.

## 자주 쓰는 추가 설정
```bash
git config --global init.defaultBranch main   # 새 저장소의 기본 브랜치 이름
git config --global core.editor "code --wait" # 커밋 메시지 편집기 (VS Code)
git config --global pull.rebase false         # pull 시 병합 방식 (기본 merge)
git config --global core.autocrlf input       # 줄바꿈 처리 (macOS/Linux), Windows는 true
git config --global core.quotepath false      # 한글 파일 이름이 깨지지 않게 표시
```

설정 확인:

```bash
git config --list --show-origin
```

## 설정 범위
| 옵션 | 적용 범위 | 저장 위치 |
|---|---|---|
| `--system` | 컴퓨터의 모든 사용자 | `/etc/gitconfig` |
| `--global` | 현재 사용자의 모든 저장소 | `~/.gitconfig` |
| `--local` (기본) | 현재 저장소만 | `.git/config` |

좁은 범위가 우선합니다. 회사 저장소에서만 회사 이메일을 쓰려면 그 저장소에서 `git config user.email` 을 따로 설정하면 됩니다.

## GitHub 인증
GitHub는 2021년부터 Git 작업에 계정 비밀번호를 받지 않습니다. 다음 중 하나를 씁니다.

1. **GitHub CLI** (가장 쉬움)
    ```bash
    gh auth login     # 브라우저로 로그인, HTTPS 인증 자동 설정
    ```
2. **SSH 키**
    ```bash
    ssh-keygen -t ed25519 -C "you@example.com"
    cat ~/.ssh/id_ed25519.pub   # 출력된 공개키를 GitHub Settings → SSH and GPG keys에 등록
    ssh -T git@github.com       # 연결 확인
    ```
3. **개인 액세스 토큰(PAT)**: HTTPS로 push할 때 비밀번호 대신 입력. 가능하면 권한과 저장소를 좁힌 fine-grained 토큰을 씁니다.

!!! warning "토큰과 키는 비밀입니다"
    토큰이나 개인키(`id_ed25519`, `.pub`가 없는 파일)를 저장소에 커밋하거나 남에게 공유하지 마세요.
