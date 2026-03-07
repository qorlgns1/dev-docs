---
title: "컴포넌트 테스트"
description: "컴포넌트 테스트는 개별 UI 컴포넌트를 격리된 상태에서 테스트하는 데 초점을 맞춘 테스트 전략입니다. 전체 사용자 흐름을 테스트하는 엔드투엔드 테스트와 달리, 컴포넌트 테스트는 각 컴포넌트가 단독으로 올바르게 동작하는지 검증하므로 실행이 더 빠르고 디버깅도 더 쉽습니다..."
---

출처 URL: https://vitest.dev/guide/browser/component-testing

# 컴포넌트 테스트

컴포넌트 테스트는 개별 UI 컴포넌트를 격리된 상태에서 테스트하는 데 초점을 맞춘 테스트 전략입니다. 전체 사용자 흐름을 테스트하는 엔드투엔드 테스트와 달리, 컴포넌트 테스트는 각 컴포넌트가 단독으로 올바르게 동작하는지 검증하므로 실행이 더 빠르고 디버깅도 더 쉽습니다.

Vitest는 Vue, React, Svelte, Lit, Preact, Qwik, Solid, Marko 등 다양한 프레임워크 전반에서 컴포넌트 테스트를 폭넓게 지원합니다. 이 가이드는 Vitest로 컴포넌트를 효과적으로 테스트하기 위한 구체적인 패턴, 도구, 모범 사례를 다룹니다.

## 왜 컴포넌트 테스트인가?

컴포넌트 테스트는 단위 테스트와 엔드투엔드 테스트 사이에 위치하며, 다음과 같은 여러 장점을 제공합니다.

- **더 빠른 피드백** - 전체 애플리케이션을 로드하지 않고 개별 컴포넌트를 테스트
- **격리된 테스트** - 외부 의존성 없이 컴포넌트 동작에 집중
- **더 나은 디버깅** - 특정 컴포넌트의 문제를 더 쉽게 식별
- **포괄적인 커버리지** - 엣지 케이스와 오류 상태를 더 쉽게 테스트

## 컴포넌트 테스트를 위한 Browser Mode

Vitest의 컴포넌트 테스트는 **Browser Mode**를 사용해 Playwright, WebdriverIO, 또는 preview mode 기반의 실제 브라우저 환경에서 테스트를 실행합니다. 이를 통해 컴포넌트가 실제 DOM 구현, CSS 렌더링, 브라우저 API를 갖춘 실제 브라우저에서 실행되므로 가장 정확한 테스트 환경을 제공합니다.

### 왜 Browser Mode인가?

Browser Mode는 가장 정확한 테스트 환경을 제공하므로 컴포넌트 테스트에서 권장되는 접근 방식입니다. DOM 시뮬레이션 라이브러리와 달리, Browser Mode는 사용자에게 영향을 줄 수 있는 실제 환경의 문제를 포착합니다.

::: tip
Browser Mode는 DOM 시뮬레이션 라이브러리가 놓칠 수 있는 다음 문제를 잡아냅니다.

- CSS 레이아웃 및 스타일링 문제
- 실제 브라우저 API 동작
- 정확한 이벤트 처리 및 전파
- 올바른 포커스 관리 및 접근성 기능

:::

### 이 가이드의 목적

이 가이드는 Vitest의 기능을 사용한 **컴포넌트 테스트 패턴과 모범 사례**에 특히 집중합니다. 많은 예제가 Browser Mode(권장 방식이기 때문)를 사용하지만, 여기서의 핵심은 브라우저 설정 세부사항보다 컴포넌트 중심 테스트 전략입니다.

