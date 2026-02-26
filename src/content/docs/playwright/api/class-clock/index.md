---
title: "Clock"
description: "시간 의존 동작을 정확히 시뮬레이션하는 것은 애플리케이션의 정확성을 검증하는 데 필수적입니다. 자세한 내용은 clock emulation을 참고하세요."
---

Source URL: https://playwright.dev/docs/api/class-clock

# Clock | Playwright

시간 의존 동작을 정확히 시뮬레이션하는 것은 애플리케이션의 정확성을 검증하는 데 필수적입니다. 자세한 내용은 [clock emulation](https://playwright.dev/docs/clock)을 참고하세요.

clock은 전체 [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")에 설치되므로, 모든 페이지와 iframe의 시간은 동일한 clock으로 제어됩니다.

---

## Methods[​](https://playwright.dev/docs/api/class-clock#methods "Methods 직접 링크")

### fastForward[​](https://playwright.dev/docs/api/class-clock#clock-fast-forward "fastForward 직접 링크")

추가된 버전: v1.45 clock.fastForward

시간을 앞으로 점프시켜 clock을 진행합니다. 만료된 타이머는 최대 한 번만 실행됩니다. 이는 사용자가 노트북 덮개를 한동안 닫았다가 지정한 시간이 지난 뒤 다시 여는 상황과 같습니다.

**Usage**

```
    await page.clock.fastForward(1000);
    await page.clock.fastForward('30:00');

```

**Arguments**

- `ticks` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-clock#clock-fast-forward-option-ticks)

시간은 clock을 진행할 밀리초 수 또는 사람이 읽기 쉬운 문자열일 수 있습니다. 유효한 문자열 형식은 8초를 의미하는 "08", 1분을 의미하는 "01:00", 2시간 34분 10초를 의미하는 "02:34:10"입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-clock#clock-fast-forward-return)

---

### install[​](https://playwright.dev/docs/api/class-clock#clock-install "install 직접 링크")

추가된 버전: v1.45 clock.install

다음 시간 관련 함수에 대한 가짜 구현을 설치합니다:

- `Date`
- `setTimeout`
- `clearTimeout`
- `setInterval`
- `clearInterval`
- `requestAnimationFrame`
- `cancelAnimationFrame`
- `requestIdleCallback`
- `cancelIdleCallback`
- `performance`

가짜 타이머는 테스트에서 시간의 흐름을 수동으로 제어하는 데 사용됩니다. 시간을 진행시키고, 타이머를 실행하며, 시간 의존 함수의 동작을 제어할 수 있습니다. 자세한 내용은 [clock.runFor()](https://playwright.dev/docs/api/class-clock#clock-run-for) 및 [clock.fastForward()](https://playwright.dev/docs/api/class-clock#clock-fast-forward)를 참고하세요.

**Usage**

```
    await clock.install();
    await clock.install(options);

```

**Arguments**

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `time` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date "Date") _(optional)_[#](https://playwright.dev/docs/api/class-clock#clock-install-option-time)

초기화할 시간입니다. 기본값은 현재 시스템 시간입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-clock#clock-install-return)

---

### pauseAt[​](https://playwright.dev/docs/api/class-clock#clock-pause-at "pauseAt 직접 링크")

추가된 버전: v1.45 clock.pauseAt

시간을 앞으로 점프시켜 clock을 진행한 뒤 시간을 일시 정지합니다. 이 메서드가 호출되면 [clock.runFor()](https://playwright.dev/docs/api/class-clock#clock-run-for), [clock.fastForward()](https://playwright.dev/docs/api/class-clock#clock-fast-forward), [clock.pauseAt()](https://playwright.dev/docs/api/class-clock#clock-pause-at), [clock.resume()](https://playwright.dev/docs/api/class-clock#clock-resume) 중 하나가 호출되지 않는 한 어떤 타이머도 실행되지 않습니다.

만료된 타이머는 최대 한 번만 실행됩니다. 이는 사용자가 노트북 덮개를 한동안 닫았다가 지정된 시각에 다시 열고 일시 정지하는 상황과 같습니다.

**Usage**

```
    await page.clock.pauseAt(new Date('2020-02-02'));
    await page.clock.pauseAt('2020-02-02');

```

최적의 결과를 위해 페이지로 이동하기 전에 clock을 설치하고, 의도한 테스트 시간보다 약간 이전 시각으로 설정하세요. 이렇게 하면 페이지 로딩 중 모든 타이머가 정상적으로 실행되어 페이지가 멈추는 문제를 방지할 수 있습니다. 페이지가 완전히 로드된 후에는 [clock.pauseAt()](https://playwright.dev/docs/api/class-clock#clock-pause-at)을 안전하게 사용해 clock을 일시 정지할 수 있습니다.

```
    // Initialize clock with some time before the test time and let the page load
    // naturally. `Date.now` will progress as the timers fire.
    await page.clock.install({ time: new Date('2024-12-10T08:00:00') });
    await page.goto('http://localhost:3333');
    await page.clock.pauseAt(new Date('2024-12-10T10:00:00'));

```

**Arguments**

- `time` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date "Date")[#](https://playwright.dev/docs/api/class-clock#clock-pause-at-option-time)

일시 정지할 시간입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-clock#clock-pause-at-return)

---

### resume[​](https://playwright.dev/docs/api/class-clock#clock-resume "resume 직접 링크")

추가된 버전: v1.45 clock.resume

타이머를 재개합니다. 이 메서드가 호출되면 시간이 다시 흐르고 타이머도 평소처럼 실행됩니다.

**Usage**

```
    await clock.resume();

```

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-clock#clock-resume-return)

---

### runFor[​](https://playwright.dev/docs/api/class-clock#clock-run-for "runFor 직접 링크")

추가된 버전: v1.45 clock.runFor

clock을 진행시키고 모든 시간 관련 콜백을 실행합니다.

**Usage**

```
    await page.clock.runFor(1000);
    await page.clock.runFor('30:00');

```

**Arguments**

- `ticks` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-clock#clock-run-for-option-ticks)

시간은 clock을 진행할 밀리초 수 또는 사람이 읽기 쉬운 문자열일 수 있습니다. 유효한 문자열 형식은 8초를 의미하는 "08", 1분을 의미하는 "01:00", 2시간 34분 10초를 의미하는 "02:34:10"입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-clock#clock-run-for-return)

---

### setFixedTime[​](https://playwright.dev/docs/api/class-clock#clock-set-fixed-time "setFixedTime 직접 링크")

추가된 버전: v1.45 clock.setFixedTime

`Date.now`와 `new Date()`가 항상 고정된 가짜 시간을 반환하도록 하며, 모든 타이머는 계속 실행되도록 유지합니다.

미리 정의된 시간으로만 테스트하면 되는 단순한 시나리오에서는 이 메서드를 사용하세요. 더 고급 시나리오에서는 대신 [clock.install()](https://playwright.dev/docs/api/class-clock#clock-install)을 사용하세요. 자세한 내용은 [clock emulation](https://playwright.dev/docs/clock) 문서를 참고하세요.

**Usage**

```
    await page.clock.setFixedTime(Date.now());
    await page.clock.setFixedTime(new Date('2020-02-02'));
    await page.clock.setFixedTime('2020-02-02');

```

**Arguments**

- `time` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date "Date")[#](https://playwright.dev/docs/api/class-clock#clock-set-fixed-time-option-time)

밀리초 단위로 설정할 시간입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-clock#clock-set-fixed-time-return)

---

### setSystemTime[​](https://playwright.dev/docs/api/class-clock#clock-set-system-time "setSystemTime 직접 링크")

추가된 버전: v1.45 clock.setSystemTime

시스템 시간을 설정하지만 어떤 타이머도 트리거하지 않습니다. 예를 들어 서머타임에서 겨울시간으로 전환하거나 시간대를 변경할 때처럼, 웹 페이지가 시간 이동에 어떻게 반응하는지 테스트할 때 사용하세요.

**Usage**

```
    await page.clock.setSystemTime(Date.now());
    await page.clock.setSystemTime(new Date('2020-02-02'));
    await page.clock.setSystemTime('2020-02-02');

```

**Arguments**

- `time` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date "Date")[#](https://playwright.dev/docs/api/class-clock#clock-set-system-time-option-time)

밀리초 단위로 설정할 시간입니다.

**Returns**

- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")>[#](https://playwright.dev/docs/api/class-clock#clock-set-system-time-return)
