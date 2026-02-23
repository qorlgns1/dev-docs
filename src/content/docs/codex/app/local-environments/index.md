---
title: '로컬 환경'
description: '로컬 환경을 통해 워크트리용 설정 단계와 프로젝트 공통 작업을 구성할 수 있습니다.'
---

Source URL: https://developers.openai.com/codex/app/local-environments

# 로컬 환경

로컬 환경을 통해 워크트리용 설정 단계와 프로젝트 공통 작업을 구성할 수 있습니다.

[Codex 앱 설정](codex://settings) 패널에서 로컬 환경을 구성합니다. 생성된 파일을 프로젝트 Git 저장소에 커밋하여 다른 사람과 공유할 수 있습니다.

Codex는 이 구성을 프로젝트 루트의 `.codex` 폴더 안에 저장합니다. 저장소에 여러 프로젝트가 있는 경우 공유 `.codex` 폴더를 포함하는 프로젝트 디렉터리를 엽니다.

## 설정 스크립트

워크트리는 로컬 작업과 다른 디렉터리에서 실행되므로 프로젝트가 완전히 설정되지 않았거나 저장소에 커밋되지 않은 종속성이나 파일이 부족할 수 있습니다. Codex가 새 스레드를 시작하고 새로운 워크트리를 생성할 때 설정 스크립트가 자동으로 실행됩니다.

종속성 설치나 빌드 실행처럼 환경 구성에 필요한 명령을 실행하려면 이 스크립트를 사용하세요.

예를 들어 TypeScript 프로젝트의 경우 다음과 같은 설정 스크립트로 종속성을 설치하고 초기 빌드를 수행할 수 있습니다.

```bash
npm install
npm run build
```

설정이 플랫폼별로 다른 경우 macOS, Windows 또는 Linux용 설정 스크립트를 정의하여 기본값을 재정의합니다.

## 작업

작업은 앱 개발 서버를 시작하거나 테스트 스위트를 실행하는 것 같은 일반 작업을 정의할 때 사용합니다. 이러한 작업은 Codex 앱 상단 바에 표시되어 빠르게 접근할 수 있습니다. 작업은 앱의 [통합 터미널](https://developers.openai.com/codex/app/features#integrated-terminal) 내에서 실행됩니다.

작업을 사용하면 프로젝트 빌드를 트리거하거나 개발 서버를 시작하는 등의 일반 명령을 반복 입력하지 않아도 됩니다. 일회성 빠른 디버깅이 필요할 때는 통합 터미널을 직접 사용할 수도 있습니다.

![Project actions list shown in Codex app settings](https://developers.openai.com/images/codex/app/actions-light.webp)

예를 들어 Node.js 프로젝트에서는 다음 스크립트가 포함된 “Run” 작업을 만들 수 있습니다.

```bash
npm start
```

작업에 사용하는 명령이 플랫폼별로 다르다면 macOS, Windows, Linux용 플랫폼별 스크립트를 정의하세요.

작업을 식별할 수 있도록 각 작업에 연관된 아이콘을 선택하세요.
