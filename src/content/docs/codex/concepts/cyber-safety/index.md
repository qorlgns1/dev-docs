---
title: '사이버 안전'
description: '안전 교육 외에도 자동 분류기 기반 모니터는 의심스러운 사이버 활동 신호를 탐지하고 고위험 트래픽을 보다 사이버 역량이 낮은 모델(GPT-5.2)로 우회시킵니다. 이러한 완화 조치의 영향을 받는 트래픽은 매우 적을 것으로 예상되며, 정책과 분류기, 제품 내 알림을 지속...'
---

Source URL: https://developers.openai.com/codex/concepts/cyber-safety

# 사이버 안전

[GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/)은 [준비태세 프레임워크](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)상 고도의 사이버 보안 역량으로 분류된 첫 번째 모델로, 이에 따라 추가적인 보호 장치가 적용됩니다. 이러한 보호 조치에는 자격 증명 탈취와 같은 명백한 악의적 요청을 거절하도록 모델을 훈련하는 작업이 포함됩니다.

안전 교육 외에도 자동 분류기 기반 모니터는 의심스러운 사이버 활동 신호를 탐지하고 고위험 트래픽을 보다 사이버 역량이 낮은 모델(GPT-5.2)로 우회시킵니다. 이러한 완화 조치의 영향을 받는 트래픽은 매우 적을 것으로 예상되며, 정책과 분류기, 제품 내 알림을 지속해서 개선하고 있습니다.

## 목적

최근 몇 달 동안 사이버 보안 과제에서 모델 성능이 상당히 향상되어 개발자와 보안 전문가 모두에게 도움이 되고 있습니다. 취약점 발견과 같은 사이버 보안 관련 과제에서 모델의 역량이 향상됨에 따라, 우리는 합법적 연구를 지원하면서 오용을 지연시키기 위해 보호와 집행을 확대하는 예방적 접근을 취하고 있습니다.

사이버 역량은 본질적으로 이중 사용적입니다. 침투 테스트, 취약점 연구, 대규모 스캐닝, 악성코드 분석, 위협 인텔리전스와 같은 중요한 방어 작업을 뒷받침하는 동일한 지식과 기술이 현실 세계의 피해를 초래할 수도 있습니다.

이러한 역량과 기술은 보안을 개선할 수 있는 맥락에서는 사용할 수 있어야 하며 더 쉽게 사용할 수 있어야 합니다. [Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/) 파일럿은 개인과 조직이 잠재적으로 고위험 사이버 보안 활동을 중단 없이 계속할 수 있게 합니다.

## 작동 방식

사이버 보안 관련 작업이나 자동 감지 시스템이 [오탐지](#false-positives)할 수 있는 유사 활동을 수행하는 개발자와 보안 전문가는 요청이 GPT-5.2로 대체될 수 있습니다. 완화 조치의 영향을 받는 트래픽은 매우 적을 것으로 예상되며, 정책과 분류기를 지속적으로 조정 중입니다.

Codex CLI 최신 알파 버전에는 요청이 우회될 때 제품 내 메시지가 포함되어 있습니다. 이 메시지는 향후 며칠 내에 모든 클라이언트에서 지원될 예정입니다.

완화 조치의 영향을 받은 계정은 아래 [Trusted Access](#trusted-access-for-cyber) 프로그램에 참여함으로써 다시 GPT-5.3-Codex에 접근할 수 있습니다.

Trusted Access 참여가 모두에게 적합하지 않을 수 있음을 알고 있으므로, 이러한 완화 조치를 확대하고 사이버 회복력을 [강화](https://openai.com/index/strengthening-cyber-resilience/)함에 따라 대부분의 경우 계정 수준을 넘어 요청 수준 검사로 전환할 계획입니다.

## 사이버용 신뢰된 접근

현재 일반 제공을 위한 정책과 분류기를 지속해서 조정하는 동안 개발자가 고급 기능을 유지할 수 있도록 “신뢰된 접근”을 파일럿 중입니다. 우리의 목표는 매우 소수의 사용자만 [Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/)에 참여하도록 하는 것입니다.

잠재적으로 고위험 사이버 보안 작업을 위해 모델을 사용하려면:

- 사용자는 [chatgpt.com/cyber](https://chatgpt.com/cyber)에서 본인 확인을 할 수 있습니다.
- 기업은 기본적으로 전체 팀에 대해 OpenAI 담당자를 통해 [trusted access](https://openai.com/form/enterprise-trusted-access-for-cyber/)를 요청할 수 있습니다.

합법적인 방어 작업을 가속화하기 위해 더 사이버 역량이 높거나 허용 범위가 넓은 모델 접근이 필요한 보안 연구자와 팀은 [초대 전용 프로그램](https://docs.google.com/forms/d/e/1FAIpQLSea_ptovrS3xZeZ9FoZFkKtEJFWGxNrZb1c52GW4BVjB2KVNA/viewform?usp=header)에 관심을 표시할 수 있습니다. 신뢰된 접근 권한이 있는 사용자는 여전히 [사용 정책](https://openai.com/policies/usage-policies/)과 [이용 약관](https://openai.com/policies/row-terms-of-use/)을 준수해야 합니다.

## 오탐지

정당하거나 사이버 보안과 무관한 활동도 때때로 플래그될 수 있습니다. 우회가 발생하면 응답한 모델은 API 요청 로그와 CLI 제품 내 알림(곧 모든 인터페이스)에서 확인할 수 있습니다. 오탐지라고 생각되는 우회가 발생하면 `/feedback`을 통해 보고해 주세요.
