# Arona API 文档

> Arona 是一个蔚蓝档案（Blue Archive）的第三方数据服务平台，提供总力战排名、学生信息、好友查询、作业管理等 API 接口。

**API 基础地址**: `https://api.arona.icu`

---

## 目录

1. [全局公共参数](#全局公共参数)
2. [状态码说明](#状态码说明)
3. [服务器ID对照表](#服务器id对照表)
4. [Boss信息](#boss信息)
5. [总力战实时数据](#总力战实时数据)
6. [学生信息](#学生信息)
7. [期数数据](#期数数据)
8. [作业管理](#作业管理)
9. [好友](#好友)
10. [账号登陆](#账号登陆)
11. [作业管理-竞技场](#作业管理-竞技场)

---

## 全局公共参数

### Header 参数

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| Referer | https://arona.icu | string | 否 | 不需要填 |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 | string | 否 | UA信息，不需要填 |
| Content-Type | application/json | string | 是 | - |
| ba-location | false | string | 否 | 环境检测，线上无效 |

### 认证方式

> 私密键值对

在 Header 添加参数：
- **key**: `2jhskfdgjldfgjldf-9639-kiuwoiruk`

---

## 状态码说明

| 状态码 | 中文描述 |
|--------|----------|
| 200 | 请求成功 |
| 404 | 无法访问 |

---

## 服务器ID对照表

| 服务器ID | 服务器名称 |
|----------|------------|
| 1 | 国服 |
| 2 | B服 |
| 3 | 日服 |
| 4 | 综合 |
| 5 | 全球 |
| 6 | 港澳台 |
| 7 | 韩服 |
| 8 | 亚服 |
| 9 | 北美服 |

---

## Boss信息

### boss信息列表

> 获取服务器 Boss 信息列表

**接口URL**: `/raids/boss/info`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID，见[服务器ID对照表](#服务器id对照表) |

---

### 查询boss信息

> 根据 boss_id 查询单个 Boss 信息

**接口URL**: `/raids/boss/info/id`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "boss_id": 1
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID，见[服务器ID对照表](#服务器id对照表) |
| boss_id | 1 | integer | 否 | Boss ID |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| code | integer | 状态码 |
| message | string | 消息 |
| data | object | 数据 |

---

### 根据难度和时间算分数

> 根据难度和时间计算分数

**接口URL**: `/raids/calculate_time/{server}`

**请求方式**: `GET`

**路径参数**:

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 是 | 1国服，3日服 |

**Query参数**:

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| bossId | 1 | integer | 是 | boss id |
| time | 240 | integer | 是 | 时间-秒单位 |
| season | 38 | integer | 否 | 赛季 |
| hard | INS | string | 是 | hard难度 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| code | integer | 状态码 |
| data | integer | 分数 |

---

### 根据分数计算时间

> 根据分数反推所需时间

**接口URL**: `/raids/calculate/{server}`

**请求方式**: `GET`

**路径参数**:

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 是 | 1国服，3日服 |

**Query参数**:

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| bossId | 1 | integer | 是 | boss id |
| point | 7148055 | integer | 是 | 分数 |
| season | 38 | integer | 否 | 赛季 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| code | integer | 状态码 |
| data | number | 时间 |

---

### 分数、时间信息

> 获取分数和时间相关信息

**接口URL**: `/raids/boss/hardSource`

**请求方式**: `GET`

**Query参数**:

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| season | 0 | integer | 否 | 赛季 |
| time | 1 | integer | 是 | 1.分数，2.时间 |
| region | 1 | integer | 是 | 1国服，2日服 |
| type | 1 | integer | 是 | 1.基础分数，2.3分钟分数，3.4.5分钟分数 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| code | integer | 状态码 |
| data | array | 数据数组 |
| data[].hard | string | 难度 |
| data[].source | integer | 分数来源 |

---

## 总力战实时数据

### 记录时间-时间分数分布

**接口URL**: `/api/v2/rank/season/score_distribute_list/list`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "season": "latest"
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID，见[服务器ID对照表](#服务器id对照表) |
| season | latest | string | 否 | 赛季，可填 "latest" |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| data.recordTime | array | 记录时间 |
| data.scoreDistributeViews | array | 最高难度 |
| data.secondHighestDifficulty | array | 次高难度 |

---

### 总力档线追踪

**接口URL**: `/api/v2/rank/new/charts`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "season": "latest"
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| season | latest | string | 否 | 赛季 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| data.time | array | 时间数组 |
| data.data | object | 数据对象 |

---

### 各档线分数

**接口URL**: `/api/v2/rank/list_top`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "season": "latest"
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| season | latest | string | 否 | 赛季 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| data[].rank | integer | 排名 |
| data[].bestRankingPoint | integer | 分数 |
| data[].hard | string | 难度 |
| data[].battleTime | string | 耗时 |
| data[].labelInfo | array | 标签信息 |

**labelInfo 参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| dataType | integer | 0下边界，1上边界 |
| tryNumber | integer | 0整体难度上下边界，1或以上出刀次数上下边界 |

---

### 各难度最低排名

**接口URL**: `/api/v2/rank/list_by_last_rank`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "season": "latest"
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| season | latest | string | 否 | 赛季 |

**响应参数**: 同各档线分数接口

---

### 排行榜-第20001位用户

**接口URL**: `/api/v2/rank/list_20001`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "season": "latest"
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| season | latest | string | 否 | 赛季 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| uid | string | 用户UID，用于查询用户信息 |
| rank | integer | 排名 |
| bestRankingPoint | integer | 分数 |
| level | integer | 用户等级 |
| nickname | string | 用户名 |
| representCharacterUniqueId | integer | 用户头像id |
| tier | integer | 档位 |
| hard | string | 难度 |
| battleTime | string | 战斗所需时间-秒 |
| bossId | integer | bossId |
| tryNumberInfos | array | 出刀次数信息 |
| recordTime | integer | 记录时间-毫秒 |
| labelInfo | array | 标签信息 |

---

### 排行榜-每期第1位用户

**接口URL**: `/api/v2/rank/list_1`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "season": "latest"
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| season | latest | string | 否 | 赛季 |

**响应参数**: 同 排行榜-第20001位用户 接口

---

### 排行榜

**接口URL**: `/api/v2/rank/list`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "season": "latest",
  "type": 2,
  "page": 1,
  "size": 10
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| season | latest | string | 否 | 赛季 |
| type | 2 | integer | 否 | 查询类型，1常规，2档线 |
| page | 1 | integer | 否 | 页 |
| size | 10 | integer | 否 | 单页数据量 |
| bossIndex | - | integer | 否 | boss序号，大决战使用 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| page | integer | 页 |
| size | integer | 单页显示数据量 |
| totalPages | integer | 总页数 |
| totalData | integer | 总数据量 |
| records | array | 记录数组 |
| lastPage | boolean | 是否最后一页 |

---

## 学生信息

### 获取服务器学生列表

**接口URL**: `/api/student/info/list`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| id | integer | 学生ID |
| bulletType | string | 攻击属性 |
| club | string | 社团 |
| name | string | 英文名 |
| cnName | string | 中文名 |
| school | string | 学校 |
| squadType | string | 队伍类型 |
| starGrade | integer | 星级 |
| tacticRole | string | 战术角色 |
| weaponType | string | 武器类型 |
| nameAlias | array | 名称别名 |

---

## 期数数据

### 期数

**接口URL**: `/api/season/list`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| season | integer | 期数 |
| map | object | 地图信息 |
| bossId | integer | boss id |
| boss | string | boss名称 |
| startTime | string | 开始时间 |
| endTime | string | 结束时间 |

---

### 期数记录时间查询

**接口URL**: `/api/season/record_time/{season}`

**请求方式**: `GET`

**路径参数**:

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| season | 3 | integer | 是 | 期数 |

**Query参数**:

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 是 | 服务器 1国服，2B服 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| data[].key | integer | 键 |
| data[].value | string | 值 |

---

## 作业管理

### 按照id查询作业

**接口URL**: `/api/job/query_one`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "job_id": 0
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| job_id | - | integer | 否 | 作业id |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| server | string | 服务器名称-中文 |
| season | integer | 赛季 |
| id | integer | 作业id |
| autoTitle | string | 自动标题 |
| title | string | 用户自定义副标题 |
| authorName | string | 作者名称 |
| videoUrl | string | 视频地址 |
| score | integer | 分数 |
| hard | string | 难度 |
| remark | string | 备注 |
| team | array | 队伍信息 |
| audit | object | 审核信息 |
| statusView | object | 状态信息 |

---

### 查询作业

**接口URL**: `/api/job/query_list`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "season": 0,
  "hard": "HC",
  "query": "",
  "exclude": [0],
  "page": 1,
  "size": 10
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| season | - | integer | 否 | 总力战赛季 |
| hard | HC | string | 是 | 难度 |
| query | - | string | 否 | 查询关键词，标题和副标题，描述 |
| exclude | - | array | 否 | 排除的角色id |
| page | 1 | integer | 否 | 页数据 |
| size | 10 | integer | 否 | 单页数据量 |

---

## 好友

### 刷新-更新好友最新数据

**接口URL**: `/api/friends/refresh`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "friend": "AYVXRVDN",
  "assistType": 0
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| friend | vlhy4mw | string | 否 | 好友码 |
| assistType | - | integer | 否 | 助战类型0全部，15总力战，2考试 |

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| key | string | 唯一id |
| special | integer | 特殊标记，0默认 |
| server | integer | 服务器信息 |
| friendCode | string | 好友码 |
| friendCount | integer | 好友数量 |
| nickname | string | 用户名 |
| representCharacterUniqueId | integer | 头像 |
| clanName | string | 公会 |
| comment | string | 签名 |
| level | integer | 等级 |
| updateTime | integer | 数据更新时间戳-毫秒 |
| maxFavorRank | integer | 最高好感度 |
| assistInfoList | array | 助战信息列表 |

---

### 排行榜

**接口URL**: `/api/friends/rank`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "page": 0,
  "size": 10,
  "studentId": 0,
  "server": 0
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| page | - | integer | 否 | 页 |
| size | 10 | integer | 否 | 单页数据量 |
| studentId | - | integer | 否 | 学生id |
| server | - | integer | 否 | 服务器ID |

---

### 查询好友最新数据

**接口URL**: `/api/friends/find`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "friend": "BaKey$dH4J5nTiasuiWeLpfrubx2bhdMeynbbE2ru2bc7t4gFYa3EBYLo7wWZfw25ynq8AeIw="
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| friend | vlhy4mw | string | 否 | 好友码 |

---

### 反查排名

**接口URL**: `/api/friends/findRank`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "friend": "BaKey$dH4J5nTiasuiWeLpfrubx2bhdMeynbbE2ru2bc7t4gFYa3EBYLo7wWZfw25ynq8AeIw="
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| friend | vlhy4mw | string | 否 | 好友码 |

---

### 助战查询

**接口URL**: `/api/friends/assist_query`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "server": 1,
  "page": 1,
  "size": 10,
  "friend": 0,
  "assistType": 0,
  "sort": 0,
  "uniqueId": 0,
  "level": 0,
  "starGrade": 0,
  "weaponLevel": 0,
  "weaponStarGrade": 0,
  "publicSkillLevel": 0,
  "exSkillLevel": 0,
  "passiveSkillLevel": 0,
  "extraPassiveSkillLevel": 0
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| server | 1 | integer | 否 | 服务器ID |
| page | 1 | integer | 否 | 页 |
| size | 10 | integer | 否 | 单页数据量 |
| friend | - | integer | 否 | 好友数量小于等于 |
| assistType | - | integer | 否 | 助战类型0全部，2总力战，15考试 |
| sort | - | integer | 否 | 0默认，1好感度降序，2好感度升序，3好友数量降序，4好友数量升序 |
| uniqueId | - | integer | 否 | 学生id |
| level | - | integer | 否 | 学生等级，大于等于 |
| starGrade | - | integer | 否 | 学生星级，大于等于 |
| weaponLevel | - | integer | 否 | 专武等级，大于等于 |
| weaponStarGrade | - | integer | 否 | 专武星级，大于等于 |
| publicSkillLevel | - | integer | 否 | 技能1等级，大于等于 |
| exSkillLevel | - | integer | 否 | 大招等级，大于等于 |
| passiveSkillLevel | - | integer | 否 | 技能2等级，大于等于 |
| extraPassiveSkillLevel | - | integer | 否 | 技能3等级，大于等于 |

---

## 账号登陆

### 注销

**接口URL**: `/api/auth/sso/logout`

**请求方式**: `POST`

**请求Body参数**: 空对象 `{}`

---

### 登陆

**接口URL**: `/api/auth/sso/login`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "email": "",
  "password": ""
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| email | - | string | 否 | 邮箱 |
| password | - | string | 否 | 密码 |

---

## 作业管理-竞技场

### 赛季

**接口URL**: `/api/job/jjc/season`

**请求方式**: `POST`

**请求Body参数**: 空对象 `{}`

**响应参数**:

| 参数名 | 类型 | 说明 |
|--------|------|------|
| season | string | 赛季名称 |
| map | string | 地形 |

---

### 添加作业

**接口URL**: `/api/job/jjc/add`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "season": "S30",
  "title": "测试标题",
  "remark": "",
  "attack": [
    {
      "studentId": 10000,
      "starGrade": 0,
      "hasWeapon": 0,
      "slotIndex": 1,
      "squadType": "Main"
    }
  ],
  "defend": [
    {
      "studentId": 10000,
      "starGrade": 0,
      "hasWeapon": 0,
      "slotIndex": 1,
      "squadType": "Main"
    }
  ]
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| season | S30 | string | 否 | 赛季 |
| title | 测试标题 | string | 是 | 标题 |
| remark | - | string | 否 | 简介 |
| attack | array | 否 | 进攻方学生 |
| defend | array | 否 | 防守方学生 |

**attack/defend 参数**:

| 参数名 | 示例值 | 类型 | 说明 |
|--------|--------|------|------|
| studentId | 10000 | integer | 学生id |
| starGrade | - | integer | 星级0-N |
| hasWeapon | - | integer | 有无专武 0没有，否则是星级 |
| slotIndex | 1 | integer | 站位信息 |
| squadType | Main | string | 弃用 |

---

### 查询作业

> **状态**: 开发中

**接口URL**: `/api/job/jjc/query`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "season": "S30",
  "queryType": 0,
  "matchType": 0,
  "list": [
    {
      "studentId": 10000,
      "slotIndex": 1
    }
  ],
  "page": 1
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| season | S30 | string | 是 | 赛季 |
| queryType | - | integer | 否 | 查询类型0点赞,1时间倒序 |
| matchType | - | integer | 否 | 匹配类型 0普通，1精确 |
| list.studentId | 10000 | integer | 否 | 学生id |
| list.slotIndex | 1 | integer | 否 | 站位信息 |
| page | 1 | integer | 否 | 页 |

---

### 点赞接口

> **状态**: 开发中

**接口URL**: `/api/job/jjc/like`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "jobId": 0,
  "status": 1
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| jobId | - | integer | 否 | 作业或评论id |
| status | 1 | integer | 否 | 0取消点赞，1点赞，2点踩 |

---

### 查询作业评论

> **状态**: 开发中

**接口URL**: `/api/job/jjc/query_comments`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "jobId": 1,
  "type": 0,
  "commentId": 0,
  "page": 1
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| jobId | 1 | integer | 否 | 作业id |
| type | - | integer | 否 | 查询类型0点赞倒序，1时间倒序，2时间正序 |
| commentId | - | integer | 否 | 评论id，默认0 |
| page | 1 | integer | 否 | 第几页 |

---

### 添加评论

> **状态**: 开发中

**接口URL**: `/api/job/jjc/add_comments`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "jobId": 1,
  "commentId": 0,
  "content": ""
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| jobId | 1 | integer | 否 | 作业id |
| commentId | - | integer | 否 | 回复的评论id，如果是在作业下面评论则为0 |
| content | - | string | 否 | 评论内容，不支持图片 |

---

### 删除作业

> **状态**: 开发中

**接口URL**: `/api/job/jjc/delete_comments`

**请求方式**: `POST`

**请求Body参数**:

```json
{
  "jobId": 1
}
```

| 参数名 | 示例值 | 类型 | 必填 | 说明 |
|--------|--------|------|------|------|
| jobId | 1 | integer | 否 | 作业id或评论id |

---

## 响应通用结构

大多数接口响应遵循以下格式：

```json
{
  "code": 0,
  "crypt": "",
  "message": "",
  "data": {},
  "traceId": "",
  "flowMillisecond": 0
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| code | integer | 业务状态码，0表示成功 |
| crypt | boolean | 是否加密 |
| message | string | 消息 |
| data | object/array | 数据 |
| traceId | string | 追踪ID |
| flowMillisecond | integer | 响应耗时(毫秒) |

---

## 备注

- 所有 POST 请求的 `Content-Type` 为 `application/json`
- `server` 参数如果不填，默认为 1（国服）
- `season` 参数可以填 `"latest"` 表示最新赛季
- 响应中的时间戳如无说明，默认单位为**毫秒**
