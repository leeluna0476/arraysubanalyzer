# 목표
> 아래 Clang Static Analyzer의 기능들을 일부 구현한다.

- [core.uninitialized.ArraySubscript (C)](https://clang.llvm.org/docs/analyzer/checkers.html#core-uninitialized-arraysubscript-c)
- [security.ArrayBound (C, C++)](https://clang.llvm.org/docs/analyzer/checkers.html#security-arraybound-c-c)
- [optin.taint.GenericTaint (C, C++)](https://clang.llvm.org/docs/analyzer/checkers.html#optin-taint-generictaint-c-c)

# gantt chart
| 기능 | 4월 5주 | 5월 1주 | 5월 2주 | 5월 3주 | 5월 4주 | 6월 1주 | 6월 2주 | 6월 3주 | 6월 4주 | 7월 1주 | 7월 2주 | 7월 3주 | 7월 4주 | 7월 5주 | 8월 1주 | 8월 2주 | 8월 3주 | 8월 4주 | 9월 1주 | 9월 2주 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AST 생성 | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 변수 상태 추적 구현 | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| uninitialized 판별 구현 | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| array subscript 검사 구현 | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| warning 출력 구현 |  | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 배열 크기 추적 구현 |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 상수 index overflow 검사 구현 |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 변수 index range 분석 구현 |  |  |  | ■ | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 조건문 기반 bounds 판단 구현 |  |  |  |  | ■ | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| static array bounds 테스트 |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| pointer base 추적 구현 |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |
| pointer offset 추적 구현 |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |
| pointer dereference 검사 구현 |  |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |  |
| pointer bounds 검사 구현 |  |  |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |
| pointer checker 테스트 |  |  |  |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |  |
| taint source 정의 구현 |  |  |  |  |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |
| taint propagation 구현 |  |  |  |  |  |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |
| taint sink 검사 구현 |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |
| taint warning 정리 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |
| LLM prompt 설계    |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ |  |  |  |
| warning → prompt 변환 구현 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ |  |  |  |
| LLM API 연동 구현 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ |  |  |
| 결과 formatting 및 리포트 생성 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ |  |
| 통합 테스트 및 리팩토링 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ |

# 비고
- pointer bound check는 `base + constant offset` 형태만 검사한다.
  - `p++`, `p + n`까지 추적하지 않는다.
- taint source: `scanf`, `gets`
  - `scanf("%s")`는 무조건 금지. `scanf("%Ns")` 형태만 허용.
