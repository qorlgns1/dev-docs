---
title: "text-align - 타이포그래피 - Tailwind CSS"
description: "요소의 텍스트를 왼쪽 정렬하려면 `text-left` 유틸리티를 사용하세요:"
---

원본 URL: https://tailwindcss.com/docs/text-align

# text-align - 타이포그래피 - Tailwind CSS

| 클래스         | 스타일                 |
| -------------- | ---------------------- |
| `text-left`    | `text-align: left;`    |
| `text-center`  | `text-align: center;`  |
| `text-right`   | `text-align: right;`   |
| `text-justify` | `text-align: justify;` |
| `text-start`   | `text-align: start;`   |
| `text-end`     | `text-align: end;`     |

## 예제

- 텍스트 왼쪽 정렬

요소의 텍스트를 왼쪽 정렬하려면 `text-left` 유틸리티를 사용하세요:

그래서 저는 물속으로 걸어 들어가기 시작했습니다. 솔직히 말하면, 여러분, 저는 겁에 질려 있었습니다. 하지만 계속 나아갔고, 부서지는 파도를 지나가면서 이상할 만큼의 평온함이 밀려왔습니다. 그게 신의 개입이었는지, 아니면 모든 생명체 사이의 유대감이었는지는 모르겠습니다. 하지만 말할 수 있어요, Jerry, 그 순간 저는 _정말_ 해양 생물학자였습니다.

```
    <p class="text-left">So I started to walk into the water...</p>
```

- 텍스트 오른쪽 정렬

요소의 텍스트를 오른쪽 정렬하려면 `text-right` 유틸리티를 사용하세요:

그래서 저는 물속으로 걸어 들어가기 시작했습니다. 솔직히 말하면, 여러분, 저는 겁에 질려 있었습니다. 하지만 계속 나아갔고, 부서지는 파도를 지나가면서 이상할 만큼의 평온함이 밀려왔습니다. 그게 신의 개입이었는지, 아니면 모든 생명체 사이의 유대감이었는지는 모르겠습니다. 하지만 말할 수 있어요, Jerry, 그 순간 저는 _정말_ 해양 생물학자였습니다.

```
    <p class="text-right">So I started to walk into the water...</p>
```

- 텍스트 가운데 정렬

요소의 텍스트를 가운데 정렬하려면 `text-center` 유틸리티를 사용하세요:

그래서 저는 물속으로 걸어 들어가기 시작했습니다. 솔직히 말하면, 여러분, 저는 겁에 질려 있었습니다. 하지만 계속 나아갔고, 부서지는 파도를 지나가면서 이상할 만큼의 평온함이 밀려왔습니다. 그게 신의 개입이었는지, 아니면 모든 생명체 사이의 유대감이었는지는 모르겠습니다. 하지만 말할 수 있어요, Jerry, 그 순간 저는 _정말_ 해양 생물학자였습니다.

```
    <p class="text-center">So I started to walk into the water...</p>
```

- 텍스트 양쪽 정렬

요소의 텍스트를 양쪽 정렬하려면 `text-justify` 유틸리티를 사용하세요:

그래서 저는 물속으로 걸어 들어가기 시작했습니다. 솔직히 말하면, 여러분, 저는 겁에 질려 있었습니다. 하지만 계속 나아갔고, 부서지는 파도를 지나가면서 이상할 만큼의 평온함이 밀려왔습니다. 그게 신의 개입이었는지, 아니면 모든 생명체 사이의 유대감이었는지는 모르겠습니다. 하지만 말할 수 있어요, Jerry, 그 순간 저는 _정말_ 해양 생물학자였습니다.

```
    <p class="text-justify">So I started to walk into the water...</p>
```

- 논리 속성 사용하기

`text-start` 및 `text-end` 유틸리티를 사용하세요. 이 유틸리티는 [논리 속성](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts)을 사용해 텍스트 방향에 따라 왼쪽 또는 오른쪽에 매핑됩니다:

بدأتُ أسير نحو الماء. لن أكذب عليكم يا رفاق، كنتُ مرعوبًا. لكنني واصلتُ المسير، وبينما كنتُ أشق طريقي عبر الأمواج، غمرني هدوءٌ غريب. لا أعلم إن كان ذلك تدخّلًا إلهيًا أم صلة قرابة بين جميع الكائنات الحية، لكنني أقول لك يا جيري، في تلك اللحظة، كنتُ عالم أحياء بحرية.

```
    <div dir="rtl" lang="ar">  <p class="text-end">فبدأت بالسير نحو الماء...</p></div>
```

- 반응형 디자인

중간 화면 크기 이상에서만 유틸리티를 적용하려면 `text-align` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이세요:

```
    <p class="text-left md:text-center ...">  Lorem ipsum dolor sit amet...</p>
```

변형 사용법에 대한 자세한 내용은 [variants 문서](https://tailwindcss.com/docs/hover-focus-and-other-states)를 참고하세요.
