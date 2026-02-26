---
title: "GenericAssertions"
description: "import { test, expect } from '@playwright/test';"
---

Source URL: https://playwright.dev/docs/api/class-genericassertions

# GenericAssertions | Playwright

[GenericAssertions](https://playwright.dev/docs/api/class-genericassertions "GenericAssertions") 클래스는 테스트에서 어떤 값에 대해서도 단언을 수행할 수 있는 단언 메서드를 제공합니다. [GenericAssertions](https://playwright.dev/docs/api/class-genericassertions "GenericAssertions")의 새 인스턴스는 [expect()](https://playwright.dev/docs/api/class-playwrightassertions#playwright-assertions-expect-generic)를 호출하여 생성됩니다:

```
    import { test, expect } from '@playwright/test';

    test('assert a value', async ({ page }) => {
      const value = 1;
      expect(value).toBe(2);
    });

```

---

## Methods[​](https://playwright.dev/docs/api/class-genericassertions#methods "Direct link to Methods")

### any[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-any "Direct link to any")

추가된 버전: v1.9 genericAssertions.any

`expect.any()`는 [constructor](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-any-option-constructor)로 생성된 모든 객체 인스턴스 또는 이에 대응하는 원시 타입과 일치합니다. 패턴 매칭을 수행하려면 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) 내부에서 사용하세요.

**Usage**

```
    // Match instance of a class.
    class Example {}
    expect(new Example()).toEqual(expect.any(Example));

    // Match any number.
    expect({ prop: 1 }).toEqual({ prop: expect.any(Number) });

    // Match any string.
    expect('abc').toEqual(expect.any(String));

```

**Arguments**

- `constructor` [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-any-option-constructor)

`ExampleClass` 같은 예상 객체의 생성자 또는 `Number` 같은 원시 박싱 타입입니다.

---

### anything[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-anything "Direct link to anything")

추가된 버전: v1.9 genericAssertions.anything

`expect.anything()`은 `null`과 `undefined`를 제외한 모든 값과 일치합니다. 패턴 매칭을 수행하려면 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) 내부에서 사용하세요.

**Usage**

```
    const value = { prop: 1 };
    expect(value).toEqual({ prop: expect.anything() });
    expect(value).not.toEqual({ otherProp: expect.anything() });

```

---

### arrayContaining[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-containing "Direct link to arrayContaining")

추가된 버전: v1.9 genericAssertions.arrayContaining

`expect.arrayContaining()`은 예상 배열의 모든 요소를 포함하는 배열과 일치하며, 순서는 상관없습니다. 전달된 배열은 예상 배열의 상위 집합일 수 있으며 추가 요소를 포함할 수 있습니다.

패턴 매칭을 수행하려면 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) 내부에서 이 메서드를 사용하세요.

**Usage**

```
    expect([1, 2, 3]).toEqual(expect.arrayContaining([3, 1]));
    expect([1, 2, 3]).not.toEqual(expect.arrayContaining([1, 4]));

```

**Arguments**

- `expected` [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")>[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-containing-option-expected)

전달된 값의 부분 집합인 예상 배열입니다.

---

### arrayOf[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-of "Direct link to arrayOf")

추가된 버전: v1.57 genericAssertions.arrayOf

`expect.arrayOf()`는 [constructor](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-of-option-constructor)로 생성된 객체 배열 또는 이에 대응하는 원시 타입과 일치합니다. 패턴 매칭을 수행하려면 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) 내부에서 사용하세요.

**Usage**

```
    // Match instance of a class.
    class Example {}
    expect([new Example(), new Example()]).toEqual(expect.arrayOf(Example));

    // Match any string.
    expect(['a', 'b', 'c']).toEqual(expect.arrayOf(String));

```

**Arguments**

- `constructor` [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-of-option-constructor)

`ExampleClass` 같은 예상 객체의 생성자 또는 `Number` 같은 원시 박싱 타입입니다.

---

### closeTo[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-close-to "Direct link to closeTo")

추가된 버전: v1.9 genericAssertions.closeTo

부동소수점 수의 근사 동등성을 비교합니다. 패턴 매칭을 수행하려면 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) 내부에서 이 메서드를 사용하세요. 단순히 두 숫자를 비교하는 경우에는 [expect(value).toBeCloseTo()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-close-to)를 우선 사용하세요.

**Usage**

```
    expect({ prop: 0.1 + 0.2 }).not.toEqual({ prop: 0.3 });
    expect({ prop: 0.1 + 0.2 }).toEqual({ prop: expect.closeTo(0.3, 5) });

```

**Arguments**

- `expected` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-close-to-option-expected)

