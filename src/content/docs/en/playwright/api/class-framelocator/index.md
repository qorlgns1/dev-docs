---
title: "FrameLocator"
description: "FrameLocator represents a view to the  on the page. It captures the logic sufficient to retrieve the  and locate elements in that iframe. FrameLocator..."
---

Source URL: https://playwright.dev/docs/api/class-framelocator

# FrameLocator | Playwright

FrameLocator represents a view to the `iframe` on the page. It captures the logic sufficient to retrieve the `iframe` and locate elements in that iframe. FrameLocator can be created with either [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame), [page.frameLocator()](https://playwright.dev/docs/api/class-page#page-frame-locator) or [locator.frameLocator()](https://playwright.dev/docs/api/class-locator#locator-frame-locator) method.

```
    const locator = page.locator('#my-frame').contentFrame().getByText('Submit');
    await locator.click();

```

**Strictness**

Frame locators are strict. This means that all operations on frame locators will throw if more than one element matches a given selector.

```
    // Throws if there are several frames in DOM:
    await page.locator('.result-frame').contentFrame().getByRole('button').click();

    // Works because we explicitly tell locator to pick the first frame:
    await page.locator('.result-frame').contentFrame().first().getByRole('button').click();

```

**Converting Locator to FrameLocator**

If you have a [Locator](https://playwright.dev/docs/api/class-locator "Locator") object pointing to an `iframe` it can be converted to [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator") using [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame).

**Converting FrameLocator to Locator**

If you have a [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator") object it can be converted to [Locator](https://playwright.dev/docs/api/class-locator "Locator") pointing to the same `iframe` using [frameLocator.owner()](https://playwright.dev/docs/api/class-framelocator#frame-locator-owner).

---

## Methods[​](https://playwright.dev/docs/api/class-framelocator#methods "Direct link to Methods")

### frameLocator[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-frame-locator "Direct link to frameLocator")

Added in: v1.17 frameLocator.frameLocator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements in that iframe.

**Usage**

```
    frameLocator.frameLocator(selector);

```

**Arguments**

- `selector` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-frame-locator-option-selector)

A selector to use when resolving DOM element.

**Returns**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-frame-locator-return)

---

### getByAltText[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-alt-text "Direct link to getByAltText")

Added in: v1.27 frameLocator.getByAltText

Allows locating elements by their alt text.

**Usage**

For example, this method will find the image by alt text "Playwright logo":

```
    <img alt='Playwright logo'>

```

```
    await page.getByAltText('Playwright logo').click();

```

**Arguments**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-alt-text-option-text)

Text to locate the element for.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-alt-text-option-exact)

Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-alt-text-return)

---

### getByLabel[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-label "Direct link to getByLabel")

Added in: v1.27 frameLocator.getByLabel

Allows locating input elements by the text of the associated `<label>` or `aria-labelledby` element, or by the `aria-label` attribute.

**Usage**

For example, this method will find inputs by label "Username" and "Password" in the following DOM:

```
    <input aria-label="Username">
    <label for="password-input">Password:</label>
    <input id="password-input">

```

```
    await page.getByLabel('Username').fill('john');
    await page.getByLabel('Password').fill('secret');

```

**Arguments**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-label-option-text)

Text to locate the element for.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-label-option-exact)

Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-label-return)

---

### getByPlaceholder[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-placeholder "Direct link to getByPlaceholder")

Added in: v1.27 frameLocator.getByPlaceholder

Allows locating input elements by the placeholder text.

**Usage**

For example, consider the following DOM structure.

```
    <input type="email" placeholder="name@example.com" />

```

You can fill the input after locating it by the placeholder text:

```
    await page
        .getByPlaceholder('name@example.com')
        .fill('playwright@microsoft.com');

```

**Arguments**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-placeholder-option-text)

Text to locate the element for.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-placeholder-option-exact)

Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-placeholder-return)

---

### getByRole[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role "Direct link to getByRole")

Added in: v1.27 frameLocator.getByRole

