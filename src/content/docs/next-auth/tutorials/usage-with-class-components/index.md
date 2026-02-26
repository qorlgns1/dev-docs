---
title: "클래스 컴포넌트에서 사용하기"
description: "클래스 컴포넌트에서  훅을 사용하려면, 고차 컴포넌트(higher order component) 또는 render prop의 도움을 받아 사용할 수 있습니다."
---

Source URL: https://next-auth.js.org/tutorials/usage-with-class-components

# 클래스 컴포넌트에서 사용하기 | NextAuth.js

버전: v4

클래스 컴포넌트에서 `useSession()` 훅을 사용하려면, 고차 컴포넌트(higher order component) 또는 render prop의 도움을 받아 사용할 수 있습니다.

## 고차 컴포넌트[​](https://next-auth.js.org/tutorials/usage-with-class-components#higher-order-component "Direct link to heading")

```
    import { useSession } from "next-auth/react"

    const withSession = (Component) => (props) => {
      const session = useSession()

      // if the component has a render property, we are good
      if (Component.prototype.render) {
        return <Component session={session} {...props} />
      }

      // if the passed component is a function component, there is no need for this wrapper
      throw new Error(
        [
          "You passed a function component, `withSession` is not needed.",
          "You can `useSession` directly in your component.",
        ].join("\n")
      )
    }

    // Usage
    class ClassComponent extends React.Component {
      render() {
        const { data: session, status } = this.props.session
        return null
      }
    }

    const ClassComponentWithSession = withSession(ClassComponent)

```

## Render Prop[​](https://next-auth.js.org/tutorials/usage-with-class-components#render-prop "Direct link to heading")

```
    import { useSession } from "next-auth/react"

    const UseSession = ({ children }) => {
      const session = useSession()
      return children(session)
    }

    // Usage
    class ClassComponent extends React.Component {
      render() {
        return (
            {(session) => <pre>{JSON.stringify(session, null, 2)}</pre>}
        )
      }
    }

```
