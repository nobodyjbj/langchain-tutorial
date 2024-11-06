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
```

## 단축키

### Cursor의 Mac 버전에서 AI 기능을 사용하기 위한 주요 단축키

AI 코드 편집 및 생성: CMD + K  
AI 채팅 창 열기: CMD + L  
선택한 텍스트로 AI 채팅 창 열기: CMD + SHIFT + L  
Composer 열기 (여러 파일 동시 수정 또는 전체 애플리케이션 생성): CMD + I (플로팅 윈도우)  
CMD + SHIFT + I (전체 화면)  
자동 완성 (Copilot++): 별도의 단축키 없이 항상 활성화, 약 1초간 동작이 없으면 자동으로 코드를 추천추천된 코드를 적용하려면 Tab 키

### Cursor 유용한 단축키

파일 탐색 및 관리:

- 파일 찾기: CMD + P
- 사이드바 토글: CMD + B
- 새 파일 생성: CMD + N
- 파일 저장: CMD + S

편집 기능:

- 줄 복사: SHIFT + OPTION + 위/아래 화살표
- 줄 이동: OPTION + 위/아래 화살표
- 다중 커서: OPTION + 클릭 또는 CMD + OPTION + 위/아래 화살표
- 전체 선택: CMD + A
- 찾기: CMD + F
- 찾기 및 바꾸기: CMD + OPTION + F

코드 네비게이션:

- 정의로 이동: F12 또는 CMD + 클릭
- 모든 참조 찾기: SHIFT + F12
- 파일의 심볼로 이동: CMD + SHIFT + O

터미널 및 패널:

- 통합 터미널 열기/닫기: `CTRL + ``
- 새 터미널 생성: `CTRL + SHIFT + ``

편집기 관리:

- 새 편집기 그룹 열기: CMD + \
- 편집기 그룹 간 이동: CMD + 1, CMD + 2, 등

마크다운 미리보기:

- 마크다운 미리보기 열기: CMD + SHIFT + V
- 마크다운 미리보기 옆에 열기: CMD + K V

기타 유용한 단축키:

- 설정 열기: CMD + ,
- 명령 팔레트 열기: CMD + SHIFT + P
- 주석 토글: CMD + /