예상 값입니다.

- `numDigits` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-close-to-option-num-digits)

소수점 이하에서 같아야 하는 자릿수입니다.

---

### objectContaining[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-object-containing "Direct link to objectContaining")

추가된 버전: v1.9 genericAssertions.objectContaining

`expect.objectContaining()`은 예상 객체의 모든 속성을 포함하고 일치하는 객체와 일치합니다. 전달된 객체는 예상 객체의 상위 집합일 수 있으며 추가 속성을 포함할 수 있습니다.

패턴 매칭을 수행하려면 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) 내부에서 이 메서드를 사용하세요. 객체 속성은 기대 조건을 더 완화하기 위한 matcher가 될 수 있습니다. 예제를 참고하세요.

**Usage**

```
    // Assert some of the properties.
    expect({ foo: 1, bar: 2 }).toEqual(expect.objectContaining({ foo: 1 }));

    // Matchers can be used on the properties as well.
    expect({ foo: 1, bar: 2 }).toEqual(expect.objectContaining({ bar: expect.any(Number) }));

    // Complex matching of sub-properties.
    expect({
      list: [1, 2, 3],
      obj: { prop: 'Hello world!', another: 'some other value' },
      extra: 'extra',
    }).toEqual(expect.objectContaining({
      list: expect.arrayContaining([2, 3]),
      obj: expect.objectContaining({ prop: expect.stringContaining('Hello') }),
    }));

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-object-containing-option-expected)

속성의 부분 집합을 포함하는 예상 객체 패턴입니다.

---

### stringContaining[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-string-containing "Direct link to stringContaining")

추가된 버전: v1.9 genericAssertions.stringContaining

`expect.stringContaining()`은 예상 부분 문자열을 포함하는 문자열과 일치합니다. 패턴 매칭을 수행하려면 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) 내부에서 이 메서드를 사용하세요.

**Usage**

```
    expect('Hello world!').toEqual(expect.stringContaining('Hello'));

```

**Arguments**

- `expected` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-string-containing-option-expected)

예상 부분 문자열입니다.

---

### stringMatching[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-string-matching "Direct link to stringMatching")

추가된 버전: v1.9 genericAssertions.stringMatching

`expect.stringMatching()`은 전달된 문자열이 예상 패턴과 일치할 때 일치합니다. 패턴 매칭을 수행하려면 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal) 내부에서 이 메서드를 사용하세요.

**Usage**

```
    expect('123ms').toEqual(expect.stringMatching(/\d+m?s/));

    // Inside another matcher.
    expect({
      status: 'passed',
      time: '123ms',
    }).toEqual({
      status: expect.stringMatching(/passed|failed/),
      time: expect.stringMatching(/\d+m?s/),
    });

```

**Arguments**

- `expected` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-string-matching-option-expected)

예상 문자열이 일치해야 하는 패턴입니다.

---

### toBe[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be "Direct link to toBe")

추가된 버전: v1.9 genericAssertions.toBe

`Object.is`를 호출해 값을 [expected](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-option-expected)와 비교합니다. 이 메서드는 엄격 동등 연산자 `===`와 유사하게 객체의 내용을 비교하지 않고 참조로 비교합니다.

**Usage**

```
    const value = { prop: 1 };
    expect(value).toBe(value);
    expect(value).not.toBe({});
    expect(value.prop).toBe(1);

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-option-expected)

예상 값입니다.

---

### toBeCloseTo[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-close-to "Direct link to toBeCloseTo")

추가된 버전: v1.9 genericAssertions.toBeCloseTo

부동소수점 수의 근사 동등성을 비교합니다. 부동소수점 수를 비교할 때는 [expect(value).toBe()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be) 대신 이 메서드를 사용하세요.

**Usage**

```
    expect(0.1 + 0.2).not.toBe(0.3);
    expect(0.1 + 0.2).toBeCloseTo(0.3, 5);

```

**Arguments**

- `expected` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-close-to-option-expected)

예상 값입니다.

- `numDigits` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-close-to-option-num-digits)

소수점 이하에서 같아야 하는 자릿수입니다.

---

### toBeDefined[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-defined "Direct link to toBeDefined")

추가된 버전: v1.9 genericAssertions.toBeDefined

값이 `undefined`가 아님을 보장합니다.

**Usage**

```
    const value = null;
    expect(value).toBeDefined();

```

---

### toBeFalsy[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-falsy "Direct link to toBeFalsy")

추가된 버전: v1.9 genericAssertions.toBeFalsy

