# README

[TOC]

---



## 1. Service Overview

**YoungDucklings**

어린 오리들이 어미 오리나 각인된 대상을 졸졸 따라다니는 모양에서 아이디어를 얻어, 사용자들이 영화인 기반으로 영화콘텐츠를 탐색하거나 추천을 받을 수 있는 서비스를 기획했다.

- dashboard

  서비스 내에서 이루어지는 사용자의 활동들은 사용자 상세 페이지에서 영화인을 중심으로 시각화된 그래프로 제공된다. 그래프는 사용자가 좋아하는 영화인과 그들이 출연한 영화들, 출연한 영화에 나온 다른 영화인 등의 관계성을 나타내며, 중심성과 선호도의 차이에 따라 다르게 시각화 된다.

- 콘텐츠 탐색

  인터랙티브한 대시보드를 통해 사용자는 새로운 영화인이나 영화를 탐색할 수 있으며, 영화인 상세페이지에서 선호하는 콘텐츠를 선택하고(like) 비슷한 취향의 유저를 선택(flock)할 수 있다.

- 콘텐츠 추천

  인기있는 영화콘텐츠를 추천하고 또한 사용자의 선호도를 바탕으로 관련성있는 새로운 콘텐츠를 추천한다.



## 2. Data Base

- JSON

- 모델링

- serializer

  

## 3. Main Pages

### pick

- 평점 기준 상위 12개의 영화를 선택하고,  그 영화에 출연한 영화인들 중 7할을 랜덤으로 선택해 그 콘텐츠들을 pick페이지에서 제시함

- 회원가입한  유저는 pick페이지로 이동, 제시된 컨텐츠 중에서 좋아하는 영화인을 선택하고, 본 영화를 평점매겨 dashboard의 데이터 제공

  

### userdetail

- UI&UX

- dashboard

- 내 활동을 기반으로한 영화 및 영화인 탐색

- sub 영화 추천

- flock(follow)

- 상세정보

  

### star & movie detail

- UI&UX
- moviedetail
  - grade
  - comments
- stardetail
  
  - like
  
    

### DB Management

- movie (crud)
- star (crud)



## 4. 작업분담

| 정윤영                              | 김민지              |
| ----------------------------------- | ------------------- |
| JSON                                | 기획                |
| Serializer                          | db 모델링           |
| DB관리페이지                        | userdetail 페이지   |
| UI&UX                               | login/signup/logout |
| like & searching 기능               | pick 페이지         |
| pick페이지의 다중선택 & progressbar | flock & grade 기능  |
| stardetail & moviedetail            | 추천기능            |
| 디버깅                              | 디자인              |







