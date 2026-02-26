---
title: "클래스 컴포넌트에서 사용하기"
description: "원본 URL: https://next-auth.js.org/v3/tutorials/usage-with-class-components"
---

원본 URL: https://next-auth.js.org/v3/tutorials/usage-with-class-components

# 클래스 컴포넌트에서 사용하기 | NextAuth.js

버전: v3

클래스 컴포넌트에서 `useSession()` 훅을 사용하려면 고차 컴포넌트(Higher Order Component) 또는 렌더 프로퍼티(render prop)를 통해 사용할 수 있습니다.

## 고차 컴포넌트[​](https://next-auth.js.org/v3/tutorials/usage-with-class-components#higher-order-component "Direct link to heading")

```
    import { useSession } from "next-auth/client"

    const withSession = (Component) => (props) => {
      const [session, loading] = useSession()

      // if the component has a render property, we are good
      if (Component.prototype.render) {
        return <Component session={session} loading={loading} {...props} />
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
        const { session, loading } = this.props
        return null
      }
    }

    const ClassComponentWithSession = withSession(ClassComponent)

```

## 렌더 프로퍼티[​](https://next-auth.js.org/v3/tutorials/usage-with-class-components#render-prop "Direct link to heading")

```
    import { useSession } from "next-auth/client"

    const UseSession = ({ children }) => {
      const [session, loading] = useSession()
      return children({ session, loading })
    }

    // Usage
    class ClassComponent extends React.Component {
      render() {
        return (
            {({ session, loading }) => (
              <pre>{JSON.stringify(session, null, 2)}</pre>
            )}
        )
      }
    }

```
