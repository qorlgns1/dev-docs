---
title: "Vitest UI"
description: "Vitest는 Vite로 구동되며, 테스트를 실행할 때 내부적으로 dev server도 함께 사용합니다. 덕분에 테스트를 보고 상호작용할 수 있는 아름다운 UI를 제공할 수 있습니다. Vitest UI는 선택 사항이므로, 다음 명령으로 설치해야 합니다:"
---

출처 URL: https://vitest.dev/guide/ui

# Vitest UI

Vitest는 Vite로 구동되며, 테스트를 실행할 때 내부적으로 dev server도 함께 사용합니다. 덕분에 테스트를 보고 상호작용할 수 있는 아름다운 UI를 제공할 수 있습니다. Vitest UI는 선택 사항이므로, 다음 명령으로 설치해야 합니다:

```bash
npm i -D @vitest/ui
```

그런 다음 `--ui` 플래그를 전달해 UI와 함께 테스트를 시작할 수 있습니다:

```bash
vitest --ui
```

이후 `http://localhost:51204/__vitest__/`에서 Vitest UI에 접속할 수 있습니다.

::: warning
UI는 상호작용형이며 실행 중인 Vite server가 필요하므로, Vitest를 `watch` 모드(기본값)로 실행하세요. 또는 config의 `reporters` 옵션에 `html`을 지정해 Vitest UI와 동일하게 보이는 정적 HTML 리포트를 생성할 수도 있습니다.
:::

UI는 reporter로도 사용할 수 있습니다. Vitest 설정에서 `'html'` reporter를 사용해 HTML 출력을 생성하고 테스트 결과를 미리 볼 수 있습니다:

```ts [vitest.config.ts]
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    reporters: ["html"],
  },
});
```