값이 불리언 컨텍스트에서 거짓(`false`)임을 보장합니다. 즉 `false`, `0`, `''`, `null`, `undefined`, `NaN` 중 하나여야 합니다. 특정 값은 중요하지 않을 때 이 메서드를 사용하세요.

**Usage**

```
    const value = null;
    expect(value).toBeFalsy();

```

---

### toBeGreaterThan[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-greater-than "Direct link to toBeGreaterThan")

추가된 버전: v1.9 genericAssertions.toBeGreaterThan

숫자 또는 big integer 값에 대해 `value > expected`임을 보장합니다.

**Usage**

```
    const value = 42;
    expect(value).toBeGreaterThan(1);

```

**Arguments**

- `expected` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [bigint][#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-greater-than-option-expected)

비교할 값입니다.

---

### toBeGreaterThanOrEqual[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-greater-than-or-equal "Direct link to toBeGreaterThanOrEqual")

추가된 버전: v1.9 genericAssertions.toBeGreaterThanOrEqual

숫자 또는 big integer 값에 대해 `value >= expected`임을 보장합니다.

**Usage**

```
    const value = 42;
    expect(value).toBeGreaterThanOrEqual(42);

```

**Arguments**

- `expected` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [bigint][#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-greater-than-or-equal-option-expected)

비교할 값입니다.

---

### toBeInstanceOf[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-instance-of "Direct link to toBeInstanceOf")

추가된 버전: v1.9 genericAssertions.toBeInstanceOf

값이 클래스의 인스턴스임을 보장합니다. `instanceof` 연산자를 사용합니다.

**Usage**

```
    expect(page).toBeInstanceOf(Page);

    class Example {}
    expect(new Example()).toBeInstanceOf(Example);

```

**Arguments**

- `expected` [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-instance-of-option-expected)

클래스 또는 생성자 함수입니다.

---

### toBeLessThan[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-less-than "Direct link to toBeLessThan")

추가된 버전: v1.9 genericAssertions.toBeLessThan

숫자 또는 big integer 값에 대해 `value < expected`임을 보장합니다.

**Usage**

```
    const value = 42;
    expect(value).toBeLessThan(100);

```

**Arguments**

- `expected` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [bigint][#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-less-than-option-expected)

비교할 값입니다.

---

### toBeLessThanOrEqual[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-less-than-or-equal "Direct link to toBeLessThanOrEqual")

추가된 버전: v1.9 genericAssertions.toBeLessThanOrEqual

숫자 또는 big integer 값에 대해 `value <= expected`임을 보장합니다.

**Usage**

```
    const value = 42;
    expect(value).toBeLessThanOrEqual(42);

```

**Arguments**

- `expected` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") | [bigint][#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-less-than-or-equal-option-expected)

비교할 값입니다.

---

### toBeNaN[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-na-n "Direct link to toBeNaN")

추가된 버전: v1.9 genericAssertions.toBeNaN

값이 `NaN`임을 보장합니다.

**Usage**

```
    const value = NaN;
    expect(value).toBeNaN();

```

---

### toBeNull[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-null "Direct link to toBeNull")

추가된 버전: v1.9 genericAssertions.toBeNull

값이 `null`임을 보장합니다.

**Usage**

```
    const value = null;
    expect(value).toBeNull();

```

---

### toBeTruthy[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-truthy "Direct link to toBeTruthy")

추가된 버전: v1.9 genericAssertions.toBeTruthy

값이 불리언 컨텍스트에서 참(`true`)임을 보장합니다. 즉 `false`, `0`, `''`, `null`, `undefined`, `NaN`을 제외한 모든 값입니다. 특정 값은 중요하지 않을 때 이 메서드를 사용하세요.

**Usage**

```
    const value = { example: 'value' };
    expect(value).toBeTruthy();

```

---

### toBeUndefined[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be-undefined "Direct link to toBeUndefined")

추가된 버전: v1.9 genericAssertions.toBeUndefined

값이 `undefined`임을 보장합니다.

**Usage**

```
    const value = undefined;
    expect(value).toBeUndefined();

```

---

### toContain(expected)[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-1 "Direct link to toContain(expected)")

추가된 버전: v1.9 genericAssertions.toContain(expected)

문자열 값에 예상 부분 문자열이 포함되어 있음을 보장합니다. 비교는 대소문자를 구분합니다.

**Usage**

```
    const value = 'Hello, World';
    expect(value).toContain('World');
    expect(value).toContain(',');

```

**Arguments**

- `expected` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-1-option-expected)

예상 부분 문자열입니다.

---

### toContain(expected)[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-2 "Direct link to toContain(expected)")

추가된 버전: v1.9 genericAssertions.toContain(expected)

값이 `Array` 또는 `Set`이며 예상 항목을 포함함을 보장합니다.

**Usage**

```
    const value = [1, 2, 3];
    expect(value).toContain(2);
    expect(new Set(value)).toContain(2);

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-2-option-expected)

컬렉션 안의 예상 값입니다.

---

### toContainEqual[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-equal "Direct link to toContainEqual")

추가된 버전: v1.9 genericAssertions.toContainEqual

값이 `Array` 또는 `Set`이며 예상 값과 같은 항목을 포함함을 보장합니다.

객체의 경우, [expect(value).toContain()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-2)처럼 참조로 비교하는 대신 모든 필드의 동등성을 재귀적으로 확인합니다.

원시 값의 경우, 이 메서드는 [expect(value).toContain()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-2)과 동일합니다.

**Usage**

```
    const value = [
      { example: 1 },
      { another: 2 },
      { more: 3 },
    ];
    expect(value).toContainEqual({ another: 2 });
    expect(new Set(value)).toContainEqual({ another: 2 });

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-contain-equal-option-expected)

컬렉션 안의 예상 값입니다.

---

### toEqual[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal "Direct link to toEqual")

추가된 버전: v1.9 genericAssertions.toEqual

값의 내용을 [expected](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal-option-expected)의 내용과 비교하며, "deep equality" 검사를 수행합니다.

객체의 경우, [expect(value).toBe()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be)처럼 참조로 비교하는 대신 모든 필드의 동등성을 재귀적으로 확인합니다.

원시 값의 경우, 이 메서드는 [expect(value).toBe()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be)와 동일합니다.

**Usage**

```
    const value = { prop: 1 };
    expect(value).toEqual({ prop: 1 });

```

**Non-strict equality**

[expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal)은 전달된 값과 예상 값의 내용을 비교하는 깊은 동등성 검사를 수행합니다. 두 객체가 동일한 인스턴스를 참조하는지 확인하려면 [expect(value).toBe()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-be)를 대신 사용하세요.

[expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal)은 `undefined` 속성과 배열 항목을 무시하며, 객체 타입의 동일성도 강제하지 않습니다. 더 엄격한 매칭이 필요하면 [expect(value).toStrictEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-strict-equal)을 사용하세요.

**Pattern matching**

[expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal)은 다음 matcher를 사용해 객체, 배열, 원시 타입에 대한 패턴 매칭에도 사용할 수 있습니다.

- [expect(value).any()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-any)
- [expect(value).anything()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-anything)
- [expect(value).arrayContaining()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-containing)
- [expect(value).arrayOf()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-array-of)
- [expect(value).closeTo()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-close-to)
- [expect(value).objectContaining()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-object-containing)
- [expect(value).stringContaining()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-string-containing)
- [expect(value).stringMatching()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-string-matching)

복잡한 객체 내부의 일부 값을 단언하는 예시는 다음과 같습니다:

```
    expect({
      list: [1, 2, 3],
      obj: { prop: 'Hello world!', another: 'some other value' },
      extra: 'extra',
    }).toEqual(expect.objectContaining({
      list: expect.arrayContaining([2, 3]),
      obj: expect.objectContaining({ prop: expect.stringContaining('Hello') }),
    }));

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal-option-expected)

예상 값입니다.

---

### toHaveLength[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-length "Direct link to toHaveLength")

추가된 버전: v1.9 genericAssertions.toHaveLength

값에 `.length` 속성이 있고 그 값이 [expected](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-length-option-expected)와 같음을 보장합니다. 배열과 문자열에 유용합니다.

**Usage**

```
    expect('Hello, World').toHaveLength(12);
    expect([1, 2, 3]).toHaveLength(3);

```

**Arguments**

- `expected` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-length-option-expected)

예상 길이입니다.

---

### toHaveProperty[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-property "Direct link to toHaveProperty")

추가된 버전: v1.9 genericAssertions.toHaveProperty

지정된 `keyPath` 위치의 속성이 객체에 존재함을 보장하고, 선택적으로 해당 속성이 [expected](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-property-option-expected)와 같은지도 확인합니다. 동등성은 [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal)과 유사하게 재귀적으로 확인됩니다.

**Usage**

```
    const value = {
      a: {
        b: [42],
      },
      c: true,
    };
    expect(value).toHaveProperty('a.b');
    expect(value).toHaveProperty('a.b', [42]);
    expect(value).toHaveProperty('a.b[0]', 42);
    expect(value).toHaveProperty('c');
    expect(value).toHaveProperty('c', true);

```

**Arguments**

- `keyPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-property-option-key-path)