Allows locating elements by their [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles), [ARIA attributes](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes) and [accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

Consider the following DOM structure.

```
    <h3>Sign up</h3>
    <label>
      <input type="checkbox" /> Subscribe
    </label>
    <button>Submit</button>

```

You can locate each element by it's implicit role:

```
    await expect(page.getByRole('heading', { name: 'Sign up' })).toBeVisible();

    await page.getByRole('checkbox', { name: 'Subscribe' }).check();

    await page.getByRole('button', { name: /submit/i }).click();

```

**Arguments**

- `role` "alert" | "alertdialog" | "application" | "article" | "banner" | "blockquote" | "button" | "caption" | "cell" | "checkbox" | "code" | "columnheader" | "combobox" | "complementary" | "contentinfo" | "definition" | "deletion" | "dialog" | "directory" | "document" | "emphasis" | "feed" | "figure" | "form" | "generic" | "grid" | "gridcell" | "group" | "heading" | "img" | "insertion" | "link" | "list" | "listbox" | "listitem" | "log" | "main" | "marquee" | "math" | "meter" | "menu" | "menubar" | "menuitem" | "menuitemcheckbox" | "menuitemradio" | "navigation" | "none" | "note" | "option" | "paragraph" | "presentation" | "progressbar" | "radio" | "radiogroup" | "region" | "row" | "rowgroup" | "rowheader" | "scrollbar" | "search" | "searchbox" | "separator" | "slider" | "spinbutton" | "status" | "strong" | "subscript" | "superscript" | "switch" | "tab" | "table" | "tablist" | "tabpanel" | "term" | "textbox" | "time" | "timer" | "toolbar" | "tooltip" | "tree" | "treegrid" | "treeitem"[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-role)

Required aria role.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `checked` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-checked)

An attribute that is usually set by `aria-checked` or native `<input type=checkbox>` controls.

Learn more about [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked).

    * `disabled` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-disabled)

An attribute that is usually set by `aria-disabled` or `disabled`.

note

Unlike most other attributes, `disabled` is inherited through the DOM hierarchy. Learn more about [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled).

    * `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_ Added in: v1.28[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-exact)

Whether [name](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-name) is matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when [name](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-name) is a regular expression. Note that exact match still trims whitespace.

    * `expanded` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-expanded)

An attribute that is usually set by `aria-expanded`.

Learn more about [`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded).

    * `includeHidden` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-include-hidden)

Option that controls whether hidden elements are matched. By default, only non-hidden elements, as [defined by ARIA](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion), are matched by role selector.

Learn more about [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden).

    * `level` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-level)

A number attribute that is usually present for roles `heading`, `listitem`, `row`, `treeitem`, with default values for `<h1>-<h6>` elements.

Learn more about [`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level).

    * `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-name)

Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use [exact](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-exact) to control this behavior.

Learn more about [accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

    * `pressed` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-pressed)

An attribute that is usually set by `aria-pressed`.

Learn more about [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed).

    * `selected` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-option-selected)

An attribute that is usually set by `aria-selected`.

