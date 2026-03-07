---
title: "함수 모킹"
description: "함수 모킹은 두 가지 범주로 나눌 수 있습니다: spying과 mocking입니다."
---

출처 URL: https://vitest.dev/guide/mocking/functions

# 함수 모킹

함수 모킹은 두 가지 범주로 나눌 수 있습니다: spying과 mocking입니다.

객체의 메서드 동작을 관찰해야 한다면, 해당 메서드 호출을 추적하는 spy를 만들기 위해 [`vi.spyOn()`](https://vitest.dev/api/vi#vi-spyon)을 사용할 수 있습니다.

인자로 사용자 정의 함수 구현을 전달하거나 새로운 mocked 엔터티를 만들어야 한다면, mock 함수를 만들기 위해 [`vi.fn()`](https://vitest.dev/api/vi#vi-fn)을 사용할 수 있습니다.

`vi.spyOn`과 `vi.fn`은 동일한 메서드를 공유합니다.

## 예시

```js
import { afterEach, describe, expect, it, vi } from "vitest";

const messages = {
  items: [
    { message: "Simple test message", from: "Testman" },
    // ...
  ],
  addItem(item) {
    messages.items.push(item);
    messages.callbacks.forEach((callback) => callback(item));
  },
  onItem(callback) {
    messages.callbacks.push(callback);
  },
  getLatest, // can also be a `getter or setter if supported`
};

function getLatest(index = messages.items.length - 1) {
  return messages.items[index];
}

it("should get the latest message with a spy", () => {
  const spy = vi.spyOn(messages, "getLatest");
  expect(spy.getMockName()).toEqual("getLatest");

  expect(messages.getLatest()).toEqual(
    messages.items[messages.items.length - 1],
  );

  expect(spy).toHaveBeenCalledTimes(1);

  spy.mockImplementationOnce(() => "access-restricted");
  expect(messages.getLatest()).toEqual("access-restricted");

  expect(spy).toHaveBeenCalledTimes(2);
});

it("passing down the mock", () => {
  const callback = vi.fn();
  messages.onItem(callback);

  messages.addItem({ message: "Another test message", from: "Testman" });
  expect(callback).toHaveBeenCalledWith({
    message: "Another test message",
    from: "Testman",
  });
});
```