Vitest UI에서 coverage report를 확인할 수 있습니다. 자세한 내용은 [Vitest UI Coverage](https://vitest.dev/guide/coverage#vitest-ui)를 참고하세요.

::: warning
터미널에서 테스트 실행 상태를 실시간으로 계속 확인하고 싶다면, `reporters` 옵션에 `default` reporter를 추가하는 것을 잊지 마세요: `['default', 'html']`.
:::

::: tip
HTML report를 미리 보려면 [vite preview](https://vitejs.dev/guide/cli.html#vite-preview) 명령을 사용할 수 있습니다:

```sh
npx vite preview --outDir ./html
```

[`outputFile`](https://vitest.dev/config/#outputfile) config 옵션으로 출력 위치를 설정할 수 있습니다. 여기에는 `.html` 경로를 지정해야 합니다. 예를 들어 기본값은 `./html/index.html`입니다.
:::

## Module Graph

Module Graph 탭은 선택한 테스트 파일의 module graph를 표시합니다.

::: info
제공된 모든 이미지는 [Zammad](https://github.com/zammad/zammad) 저장소를 예시로 사용합니다.
:::

모듈이 50개를 초과하면 시각적 혼잡을 줄이기 위해 module graph는 처음 두 단계만 표시합니다. "Show Full Graph" 아이콘을 클릭하면 언제든 전체 graph를 볼 수 있습니다.

::: warning
graph가 너무 크면 노드 위치가 안정화되기까지 시간이 걸릴 수 있습니다.
:::

"Reset"을 클릭하면 언제든 엔트리 module graph로 되돌릴 수 있습니다. module graph를 확장하려면 관심 있는 노드를 마우스 오른쪽 버튼으로 클릭하거나 Shift를 누른 채 클릭하세요. 선택한 노드와 관련된 모든 노드가 표시됩니다.

기본적으로 Vitest는 `node_modules`의 모듈을 표시하지 않습니다. 일반적으로 이 모듈들은 externalized됩니다. "Hide node_modules" 선택을 해제하면 표시할 수 있습니다.

### Module Info

모듈 노드를 마우스 왼쪽 버튼으로 클릭하면 Module Info 뷰가 열립니다.

이 뷰는 두 부분으로 나뉩니다. 상단에는 전체 module ID와 모듈에 대한 진단 정보가 표시됩니다. [`experimental.fsModuleCache`](https://vitest.dev/config/experimental#experimental-fsmodulecache)가 활성화되어 있으면 "cached" 또는 "not cached" 배지가 나타납니다. 오른쪽에서는 시간 진단 정보를 볼 수 있습니다:

- Self Time: 정적 import를 제외하고 모듈을 import하는 데 걸린 시간
- Total Time: 정적 import를 포함해 모듈을 import하는 데 걸린 시간. 현재 모듈의 `transform` 시간은 포함되지 않습니다.
- Transform: 모듈을 transform하는 데 걸린 시간

import를 클릭해 이 뷰를 열었다면, 시작 부분에 이전 모듈로 돌아가는 "Back" 버튼도 표시됩니다.

하단 부분은 모듈 타입에 따라 달라집니다. 모듈이 external이면 해당 파일의 source code만 표시됩니다. module graph를 더 탐색할 수 없고, 정적 import를 불러오는 데 걸린 시간도 볼 수 없습니다.

모듈이 inlined된 경우에는 창이 세 개 더 표시됩니다:

- Source: 모듈의 변경되지 않은 source code
- Transformed: Vitest가 Vite의 [module runner](https://vite.dev/guide/api-environment-runtimes#modulerunner)를 사용해 실행하는 transformed code
- Source Map (v3): source map 매핑

"Source" 창의 모든 정적 import에는 현재 모듈이 그것들을 평가하는 데 걸린 총 시간이 표시됩니다. 해당 import가 module graph에서 이미 평가되었다면, 그 시점에는 캐시되어 있으므로 `0ms`로 표시됩니다.

모듈 로드 시간이 500밀리초를 넘으면 시간은 빨간색으로 표시됩니다. 100밀리초를 넘으면 주황색으로 표시됩니다.

import source를 클릭해 해당 모듈로 이동하고 graph를 더 탐색할 수 있습니다(아래 `./support/assertions/index.ts` 참고).

::: warning
type-only import는 런타임에서 실행되지 않으며 총 소요 시간이 표시되지 않습니다. 또한 열 수 없습니다.
:::

다른 plugin이 transformation 중 module import를 주입하면, 해당 import들은 모듈 시작 부분에 회색으로 표시됩니다(예: `import.meta.glob`이 주입한 모듈). 이들도 총 시간이 표시되며 계속 탐색할 수 있습니다.

::: tip
Vitest 위에 커스텀 integration을 개발 중이라면 [`vitest.experimental_getSourceModuleDiagnostic`](https://vitest.dev/api/advanced/vitest#getsourcemodulediagnostic)을 사용해 이 정보를 가져올 수 있습니다.
:::

### Import Breakdown

::: tip FEEDBACK
이 기능에 대한 피드백을 [GitHub Discussion](https://github.com/vitest-dev/vitest/discussions/9224)에 남겨 주세요.
:::

Module Graph 탭은 Import Breakdown도 제공합니다. Total Time 기준으로 정렬된, 로드 시간이 가장 긴 모듈 목록을 보여줍니다(기본 상위 10개이며 "Show more"를 누르면 10개를 더 불러올 수 있습니다).

모듈을 클릭하면 Module Info를 볼 수 있습니다. 모듈이 external이면 노란색으로 표시됩니다(module graph에서와 같은 색상).

breakdown에는 각 모듈의 self time, total time, 그리고 전체 테스트 파일 로드 시간 대비 비율이 표시됩니다.

"Show Import Breakdown" 아이콘은 500밀리초를 초과해 로드된 파일이 하나라도 있으면 빨간색이 되고, 100밀리초를 초과한 파일이 하나라도 있으면 주황색이 됩니다.

기본적으로 Vitest는 500밀리초를 초과한 모듈이 하나라도 있으면 breakdown을 자동으로 표시합니다. [`experimental.printImportBreakdown`](https://vitest.dev/config/experimental#experimental-printimportbreakdown) 옵션으로 이 동작을 제어할 수 있습니다.
