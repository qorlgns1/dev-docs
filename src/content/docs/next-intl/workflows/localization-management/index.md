---
title: 'Crowdin을 사용한 현지화 관리'
description: '완전한 AI 기반 워크플로를 사용하는 것이 더 좋으신가요?'
---

소스 URL: https://next-intl.dev/docs/workflows/localization-management

[문서](https://next-intl.dev/docs/getting-started "Docs")[워크플로 및 통합](https://next-intl.dev/docs/workflows "Workflows & integrations")Crowdin을 사용한 현지화 관리

# Crowdin을 사용한 현지화 관리

완전한 AI 기반 워크플로를 사용하는 것이 더 좋으신가요?

[Crowdin을 사용한 AI 번역](https://learn.next-intl.dev/chapters/10-continuous-localization/01-local-workflow)

앱을 `next-intl`로 설정하고 나면 메시지를 담고 있는 여러 번역 번들(예: `en.json`)이 생깁니다. 이를 더 효율적으로 관리하고 다른 팀원도 번역에 기여할 수 있게 하려면, 현지화 관리 플랫폼을 사용하는 것이 좋습니다.

`next-intl`는 JSON 파일 번역을 지원하는 모든 현지화 관리 플랫폼과 함께 동작하지만, 번역 관리에는 [Crowdin](https://crowdin.com)을 권장합니다.

## 번역가와 협업하기[](https://next-intl.dev/docs/workflows/localization-management#collaborate-with-translators)

Crowdin Editor는 메시지를 번역하기 쉬운 환경을 제공합니다. 번역가가 메시지를 따라가며 작업할 수 있도록 안내할 뿐 아니라, 기계 번역 제안, 용어집, 컨텍스트 스크린샷 같은 고급 기능으로 워크플로를 개선합니다.

[![Crowdin Editor](https://next-intl.dev/_next/image?url=%2Fcrowdin-editor-schematic.png&w=1920&q=75)](https://crowdin.com/page/freelance-translators)

Crowdin Editor를 사용하면 번역가가 `next-intl`의 JSON 파일로 작업할 수 있습니다(일러스트).

## 개발과 현지화 분리하기[](https://next-intl.dev/docs/workflows/localization-management#decouple-localization-from-development)

개발자 중심의 현지화 서비스인 Crowdin은 현지화 프로세스를 개발과 분리할 수 있도록 돕고, 기존 워크플로와 통합됩니다.

**통합 옵션:**

  1. [Crowdin CLI](https://developer.crowdin.com/cli-tool/)를 사용한 명령줄 통합
  2. [GitHub app](https://support.crowdin.com/github-integration/)을 통한 Git 통합
  3. [webhooks](https://developer.crowdin.com/api/v2/#tag/Webhooks)에서 트리거되는 자동 워크플로
  4. [JS SDK](https://developer.crowdin.com/sdk-ota-web/)를 통한 OTA(Over-the-air) 전송
  5. 메시지 수동 업로드/다운로드

[![Crowdin 워크플로](https://next-intl.dev/_next/image?url=%2Fcrowdin-workflow.png&w=1920&q=75)](https://crowdin.com/teams/engineering)

번역이 업데이트되면 [Crowdin GitHub 통합](https://support.crowdin.com/github-integration/)이 자동으로 pull request를 생성합니다.

## GitHub 통합을 사용하는 예시 워크플로[](https://next-intl.dev/docs/workflows/localization-management#example-workflow-with-the-github-integration)

이 예시에서는 GitHub에 공개된 샘플인 [Street Photography Viewer](https://github.com/amannn/street-photography-viewer)를 사용합니다. 이 프로젝트는 Unsplash의 스트리트 포토그래피 사진을 표시하는 Next.js 앱이며, 국제화 전반에 `next-intl`를 사용합니다.

앱이 들어 있는 GitHub 저장소가 준비되었다면 다음 단계를 따르세요:

  1. [Crowdin 스토어에서 GitHub app 설치](https://store.crowdin.com/github)
  2. [GitHub 통합 설정 가이드](https://support.crowdin.com/github-integration/) 진행

이 과정을 마치면 Crowdin이 설정을 기반으로 구성 파일을 저장소에 커밋합니다.

crowdin.yml
```
    files:
      - source: /messages/en.json
        translation: /messages/%locale%.json
```

이 파일은 저장소의 로컬 번역을 Crowdin에 제공합니다.

![Crowdin 저장소 매핑](https://next-intl.dev/_next/image?url=%2Fcrowdin-repo-mapping.png&w=1920&q=75)

구성 파일이 준비되면 Crowdin은 저장소의 번역 파일을 인식합니다.

이제 Crowdin에서 번역이 업데이트되면, 다음 동기화 시 업데이트 내용이 포함된 pull request가 저장소에 생성됩니다.

![Crowdin 저장소 동기화](https://next-intl.dev/_next/image?url=%2Fcrowdin-repo-sync.png&w=1920&q=75)

Crowdin의 자동 번역 동기화([예시 pull request](https://github.com/amannn/street-photography-viewer/pull/3))

→ 자세한 내용은 [Crowdin](https://support.crowdin.com/introduction/)에서 확인하세요.

