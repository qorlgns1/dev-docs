---
title: 'Crons 설정 | Next.js용 Sentry'
description: '구현을 완료하면 오류 해결, 타임아웃 감지, 서비스 중단 방지를 돕는 알림과 메트릭을 받을 수 있습니다.'
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/crons

# Crons 설정 | Next.js용 Sentry

구현을 완료하면 오류 해결, 타임아웃 감지, 서비스 중단 방지를 돕는 알림과 메트릭을 받을 수 있습니다.

## [요구 사항](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#requirements)

* 반복 작업에 대해 Sentry SDK(버전 `7.51.1` 이상)를 설치하고 구성하려면 [시작 가이드](https://docs.sentry.io/platforms/javascript/guides/nextjs.md)를 사용하세요.
* 첫 번째 Monitor를 [생성하고 구성](https://sentry.io/issues/alerts/new/crons/)하세요.

Cron 모니터링은 Next.js의 Server 및 Edge 런타임에서만 지원됩니다.

## [자동 Check-In (Vercel 전용)](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#automatic-check-ins-vercel-only)

Next.js 애플리케이션을 Vercel에서 호스팅하고 [Vercel의 Cron Jobs 기능](https://vercel.com/docs/cron-jobs)을 사용 중이라면, Next.js SDK가 Check-In을 자동으로 생성하도록 설정할 수 있습니다. 계측할 cron job은 런타임에 `vercel.json` 파일의 `crons` 필드를 검사하여 결정됩니다.

`next.config.js`의 Sentry 설정에서 `automaticVercelMonitors` 옵션을 `true`로 설정하세요. 자세한 내용은 [수동 설정](https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup.md#opt-out-of-auto-instrumentation-of-vercel-cron-jobs)을 참고하세요.

현재 Vercel cron job 자동 계측은 Pages Router에서만 동작합니다. App Router route handler는 아직 지원되지 않습니다.

## [자동 Crons 계측](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#automatic-crons-instrumentation)

주기 작업 실행에 [`cron`](https://www.npmjs.com/package/cron), [`node-cron`](https://www.npmjs.com/package/node-cron), [`node-schedule`](https://www.npmjs.com/package/node-schedule) 라이브러리를 사용한다면, `Sentry.cron` export의 계측 함수를 사용해 cron job을 모니터링할 수 있습니다.

- [Cron](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#cron)

SDK 버전 `7.92.0` 이상이 필요합니다.

[`cron`](https://www.npmjs.com/package/cron) 라이브러리의 `CronJob` 생성자 또는 `CronJob.from` 메서드를 계측하려면 `Sentry.cron.instrumentCron`을 사용하세요. 함수의 두 번째 인자로 cron monitor 이름을 전달하세요.

```JavaScript
import { CronJob } from "cron";

const CronJobWithCheckIn = Sentry.cron.instrumentCron(CronJob, "my-cron-job");

// use the constructor
const job = new CronJobWithCheckIn("* * * * *", () => {
  console.log("You will see this message every minute");
});

// or from method
const job = CronJobWithCheckIn.from({
  cronTime: "* * * * *",
  onTick: () => {
    console.log("You will see this message every minute");
  },
});
```

- [Node Cron](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#node-cron)

SDK 버전 `7.92.0` 이상이 필요합니다.

[`node-cron`](https://www.npmjs.com/package/node-cron) 라이브러리의 `cron` export를 계측하려면 `Sentry.cron.instrumentNodeCron`을 사용하세요. 원래 `cron` export와 동일한 API를 가진 객체를 반환하지만, `schedule` 메서드가 계측됩니다. 함수의 세 번째 options 인자로 cron monitor 이름과 선택적 time zone을 전달할 수 있습니다.

```JavaScript
import cron from "node-cron";

const cronWithCheckIn = Sentry.cron.instrumentNodeCron(cron);

cronWithCheckIn.schedule(
  "* * * * *",
  () => {
    console.log("running a task every minute");
  },
  { name: "my-cron-job" }
);
```

- [Node Schedule](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#node-schedule)

SDK 버전 `7.93.0` 이상이 필요합니다.

[`node-schedule`](https://www.npmjs.com/package/node-schedule) 라이브러리의 `schedule` export를 계측하려면 `Sentry.cron.instrumentNodeSchedule`을 사용하세요. 원래 `schedule` export와 동일한 API를 가진 객체를 반환하지만, `scheduleJob` 메서드가 계측됩니다. 함수의 첫 번째 인자로 cron job 이름을 전달할 수 있습니다. 현재 `scheduleJob`의 두 번째 인자는 cronstring만 지원합니다.

```JavaScript
import * as schedule from "node-schedule";

const scheduleWithCheckIn = Sentry.cron.instrumentNodeSchedule(schedule);

scheduleWithCheckIn.scheduleJob(
  "my-cron-job",
  "* * * * *",
  () => {
    console.log("running a task every minute");
  }
);
```

## [작업 모니터링](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#job-monitoring)

`Sentry.withMonitor()` API를 사용하면 콜백을 모니터링하고, 주기 작업이 누락되었을 때(또는 예상 시점에 시작되지 않았을 때), 런타임 문제(예: 오류)로 실패했을 때, 또는 최대 실행 시간을 초과해 실패했을 때 알림을 받을 수 있습니다.

`Sentry.withMonitor()`는 SDK 버전 `7.76.0`이 필요합니다.

```javascript
Sentry.withMonitor("<monitor-slug>", () => {
  // Execute your scheduled task here...
});
```

`Sentry.withMonitor()`는 새 trace를 생성하지 않습니다. 모니터링되는 콜백 내에서 발생한 이벤트와 오류는 현재 trace context와 연결됩니다.

SDK 버전이 `7.76.0` 미만이라면, 아래에 설명된 `Sentry.captureCheckIn()` API를 사용할 수 있습니다.

## [Check-In](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#check-ins)

Check-in 모니터링을 사용하면 작업 시작 시 한 번, 작업 종료 시 한 번, 총 두 번의 check-in을 완료해 작업 진행 상황을 추적할 수 있습니다. 이 2단계 프로세스를 통해 Sentry는 작업이 예상대로 시작되지 않았는지(누락) 또는 최대 실행 시간을 초과했는지(실패)를 알려줄 수 있습니다.

```javascript
// 🟡 Notify Sentry your job is running:
const checkInId = Sentry.captureCheckIn({
  monitorSlug: "<monitor-slug>",
  status: "in_progress",
});

// Execute your scheduled task here...

// 🟢 Notify Sentry your job has completed successfully:
Sentry.captureCheckIn({
  // Make sure this variable is named `checkInId`
  checkInId,
  monitorSlug: "<monitor-slug>",
  status: "ok",
});
```

작업 실행이 실패하면, 다음과 같이 Sentry에 실패를 알릴 수 있습니다.

```javascript
// 🔴 Notify Sentry your job has failed:
Sentry.captureCheckIn({
  // Make sure this variable is named `checkInId`
  checkInId,
  monitorSlug: "<monitor-slug>",
  status: "error",
});
```

## [Heartbeat](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#heartbeat)

Heartbeat 모니터링은 한 번의 check-in으로 작업 상태를 Sentry에 알립니다. 이 설정에서는 작업이 예상 시점에 시작되지 않았을 때(누락)만 알림을 받습니다. 작업이 최대 실행 시간을 초과했는지(실패)까지 추적해야 한다면, 대신 check-in 방식을 사용하세요.

```javascript
// Execute your scheduled task...

// 🟢 Notify Sentry your job completed successfully:
Sentry.captureCheckIn({
  monitorSlug: "<monitor-slug>",
  status: "ok",
});
```

작업 실행이 실패하면, 다음과 같이 할 수 있습니다.

```javascript
// 🔴 Notify Sentry your job has failed:
Sentry.captureCheckIn({
  monitorSlug: "<monitor-slug>",
  status: "error",
});
```

## [Cron Monitor 업서트](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#upserting-cron-monitors)

[ Sentry.io에서 생성/구성](https://sentry.io/issues/alerts/new/crons/)하는 대신, 코드로 Monitor를 프로그래밍 방식으로 생성하고 업데이트할 수 있습니다.

monitor를 생성/업데이트하려면 `Sentry.withMonitor()`를 사용하고 세 번째 파라미터로 monitor 구성을 전달하세요.

```javascript
const monitorConfig = {
  schedule: {
    type: "crontab",
    value: "* * * * *",
  },
  checkinMargin: 2, // In minutes. Optional.
  maxRuntime: 10, // In minutes. Optional.
  timezone: "America/Los_Angeles", // Optional.
};

Sentry.withMonitor(
  "<monitor-slug>",
  () => {
    // Execute your scheduled task here...
  },
  monitorConfig,
);
```

monitor의 check-in을 구성하려면 `Sentry.captureCheckIn()`을 사용하고 두 번째 파라미터로 monitor 구성을 전달하세요.

```javascript
const monitorConfig = {
  schedule: {
    type: "crontab",
    value: "* * * * *",
  },
  checkinMargin: 2, // In minutes. Optional.
  maxRuntime: 10, // In minutes. Optional.
  timezone: "America/Los_Angeles", // Optional.
};

// 🟡 Notify Sentry your job is running:
const checkInId = Sentry.captureCheckIn(
  {
    monitorSlug: "<monitor-slug>",
    status: "in_progress",
  },
  monitorConfig,
);

// Execute your scheduled task here...

// 🟢 Notify Sentry your job has completed successfully:
Sentry.captureCheckIn(
  {
    // Make sure this variable is named `checkInId`
    checkInId,
    monitorSlug: "<monitor-slug>",
    status: "ok",
  },
  monitorConfig,
);
```

- [Monitor 구성 속성](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#monitor-configuration-properties)

다음 monitor 구성 속성을 사용할 수 있습니다.

`schedule`:

작업 스케줄:

monitor의 스케줄 표현으로 `crontab` 또는 `interval`을 사용합니다. 구조는 타입에 따라 달라집니다.

```json
{"type": "crontab", "value": "0 * * * *"}
{"type": "interval", "value": "2", "unit": "hour"}
```

`checkinMargin`:

check-in이 누락된 것으로 간주되기 전까지 Sentry가 대기할 시간(분)입니다("grace period"). 선택 사항입니다.

check-in margin은 interval 이하로 설정하는 것을 권장합니다.

`maxRuntime`:

작업이 실패로 간주되기 전까지 허용되는 실행 시간(분)입니다. 선택 사항입니다.

`timezone`:

작업이 실행되는 `tz`입니다. 일반적으로 서버의 timezone(예: `America/Los_Angeles`)입니다. [tz 데이터베이스 time zone 목록](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)을 참고하세요. 선택 사항입니다.

`node-cron`은 luxon timezone 전달을 허용하지만, Sentry와 함께 사용할 때는 IANA timezone으로 변환해야 합니다(예: `DateTime.local().zoneName` 사용).

`failureIssueThreshold`:

*SDK 버전 `8.7.0` 이상 필요*

이슈가 생성되기 전에 필요한 연속 실패 check-in 횟수입니다. 선택 사항입니다.

`recoveryThreshold`:

*SDK 버전 `8.7.0` 이상 필요*

이슈가 해결된 것으로 간주되기 전에 필요한 연속 성공 check-in 횟수입니다. 선택 사항입니다.

## [알림](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#alerts)

반복 작업이 check-in에 실패했을 때(누락), 설정된 최대 실행 시간을 초과해 실행됐을 때(실패), 또는 수동으로 실패를 보고했을 때, Sentry는 monitor에 태그가 포함된 오류 이벤트를 생성합니다.

이 이벤트에 대한 알림을 받으려면:

1. 사이드바에서 **Alerts**로 이동합니다.
2. 새 알림을 만들고 알림 유형으로 "Errors" 아래의 "Issues"를 선택합니다.
3. 알림을 구성하고 다음 필터 매치를 사용하도록 정의합니다: `The event's tags match {key} {match} {value}`.

예시: `The event's tags match monitor.slug equals my-monitor-slug-here`

자세한 내용은 [Issue Alert Configuration](https://docs.sentry.io/product/alerts/create-alerts/issue-alert-config.md)을 참고하세요.

## [Rate Limits](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons.md#rate-limits)

오남용 및 리소스 과다 사용을 방지하기 위해, Crons는 **각 monitor environment당 분당 6회**로 check-in을 제한합니다.

예를 들어 "database-backup"이라는 monitor에 두 개의 environment가 있다면:

* `database-backup`의 `production` environment는 분당 최대 6개의 check-in을 전송할 수 있습니다.
* `database-backup`의 `staging` environment도 분당 최대 6개의 check-in을 전송할 수 있습니다.
* 합산하면 분당 최대 12개의 check-in을 전송할 수 있습니다.

[Usage Stats](https://docs.sentry.io/product/stats.md#usage-stats) 페이지에서 check-in이 드롭되고 있는지 확인할 수 있습니다. check-in 드롭을 방지하려면 monitor가 rate limit을 초과하지 않도록 하세요.

## 이 섹션의 페이지

- [문제 해결](https://docs.sentry.io/platforms/javascript/guides/nextjs/crons/troubleshooting.md)

