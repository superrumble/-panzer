## 요약
CAN 통신은 차량용 전자제어장치(ECU) 간 실시간 메시지 교환을 가능케 하는 견고한 버스 프로토콜이며 (csselectronics.com), 산업용·자동차용 네트워크의 표준으로 널리 사용됩니다 (데이터 수집 및 측정 솔루션).  
이 프로젝트를 위해서는 크게 다음 네 가지 영역에서 학습이 필요합니다:
1. CAN 버스 및 차량용 네트워크
2. 임베디드 시스템·RTOS·AUTOSAR
3. GIS·지도 UI 설계
4. 프로그래밍 언어·프레임워크

## 1. CAN 통신 개요
### 1.1 CAN 통신이란?
CAN(Controller Area Network)은 차량·산업용 장비 내 여러 ECU를 병렬로 연결하여 메시지를 주고받는 통신 시스템입니다 (csselectronics.com).  
메시지(프레임)를 버스 상에 브로드캐스트 방식으로 전송하며, 각 노드는 필요한 메시지를 필터링해 수신합니다 (데이터 수집 및 측정 솔루션).

### 1.2 주요 특징 및 프로토콜 구성
- **표준화**: ISO 11898 표준에 정의되어 있으며, 물리계층·데이터링크 계층을 규정 (csselectronics.com)  
- **비호스트 방식**: 중앙 제어 컴퓨터 없이도 노드 간 통신이 가능 (데이터 수집 및 측정 솔루션)  
- **오류 검출 및 우선순위**: CRC, ACK, 에러 프레임, 메시지 ID 기반 우선순위 기능 제공 (csselectronics.com)

## 2. 필수 지식 영역
### 2.1 임베디드 시스템 및 차량용 네트워크
- **마이크로컨트롤러 & 트랜시버**: CAN 컨트롤러 내장 MCU 및 외부 CAN 트랜시버 설계·구성법 (ccontrols.com)  
- **실시간 운영체제(RTOS)**: 차량용 제어 루프 제어를 위해 최소 지연·결정적 동작 보장 (blackberry.qnx.com / Aptiv)  
- **AUTOSAR**: ECU 소프트웨어 아키텍처 표준, Classic·Adaptive 플랫폼 이해 (vector.com / sbdautomotive.com)

### 2.2 GIS 및 지도 UI 개발
- **GIS 기본**: 좌표계·지도 투영·공간 분석 개념 습득(벡터·래스터 데이터) (Reddit)  
- **지도 UI 패턴**: 확대·축소, 레이어 관리, 사용자 인터랙션 패턴 참고 (아마존)

### 2.3 프로그래밍 언어 및 프레임워크
- **C/C++ & Qt**: 크로스플랫폼 GUI, Google Maps 등 외부 맵 서비스 연동 (아마존)  
- **C# WPF**:  
  - SharpMap, DotSpatial, MapWinGIS 같은 오픈소스 GIS 라이브러리 활용 (LinkedIn / mapwindow.org)  
  - BruTile 등을 이용한 타일 서비스(OpenStreetMap, Bing) 연동 (NuGet Gallery)  
- **Web(선택)**: Leaflet, OpenLayers, Mapbox GL JS 등 웹 맵 프레임워크 (추가 학습 권장)

## 3. 추천 학습 자료 및 도서
### CAN 통신
- **A Comprehensible Guide to Controller Area Network** by Wilfried Voss  
- **Understanding and Using the Controller Area Network** (Springer)  
- **CAN Application Programming Interface** (Renesas Application Note)

### 임베디드·RTOS·AUTOSAR
- **AUTOSAR Fundamentals and Applications**  
- **온라인 리소스**: AUTOSAR 공식 문서 (autosar.org), QNX / FreeRTOS / VxWorks RTOS 개념 자료

### GIS·지도 UI
- **GIS Fundamentals: A First Text on Geographic Information Systems** by Paul Bolstad  
- **Designing Map Interfaces: Patterns for Building Effective Map Apps**

### GUI 프로그래밍
- **Qt 6 C++ GUI Programming Cookbook**  
- **C# WPF 및 .NET GIS 라이브러리 튜토리얼** (SharpMap 공식 GitHub, DotSpatial, MapWinGIS 튜토리얼 문서)

---

위 목록을 바탕으로 순차적으로 학습하면, **CAN 버스 → 임베디드/RTOS/AUTOSAR → GIS 이론 → 지도 UI 개발 → 프로그래밍 프레임워크 실습** 순으로 지식을 쌓아나갈 수 있습니다. 프로젝트 요구사항에 따라 실제 하드웨어(ECU, 트랜시버)와 맵 서비스(API(예: OpenStreetMap, Google Maps))를 연동하며 실습하시길 권장드립니다.
