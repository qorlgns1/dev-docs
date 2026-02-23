---
title: 'Components: Form'
description: 'The  component extends the HTML  element to provide  client-side navigation on submission, and progressive enhancement.'
---

# Components: Form | Next.js

Source URL: https://nextjs.org/docs/pages/api-reference/components/form

[API Reference](https://nextjs.org/docs/pages/api-reference)[Components](https://nextjs.org/docs/pages/api-reference/components)Form

Copy page

# Form

Last updated February 20, 2026

The `<Form>` component extends the HTML `<form>` element to provide  **client-side navigation** on submission, and **progressive enhancement**.

It's useful for forms that update URL search params as it reduces the boilerplate code needed to achieve the above.

Basic usage:

/ui/search.js

JavaScriptTypeScript
[code]
    import Form from 'next/form'
     
    export default function Page() {
      return (
        <Form action="/search">
          {/* On submission, the input value will be appended to
              the URL, e.g. /search?query=abc */}
          <input name="query" />
          <button type="submit">Submit</button>
        </Form>
      )
    }
[/code]

## Reference[](https://nextjs.org/docs/pages/api-reference/components/form#reference)

The behavior of the `<Form>` component depends on whether the `action` prop is passed a `string` or `function`.

  * When `action` is a **string** , the `<Form>` behaves like a native HTML form that uses a **`GET`** method. The form data is encoded into the URL as search params, and when the form is submitted, it navigates to the specified URL. In addition, Next.js:
    * Performs a [client-side navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) instead of a full page reload when the form is submitted. This retains shared UI and client-side state.



### `action` (string) Props[](https://nextjs.org/docs/pages/api-reference/components/form#action-string-props)

When `action` is a string, the `<Form>` component supports the following props:

Prop| Example| Type| Required  
---|---|---|---  
`action`| `action="/search"`| `string` (URL or relative path)| Yes  
`replace`| `replace={false}`| `boolean`| -  
`scroll`| `scroll={true}`| `boolean`| -  
  
  * **`action`** : The URL or path to navigate to when the form is submitted.
    * An empty string `""` will navigate to the same route with updated search params.
  * **`replace`** : Replaces the current history state instead of pushing a new one to the [browser's history](https://developer.mozilla.org/en-US/docs/Web/API/History_API) stack. Default is `false`.
  * **`scroll`** : Controls the scroll behavior during navigation. Defaults to `true`, this means it will scroll to the top of the new route, and maintain the scroll position for backwards and forwards navigation.



### Caveats[](https://nextjs.org/docs/pages/api-reference/components/form#caveats)

  * **`onSubmit`** : Can be used to handle form submission logic. However, calling `event.preventDefault()` will override `<Form>` behavior such as navigating to the specified URL.
  * **[`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method), [`encType`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#enctype), [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#target)**: Are not supported as they override `<Form>` behavior.
    * Similarly, `formMethod`, `formEncType`, and `formTarget` can be used to override the `method`, `encType`, and `target` props respectively, and using them will fallback to native browser behavior.
    * If you need to use these props, use the HTML `<form>` element instead.
  * **`<input type="file">`**: Using this input type when the `action` is a string will match browser behavior by submitting the filename instead of the file object.



Was this helpful?

supported.

Send
