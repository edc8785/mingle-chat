# API

### GET /posts/:id

#### response

|        | type            | desc              |
| ------ | --------------- | ----------------- |
| id     | `number`        | post 의 unique id |
| name   | `string`        | post 제목         |
| user   | `User`          |                   |
| period | number? string? | 만남 주기         |
| intro  | `string`        | 소개 글           |
| offer  | `string`        | 드릴 수 있는 것   |

```js
// example
{
  id: 1,
  name: '진정성 있는 영상 편집 프로젝트',
  user: {
    id: 1,
    name: '커밍쏜',
    profile_img_url: 'https://i.pravatar.cc/'
  },
  period: 7,
  intro: '안녕하세요!\n커밍쏜과 함께 일할 영상 디자이너를 찾고 있습니다. 저 커밍쏜은 [유튜버 채널 이름] 채널을 운영하며 [채널 구독자 수]명 이상의 구독자를 보유한 유명한 크리에이터로, 퇴사 인터뷰 콘텐츠와 자기계발 영상으로 많은 사람들에게 영감을 주고 있습니다. 퇴사 후 자신만의 이야기를 그려 나가는 사람들의 이야기를 전달하고 싶으신 영상 디자이너 분들을 찾습니다.',
  offer: '유튜브랜딩 챌린지 10여 회를 진행하며 쌓인 노하우를 드릴 수 있습니다.'
}
```

---

### GET /posts

#### query parameters

|       | desc                  |
| ----- | --------------------- |
| page  | 페이지 번호           |
| limit | 페이지 당 아이템 갯수 |
| sort  | 나중에 추가?          |
| order | 나중에 추가?          |

```sh
# example
GET /posts?page=1&limit=100&sort=id,name&order=asc,desc
```

#### response

|            | type         | desc                       |
| ---------- | ------------ | -------------------------- |
| items      |              | GET /post response의 array |
| pagination | `Pagination` | 페이지네이션 정보          |

```js
// example
{
  items: [
    {
      id: 1,
      name: '진정성 있는 영상 편집 프로젝트',
      user: {
        id: 1,
        name: '커밍쏜',
        profile_img_url: 'https://i.pravatar.cc/'
      },
      period: 7,
      intro: '안녕하세요!\n커밍쏜과 함께 일할 영상 디자이너를 찾고 있습니다. 저 커밍쏜은 [유튜버 채널 이름] 채널을 운영하며 [채널 구독자 수]명 이상의 구독자를 보유한 유명한 크리에이터로, 퇴사 인터뷰 콘텐츠와 자기계발 영상으로 많은 사람들에게 영감을 주고 있습니다. 퇴사 후 자신만의 이야기를 그려 나가는 사람들의 이야기를 전달하고 싶으신 영상 디자이너 분들을 찾습니다.',
      offer: '유튜브랜딩 챌린지 10여 회를 진행하며 쌓인 노하우를 드릴 수 있습니다.'
    },
    ... 생략
  ],
  pagination: {
    current_page: 1,
    next_page: 2,
    limit: 100,
    previous_page: null,
    total_entries: 101,
    total_pages: 2
  }

}

```

---

### POST /posts

#### payload

|         | type            | required | desc               |
| ------- | --------------- | -------- | ------------------ |
| name    | `string`        | `true`   | post 제목          |
| user_id | `number`        | `true`   | 유저 유니크 아이디 |
| period  | number? string? | ?        | 만남 주기          |
| intro   | `string`        | ?        | 소개 글            |
| offer   | `string`        | ?        | 드릴 수 있는 것    |

example

```js
{
  name: '진정성 있는 영상 편집 프로젝트',
  user_id: 1
  period: 7,
  intro: '안녕하세요!\n커밍쏜과 함께 일할 영상 디자이너를 찾고 있습니다. 저 커밍쏜은 [유튜버 채널 이름] 채널을 운영하며 [채널 구독자 수]명 이상의 구독자를 보유한 유명한 크리에이터로, 퇴사 인터뷰 콘텐츠와 자기계발 영상으로 많은 사람들에게 영감을 주고 있습니다. 퇴사 후 자신만의 이야기를 그려 나가는 사람들의 이야기를 전달하고 싶으신 영상 디자이너 분들을 찾습니다.',
  offer: '유튜브랜딩 챌린지 10여 회를 진행하며 쌓인 노하우를 드릴 수 있습니다.'
}
```

#### response

GET /posts/:id 와 동일

---

### PUT /posts/:id

#### payload

post 와 동일

#### response

post 와 동일

---

### DELETE /posts/:id

#### response

200

---

### 공통

#### User

|                 | type     | desc          |
| --------------- | -------- | ------------- |
| id              | `string` | user id       |
| name            | `string` | user 이름     |
| profile_img_url | `string` | 프로필 이미지 |

#### Pagination

|               | type           | desc                         |
| ------------- | -------------- | ---------------------------- |
| current_page  | `number`       | 현재 페이지 번호             |
| next_page     | `number\|null` | 다음 페이지 번호             |
| limit         | `number`       | 페이지 당 가져올 아이템 갯수 |
| previous_page | `number\|null` | 이전 페이지 번호             |
| total_entries | `number`       | 전체 아이템 갯수             |
| total_pages   | `number`       | 전체 페이지 수               |
