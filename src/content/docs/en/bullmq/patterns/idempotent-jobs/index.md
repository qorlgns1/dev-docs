---
title: 'Idempotent jobs'
description: 'In order to take advantage of the ability to retry failed jobs, your jobs should be designed with failure in mind.'
---

Source URL: https://docs.bullmq.io/patterns/idempotent-jobs

# Idempotent jobs

In order to take advantage of [the ability to retry failed jobs](https://docs.bullmq.io/guide/retrying-failing-jobs), your jobs should be designed with failure in mind.

This means that it should not make a difference to the final state of the system if a job successfully completes on its first attempt, or if it fails initially and succeeds when retried. This is called *Idempotence*.

To achieve this behaviour, your jobs should be as atomic and simple as possible. Performing many different actions (such as database updates, API calls, ...) at once makes it hard to keep track of the process flow and, if needed, rollback partial progress when an exception occurs.

Simpler jobs also means simpler debugging, identifying bottlenecks, etc.

If necessary, split complex jobs [as described in the flow pattern](https://docs.bullmq.io/patterns/flows).