브라우저 설정, 구성 옵션, 고급 브라우저 기능에 대한 자세한 내용은 [Browser Mode documentation](https://vitest.dev/guide/browser/)를 참고하세요.

## 좋은 컴포넌트 테스트의 조건

좋은 컴포넌트 테스트는 구현 세부사항보다 **동작과 사용자 경험**에 집중합니다.

- **계약을 테스트** - 컴포넌트가 입력(props)을 받고 출력(events, renders)을 생성하는 방식
- **사용자 상호작용 테스트** - 클릭, 폼 제출, 키보드 내비게이션
- **엣지 케이스 테스트** - 오류 상태, 로딩 상태, 빈 상태
- **내부 구현 테스트 지양** - 상태 변수, private methods, CSS classes

### 컴포넌트 테스트 계층

```
1. Critical User Paths → Always test these
2. Error Handling      → Test failure scenarios
3. Edge Cases          → Empty data, extreme values
4. Accessibility       → Screen readers, keyboard nav
5. Performance         → Large datasets, animations
```

## 컴포넌트 테스트 전략

### 격리 전략

의존성을 모킹하여 컴포넌트를 격리된 상태로 테스트합니다.

```tsx
// For API requests, we recommend MSW (Mock Service Worker)
// See: https://vitest.dev/guide/mocking/requests
//
// vi.mock(import('../api/userService'), () => ({
//   fetchUser: vi.fn().mockResolvedValue({ name: 'John' })
// }))

// Mock child components to focus on parent logic
vi.mock(import("../components/UserCard"), () => ({
  default: vi.fn(({ user }) => `<div>User: ${user.name}</div>`),
}));

test("UserProfile handles loading and data states", async () => {
  const { getByText } = render(<UserProfile userId="123" />);

  // Test loading state
  await expect.element(getByText("Loading...")).toBeInTheDocument();

  // Test for data to load (expect.element auto-retries)
  await expect.element(getByText("User: John")).toBeInTheDocument();
});
```

### 통합 전략

컴포넌트 간 협업과 데이터 흐름을 테스트합니다.

```tsx
test("ProductList filters and displays products correctly", async () => {
  const mockProducts = [
    { id: 1, name: "Laptop", category: "Electronics", price: 999 },
    { id: 2, name: "Book", category: "Education", price: 29 },
  ];

  const { getByLabelText, getByText } = render(
    <ProductList products={mockProducts} />,
  );

  // Initially shows all products
  await expect.element(getByText("Laptop")).toBeInTheDocument();
  await expect.element(getByText("Book")).toBeInTheDocument();

  // Filter by category
  await userEvent.selectOptions(getByLabelText(/category/i), "Electronics");

  // Only electronics should remain
  await expect.element(getByText("Laptop")).toBeInTheDocument();
  await expect.element(queryByText("Book")).not.toBeInTheDocument();
});
```

## Testing Library 통합

Vitest는 주요 프레임워크용 공식 패키지([`vitest-browser-vue`](https://www.npmjs.com/package/vitest-browser-vue), [`vitest-browser-react`](https://www.npmjs.com/package/vitest-browser-react), [`vitest-browser-svelte`](https://www.npmjs.com/package/vitest-browser-svelte))를 제공하지만, 아직 공식 지원되지 않는 프레임워크의 경우 [Testing Library](https://testing-library.com/)와 통합할 수 있습니다.

### Testing Library를 사용할 때

- 사용하는 프레임워크에 공식 Vitest browser 패키지가 아직 없음
- 기존 Testing Library 기반 테스트를 마이그레이션 중임
- 특정 테스트 시나리오에서 Testing Library API를 선호함

### 통합 패턴

핵심은 `page.elementLocator()`를 사용해 Testing Library의 DOM 출력과 Vitest browser mode API를 연결하는 것입니다.

```jsx
// For Solid.js components
import { render } from "@testing-library/solid";
import { page } from "vitest/browser";

test("Solid component handles user interaction", async () => {
  // Use Testing Library to render the component
  const { baseElement, getByRole } = render(() => <Counter initialValue={0} />);

  // Bridge to Vitest's browser mode for interactions and assertions
  const screen = page.elementLocator(baseElement);

  // Use Vitest's page queries for finding elements
  const incrementButton = screen.getByRole("button", { name: /increment/i });

  // Use Vitest's assertions and interactions
  await expect.element(screen.getByText("Count: 0")).toBeInTheDocument();

  // Trigger user interaction using Vitest's page API
  await incrementButton.click();

  await expect.element(screen.getByText("Count: 1")).toBeInTheDocument();
});
```

### 사용 가능한 Testing Library 패키지

Vitest와 잘 동작하는 인기 Testing Library 패키지:

- [`@testing-library/solid`](https://github.com/solidjs/solid-testing-library) - Solid.js용
- [`@marko/testing-library`](https://testing-library.com/docs/marko-testing-library/intro) - Marko용
- `@testing-library/svelte`](https://testing-library.com/docs/svelte-testing-library/intro) - [`vitest-browser-svelte`의 대안
- `@testing-library/vue`](https://testing-library.com/docs/vue-testing-library/intro) - [`vitest-browser-vue`의 대안

::: tip Migration Path
나중에 사용하는 프레임워크가 Vitest 공식 지원을 받게 되면, Testing Library의 `render` 함수만 교체하면서 기존 테스트 로직 대부분은 유지한 채 점진적으로 마이그레이션할 수 있습니다.
:::

## 모범 사례

### 1. CI/CD에서 Browser Mode 사용

가장 정확한 테스트를 위해 실제 브라우저 환경에서 테스트가 실행되도록 하세요. Browser Mode는 정확한 CSS 렌더링, 실제 브라우저 API, 올바른 이벤트 처리를 제공합니다.

### 2. 사용자 상호작용 테스트

Vitest의 [Interactivity API](https://vitest.dev/api/browser/interactivity)를 사용해 실제 사용자 동작을 시뮬레이션하세요. [Advanced Testing Patterns](#advanced-testing-patterns)에 나온 것처럼 `page.getByRole()`과 `userEvent` 메서드를 사용하세요.

```tsx
// Good: Test actual user interactions
await page.getByRole("button", { name: /submit/i }).click();
await page.getByLabelText(/email/i).fill("user@example.com");

// Avoid: Testing implementation details
// component.setState({ email: 'user@example.com' })
```

### 3. 접근성 테스트

키보드 내비게이션, 포커스 관리, ARIA 속성을 테스트해 모든 사용자가 컴포넌트를 사용할 수 있도록 하세요. 실전 패턴은 [Testing Accessibility](#testing-accessibility) 예제를 참고하세요.

```tsx
// Test keyboard navigation
await userEvent.keyboard("{Tab}");
await expect.element(document.activeElement).toHaveFocus();

// Test ARIA attributes
await expect.element(modal).toHaveAttribute("aria-modal", "true");
```

### 4. 외부 의존성 모킹

API와 외부 서비스를 모킹해 테스트를 컴포넌트 로직에 집중시키세요. 이렇게 하면 테스트가 더 빠르고 안정적입니다. 예시는 [Isolation Strategy](#isolation-strategy)를 참고하세요.

```tsx
// For API requests, we recommend using MSW (Mock Service Worker)
// See: https://vitest.dev/guide/mocking/requests
// This provides more realistic request/response mocking

// For module mocking, use the import() syntax
vi.mock(import("../components/UserCard"), () => ({
  default: vi.fn(() => <div>Mocked UserCard</div>),
}));
```

### 5. 의미 있는 테스트 설명 작성

구현 세부사항이 아니라 기대 동작을 설명하는 테스트 설명을 작성하세요.

```tsx
// Good: Describes user-facing behavior
test("shows error message when email format is invalid");
test("disables submit button while form is submitting");

// Avoid: Implementation-focused descriptions
test("calls validateEmail function");
test("sets isSubmitting state to true");
```

## 고급 테스트 패턴

### 컴포넌트 상태 관리 테스트

```tsx
// Testing stateful components and state transitions
test("ShoppingCart manages items correctly", async () => {
  const { getByText, getByTestId } = render(<ShoppingCart />);

  // Initially empty
  await expect.element(getByText("Your cart is empty")).toBeInTheDocument();

  // Add item
  await page.getByRole("button", { name: /add laptop/i }).click();

  // Verify state change
  await expect.element(getByText("1 item")).toBeInTheDocument();
  await expect.element(getByText("Laptop - $999")).toBeInTheDocument();

  // Test quantity updates
  await page.getByRole("button", { name: /increase quantity/i }).click();
  await expect.element(getByText("2 items")).toBeInTheDocument();
});
```

### 데이터 페칭이 있는 비동기 컴포넌트 테스트

```tsx
// Option 1: Recommended - Use MSW (Mock Service Worker) for API mocking
import { http, HttpResponse } from "msw";
import { setupWorker } from "msw/browser";

// Set up MSW worker with API handlers
const worker = setupWorker(
  http.get("/api/users/:id", ({ params }) => {
    // Describe the happy path
    return HttpResponse.json({
      id: params.id,
      name: "John Doe",
      email: "john@example.com",
    });
  }),
);

// Start the worker before all tests
beforeAll(() => worker.start());
afterEach(() => worker.resetHandlers());
afterAll(() => worker.stop());

test("UserProfile handles loading, success, and error states", async () => {
  // Test success state
  const { getByText } = render(<UserProfile userId="123" />);
  // expect.element auto-retries until elements are found
  await expect.element(getByText("John Doe")).toBeInTheDocument();
  await expect.element(getByText("john@example.com")).toBeInTheDocument();

  // Test error state by overriding the handler for this test
  worker.use(
    http.get("/api/users/:id", () => {
      return HttpResponse.json({ error: "User not found" }, { status: 404 });
    }),
  );

  const { getByText: getErrorText } = render(<UserProfile userId="999" />);
  await expect
    .element(getErrorText("Error: User not found"))
    .toBeInTheDocument();
});
```

::: tip
[using MSW in the browser](https://mswjs.io/docs/integrations/browser)에서 더 자세한 내용을 확인하세요.
:::

### 컴포넌트 간 통신 테스트

```tsx
// Test parent-child component interaction
test("parent and child components communicate correctly", async () => {
  const mockOnSelectionChange = vi.fn();

  const { getByText } = render(
    <ProductCatalog onSelectionChange={mockOnSelectionChange}>
      <ProductFilter />
      <ProductGrid />
    </ProductCatalog>,
  );

  // Interact with child component
  await page.getByRole("checkbox", { name: /electronics/i }).click();

  // Verify parent receives the communication
  expect(mockOnSelectionChange).toHaveBeenCalledWith({
    category: "electronics",
    filters: ["electronics"],
  });

  // Verify other child component updates (expect.element auto-retries)
  await expect
    .element(getByText("Showing Electronics products"))
    .toBeInTheDocument();
});
```

### 검증이 포함된 복잡한 폼 테스트

```tsx
test("ContactForm handles complex validation scenarios", async () => {
  const mockSubmit = vi.fn();
  const { getByLabelText, getByText } = render(
    <ContactForm onSubmit={mockSubmit} />,
  );

  const nameInput = page.getByLabelText(/full name/i);
  const emailInput = page.getByLabelText(/email/i);
  const messageInput = page.getByLabelText(/message/i);
  const submitButton = page.getByRole("button", { name: /send message/i });

  // Test validation triggers
  await submitButton.click();

  await expect.element(getByText("Name is required")).toBeInTheDocument();
  await expect.element(getByText("Email is required")).toBeInTheDocument();
  await expect.element(getByText("Message is required")).toBeInTheDocument();

  // Test partial validation
  await nameInput.fill("John Doe");
  await submitButton.click();

  await expect.element(getByText("Name is required")).not.toBeInTheDocument();
  await expect.element(getByText("Email is required")).toBeInTheDocument();

  // Test email format validation
  await emailInput.fill("invalid-email");
  await submitButton.click();

  await expect
    .element(getByText("Please enter a valid email"))
    .toBeInTheDocument();

  // Test successful submission
  await emailInput.fill("john@example.com");
  await messageInput.fill("Hello, this is a test message.");
  await submitButton.click();

  expect(mockSubmit).toHaveBeenCalledWith({
    name: "John Doe",
    email: "john@example.com",
    message: "Hello, this is a test message.",
  });
});
```

### 에러 바운더리 테스트

```tsx
// Test how components handle and recover from errors
function ThrowError({ shouldThrow }: { shouldThrow: boolean }) {
  if (shouldThrow) {
    throw new Error("Component error!");
  }
  return <div>Component working fine</div>;
}

test("ErrorBoundary catches and displays errors gracefully", async () => {
  const { getByText, rerender } = render(
    <ErrorBoundary fallback={<div>Something went wrong</div>}>
      <ThrowError shouldThrow={false} />
    </ErrorBoundary>,
  );

  // Initially working
  await expect.element(getByText("Component working fine")).toBeInTheDocument();

  // Trigger error
  rerender(
    <ErrorBoundary fallback={<div>Something went wrong</div>}>
      <ThrowError shouldThrow={true} />
    </ErrorBoundary>,
  );

  // Error boundary should catch it
  await expect.element(getByText("Something went wrong")).toBeInTheDocument();
});
```

### 접근성 테스트

```tsx
test("Modal component is accessible", async () => {
  const { getByRole, getByLabelText } = render(
    <Modal isOpen={true} title="Settings">
      <SettingsForm />
    </Modal>,
  );

  // Test focus management - modal should receive focus when opened
  // This is crucial for screen reader users to know a modal opened
  const modal = getByRole("dialog");
  await expect.element(modal).toHaveFocus();

  // Test ARIA attributes - these provide semantic information to screen readers
  await expect.element(modal).toHaveAttribute("aria-labelledby"); // Links to title element
  await expect.element(modal).toHaveAttribute("aria-modal", "true"); // Indicates modal behavior

  // Test keyboard navigation - Escape key should close modal
  // This is required by ARIA authoring practices
  await userEvent.keyboard("{Escape}");
  // expect.element auto-retries until modal is removed
  await expect.element(modal).not.toBeInTheDocument();

  // Test focus trap - tab navigation should cycle within modal
  // This prevents users from tabbing to content behind the modal
  const firstInput = getByLabelText(/username/i);
  const lastButton = getByRole("button", { name: /save/i });

  // Use click to focus on the first input, then test tab navigation
  await firstInput.click();
  await userEvent.keyboard("{Shift>}{Tab}{/Shift}"); // Shift+Tab goes backwards
  await expect.element(lastButton).toHaveFocus(); // Should wrap to last element
});
```

## 컴포넌트 테스트 디버깅

### 1. Browser Dev Tools 사용

Browser Mode는 테스트를 실제 브라우저에서 실행하므로 전체 개발자 도구에 접근할 수 있습니다. 테스트가 실패하면 다음을 할 수 있습니다.

- **브라우저 개발자 도구 열기** 테스트 실행 중(F12 또는 우클릭 → Inspect)
- **브레이크포인트 설정** 테스트 코드 또는 컴포넌트 코드에
- **DOM 검사** 실제 렌더링 결과 확인
- **콘솔 오류 확인** JavaScript 오류 또는 경고 파악
- **네트워크 요청 모니터링** API 호출 디버깅

headful mode 디버깅을 위해서는 브라우저 설정에 `headless: false`를 임시로 추가하세요.

### 2. 디버그 구문 추가

테스트 실패 원인을 파악하기 위해 전략적으로 로깅을 사용하세요.

```tsx
test("debug form validation", async () => {
  render(<ContactForm />);

  const submitButton = page.getByRole("button", { name: /submit/i });
  await submitButton.click();

  // Debug: Check if element exists with different query
  const errorElement = page.getByText("Email is required");
  console.log("Error element found:", errorElement.length);

  await expect.element(errorElement).toBeInTheDocument();
});
```

### 3. 렌더링 출력 검사

컴포넌트가 예상대로 렌더링되지 않을 때는 체계적으로 조사하세요.

**Vitest의 browser UI 사용:**

- browser mode를 활성화해 테스트 실행
- 터미널에 표시된 브라우저 URL을 열어 실행 중인 테스트 확인
- 시각적 점검으로 CSS 이슈, 레이아웃 문제, 누락된 요소 식별

**요소 쿼리 테스트:**

```tsx
// Debug why elements can't be found
const button = page.getByRole("button", { name: /submit/i });
console.log("Button count:", button.length); // Should be 1

// Try alternative queries if the first one fails
if (button.length === 0) {
  console.log("All buttons:", page.getByRole("button").length);
  console.log("By test ID:", page.getByTestId("submit-btn").length);
}
```

### 4. 셀렉터 검증

셀렉터 문제는 테스트 실패의 흔한 원인입니다. 체계적으로 디버깅하세요.

**접근 가능한 이름 확인:**

```tsx
// If getByRole fails, check what roles/names are available
const buttons = page.getByRole("button").all();
for (const button of buttons) {
  // Use element() to get the DOM element and access native properties
  const element = button.element();
  const accessibleName =
    element.getAttribute("aria-label") || element.textContent;
  console.log(`Button: "${accessibleName}"`);
}
```

**서로 다른 쿼리 전략 테스트:**

```tsx
// Multiple ways to find the same element using .or for auto-retrying
const submitButton = page
  .getByRole("button", { name: /submit/i }) // By accessible name
  .or(page.getByTestId("submit-button")) // By test ID
  .or(page.getByText("Submit")); // By exact text
// Note: Vitest doesn't have page.locator(), use specific getBy* methods instead
```

**일반적인 셀렉터 디버깅 패턴:**

```tsx
test("debug element queries", async () => {
  render(<LoginForm />);

  // Check if element is visible and enabled
  const emailInput = page.getByLabelText(/email/i);
  await expect.element(emailInput).toBeVisible(); // Will show if element is visible and print DOM if not
});
```

### 5. 비동기 이슈 디버깅

컴포넌트 테스트에는 타이밍 이슈가 자주 포함됩니다.

```tsx
test("debug async component behavior", async () => {
  render(<AsyncUserProfile userId="123" />);

  // expect.element will automatically retry and show helpful error messages
  await expect.element(page.getByText("John Doe")).toBeInTheDocument();
});
```

## 다른 테스트 프레임워크에서 마이그레이션

### Jest + Testing Library에서

대부분의 Jest + Testing Library 테스트는 최소한의 변경으로 동작합니다.

```ts
// Before (Jest)
import { render, screen } from "@testing-library/react"; // [!code --]

// After (Vitest)
import { render } from "vitest-browser-react"; // [!code ++]
```

### 주요 차이점

- DOM assertion에는 `expect()` 대신 `await expect.element()` 사용
- 사용자 상호작용에는 `@testing-library/user-event` 대신 `vitest/browser` 사용
- Browser Mode는 정확한 테스트를 위해 실제 브라우저 환경 제공

## 더 알아보기

- Browser Mode Documentation
- Assertion API
- Interactivity API
- Example Repository