Learn more about [`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected).

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-role-return)

**Details**

Role selector **does not replace** accessibility audits and conformance tests, but rather gives early feedback about the ARIA guidelines.

Many html elements have an implicitly [defined role](https://w3c.github.io/html-aam/#html-element-role-mappings) that is recognized by the role selector. You can find all the [supported roles here](https://www.w3.org/TR/wai-aria-1.2/#role_definitions). ARIA guidelines **do not recommend** duplicating implicit roles and attributes by setting `role` and/or `aria-*` attributes to default values.

---

### getByTestId[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-test-id "Direct link to getByTestId")

Added in: v1.27 frameLocator.getByTestId

Locate element by the test id.

**Usage**

Consider the following DOM structure.

```
    <button data-testid="directions">Itinéraire</button>

```

You can locate the element by it's test id:

```
    await page.getByTestId('directions').click();

```

**Arguments**

- `testId` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-test-id-option-test-id)

Id to locate the element by.

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-test-id-return)

**Details**

By default, the `data-testid` attribute is used as a test id. Use [selectors.setTestIdAttribute()](https://playwright.dev/docs/api/class-selectors#selectors-set-test-id-attribute) to configure a different test id attribute if necessary.

```
    // Set custom test id attribute from @playwright/test config:
    import { defineConfig } from '@playwright/test';

    export default defineConfig({
      use: {
        testIdAttribute: 'data-pw'
      },
    });

```

---

### getByText[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-text "Direct link to getByText")

Added in: v1.27 frameLocator.getByText

Allows locating elements that contain given text.

See also [locator.filter()](https://playwright.dev/docs/api/class-locator#locator-filter) that allows to match by another criteria, like an accessible role, and then filter by the text content.

**Usage**

Consider the following DOM structure:

```
    <div>Hello <span>world</span></div>
    <div>Hello</div>

```

You can locate by text substring, exact string, or a regular expression:

```
    // Matches <span>
    page.getByText('world');

    // Matches first <div>
    page.getByText('Hello world');

    // Matches second <div>
    page.getByText('Hello', { exact: true });

    // Matches both <div>s
    page.getByText(/Hello/);

    // Matches second <div>
    page.getByText(/^hello$/i);

```

**Arguments**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-text-option-text)

Text to locate the element for.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-text-option-exact)

Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-text-return)

**Details**

Matching by text always normalizes whitespace, even with exact match. For example, it turns multiple spaces into one, turns line breaks into spaces and ignores leading and trailing whitespace.

Input elements of the type `button` and `submit` are matched by their `value` instead of the text content. For example, locating by text `"Log in"` matches `<input type=button value="Log in">`.

---

### getByTitle[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-title "Direct link to getByTitle")

Added in: v1.27 frameLocator.getByTitle

Allows locating elements by their title attribute.

**Usage**

Consider the following DOM structure.

```
    <span title='Issues count'>25 issues</span>

```

You can check the issues count after locating it by the title text:

```
    await expect(page.getByTitle('Issues count')).toHaveText('25 issues');

```

**Arguments**

- `text` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-title-option-text)

Text to locate the element for.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `exact` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-title-option-exact)

Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-get-by-title-return)

---

### locator[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator "Direct link to locator")

Added in: v1.17 frameLocator.locator

The method finds an element matching the specified selector in the locator's subtree. It also accepts filter options, similar to [locator.filter()](https://playwright.dev/docs/api/class-locator#locator-filter) method.

[Learn more about locators](https://playwright.dev/docs/locators).

**Usage**

```
    frameLocator.locator(selectorOrLocator);
    frameLocator.locator(selectorOrLocator, options);

```

**Arguments**

- `selectorOrLocator` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-selector-or-locator)

A selector or locator to use when resolving DOM element.

- `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") _(optional)_
  - `has` [Locator](https://playwright.dev/docs/api/class-locator "Locator") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-has)

Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.

Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.

Note that outer and inner locators must belong to the same frame. Inner locator must not contain [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")s.

    * `hasNot` [Locator](https://playwright.dev/docs/api/class-locator "Locator") _(optional)_ Added in: v1.33[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-has-not)

Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.

Note that outer and inner locators must belong to the same frame. Inner locator must not contain [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")s.

    * `hasNotText` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_ Added in: v1.33[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-has-not-text)

Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), matching is case-insensitive and searches for a substring.

    * `hasText` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp "RegExp") _(optional)_[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-option-has-text)

Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`.

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-locator-return)

---

### owner[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-owner "Direct link to owner")

Added in: v1.43 frameLocator.owner

Returns a [Locator](https://playwright.dev/docs/api/class-locator "Locator") object pointing to the same `iframe` as this frame locator.

Useful when you have a [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator") object obtained somewhere, and later on would like to interact with the `iframe` element.

For a reverse operation, use [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame).

**Usage**

```
    const frameLocator = page.locator('iframe[name="embedded"]').contentFrame();
    // ...
    const locator = frameLocator.owner();
    await expect(locator).toBeVisible();

```

**Returns**

- [Locator](https://playwright.dev/docs/api/class-locator "Locator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-owner-return)

---

## Deprecated[​](https://playwright.dev/docs/api/class-framelocator#deprecated "Direct link to Deprecated")

### first[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-first "Direct link to first")

Added in: v1.17 frameLocator.first

Deprecated

Use [locator.first()](https://playwright.dev/docs/api/class-locator#locator-first) followed by [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame) instead.

Returns locator to the first matching frame.

**Usage**

```
    frameLocator.first();

```

**Returns**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-first-return)

---

### last[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-last "Direct link to last")

Added in: v1.17 frameLocator.last

Deprecated

Use [locator.last()](https://playwright.dev/docs/api/class-locator#locator-last) followed by [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame) instead.

Returns locator to the last matching frame.

**Usage**

```
    frameLocator.last();

```

**Returns**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-last-return)

---

### nth[​](https://playwright.dev/docs/api/class-framelocator#frame-locator-nth "Direct link to nth")

Added in: v1.17 frameLocator.nth

Deprecated

Use [locator.nth()](https://playwright.dev/docs/api/class-locator#locator-nth) followed by [locator.contentFrame()](https://playwright.dev/docs/api/class-locator#locator-content-frame) instead.

Returns locator to the n-th matching frame. It's zero based, `nth(0)` selects the first frame.

**Usage**

```
    frameLocator.nth(index);

```

**Arguments**

- `index` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-nth-option-index)

**Returns**

- [FrameLocator](https://playwright.dev/docs/api/class-framelocator "FrameLocator")[#](https://playwright.dev/docs/api/class-framelocator#frame-locator-nth-return)
