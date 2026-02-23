---
title: 'Testing'
description: 'In React and Next.js, there are a few different types of tests you can write, each with its own purpose and use cases. This page provides an overview ...'
---

Source URL: https://nextjs.org/docs/pages/guides/testing

# Testing

In React and Next.js, there are a few different types of tests you can write, each with its own purpose and use cases. This page provides an overview of types and commonly used tools you can use to test your application.

## Types of tests

* **Unit Testing** involves testing individual units (or blocks of code) in isolation. In React, a unit can be a single function, hook, or component.
* **Component Testing** is a more focused version of unit testing where the primary subject of the tests is React components. This may involve testing how components are rendered, their interaction with props, and their behavior in response to user events.
* **Integration Testing** involves testing how multiple units work together. This can be a combination of components, hooks, and functions.
* **End-to-End (E2E) Testing** involves testing user flows in an environment that simulates real user scenarios, like the browser. This means testing specific tasks (e.g. signup flow) in a production-like environment.
* **Snapshot Testing** involves capturing the rendered output of a component and saving it to a snapshot file. When tests run, the current rendered output of the component is compared against the saved snapshot. Changes in the snapshot are used to indicate unexpected changes in behavior.

## Guides

See the guides below to learn how to set up Next.js with these commonly used testing tools:

- [Cypress](https://nextjs.org/docs/pages/guides/testing/cypress)
  - Learn how to set up Next.js with Cypress for End-to-End (E2E) and Component Testing.
- [Jest](https://nextjs.org/docs/pages/guides/testing/jest)
  - Learn how to set up Next.js with Jest for Unit Testing.
- [Playwright](https://nextjs.org/docs/pages/guides/testing/playwright)
  - Learn how to set up Next.js with Playwright for End-to-End (E2E) and Integration testing.
- [Vitest](https://nextjs.org/docs/pages/guides/testing/vitest)
  - Learn how to set up Next.js with Vitest and React Testing Library - two popular unit testing libraries.

---

