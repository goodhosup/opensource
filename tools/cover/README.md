# 책 표지

- `cover.html`: 표지 원본 (1200×1600). 글꼴은 `@fontsource/noto-sans-kr`, `@fontsource/jetbrains-mono` 의 woff2 파일을 같은 폴더에 두고 렌더링합니다.
- `shot.js`: Playwright로 PNG를 만듭니다. `node shot.js $PWD/cover.html $PWD/../../docs/assets/cover.png`
