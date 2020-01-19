# README

[TOC]

---



## 1. Service Overview

**YoungDucklings**

어린 오리들이 어미 오리나 각인된 대상을 졸졸 따라다니는 모양에서 아이디어를 얻어, 사용자들이 영화인 기반으로 영화콘텐츠를 탐색하거나 추천을 받을 수 있는 서비스를 기획했다.

- **dashboard**

  서비스 내에서 이루어지는 사용자의 활동들은 사용자 상세 페이지에서 영화인을 중심으로 시각화된 그래프로 제공된다. 그래프는 사용자가 좋아하는 영화인과 그들이 출연한 영화들, 출연한 영화에 나온 다른 영화인 등의 관계성을 나타내며, 중심성과 선호도의 차이에 따라 다르게 시각화 된다.

- **콘텐츠 탐색**

  인터랙티브한 대시보드를 통해 사용자는 새로운 영화인이나 영화를 탐색할 수 있으며, 영화인 상세페이지에서 선호하는 콘텐츠를 선택하고(like) 비슷한 취향의 유저를 선택(flock)할 수 있다.

- **콘텐츠 추천**

  인기있는 영화콘텐츠를 추천하고 또한 사용자의 선호도를 바탕으로 관련성있는 새로운 콘텐츠를 추천한다.



## 2. Data Base

### 모델링

### JSON

- 모델링한 DB Model에 맞춰 JSON 파일을 만들었으며, 프로젝트의 각 App의 fixtures 내에 배치 시켰다. stars 앱을 예로 들어 다음과 같은 폴더 구조를 볼 수 있다.

  ```
  stars [app 이름]
  └ fixtures
  	└ stars [app 이름와 같은 폴더명]
  		└ Cast.json
  		└ Coworker.json
  		└ ProfileImg.json
  		└ Star.json
  		└ TaggedImg.json
  ```

- fixtures에 파일을 저장한 후, 다음과 같은 명령어로 DB에 Data를 저장할 수 있다.

  ```bash
  $ python manage.py loaddata [파일명]/폴더명
  ```

- JSON 파일 목록

  - fixtures/stars

    Cast.json / Coworker.json / ProfileImg.json / Star.json / TaggedImg.json

  - fixtures/movies

    Backdrop.json / Genre.json / Movie.json / Poster.json / Video.json

### Serializer



## 3. Main Pages

### pick

- 평점 기준 상위 12개의 영화를 선택하고,  그 영화에 출연한 영화인들 중 7할을 랜덤으로 선택해 그 콘텐츠들을 pick페이지에서 제시한다.

- 회원가입한 유저는 pick페이지로 이동, 제시된 컨텐츠 중에서 좋아하는 영화인을 선택하고, 본 영화를 평점매겨 dashboard의 데이터 제공한다.

- 유저가 선택한 갯수에 맞춰 progressing bar 게이지가 올라가며, 100%가 되지 않아도 선택이 완료되면 submit 버튼을 눌러 제출이 가능하다.

  

### userdetail

- dashboard

- 내 활동을 기반으로한 영화 및 영화인 탐색

- sub 영화 추천

- flock(follow)

- 상세정보

  

### star & movie detail

- **moviedetail**
  
  DB 내에 저장되어 있는 각각의 영화 정보를 볼 수 있는 페이지다. **별점 주기(grade)**, **댓글 달기(comments)** 기능이 있으며, 각 영화에 대한 정보를 볼 수 있다. 내용이 없는 경우에는 해당 정보가 없음을 알려준다.
  
  - *영화 정보* : 평점(TMDB 사이트 기준), 장르, 청소년관람불가 여부, 개봉일, 러닝타임, 개봉여부, 캐스팅 정보, 비디오 및 포스터, 시놉시스
  
  - *별점 주기(grade)* : 해당 영화에 대한 평점을 별의 형태로 남길 수 있다. 평점을 남기면 해당 영화를 관람한 경험이 있다고 간주한다. 또한, userdetail 페이지에서 별점을 준 영화의 목록을 볼 수 있다. 
  - *댓글 달기(comments)* : 해당 영화에 대한 의견을 남길 수 있다. 해당 댓글은 등록한 user만이 삭제가 가능하며, user 이름을 클릭했을 시 해당 user의 userdetail 페이지로 이동하게 된다.
  
- **stardetail**
  
  영화인을 소개하는 페이지로 **좋아요(like)** 기능이 있으며, 각 영화인에 대한 정보를 볼 수 있다. 내용이 없는 경우에는 해당 정보가 없음을 알려준다.
  
  - *영화인 정보* : 생일, 사망일(해당 영화인이 사망한 경우), 직업(배우 / 감독), 생애 정보, 홈페이지, 프로필 이미지, 출연 또는 제작 영화 목록, 태그된 이미지
  
  - *좋아요(like)* : 좋아하는 영화인을 '좋아요'할 수 있으며, 후에 My page(userdetail)에서 모아보기로 볼 수 있고, 각 User의 Star Dashboard에 해당 배우가 등록된다.
  
    또한, 몇 명의 user가 해당 영화인을 좋아하는 지 count가 되어 이를 확인할 수 있다.
    
    

### DB Management

- **Data CRUD**

  Super user(관리자)로 등록된 계정만이 DB에 있는 모든 영화와 영화인의 Create / Update / Delete 기능에 접근이 가능하다. 대신, Read에 해당되는 moviedetail과 stardetail에는 모든 user 접근이 가능하다.

  - **movie (crud)** 
    - *create* : 새로운 영화 Data를 DB에 저장할 수 있다.
    - *update* : DB에 저장되어 있는 영화 Data의 각 정보를 수정할 수 있다.
    - *delete* : DB에 저장되어 있는 영화 Data를 삭제할 수 있다.
  - **star (crud)**
    - *create* : 새로운 영화인 Data를 DB에 저장할 수 있다.
    - *update* : DB에 저장되어 있는 영화인 Data의 각 정보를 수정할 수 있다.
    - *delete* : DB에 저장되어 있는 영화인 Data를 삭제할 수 있다.



## 4. 그 외

### searching

- DB 내에 있는 영화 / 영화인 / 유저를 검색이 가능하게 기능을 구현했다.

  검색어의 일부를 입력하여도 검색이 가능하다.

### UI / UX

- 각 페이지의 특성에 맞게 UI / UX 디자인을 구현했다.



## 5. 작업분담

| 정윤영                              | 김민지              |
| ----------------------------------- | ------------------- |
| JSON                                | 기획                |
| Serializer                          | db 모델링           |
| DB관리페이지                        | userdetail 페이지   |
| UI & UX                             | login/signup/logout |
| like & searching 기능               | pick 페이지         |
| pick페이지의 다중선택 & progressbar | flock & grade 기능  |
| stardetail & moviedetail            | 추천기능            |
| 디버깅                              | 디자인              |







