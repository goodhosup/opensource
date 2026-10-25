# 오픈소스 핸드북

오픈소스의 개념과 라이선스부터 Git·GitHub 실전 사용법, 국내 정책과 커뮤니티, AI 시대의 향후 방향까지 정리한 한글 안내서입니다.

- 웹 사이트: https://goodhosup.github.io/opensource/

## 로컬 실행

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve                    # http://127.0.0.1:8000
```

## 폴더 구조

| 경로 | 내용 |
|---|---|
| `mkdocs.yml` | 사이트 설정과 **전체 목차(nav)** — 페이지 추가는 여기서 시작 |
| `docs/` | 본문 마크다운 |
| `wikidocs/` | 위키독스 깃허브 연동 책 형식 내보내기 결과 (직접 수정하지 않음) |
| `tools/export_wikidocs.py` | `docs/` → `wikidocs/` 변환 |
| `tools/publish_wikidocs.py` | 위키독스 API로 업로드 (`WIKIDOCS_TOKEN` 환경 변수) |
| `.github/workflows/wikidocs.yml` | 위키독스 자동 업로드 (Actions 시크릿 `WIKIDOCS_TOKEN`) |

## 배포

- **GitHub Pages**: `main` 브랜치에 push하면 GitHub Actions(`.github/workflows/deploy.yml`)가 사이트를 빌드해 올립니다.
- **위키독스**: 본문을 고친 뒤 `python tools/export_wikidocs.py --out wikidocs` 로 다시 내보냅니다. `main` 에 push하면 Actions(`.github/workflows/wikidocs.yml`)가 저장소 시크릿 `WIKIDOCS_TOKEN` 으로 위키독스에 올립니다. 로컬에서는 `WIKIDOCS_TOKEN` 을 설정하고 `python tools/publish_wikidocs.py --src wikidocs` 로 올릴 수 있습니다.