속성 경로입니다. 중첩 속성 확인에는 점 표기법 `a.b`를 사용하고, 중첩 배열 항목 확인에는 인덱스 표기법 `a[2]`를 사용하세요.

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-have-property-option-expected)

속성과 비교할 선택적 예상 값입니다.

---

### toMatch[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-match "Direct link to toMatch")

추가된 버전: v1.9 genericAssertions.toMatch

문자열 값이 정규식과 일치함을 보장합니다.

**Usage**

```
    const value = 'Is 42 enough?';
    expect(value).toMatch(/Is \d+ enough/);

```

**Arguments**

- `expected` [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") | [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-match-option-expected)

대조할 정규식입니다.

---

### toMatchObject[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-match-object "Direct link to toMatchObject")

추가된 버전: v1.9 genericAssertions.toMatchObject

값의 내용을 [expected](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-match-object-option-expected)의 내용과 비교하며, "deep equality" 검사를 수행합니다. [expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal)과 달리 값에 추가 속성이 있어도 허용하므로 객체 속성의 일부만 검사할 수 있습니다.

배열을 비교할 때는 항목 수가 같아야 하며, 각 항목은 재귀적으로 검사됩니다.

**Usage**

```
    const value = {
      a: 1,
      b: 2,
      c: true,
    };
    expect(value).toMatchObject({ a: 1, c: true });
    expect(value).toMatchObject({ b: 2, c: true });

    expect([{ a: 1, b: 2 }]).toMatchObject([{ a: 1 }]);

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") | [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-match-object-option-expected)

대조할 예상 객체 값입니다.

---

### toStrictEqual[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-strict-equal "Direct link to toStrictEqual")

추가된 버전: v1.9 genericAssertions.toStrictEqual

값의 내용을 [expected](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-strict-equal-option-expected)의 내용과 **그리고** 타입까지 비교합니다.

[expect(value).toEqual()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-equal)과의 차이점:

- `undefined` 속성을 가진 키를 검사합니다. 예: `{ a: undefined, b: 2 }`는 `{ b: 2 }`와 일치하지 않습니다.
- 배열의 희소성(sparseness)을 검사합니다. 예: `[, 1]`은 `[undefined, 1]`과 일치하지 않습니다.
- 객체 타입의 동일성을 검사합니다. 예: `a`, `b` 필드를 가진 클래스 인스턴스는 `a`, `b` 필드를 가진 리터럴 객체와 같지 않습니다.

**Usage**

```
    const value = { prop: 1 };
    expect(value).toStrictEqual({ prop: 1 });

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-strict-equal-option-expected)

