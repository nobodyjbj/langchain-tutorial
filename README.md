# Cursor Setup Guide

## Install

### homebrew

```shell
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### python & pyenv

```shell
# penv 설치 (python 버전관리 툴)
> brew update
> brew install pyenv
> brew install pyenv-virtualenv

# 환경변수 설정
> echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
> echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
> echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# terminal restart
> exec "$SHELL"
```

```shell
# python 설치
> pyenv install 3.12.7
> pyenv global 3.12.7
> exec zsh

# python 버전 확인
> python --version

# poetry 설치
> pip install poetry
```

### poetry 명령어

1.기본 명령어

- poetry init: 현재 디렉토리에 pyproject.toml 파일을 생성하고, 초기 프로젝트 설정을 시작합니다.
- poetry add 패키지명: 패키지를 설치하고 pyproject.toml 및 poetry.lock 파일에 기록합니다.
- poetry remove 패키지명: 패키지를 삭제하고 의존성 파일에서 제거합니다.
- poetry install: pyproject.toml에 정의된 모든 패키지를 설치합니다. 새로 클론한 프로젝트에서 한 번에 의존성을 설치할 때 유용합니다.
- poetry update: 모든 의존성을 최신 버전으로 업데이트하고 poetry.lock 파일을 갱신합니다.

2.가상환경 관련 명령어

- poetry shell: 프로젝트에 생성된 가상환경을 활성화하여 사용할 수 있도록 합니다.
- poetry env use /path/to/python: 특정 파이썬 버전으로 가상환경을 설정합니다.
- poetry env list: 현재 프로젝트에서 사용할 수 있는 가상환경 목록을 보여줍니다.
- poetry env remove `<env>`: 특정 가상환경을 삭제합니다.

3.프로젝트 관리 명령어

- poetry run 명령어: 가상환경 내에서 특정 명령어를 실행할 수 있습니다. 예: poetry run python script.py.
- poetry check: pyproject.toml 파일에 잘못된 구성이 있는지 확인합니다.
- poetry show: 프로젝트에 설치된 패키지의 목록과 버전을 보여줍니다.
- poetry show --tree: 패키지의 의존성 트리를 볼 수 있어 의존성 구조를 확인하는 데 유용합니다.

4.배포 및 릴리즈 관련 명령어

- poetry build: 현재 프로젝트를 빌드하여 패키지를 생성합니다 (예: wheel 파일과 sdist 파일 생성).
- poetry publish: 빌드한 패키지를 PyPI 또는 다른 패키지 저장소에 업로드하여 배포합니다.

5.설정 확인

- poetry config --list: poetry의 모든 설정 값을 확인합니다.
- poetry config 설정명 값: poetry의 특정 설정 값을 변경합니다. 예를 들어 poetry config virtualenvs.-in-project true를 설정하면 가상환경을 프로젝트 내에 생성합니다.

6.의존성 검사 및 해결

- poetry lock: 의존성을 재설정하고 poetry.lock 파일을 업데이트합니다.
- poetry export -f requirements.txt --output requirements.txt: requirements.txt 파일 형식으로 의존성 목록을 내보냅니다. poetry를 사용하지 않는 환경에서 패키지 설치가 필요할 때 유용합니다.

## 단축키

### Pycharm 단축키

AI 코드 어시스턴트 관련 단축키

- AI 어시스턴트 창 열기: `Command + Shift + Enter`
- 코드 설명 생성: 코드 선택 후 `Command + Shift + I`
- 코드 리팩터링 제안: 코드 선택 후 `Command + Option + R`
- 코드 요약 요청: `Command + Shift + S`
- AI 코드 리뷰: 파일 열고 `Command + Shift + C`

셀 관련 단축키

- 새 셀 추가: `Option + Enter` 또는 `Esc + B` (아래에 새 셀), `Esc + A` (위에 새 셀)
- 셀 삭제: `Shift + Delete`
- 셀 실행: `Shift + Enter` (셀 실행 후 다음 셀로 이동), `Command + Enter` (현재 셀만 실행)
- 셀 합치기: `Shift + M`
- 셀 유형 변경 (코드 <-> 마크다운): `Command + Shift + M`

셀 이동 및 복사

- 셀 위로/아래로 이동: `Option + ↑ / Option + ↓`
- 셀 복사: `Command + D`
- 셀 붙여넣기: `Command + V`

실행 관련 단축키

- 모든 셀 실행: `Shift + F10` 또는 `Command + Option + R`
- 커널 재시작: `Command + Option + .`

탐색 관련 단축키

- 명령 팔레트 열기: `Command + Shift + A`
- 검색 (Find): `Command + F`
- 전체 노트북 검색 (Replace): `Command + R`
- 목차 열기 (Outline): `Command + F12`

편집 관련 단축키

- 자동완성: `Command + Space`
- 빠른 문서 조회: `Command + Q` (함수, 변수의 빠른 설명 보기)
- 코드 포맷: `Command + Option + L`
- 코드 주석 처리: `Command + /`

### Cursor 단축키

AI 기능

- AI 코드 편집 및 생성: `CMD + K`
- AI 채팅 창 열기: `CMD + L`  
- 선택한 텍스트로 AI 채팅 창 열기: `CMD + SHIFT + L`  
- Composer 열기 (여러 파일 동시 수정 또는 전체 애플리케이션 생성): `CMD + I (플로팅 윈도우)`  
- `CMD + SHIFT + I (전체 화면)`  
- 자동 완성 (Copilot++): 별도의 단축키 없이 항상 활성화, 약 1초간 동작이 없으면 자동으로 코드를 추천추천된 코드를 적용하려면 Tab 키

파일 탐색 및 관리

- 파일 찾기: `CMD + P`
- 사이드바 토글: `CMD + B`
- 새 파일 생성: `CMD + N`
- 파일 저장: `CMD + S`

편집 기능

- 줄 복사: `SHIFT + OPTION + 위/아래 화살표`
- 줄 이동: `OPTION + 위/아래 화살표`
- 다중 커서: `OPTION + 클릭` 또는 `CMD + OPTION + 위/아래 화살표`
- 전체 선택: `CMD + A`
- 찾기: `CMD + F`
- 찾기 및 바꾸기: `CMD + OPTION + F`

코드 네비게이션

- 정의로 이동: `F12` 또는 `CMD + 클릭`
- 모든 참조 찾기: `SHIFT + F12`
- 파일의 심볼로 이동: `CMD + SHIFT + O`

터미널 및 패널

- 통합 터미널 열기/닫기: `CTRL + ```
- 새 터미널 생성: `CTRL + SHIFT + ```

편집기 관리

- 새 편집기 그룹 열기: `CMD + \`
- 편집기 그룹 간 이동: `CMD + 1`, `CMD + 2`, 등

마크다운 미리보기

- 마크다운 미리보기 열기: `CMD + SHIFT + V`
- 마크다운 미리보기 옆에 열기: `CMD + K V`

기타 유용한 단축키

- 설정 열기: `CMD + ,`
- 명령 팔레트 열기: `CMD + SHIFT + P`
- 주석 토글: `CMD + /`
