GitHub Pages는 저장소의 HTML·마크다운을 무료 정적 웹사이트로 호스팅합니다. 프로젝트 문서, 블로그, 이 책 같은 사이트를 만들 때 씁니다.

## 주소 규칙
| 저장소 | 사이트 주소 |
|---|---|
| `아이디.github.io` (사용자 사이트) | `https://아이디.github.io/` |
| 그 밖의 저장소 (프로젝트 사이트) | `https://아이디.github.io/저장소이름/` |

**Settings → Pages → Custom domain** 에서 직접 소유한 도메인을 연결하고 HTTPS를 켤 수 있습니다.

## 발행 방식
| 방식 | 설정 | 특징 |
|---|---|---|
| 브랜치에서 배포 | Source: Deploy from a branch → `main` 의 `/` 또는 `/docs` | 가장 간단. 기본 Jekyll로 마크다운 변환 |
| **GitHub Actions** | Source: GitHub Actions | MkDocs, Docusaurus, Hugo 등 어떤 도구로 빌드해도 됨 (권장) |

## 예: MkDocs Material 문서 사이트
이 책도 같은 방식으로 만들었습니다.

```yaml
# mkdocs.yml
site_name: 내 프로젝트 문서
theme:
  name: material
  language: ko
nav:
  - 홈: index.md
  - 시작하기: getting-started.md
```

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install mkdocs-material
      - run: mkdocs build --strict
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

1. 위 두 파일과 `docs/` 폴더를 저장소에 올립니다.
2. **Settings → Pages → Source** 를 **GitHub Actions** 로 바꿉니다.
3. `main` 에 push하면 몇 분 안에 사이트가 갱신됩니다. 진행 상황은 **Actions** 탭에서 봅니다.

로컬 미리보기: `pip install mkdocs-material && mkdocs serve` → `http://127.0.0.1:8000`
