---
title: "클래스 모킹"
description: "단 한 번의  호출로 클래스 전체를 모킹할 수 있습니다."
---

# 클래스 모킹

단 한 번의 [`vi.fn`](https://vitest.dev/api/vi#fn) 호출로 클래스 전체를 모킹할 수 있습니다.

```ts
class Dog {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  static getType(): string {
    return "animal";
  }

  greet = (): string => {
    return `Hi! My name is ${this.name}!`;
  };

  speak(): string {
    return "bark!";
  }

  isHungry() {}
  feed() {}
}
```

`vi.fn`(또는 `vi.spyOn().mockImplementation()`)으로 이 클래스를 다시 만들 수 있습니다:

```ts
const Dog = vi.fn(
  class {
    static getType = vi.fn(() => "mocked animal");

    constructor(name) {
      this.name = name;
    }

    greet = vi.fn(() => `Hi! My name is ${this.name}!`);
    speak = vi.fn(() => "loud bark!");
    feed = vi.fn();
  },
);
```

::: warning
생성자 함수에서 non-primitive를 반환하면, 그 값이 `new` 표현식의 결과가 됩니다. 이 경우 `[[Prototype]]`이 올바르게 바인딩되지 않을 수 있습니다:

```ts
const CorrectDogClass = vi.fn(function (name) {
  this.name = name;
});

const IncorrectDogClass = vi.fn((name) => ({
  name,
}));

const Marti = new CorrectDogClass("Marti");
const Newt = new IncorrectDogClass("Newt");

Marti instanceof CorrectDogClass; // ✅ true
Newt instanceof IncorrectDogClass; // ❌ false!
```

클래스를 모킹할 때는 함수보다 클래스 문법을 사용하는 것을 권장합니다.
:::

::: tip 언제 사용하나요?
일반적으로 클래스가 다른 모듈에서 다시 export되는 경우, 모듈 팩토리 내부에서 다음과 같이 클래스를 재구성합니다:

```ts
import { Dog } from "./dog.js";

vi.mock(import("./dog.js"), () => {
  const Dog = vi.fn(
    class {
      feed = vi.fn();
      // ... other mocks
    },
  );
  return { Dog };
});
```

이 방법은 동일한 인터페이스를 받는 함수에 클래스 인스턴스를 전달할 때도 사용할 수 있습니다:

```ts [src/feed.ts]
function feed(dog: Dog) {
  // ...
}
```

```ts [tests/dog.test.ts]
import { expect, test, vi } from "vitest";
import { feed } from "../src/feed.js";

const Dog = vi.fn(
  class {
    feed = vi.fn();
  },
);

test("can feed dogs", () => {
  const dogMax = new Dog("Max");

  feed(dogMax);

  expect(dogMax.feed).toHaveBeenCalled();
  expect(dogMax.isHungry()).toBe(false);
});
```

:::

이제 `Dog` 클래스의 새 인스턴스를 만들면 `speak` 메서드(`feed`, `greet`와 함께)가 이미 모킹되어 있습니다:

```ts
const Cooper = new Dog("Cooper");
Cooper.speak(); // loud bark!
Cooper.greet(); // Hi! My name is Cooper!

// you can use built-in assertions to check the validity of the call
expect(Cooper.speak).toHaveBeenCalled();
expect(Cooper.greet).toHaveBeenCalled();

const Max = new Dog("Max");

// methods are not shared between instances if you assigned them directly
expect(Max.speak).not.toHaveBeenCalled();
expect(Max.greet).not.toHaveBeenCalled();
```

특정 인스턴스에 대해 반환값을 다시 할당할 수 있습니다:

```ts
const dog = new Dog("Cooper");

// "vi.mocked" is a type helper, since
// TypeScript doesn't know that Dog is a mocked class,
// it wraps any function in a Mock<T> type
// without validating if the function is a mock
vi.mocked(dog.speak).mockReturnValue("woof woof");

dog.speak(); // woof woof
```

프로퍼티를 모킹하려면 `vi.spyOn(dog, 'name', 'get')` 메서드를 사용할 수 있습니다. 이렇게 하면 모킹된 프로퍼티에 대해 spy assertion을 사용할 수 있습니다:

```ts
const dog = new Dog("Cooper");

const nameSpy = vi.spyOn(dog, "name", "get").mockReturnValue("Max");

expect(dog.name).toBe("Max");
expect(nameSpy).toHaveBeenCalledTimes(1);
```

::: tip
같은 방법으로 getter와 setter도 spy할 수 있습니다.
:::

::: danger
`vi.fn()`에서 클래스를 사용하는 기능은 Vitest 4에서 도입되었습니다. 이전에는 `function`과 `prototype` 상속을 직접 사용해야 했습니다. [v3 guide](https://v3.vitest.dev/guide/mocking.html#classes)를 참고하세요.
:::
