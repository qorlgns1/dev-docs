---
title: "Handles"
description: "Playwright can create handles to the page DOM elements or any other objects inside the page. These handles live in the Playwright process, whereas the..."
---

Source URL: https://playwright.dev/docs/handles

# Handles | Playwright

## Introduction[​](https://playwright.dev/docs/handles#introduction "Direct link to Introduction")

Playwright can create handles to the page DOM elements or any other objects inside the page. These handles live in the Playwright process, whereas the actual objects live in the browser. There are two types of handles:

- [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle") to reference any JavaScript objects in the page
- [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") to reference DOM elements in the page, it has extra methods that allow performing actions on the elements and asserting their properties.

Since any DOM element in the page is also a JavaScript object, any [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") is a [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle") as well.

Handles are used to perform operations on those actual objects in the page. You can evaluate on a handle, get handle properties, pass handle as an evaluation parameter, serialize page object into JSON etc. See the [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle") class API for these and methods.

### API reference[​](https://playwright.dev/docs/handles#api-reference "Direct link to API reference")

- [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")
- [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")

Here is the easiest way to obtain a [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle").

```
    const jsHandle = await page.evaluateHandle('window');
    //  Use jsHandle for evaluations.

```

## Element Handles[​](https://playwright.dev/docs/handles#element-handles "Direct link to Element Handles")

Discouraged

The use of [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") is discouraged, use [Locator](https://playwright.dev/docs/api/class-locator "Locator") objects and web-first assertions instead.

When [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") is required, it is recommended to fetch it with the [page.waitForSelector()](https://playwright.dev/docs/api/class-page#page-wait-for-selector) or [frame.waitForSelector()](https://playwright.dev/docs/api/class-frame#frame-wait-for-selector) methods. These APIs wait for the element to be attached and visible.

```
    // Get the element handle
    const elementHandle = page.waitForSelector('#box');

    // Assert bounding box for the element
    const boundingBox = await elementHandle.boundingBox();
    expect(boundingBox.width).toBe(100);

    // Assert attribute for the element
    const classNames = await elementHandle.getAttribute('class');
    expect(classNames.includes('highlighted')).toBeTruthy();

```

## Handles as parameters[​](https://playwright.dev/docs/handles#handles-as-parameters "Direct link to Handles as parameters")

Handles can be passed into the [page.evaluate()](https://playwright.dev/docs/api/class-page#page-evaluate) and similar methods. The following snippet creates a new array in the page, initializes it with data and returns a handle to this array into Playwright. It then uses the handle in subsequent evaluations:

```
    // Create new array in page.
    const myArrayHandle = await page.evaluateHandle(() => {
      window.myArray = [1];
      return myArray;
    });

    // Get the length of the array.
    const length = await page.evaluate(a => a.length, myArrayHandle);

    // Add one more element to the array using the handle
    await page.evaluate(arg => arg.myArray.push(arg.newElement), {
      myArray: myArrayHandle,
      newElement: 2
    });

    // Release the object when it's no longer needed.
    await myArrayHandle.dispose();

```

## Handle Lifecycle[​](https://playwright.dev/docs/handles#handle-lifecycle "Direct link to Handle Lifecycle")

Handles can be acquired using the page methods such as [page.evaluateHandle()](https://playwright.dev/docs/api/class-page#page-evaluate-handle), [page.$()](https://playwright.dev/docs/api/class-page#page-query-selector) or [page.$$()](https://playwright.dev/docs/api/class-page#page-query-selector-all) or their frame counterparts [frame.evaluateHandle()](https://playwright.dev/docs/api/class-frame#frame-evaluate-handle), [frame.$()](https://playwright.dev/docs/api/class-frame#frame-query-selector) or [frame.$$()](https://playwright.dev/docs/api/class-frame#frame-query-selector-all). Once created, handles will retain object from [garbage collection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management) unless page navigates or the handle is manually disposed via the [jsHandle.dispose()](https://playwright.dev/docs/api/class-jshandle#js-handle-dispose) method.

### API reference[​](https://playwright.dev/docs/handles#api-reference-1 "Direct link to API reference")

- [JSHandle](https://playwright.dev/docs/api/class-jshandle "JSHandle")
- [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle")
- [elementHandle.boundingBox()](https://playwright.dev/docs/api/class-elementhandle#element-handle-bounding-box)
- [elementHandle.getAttribute()](https://playwright.dev/docs/api/class-elementhandle#element-handle-get-attribute)
- [elementHandle.innerText()](https://playwright.dev/docs/api/class-elementhandle#element-handle-inner-text)
- [elementHandle.innerHTML()](https://playwright.dev/docs/api/class-elementhandle#element-handle-inner-html)
- [elementHandle.textContent()](https://playwright.dev/docs/api/class-elementhandle#element-handle-text-content)
- [jsHandle.evaluate()](https://playwright.dev/docs/api/class-jshandle#js-handle-evaluate)
- [page.evaluateHandle()](https://playwright.dev/docs/api/class-page#page-evaluate-handle)
- [page.$()](https://playwright.dev/docs/api/class-page#page-query-selector)
- [page.$$()](https://playwright.dev/docs/api/class-page#page-query-selector-all)

## Locator vs ElementHandle[​](https://playwright.dev/docs/handles#locator-vs-elementhandle "Direct link to Locator vs ElementHandle")

caution

We only recommend using [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") in the rare cases when you need to perform extensive DOM traversal on a static page. For all user actions and assertions use locator instead.

The difference between the [Locator](https://playwright.dev/docs/api/class-locator "Locator") and [ElementHandle](https://playwright.dev/docs/api/class-elementhandle "ElementHandle") is that the latter points to a particular element, while Locator captures the logic of how to retrieve that element.

In the example below, handle points to a particular DOM element on page. If that element changes text or is used by React to render an entirely different component, handle is still pointing to that very stale DOM element. This can lead to unexpected behaviors.

```
    const handle = await page.$('text=Submit');
    // ...
    await handle.hover();
    await handle.click();

```

With the locator, every time the locator is used, up-to-date DOM element is located in the page using the selector. So in the snippet below, underlying DOM element is going to be located twice.

```
    const locator = page.getByText('Submit');
    // ...
    await locator.hover();
    await locator.click();

```
