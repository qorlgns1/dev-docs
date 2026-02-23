---
title: 사이버 안전
description: "출처 URL: https://developers.openai.com/codex/concepts/cyber-safety"
---

# 사이버 안전

출처 URL: https://developers.openai.com/codex/concepts/cyber-safety

[GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/)는 우리의 [Preparedness Framework](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) 기준으로 고급 사이버보안 역량을 가진 첫 번째 모델로 분류되며, 이에 따라 추가적인 안전장치가 필요합니다. 이러한 안전장치에는 자격 증명 탈취와 같이 명백히 악의적인 요청을 거부하도록 모델을 훈련하는 과정이 포함됩니다.

안전 훈련 외에도 자동화된 분류기 기반 모니터가 의심스러운 사이버 활동 신호를 감지하고, 위험도가 높은 트래픽을 더 낮은 사이버 역량의 모델(GPT-5.2)로 라우팅합니다. 우리는 이러한 완화 조치로 영향을 받는 트래픽이 극히 적을 것으로 예상하며, 정책·분류기·제품 내 알림을 계속 개선하고 있습니다.

## 우리가 이렇게 하는 이유

최근 몇 달 동안 사이버보안 작업에서 모델 성능이 의미 있게 향상되어 개발자와 보안 전문가 모두에게 도움이 되었습니다. 모델이 취약점 발견과 같은 사이버보안 관련 작업에서 더 나은 성능을 보임에 따라, 우리는 오용을 늦추면서 합법적인 연구를 지원하기 위해 보호와 집행을 확대하는 예방적 접근을 취하고 있습니다.

사이버 역량은 본질적으로 이중 용도입니다. 침투 테스트, 취약점 연구, 대규모 스캐닝, 악성코드 분석, 위협 인텔리전스와 같은 중요한 방어 작업을 뒷받침하는 지식과 기술은 실제 피해를 야기하는 데에도 사용될 수 있습니다.

이러한 역량과 기술은 보안을 향상할 수 있는 맥락에서 제공되고 활용이 쉬워야 합니다. 우리의 [Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/) 파일럿은 개인과 조직이 잠재적으로 고위험 사이버보안 활동을 지속적으로 수행할 수 있도록 지원합니다.

## 작동 방식

사이버보안 관련 작업이나 자동 탐지 시스템이 [오탐지](https://developers.openai.com/codex/concepts/cyber-safety#false-positives)할 수 있는 유사 활동을 수행하는 개발자와 보안 전문가는 요청이 GPT-5.2로 재라우팅될 수 있습니다. 우리는 완화 조치로 영향을 받는 트래픽이 매우 적을 것으로 예상하며, 정책과 분류기를 정교하게 조정하고 있습니다.

Codex CLI의 최신 알파 버전은 요청이 재라우팅될 때 제품 내 메시지를 제공합니다. 향후 며칠 내에 모든 클라이언트에서 이 메시지가 지원될 예정입니다.

완화 조치의 영향을 받은 계정은 아래의 [Trusted Access](https://developers.openai.com/codex/concepts/cyber-safety#trusted-access-for-cyber) 프로그램에 참여하면 GPT-5.3-Codex 사용 권한을 회복할 수 있습니다.

Trusted Access 가입이 모든 사용자에게 적합하지 않을 수 있음을 인지하고 있으며, 이러한 완화 조치를 확장하고 사이버 회복력을 [강화](https://openai.com/index/strengthening-cyber-resilience/)함에 따라 대부분의 경우 계정 단위 안전 점검에서 요청 단위 점검으로 전환할 계획입니다.

## 사이버를 위한 Trusted Access

우리는 정책과 분류기를 일반 공급에 맞춰 조정하는 동안 개발자가 고급 역량을 유지할 수 있도록 “trusted access”를 시범 운영 중입니다. 우리의 목표는 [Trusted Access for Cyber](https://openai.com/index/trusted-access-for-cyber/)에 참여해야 하는 사용자를 가능한 한 최소로 유지하는 것입니다.

잠재적으로 고위험 사이버보안 작업에 모델을 사용하려면:

  * 사용자는 [chatgpt.com/cyber](https://chatgpt.com/cyber)에서 신원을 확인할 수 있습니다.
  * 엔터프라이즈는 OpenAI 담당자를 통해 전체 팀에 대해 기본적으로 [trusted access](https://openai.com/form/enterprise-trusted-access-for-cyber/)를 요청할 수 있습니다.

보안 연구자나 팀이 합법적인 방어 업무를 가속하기 위해 더 강력한 사이버 역량이나 완화된 제한을 가진 모델에 접근해야 하는 경우, [초대 전용 프로그램](https://docs.google.com/forms/d/e/1FAIpQLSea_ptovrS3xZeZ9FoZFkKtEJFWGxNrZb1c52GW4BVjB2KVNA/viewform?usp=header)에 관심을 등록할 수 있습니다. 신뢰받는 접근 권한을 가진 사용자도 여전히 [사용 정책](https://openai.com/policies/usage-policies/)과 [이용 약관](https://openai.com/policies/row-terms-of-use/)을 준수해야 합니다.

## False positives

합법적이거나 비(非)사이버보안 활동이 때때로 플래그될 수 있습니다. 재라우팅이 발생하면, 응답하는 모델이 API 요청 로그와 CLI 내 제품 공지에서 확인되며 곧 모든 인터페이스에서 표시됩니다. 잘못되었다고 판단되는 재라우팅을 겪고 있다면, `/feedback`을 통해 false positive로 보고해주세요.