예상 값입니다.

---

### toThrow[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-throw "Direct link to toThrow")

추가된 버전: v1.9 genericAssertions.toThrow

함수를 호출하고 에러를 던지는지 보장합니다.

선택적으로 에러를 [expected](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-throw-option-expected)와 비교합니다. 허용되는 예상 값:

- 정규식 - 에러 메시지가 패턴과 **match**해야 합니다.
- 문자열 - 에러 메시지가 부분 문자열을 **include**해야 합니다.
- Error 객체 - 에러 메시지가 해당 객체의 message 속성과 **equal to**여야 합니다.
- Error 클래스 - 에러 객체가 해당 클래스의 **instance of**여야 합니다.

**Usage**

```
    expect(() => {
      throw new Error('Something bad');
    }).toThrow();

    expect(() => {
      throw new Error('Something bad');
    }).toThrow(/something/);

    expect(() => {
      throw new Error('Something bad');
    }).toThrow(Error);

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-throw-option-expected)

예상 에러 메시지 또는 에러 객체입니다.

---

### toThrowError[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-throw-error "Direct link to toThrowError")

추가된 버전: v1.9 genericAssertions.toThrowError

[expect(value).toThrow()](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-throw)의 별칭입니다.

**Usage**

```
    expect(() => {
      throw new Error('Something bad');
    }).toThrowError();

```

**Arguments**

- `expected` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_[#](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-to-throw-error-option-expected)

예상 에러 메시지 또는 에러 객체입니다.

---

## Properties[​](https://playwright.dev/docs/api/class-genericassertions#properties "Direct link to Properties")

### not[​](https://playwright.dev/docs/api/class-genericassertions#generic-assertions-not "Direct link to not")

추가된 버전: v1.9 genericAssertions.not

반대 조건을 검사하도록 단언을 만듭니다. 예를 들어 다음 코드는 통과합니다:

```
    const value = 1;
    expect(value).not.toBe(2);

```

**Usage**

```
    expect(value).not

```

**Type**

- [GenericAssertions](https://playwright.dev/docs/api/class-genericassertions "GenericAssertions")
