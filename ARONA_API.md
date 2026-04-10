# 全局公共参数

**全局Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Referer | https://arona.icu | string | 否 | 不需要填 |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36 | string | 否 | UA信息，不需要填 |
| Content-Type | application/json | string | 是 | - |
| ba-location | false | string | 否 | 环境检测，线上无效 |

**全局Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**全局Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**全局认证方式**

> 私密键值对

> 在Header添加参数

> key: 2jhskfdgjldfgjldf-9639-kiuwoiruk

# 状态码说明

| 状态码 | 中文描述 |
| --- | ---- |
| 200 | 请求成功 |
| 404 | 无法访问 |

# boss信息

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## boss信息列表

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /raids/boss/info

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 查询boss信息

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /raids/boss/info/id

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"boss_id": 1
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| boss_id | 1 | integer | 否 | BOSS Id信息 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 根据难度和时间算分数

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /raids/calculate_time/{server}?bossId=1&time=240&season=38&hard=INS

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> GET

**Content-Type**

> json

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| bossId | 1 | integer | 是 | boss id |
| time | 240 | integer | 是 | 时间-秒单位 |
| season | 38 | integer | 否 | 赛季 |
| hard | INS | string | 是 | hard，可以在分数，时间接口查询 |

**路径变量**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 是 | 1国服，3日服 |

**请求Body参数**

```javascript
暂无数据
```

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": 0,
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data | - | integer | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 根据分数计算时间

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /raids/calculate/{server}?bossId=1&point=7148055&season=38

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> GET

**Content-Type**

> json

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| bossId | 1 | integer | 是 | boss id |
| point | 7148055 | integer | 是 | 分数 |
| season | 38 | integer | 否 | 赛季 |

**路径变量**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 是 | 1国服，3日服 |

**请求Body参数**

```javascript
暂无数据
```

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": "",
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data | - | number | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 分数、时间信息

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /raids/boss/hardSource?season=0&time=1&region=1&type=1

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> GET

**Content-Type**

> json

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| season | 0 | integer | 否 | 赛季 |
| time | 1 | integer | 是 | 1.分数，2.时间， |
| region | 1 | integer | 是 | 1国服，2日服， |
| type | 1 | integer | 是 | 1.基础分数，2.3分钟分数，3.4.5分钟分数 |

**请求Body参数**

```javascript
暂无数据
```

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": [
		{
			"hard": "",
			"source": 0
		}
	],
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.hard | - | string | - |
| data.source | - | integer | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 总力战实时数据

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 最高难度参与人数变化

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

**整合到综合查询参与人数信息接口**

**接口状态**

> 已废弃

**接口URL**

> /api/v2/rank/season/topRank/charts

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": "latest"
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"key": [
			0
		],
		"value": [
			0
		]
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.key.0 | - | array | - |
| data.value.0 | - | array | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 记录时间-时间分数分布

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/v2/rank/season/score_distribute_list/list

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": "latest"
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"recordTime": [
			0
		],
		"scoreDistributeViews": [
			""
		],
		"secondHighestDifficulty": [
			""
		]
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.recordTime.0 | - | array | 记录时间 |
| data.scoreDistributeViews.0 | - | array | 最高难度 |
| data.secondHighestDifficulty.0 | - | array | 次高难度 |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 参与人数变化

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

**整合到综合查询参与人数信息接口**

**接口状态**

> 已废弃

**接口URL**

> /api/v2/rank/season/lastRank/charts

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": "latest"
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"key": [
			0
		],
		"value": [
			0
		]
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.key.0 | - | array | - |
| data.value.0 | - | array | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 总力档线追踪

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/v2/rank/new/charts

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": "latest"
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"time": [
			0
		],
		"data": {}
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.time.0 | - | array | - |
| data.data | - | object | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 各档线分数

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/v2/rank/list_top

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": "latest"
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": [
		{
			"rank": 0,
			"bestRankingPoint": 0,
			"hard": "",
			"battleTime": "",
			"labelInfo": [
				{
					"dataType": 0,
					"tryNumber": 0
				}
			]
		}
	],
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.rank | - | integer | 排名 |
| data.bestRankingPoint | - | integer | 分数 |
| data.hard | - | string | 难度 |
| data.battleTime | - | string | 耗时 |
| data.labelInfo.dataType | - | integer | 0下边界，1上边界 |
| data.labelInfo.tryNumber | - | integer | 0整体难度上下边界，1或以上出刀次数上下边界 |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 各难度最低排名

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/v2/rank/list_by_last_rank

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": "latest"
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": [
		{
			"rank": 0,
			"bestRankingPoint": 0,
			"hard": "",
			"battleTime": "",
			"labelInfo": [
				{
					"dataType": 0,
					"tryNumber": 0
				}
			]
		}
	],
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.rank | - | integer | 排名 |
| data.bestRankingPoint | - | integer | 分数 |
| data.hard | - | string | 难度 |
| data.battleTime | - | string | 耗时 |
| data.labelInfo.dataType | - | integer | 0下边界，1上边界 |
| data.labelInfo.tryNumber | - | integer | 0整体难度上下边界，1或以上出刀次数上下边界 |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 排行榜-第20001位用户

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/v2/rank/list_20001

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": "latest"
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"uid": "",
		"rank": 0,
		"bestRankingPoint": 0,
		"level": 0,
		"nickname": "",
		"representCharacterUniqueId": 0,
		"tier": 0,
		"hard": "",
		"battleTime": "",
		"bossId": 0,
		"tryNumberInfos": [
			{
				"tryNumber": 0,
				"mainCharacters": [
					{
						"hasWeapon": "",
						"isAssist": "",
						"level": 0,
						"slotIndex": 0,
						"starGrade": 0,
						"uniqueId": 0,
						"bulletType": "",
						"tacticRole": "",
						"weaponStarGrade": 0
					}
				],
				"supportCharacters": [
					{
						"hasWeapon": "",
						"isAssist": "",
						"level": 0,
						"slotIndex": 0,
						"starGrade": 0,
						"uniqueId": 0,
						"bulletType": "",
						"tacticRole": "",
						"weaponStarGrade": 0
					}
				],
				"skillCardMulliganCharacters": [
					0
				]
			}
		],
		"recordTime": 0,
		"labelInfo": [
			{
				"dataType": 0,
				"tryNumber": 0
			}
		]
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.uid | - | string | 用户UID，用于查询用户信息 |
| data.rank | - | integer | 排名 |
| data.bestRankingPoint | - | integer | 分数 |
| data.level | - | integer | 用户等级 |
| data.nickname | - | string | 用户名 |
| data.representCharacterUniqueId | - | integer | 用户头像id |
| data.tier | - | integer | 档位 |
| data.hard | - | string | 难度 |
| data.battleTime | - | string | 战斗所需时间-秒 |
| data.bossId | - | integer | bossId |
| data.tryNumberInfos.tryNumber | - | integer | 用户出刀次数 |
| data.tryNumberInfos.mainCharacters.hasWeapon | - | boolean | 有无专武 |
| data.tryNumberInfos.mainCharacters.isAssist | - | boolean | 是否助战 |
| data.tryNumberInfos.mainCharacters.level | - | integer | 学生等级 |
| data.tryNumberInfos.mainCharacters.slotIndex | - | integer | 队伍所在位置 |
| data.tryNumberInfos.mainCharacters.starGrade | - | integer | 学生星级 |
| data.tryNumberInfos.mainCharacters.uniqueId | - | integer | 学生id |
| data.tryNumberInfos.mainCharacters.bulletType | - | string | 攻击属性 |
| data.tryNumberInfos.mainCharacters.tacticRole | - | string | 输出类型 |
| data.tryNumberInfos.mainCharacters.weaponStarGrade | - | integer | 专武星级 0表示没有 |
| data.tryNumberInfos.supportCharacters.hasWeapon | - | boolean | 有无专武 |
| data.tryNumberInfos.supportCharacters.isAssist | - | boolean | 是否助战 |
| data.tryNumberInfos.supportCharacters.level | - | integer | 学生等级 |
| data.tryNumberInfos.supportCharacters.slotIndex | - | integer | 队伍所在位置 |
| data.tryNumberInfos.supportCharacters.starGrade | - | integer | 学生星级 |
| data.tryNumberInfos.supportCharacters.uniqueId | - | integer | 学生id |
| data.tryNumberInfos.supportCharacters.bulletType | - | string | 攻击属性 |
| data.tryNumberInfos.supportCharacters.tacticRole | - | string | 输出类型 |
| data.tryNumberInfos.supportCharacters.weaponStarGrade | - | integer | 专武星级 0表示没有 |
| data.tryNumberInfos.skillCardMulliganCharacters.0 | - | array | 初始技能牌 |
| data.recordTime | - | integer | 记录时间-毫秒 |
| data.labelInfo.dataType | - | integer | 0下边界，1上边界 |
| data.labelInfo.tryNumber | - | integer | 0整体难度上下边界，1或以上出刀次数上下边界 |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 排行榜-每期第1位用户

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/v2/rank/list_1

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": "latest"
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"uid": "",
		"rank": 0,
		"bestRankingPoint": 0,
		"level": 0,
		"nickname": "",
		"representCharacterUniqueId": 0,
		"tier": 0,
		"hard": "",
		"battleTime": "",
		"bossId": 0,
		"tryNumberInfos": [
			{
				"tryNumber": 0,
				"mainCharacters": [
					{
						"hasWeapon": "",
						"isAssist": "",
						"level": 0,
						"slotIndex": 0,
						"starGrade": 0,
						"uniqueId": 0,
						"bulletType": "",
						"tacticRole": "",
						"weaponStarGrade": 0
					}
				],
				"supportCharacters": [
					{
						"hasWeapon": "",
						"isAssist": "",
						"level": 0,
						"slotIndex": 0,
						"starGrade": 0,
						"uniqueId": 0,
						"bulletType": "",
						"tacticRole": "",
						"weaponStarGrade": 0
					}
				],
				"skillCardMulliganCharacters": [
					0
				]
			}
		],
		"recordTime": 0,
		"labelInfo": [
			{
				"dataType": 0,
				"tryNumber": 0
			}
		]
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.uid | - | string | 用户UID，用于查询用户信息 |
| data.rank | - | integer | 排名 |
| data.bestRankingPoint | - | integer | 分数 |
| data.level | - | integer | 用户等级 |
| data.nickname | - | string | 用户名 |
| data.representCharacterUniqueId | - | integer | 用户头像id |
| data.tier | - | integer | 档位 |
| data.hard | - | string | 难度 |
| data.battleTime | - | string | 战斗所需时间-秒 |
| data.bossId | - | integer | bossId |
| data.tryNumberInfos.tryNumber | - | integer | 用户出刀次数 |
| data.tryNumberInfos.mainCharacters.hasWeapon | - | boolean | 有无专武 |
| data.tryNumberInfos.mainCharacters.isAssist | - | boolean | 是否助战 |
| data.tryNumberInfos.mainCharacters.level | - | integer | 学生等级 |
| data.tryNumberInfos.mainCharacters.slotIndex | - | integer | 队伍所在位置 |
| data.tryNumberInfos.mainCharacters.starGrade | - | integer | 学生星级 |
| data.tryNumberInfos.mainCharacters.uniqueId | - | integer | 学生id |
| data.tryNumberInfos.mainCharacters.bulletType | - | string | 攻击属性 |
| data.tryNumberInfos.mainCharacters.tacticRole | - | string | 输出类型 |
| data.tryNumberInfos.mainCharacters.weaponStarGrade | - | integer | 专武星级 0表示没有 |
| data.tryNumberInfos.supportCharacters.hasWeapon | - | boolean | 有无专武 |
| data.tryNumberInfos.supportCharacters.isAssist | - | boolean | 是否助战 |
| data.tryNumberInfos.supportCharacters.level | - | integer | 学生等级 |
| data.tryNumberInfos.supportCharacters.slotIndex | - | integer | 队伍所在位置 |
| data.tryNumberInfos.supportCharacters.starGrade | - | integer | 学生星级 |
| data.tryNumberInfos.supportCharacters.uniqueId | - | integer | 学生id |
| data.tryNumberInfos.supportCharacters.bulletType | - | string | 攻击属性 |
| data.tryNumberInfos.supportCharacters.tacticRole | - | string | 输出类型 |
| data.tryNumberInfos.supportCharacters.weaponStarGrade | - | integer | 专武星级 0表示没有 |
| data.tryNumberInfos.skillCardMulliganCharacters.0 | - | array | 初始技能牌 |
| data.recordTime | - | integer | 记录时间-毫秒 |
| data.labelInfo.dataType | - | integer | 0下边界，1上边界 |
| data.labelInfo.tryNumber | - | integer | 0整体难度上下边界，1或以上出刀次数上下边界 |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 排行榜

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-10 00:25:47

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/v2/rank/list

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{"server":1,"season":11,"type":2,"page":1,"size":10,"timestamp":1773046095514}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | latest | string | 否 | 赛季 |
| type | 2 | integer | 否 | 查询类型，1常规，2档线 |
| page | 1 | integer | 否 | 页 |
| size | 10 | integer | 否 | 单页数据量 |
| bossIndex | - | integer | 否 | boss序号，大决战使用 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"page": 0,
		"size": 0,
		"totalPages": 0,
		"totalData": 0,
		"records": [
			{
				"uid": "",
				"rank": 0,
				"bestRankingPoint": 0,
				"level": 0,
				"nickname": "",
				"representCharacterUniqueId": 0,
				"tier": 0,
				"hard": "",
				"battleTime": "",
				"bossId": 0,
				"tryNumberInfos": [
					{
						"tryNumber": 0,
						"mainCharacters": [
							{
								"hasWeapon": "",
								"isAssist": "",
								"level": 0,
								"slotIndex": 0,
								"starGrade": 0,
								"uniqueId": 0,
								"bulletType": "",
								"tacticRole": "",
								"weaponStarGrade": 0
							}
						],
						"supportCharacters": [
							{
								"hasWeapon": "",
								"isAssist": "",
								"level": 0,
								"slotIndex": 0,
								"starGrade": 0,
								"uniqueId": 0,
								"bulletType": "",
								"tacticRole": "",
								"weaponStarGrade": 0
							}
						],
						"skillCardMulliganCharacters": [
							0
						]
					}
				],
				"recordTime": 0,
				"labelInfo": [
					{
						"dataType": 0,
						"tryNumber": 0
					}
				]
			}
		],
		"lastPage": ""
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.page | - | integer | 页 |
| data.size | - | integer | 单页显示数据量 |
| data.totalPages | - | integer | 总页数 |
| data.totalData | - | integer | 总数据量 |
| data.records.uid | - | string | 用户UID，用于查询用户信息 |
| data.records.rank | - | integer | 排名 |
| data.records.bestRankingPoint | - | integer | 分数 |
| data.records.level | - | integer | 用户等级 |
| data.records.nickname | - | string | 用户名 |
| data.records.representCharacterUniqueId | - | integer | 用户头像id |
| data.records.tier | - | integer | 档位 |
| data.records.hard | - | string | 难度 |
| data.records.battleTime | - | string | 战斗所需时间-秒 |
| data.records.bossId | - | integer | bossId |
| data.records.tryNumberInfos.tryNumber | - | integer | 用户出刀次数 |
| data.records.tryNumberInfos.mainCharacters.hasWeapon | - | boolean | 有无专武 |
| data.records.tryNumberInfos.mainCharacters.isAssist | - | boolean | 是否助战 |
| data.records.tryNumberInfos.mainCharacters.level | - | integer | 学生等级 |
| data.records.tryNumberInfos.mainCharacters.slotIndex | - | integer | 队伍所在位置 |
| data.records.tryNumberInfos.mainCharacters.starGrade | - | integer | 学生星级 |
| data.records.tryNumberInfos.mainCharacters.uniqueId | - | integer | 学生id |
| data.records.tryNumberInfos.mainCharacters.bulletType | - | string | 攻击属性 |
| data.records.tryNumberInfos.mainCharacters.tacticRole | - | string | 输出类型 |
| data.records.tryNumberInfos.mainCharacters.weaponStarGrade | - | integer | 专武星级 0表示没有 |
| data.records.tryNumberInfos.supportCharacters.hasWeapon | - | boolean | 有无专武 |
| data.records.tryNumberInfos.supportCharacters.isAssist | - | boolean | 是否助战 |
| data.records.tryNumberInfos.supportCharacters.level | - | integer | 学生等级 |
| data.records.tryNumberInfos.supportCharacters.slotIndex | - | integer | 队伍所在位置 |
| data.records.tryNumberInfos.supportCharacters.starGrade | - | integer | 学生星级 |
| data.records.tryNumberInfos.supportCharacters.uniqueId | - | integer | 学生id |
| data.records.tryNumberInfos.supportCharacters.bulletType | - | string | 攻击属性 |
| data.records.tryNumberInfos.supportCharacters.tacticRole | - | string | 输出类型 |
| data.records.tryNumberInfos.supportCharacters.weaponStarGrade | - | integer | 专武星级 0表示没有 |
| data.records.tryNumberInfos.skillCardMulliganCharacters.0 | - | array | 初始技能牌 |
| data.records.recordTime | - | integer | 记录时间-毫秒 |
| data.records.labelInfo.dataType | - | integer | 0下边界，1上边界 |
| data.records.labelInfo.tryNumber | - | integer | 0整体难度上下边界，1或以上出刀次数上下边界 |
| data.lastPage | - | boolean | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 学生信息

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 获取服务器学生列表

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/student/info/list

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": [
		{
			"id": 0,
			"bulletType": "",
			"club": "",
			"name": "",
			"cnName": "",
			"school": "",
			"squadType": "",
			"starGrade": 0,
			"tacticRole": "",
			"weaponType": "",
			"nameAlias": [
				""
			]
		}
	],
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.id | - | integer | - |
| data.bulletType | - | string | - |
| data.club | - | string | - |
| data.name | - | string | - |
| data.cnName | - | string | - |
| data.school | - | string | - |
| data.squadType | - | string | - |
| data.starGrade | - | integer | - |
| data.tacticRole | - | string | - |
| data.weaponType | - | string | - |
| data.nameAlias.0 | - | array | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 期数数据

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 期数

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/season/list

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": [
		{
			"season": 0,
			"map": {
				"key": "",
				"value": ""
			},
			"bossId": 0,
			"boss": "",
			"startTime": "",
			"endTime": ""
		}
	],
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.season | - | integer | 期数 |
| data.map.key | - | string | - |
| data.map.value | - | string | - |
| data.map | - | object | - |
| data.bossId | - | integer | boss id |
| data.boss | - | string | boss名称 |
| data.startTime | - | string | 开始时间 |
| data.endTime | - | string | 结束时间 |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 期数记录时间查询

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/season/record_time/{season}?server=1

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> GET

**Content-Type**

> json

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 是 | 服务器 1国服，2B服 |

**路径变量**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| season | 3 | integer | 是 | 期数 |

**请求Body参数**

```javascript
暂无数据
```

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": [
		{
			"key": 0,
			"value": ""
		}
	],
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.key | - | integer | - |
| data.value | - | string | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 作业管理

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 按照id查询作业

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/job/query_one

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"job_id": 0
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| job_id | - | integer | 否 | 作业id |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"server": "",
		"season": 0,
		"id": 0,
		"autoTitle": "",
		"title": "",
		"authorName": "",
		"videoUrl": "",
		"score": 0,
		"hard": "",
		"remark": "",
		"team": [
			""
		],
		"audit": {
			"auditStatus": 0,
			"auditCount": 0,
			"message": ""
		},
		"statusView": {
			"userLikeStatus": 0,
			"like": 0,
			"negative": 0,
			"views": 0
		},
		"updateTime": 0
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.server | - | string | 服务器名称-中文 |
| data.season | - | integer | 赛季 |
| data.id | - | integer | 作业id |
| data.autoTitle | - | string | 自动标题 |
| data.title | - | string | 用户自定义副标题 |
| data.authorName | - | string | 作者名称 |
| data.videoUrl | - | string | 视频地址 |
| data.score | - | integer | 分数 |
| data.hard | - | string | 难度 |
| data.remark | - | string | 备注 |
| data.team.0 | - | array | 队伍信息 |
| data.audit.auditStatus | - | integer | 审核状态 0待审核，1审核通过，2复审 |
| data.audit.auditCount | - | integer | 审核次数 |
| data.audit.message | - | string | 审核结果消息 |
| data.audit | - | object | - |
| data.statusView.userLikeStatus | - | integer | 用户的点赞状态，0无状态，1点赞，2点踩 |
| data.statusView.like | - | integer | 点赞人数 |
| data.statusView.negative | - | integer | 点踩人数 |
| data.statusView.views | - | integer | 浏览量 |
| data.statusView | - | object | - |
| data.updateTime | - | integer | 更新时间 |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 查询作业

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/job/query_list

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"season": 0,
	"hard": "HC",
	"query": "",
	"exclude": [
		0
	],
	"page": 1,
	"size": 10
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| season | - | integer | 否 | 总力战赛季 |
| hard | HC | string | 是 | 难度 |
| query | - | string | 否 | 查询关键词，标题和副标题，描述 |
| exclude.0 | - | array | 否 | 排除的角色id |
| page | 1 | integer | 否 | 页数据 |
| size | 10 | integer | 否 | 单页数据量 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"page": 0,
		"size": 0,
		"totalPages": 0,
		"totalData": 0,
		"records": [
			{
				"server": "",
				"season": 0,
				"id": 0,
				"autoTitle": "",
				"title": "",
				"authorName": "",
				"videoUrl": "",
				"score": 0,
				"hard": "",
				"remark": "",
				"team": [
					""
				],
				"audit": {
					"auditStatus": 0,
					"auditCount": 0,
					"message": ""
				},
				"statusView": {
					"userLikeStatus": 0,
					"like": 0,
					"negative": 0,
					"views": 0
				},
				"updateTime": 0
			}
		],
		"lastPage": ""
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.page | - | integer | 页 |
| data.size | - | integer | 单页显示数据量 |
| data.totalPages | - | integer | 总页数 |
| data.totalData | - | integer | 总数据量 |
| data.records.server | - | string | 服务器名称-中文 |
| data.records.season | - | integer | 赛季 |
| data.records.id | - | integer | 作业id |
| data.records.autoTitle | - | string | 自动标题 |
| data.records.title | - | string | 用户自定义副标题 |
| data.records.authorName | - | string | 作者名称 |
| data.records.videoUrl | - | string | 视频地址 |
| data.records.score | - | integer | 分数 |
| data.records.hard | - | string | 难度 |
| data.records.remark | - | string | 备注 |
| data.records.team.0 | - | array | 队伍信息 |
| data.records.audit.auditStatus | - | integer | 审核状态 0待审核，1审核通过，2复审 |
| data.records.audit.auditCount | - | integer | 审核次数 |
| data.records.audit.message | - | string | 审核结果消息 |
| data.records.audit | - | object | - |
| data.records.statusView.userLikeStatus | - | integer | 用户的点赞状态，0无状态，1点赞，2点踩 |
| data.records.statusView.like | - | integer | 点赞人数 |
| data.records.statusView.negative | - | integer | 点踩人数 |
| data.records.statusView.views | - | integer | 浏览量 |
| data.records.statusView | - | object | - |
| data.records.updateTime | - | integer | 更新时间 |
| data.lastPage | - | boolean | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 好友

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 刷新-更新好友最新数据

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 21:00:42

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/friends/refresh

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"friend": "AYVXRVDN",
	"assistType": 0
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| friend | vlhy4mw | string | 否 | 好友码 |
| assistType | - | integer | 否 | 助战类型0全部，15总力战，2考试 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"key": "",
		"special": 0,
		"server": 0,
		"friendCode": "",
		"friendCount": 0,
		"nickname": "",
		"representCharacterUniqueId": 0,
		"clanName": "",
		"comment": "",
		"level": 0,
		"db": "",
		"lastHardCampaignClearStageId": 0,
		"lastNormalCampaignClearStageId": 0,
		"updateTime": 0,
		"maxFavorRank": 0,
		"echelonType": 0,
		"assistInfoList": [
			{
				"baRank": {
					"key": 0,
					"value": 0
				},
				"baGlobalRank": {
					"key": 0,
					"value": 0
				},
				"rankUpdateTime": 0,
				"type": 0,
				"uniqueId": 0,
				"bulletType": "",
				"tacticRole": "",
				"echelonType": 0,
				"level": 0,
				"slotIndex": 0,
				"starGrade": 0,
				"favorRank": 0,
				"favorExp": 0,
				"maxFavorExp": 0,
				"publicSkillLevel": 0,
				"exSkillLevel": 0,
				"passiveSkillLevel": 0,
				"extraPassiveSkillLevel": 0,
				"equipment": {
					"empty": "",
					"array": "",
					"null": "",
					"object": "",
					"float": "",
					"number": "",
					"missingNode": "",
					"bigDecimal": "",
					"floatingPointNumber": "",
					"bigInteger": "",
					"nodeType": "",
					"valueNode": "",
					"container": "",
					"integralNumber": "",
					"string": "",
					"textual": "",
					"long": "",
					"short": "",
					"int": "",
					"double": "",
					"boolean": "",
					"binary": "",
					"pojo": "",
					"embeddedValue": ""
				},
				"weapon": "",
				"weaponUniqueId": 0,
				"weaponType": 0,
				"weaponLevel": 0,
				"weaponStarGrade": 0,
				"gearInfo": {
					"tier": 0
				},
				"potentialStats": {}
			}
		]
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.key | - | string | 唯一id |
| data.special | - | integer | 特殊标记，0默认 |
| data.server | - | integer | 服务器信息 |
| data.friendCode | - | string | 好友码 |
| data.friendCount | - | integer | 好友数量 |
| data.nickname | - | string | 用户名 |
| data.representCharacterUniqueId | - | integer | 头像 |
| data.clanName | - | string | 公会 |
| data.comment | - | string | 签名 |
| data.level | - | integer | 等级 |
| data.db | - | boolean | 是否服务器存档的数据 |
| data.lastHardCampaignClearStageId | - | integer | 推图进度 |
| data.lastNormalCampaignClearStageId | - | integer | 推图进度 |
| data.updateTime | - | integer | 数据更新时间戳-毫秒 |
| data.maxFavorRank | - | integer | 最高好感度 |
| data.echelonType | - | integer | 助战类型,多种类型时为0，否则就是唯一的类型 |
| data.assistInfoList.baRank.key | - | integer | - |
| data.assistInfoList.baRank.value | - | integer | - |
| data.assistInfoList.baRank | - | object | - |
| data.assistInfoList.baGlobalRank.key | - | integer | - |
| data.assistInfoList.baGlobalRank.value | - | integer | - |
| data.assistInfoList.baGlobalRank | - | object | - |
| data.assistInfoList.rankUpdateTime | - | integer | 排名更新时间 |
| data.assistInfoList.type | - | integer | 角色类型 |
| data.assistInfoList.uniqueId | - | integer | 学生id |
| data.assistInfoList.bulletType | - | string | - |
| data.assistInfoList.tacticRole | - | string | - |
| data.assistInfoList.echelonType | - | integer | 助战类型 |
| data.assistInfoList.level | - | integer | 学生等级 |
| data.assistInfoList.slotIndex | - | integer | 排序位置0或1 |
| data.assistInfoList.starGrade | - | integer | 学生星级 |
| data.assistInfoList.favorRank | - | integer | 学生好感度 |
| data.assistInfoList.favorExp | - | integer | 学生好感度经验值 |
| data.assistInfoList.maxFavorExp | - | integer | 当前好感升级所需经验 |
| data.assistInfoList.publicSkillLevel | - | integer | 技能1等级 |
| data.assistInfoList.exSkillLevel | - | integer | 大招等级 |
| data.assistInfoList.passiveSkillLevel | - | integer | 技能2等级 |
| data.assistInfoList.extraPassiveSkillLevel | - | integer | 技能3等级 |
| data.assistInfoList.equipment.empty | - | boolean | - |
| data.assistInfoList.equipment.array | - | boolean | - |
| data.assistInfoList.equipment.null | - | boolean | - |
| data.assistInfoList.equipment.object | - | boolean | - |
| data.assistInfoList.equipment.float | - | boolean | - |
| data.assistInfoList.equipment.number | - | boolean | - |
| data.assistInfoList.equipment.missingNode | - | boolean | - |
| data.assistInfoList.equipment.bigDecimal | - | boolean | - |
| data.assistInfoList.equipment.floatingPointNumber | - | boolean | - |
| data.assistInfoList.equipment.bigInteger | - | boolean | - |
| data.assistInfoList.equipment.nodeType | - | string | - |
| data.assistInfoList.equipment.valueNode | - | boolean | - |
| data.assistInfoList.equipment.container | - | boolean | - |
| data.assistInfoList.equipment.integralNumber | - | boolean | - |
| data.assistInfoList.equipment.string | - | boolean | - |
| data.assistInfoList.equipment.textual | - | boolean | - |
| data.assistInfoList.equipment.long | - | boolean | - |
| data.assistInfoList.equipment.short | - | boolean | - |
| data.assistInfoList.equipment.int | - | boolean | - |
| data.assistInfoList.equipment.double | - | boolean | - |
| data.assistInfoList.equipment.boolean | - | boolean | - |
| data.assistInfoList.equipment.binary | - | boolean | - |
| data.assistInfoList.equipment.pojo | - | boolean | - |
| data.assistInfoList.equipment.embeddedValue | - | boolean | - |
| data.assistInfoList.equipment | - | object | - |
| data.assistInfoList.weapon | - | boolean | 是否有专武 |
| data.assistInfoList.weaponUniqueId | - | integer | 专武id |
| data.assistInfoList.weaponType | - | integer | 专武类型 |
| data.assistInfoList.weaponLevel | - | integer | 专武等级 |
| data.assistInfoList.weaponStarGrade | - | integer | 专武星级 |
| data.assistInfoList.gearInfo.tier | - | integer | - |
| data.assistInfoList.gearInfo | - | object | - |
| data.assistInfoList.potentialStats | - | object | 解放等级 |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 排行榜

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/friends/rank

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"page": 0,
	"size": 10,
	"studentId": 0,
	"server": 0
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | - | integer | 否 | 页 |
| size | 10 | integer | 否 | 单页数据量 |
| studentId | - | integer | 否 | 学生id |
| server | - | integer | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"page": 0,
		"size": 0,
		"totalPages": 0,
		"totalData": 0,
		"records": [
			{
				"key": "",
				"special": 0,
				"server": 0,
				"friendCode": "",
				"friendCount": 0,
				"nickname": "",
				"representCharacterUniqueId": 0,
				"clanName": "",
				"comment": "",
				"level": 0,
				"db": "",
				"lastHardCampaignClearStageId": 0,
				"lastNormalCampaignClearStageId": 0,
				"updateTime": 0,
				"maxFavorRank": 0,
				"echelonType": 0,
				"assistInfoList": [
					{
						"baRank": {
							"key": 0,
							"value": 0
						},
						"baGlobalRank": {
							"key": 0,
							"value": 0
						},
						"rankUpdateTime": 0,
						"type": 0,
						"uniqueId": 0,
						"bulletType": "",
						"tacticRole": "",
						"echelonType": 0,
						"level": 0,
						"slotIndex": 0,
						"starGrade": 0,
						"favorRank": 0,
						"favorExp": 0,
						"maxFavorExp": 0,
						"publicSkillLevel": 0,
						"exSkillLevel": 0,
						"passiveSkillLevel": 0,
						"extraPassiveSkillLevel": 0,
						"equipment": {
							"empty": "",
							"array": "",
							"null": "",
							"object": "",
							"float": "",
							"number": "",
							"missingNode": "",
							"bigDecimal": "",
							"floatingPointNumber": "",
							"bigInteger": "",
							"nodeType": "",
							"valueNode": "",
							"container": "",
							"integralNumber": "",
							"string": "",
							"textual": "",
							"long": "",
							"short": "",
							"int": "",
							"double": "",
							"boolean": "",
							"binary": "",
							"pojo": "",
							"embeddedValue": ""
						},
						"weapon": "",
						"weaponUniqueId": 0,
						"weaponType": 0,
						"weaponLevel": 0,
						"weaponStarGrade": 0,
						"gearInfo": {
							"tier": 0
						},
						"potentialStats": {}
					}
				]
			}
		],
		"lastPage": ""
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.page | - | integer | 页 |
| data.size | - | integer | 单页显示数据量 |
| data.totalPages | - | integer | 总页数 |
| data.totalData | - | integer | 总数据量 |
| data.records.key | - | string | 唯一id |
| data.records.special | - | integer | 特殊标记，0默认 |
| data.records.server | - | integer | 服务器信息 |
| data.records.friendCode | - | string | 好友码 |
| data.records.friendCount | - | integer | 好友数量 |
| data.records.nickname | - | string | 用户名 |
| data.records.representCharacterUniqueId | - | integer | 头像 |
| data.records.clanName | - | string | 公会 |
| data.records.comment | - | string | 签名 |
| data.records.level | - | integer | 等级 |
| data.records.db | - | boolean | 是否服务器存档的数据 |
| data.records.lastHardCampaignClearStageId | - | integer | 推图进度 |
| data.records.lastNormalCampaignClearStageId | - | integer | 推图进度 |
| data.records.updateTime | - | integer | 数据更新时间戳-毫秒 |
| data.records.maxFavorRank | - | integer | 最高好感度 |
| data.records.echelonType | - | integer | 助战类型,多种类型时为0，否则就是唯一的类型 |
| data.records.assistInfoList.baRank.key | - | integer | - |
| data.records.assistInfoList.baRank.value | - | integer | - |
| data.records.assistInfoList.baRank | - | object | - |
| data.records.assistInfoList.baGlobalRank.key | - | integer | - |
| data.records.assistInfoList.baGlobalRank.value | - | integer | - |
| data.records.assistInfoList.baGlobalRank | - | object | - |
| data.records.assistInfoList.rankUpdateTime | - | integer | 排名更新时间 |
| data.records.assistInfoList.type | - | integer | 角色类型 |
| data.records.assistInfoList.uniqueId | - | integer | 学生id |
| data.records.assistInfoList.bulletType | - | string | - |
| data.records.assistInfoList.tacticRole | - | string | - |
| data.records.assistInfoList.echelonType | - | integer | 助战类型 |
| data.records.assistInfoList.level | - | integer | 学生等级 |
| data.records.assistInfoList.slotIndex | - | integer | 排序位置0或1 |
| data.records.assistInfoList.starGrade | - | integer | 学生星级 |
| data.records.assistInfoList.favorRank | - | integer | 学生好感度 |
| data.records.assistInfoList.favorExp | - | integer | 学生好感度经验值 |
| data.records.assistInfoList.maxFavorExp | - | integer | 当前好感升级所需经验 |
| data.records.assistInfoList.publicSkillLevel | - | integer | 技能1等级 |
| data.records.assistInfoList.exSkillLevel | - | integer | 大招等级 |
| data.records.assistInfoList.passiveSkillLevel | - | integer | 技能2等级 |
| data.records.assistInfoList.extraPassiveSkillLevel | - | integer | 技能3等级 |
| data.records.assistInfoList.equipment.empty | - | boolean | - |
| data.records.assistInfoList.equipment.array | - | boolean | - |
| data.records.assistInfoList.equipment.null | - | boolean | - |
| data.records.assistInfoList.equipment.object | - | boolean | - |
| data.records.assistInfoList.equipment.float | - | boolean | - |
| data.records.assistInfoList.equipment.number | - | boolean | - |
| data.records.assistInfoList.equipment.missingNode | - | boolean | - |
| data.records.assistInfoList.equipment.bigDecimal | - | boolean | - |
| data.records.assistInfoList.equipment.floatingPointNumber | - | boolean | - |
| data.records.assistInfoList.equipment.bigInteger | - | boolean | - |
| data.records.assistInfoList.equipment.nodeType | - | string | - |
| data.records.assistInfoList.equipment.valueNode | - | boolean | - |
| data.records.assistInfoList.equipment.container | - | boolean | - |
| data.records.assistInfoList.equipment.integralNumber | - | boolean | - |
| data.records.assistInfoList.equipment.string | - | boolean | - |
| data.records.assistInfoList.equipment.textual | - | boolean | - |
| data.records.assistInfoList.equipment.long | - | boolean | - |
| data.records.assistInfoList.equipment.short | - | boolean | - |
| data.records.assistInfoList.equipment.int | - | boolean | - |
| data.records.assistInfoList.equipment.double | - | boolean | - |
| data.records.assistInfoList.equipment.boolean | - | boolean | - |
| data.records.assistInfoList.equipment.binary | - | boolean | - |
| data.records.assistInfoList.equipment.pojo | - | boolean | - |
| data.records.assistInfoList.equipment.embeddedValue | - | boolean | - |
| data.records.assistInfoList.equipment | - | object | - |
| data.records.assistInfoList.weapon | - | boolean | 是否有专武 |
| data.records.assistInfoList.weaponUniqueId | - | integer | 专武id |
| data.records.assistInfoList.weaponType | - | integer | 专武类型 |
| data.records.assistInfoList.weaponLevel | - | integer | 专武等级 |
| data.records.assistInfoList.weaponStarGrade | - | integer | 专武星级 |
| data.records.assistInfoList.gearInfo.tier | - | integer | - |
| data.records.assistInfoList.gearInfo | - | object | - |
| data.records.assistInfoList.potentialStats | - | object | 解放等级 |
| data.lastPage | - | boolean | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 查询好友最新数据

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-14 20:25:07

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/friends/find

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"server": 1,
	"friend": "BaKey$dH4J5nTiasuiWeLpfrubx2bhdMeynbbE2ru2bc7t4gFYa3EBYLo7wWZfw25ynq8AeIw="
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| friend | vlhy4mw | string | 否 | 好友码 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"key": "",
		"special": 0,
		"server": 0,
		"friendCode": "",
		"friendCount": 0,
		"nickname": "",
		"representCharacterUniqueId": 0,
		"clanName": "",
		"comment": "",
		"level": 0,
		"db": "",
		"lastHardCampaignClearStageId": 0,
		"lastNormalCampaignClearStageId": 0,
		"updateTime": 0,
		"maxFavorRank": 0,
		"echelonType": 0,
		"assistInfoList": [
			{
				"baRank": {
					"key": 0,
					"value": 0
				},
				"baGlobalRank": {
					"key": 0,
					"value": 0
				},
				"rankUpdateTime": 0,
				"type": 0,
				"uniqueId": 0,
				"bulletType": "",
				"tacticRole": "",
				"echelonType": 0,
				"level": 0,
				"slotIndex": 0,
				"starGrade": 0,
				"favorRank": 0,
				"favorExp": 0,
				"maxFavorExp": 0,
				"publicSkillLevel": 0,
				"exSkillLevel": 0,
				"passiveSkillLevel": 0,
				"extraPassiveSkillLevel": 0,
				"equipment": {
					"empty": "",
					"array": "",
					"null": "",
					"object": "",
					"float": "",
					"number": "",
					"missingNode": "",
					"bigDecimal": "",
					"floatingPointNumber": "",
					"bigInteger": "",
					"nodeType": "",
					"valueNode": "",
					"container": "",
					"integralNumber": "",
					"string": "",
					"textual": "",
					"long": "",
					"short": "",
					"int": "",
					"double": "",
					"boolean": "",
					"binary": "",
					"pojo": "",
					"embeddedValue": ""
				},
				"weapon": "",
				"weaponUniqueId": 0,
				"weaponType": 0,
				"weaponLevel": 0,
				"weaponStarGrade": 0,
				"gearInfo": {
					"tier": 0
				},
				"potentialStats": {}
			}
		]
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.key | - | string | 唯一id |
| data.special | - | integer | 特殊标记，0默认 |
| data.server | - | integer | 服务器信息 |
| data.friendCode | - | string | 好友码 |
| data.friendCount | - | integer | 好友数量 |
| data.nickname | - | string | 用户名 |
| data.representCharacterUniqueId | - | integer | 头像 |
| data.clanName | - | string | 公会 |
| data.comment | - | string | 签名 |
| data.level | - | integer | 等级 |
| data.db | - | boolean | 是否服务器存档的数据 |
| data.lastHardCampaignClearStageId | - | integer | 推图进度 |
| data.lastNormalCampaignClearStageId | - | integer | 推图进度 |
| data.updateTime | - | integer | 数据更新时间戳-毫秒 |
| data.maxFavorRank | - | integer | 最高好感度 |
| data.echelonType | - | integer | 助战类型,多种类型时为0，否则就是唯一的类型 |
| data.assistInfoList.baRank.key | - | integer | - |
| data.assistInfoList.baRank.value | - | integer | - |
| data.assistInfoList.baRank | - | object | - |
| data.assistInfoList.baGlobalRank.key | - | integer | - |
| data.assistInfoList.baGlobalRank.value | - | integer | - |
| data.assistInfoList.baGlobalRank | - | object | - |
| data.assistInfoList.rankUpdateTime | - | integer | 排名更新时间 |
| data.assistInfoList.type | - | integer | 角色类型 |
| data.assistInfoList.uniqueId | - | integer | 学生id |
| data.assistInfoList.bulletType | - | string | - |
| data.assistInfoList.tacticRole | - | string | - |
| data.assistInfoList.echelonType | - | integer | 助战类型 |
| data.assistInfoList.level | - | integer | 学生等级 |
| data.assistInfoList.slotIndex | - | integer | 排序位置0或1 |
| data.assistInfoList.starGrade | - | integer | 学生星级 |
| data.assistInfoList.favorRank | - | integer | 学生好感度 |
| data.assistInfoList.favorExp | - | integer | 学生好感度经验值 |
| data.assistInfoList.maxFavorExp | - | integer | 当前好感升级所需经验 |
| data.assistInfoList.publicSkillLevel | - | integer | 技能1等级 |
| data.assistInfoList.exSkillLevel | - | integer | 大招等级 |
| data.assistInfoList.passiveSkillLevel | - | integer | 技能2等级 |
| data.assistInfoList.extraPassiveSkillLevel | - | integer | 技能3等级 |
| data.assistInfoList.equipment.empty | - | boolean | - |
| data.assistInfoList.equipment.array | - | boolean | - |
| data.assistInfoList.equipment.null | - | boolean | - |
| data.assistInfoList.equipment.object | - | boolean | - |
| data.assistInfoList.equipment.float | - | boolean | - |
| data.assistInfoList.equipment.number | - | boolean | - |
| data.assistInfoList.equipment.missingNode | - | boolean | - |
| data.assistInfoList.equipment.bigDecimal | - | boolean | - |
| data.assistInfoList.equipment.floatingPointNumber | - | boolean | - |
| data.assistInfoList.equipment.bigInteger | - | boolean | - |
| data.assistInfoList.equipment.nodeType | - | string | - |
| data.assistInfoList.equipment.valueNode | - | boolean | - |
| data.assistInfoList.equipment.container | - | boolean | - |
| data.assistInfoList.equipment.integralNumber | - | boolean | - |
| data.assistInfoList.equipment.string | - | boolean | - |
| data.assistInfoList.equipment.textual | - | boolean | - |
| data.assistInfoList.equipment.long | - | boolean | - |
| data.assistInfoList.equipment.short | - | boolean | - |
| data.assistInfoList.equipment.int | - | boolean | - |
| data.assistInfoList.equipment.double | - | boolean | - |
| data.assistInfoList.equipment.boolean | - | boolean | - |
| data.assistInfoList.equipment.binary | - | boolean | - |
| data.assistInfoList.equipment.pojo | - | boolean | - |
| data.assistInfoList.equipment.embeddedValue | - | boolean | - |
| data.assistInfoList.equipment | - | object | - |
| data.assistInfoList.weapon | - | boolean | 是否有专武 |
| data.assistInfoList.weaponUniqueId | - | integer | 专武id |
| data.assistInfoList.weaponType | - | integer | 专武类型 |
| data.assistInfoList.weaponLevel | - | integer | 专武等级 |
| data.assistInfoList.weaponStarGrade | - | integer | 专武星级 |
| data.assistInfoList.gearInfo.tier | - | integer | - |
| data.assistInfoList.gearInfo | - | object | - |
| data.assistInfoList.potentialStats | - | object | 解放等级 |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 反查排名

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-14 20:25:08

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/friends/findRank

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"friend": "BaKey$dH4J5nTiasuiWeLpfrubx2bhdMeynbbE2ru2bc7t4gFYa3EBYLo7wWZfw25ynq8AeIw="
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| friend | vlhy4mw | string | 否 | 好友码 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"key": "",
		"special": 0,
		"server": 0,
		"friendCode": "",
		"friendCount": 0,
		"nickname": "",
		"representCharacterUniqueId": 0,
		"clanName": "",
		"comment": "",
		"level": 0,
		"db": "",
		"lastHardCampaignClearStageId": 0,
		"lastNormalCampaignClearStageId": 0,
		"updateTime": 0,
		"maxFavorRank": 0,
		"echelonType": 0,
		"assistInfoList": [
			{
				"baRank": {
					"key": 0,
					"value": 0
				},
				"baGlobalRank": {
					"key": 0,
					"value": 0
				},
				"rankUpdateTime": 0,
				"type": 0,
				"uniqueId": 0,
				"bulletType": "",
				"tacticRole": "",
				"echelonType": 0,
				"level": 0,
				"slotIndex": 0,
				"starGrade": 0,
				"favorRank": 0,
				"favorExp": 0,
				"maxFavorExp": 0,
				"publicSkillLevel": 0,
				"exSkillLevel": 0,
				"passiveSkillLevel": 0,
				"extraPassiveSkillLevel": 0,
				"equipment": {
					"empty": "",
					"array": "",
					"null": "",
					"object": "",
					"float": "",
					"number": "",
					"missingNode": "",
					"bigDecimal": "",
					"floatingPointNumber": "",
					"bigInteger": "",
					"nodeType": "",
					"valueNode": "",
					"container": "",
					"integralNumber": "",
					"string": "",
					"textual": "",
					"long": "",
					"short": "",
					"int": "",
					"double": "",
					"boolean": "",
					"binary": "",
					"pojo": "",
					"embeddedValue": ""
				},
				"weapon": "",
				"weaponUniqueId": 0,
				"weaponType": 0,
				"weaponLevel": 0,
				"weaponStarGrade": 0,
				"gearInfo": {
					"tier": 0
				},
				"potentialStats": {}
			}
		]
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.key | - | string | 唯一id |
| data.special | - | integer | 特殊标记，0默认 |
| data.server | - | integer | 服务器信息 |
| data.friendCode | - | string | 好友码 |
| data.friendCount | - | integer | 好友数量 |
| data.nickname | - | string | 用户名 |
| data.representCharacterUniqueId | - | integer | 头像 |
| data.clanName | - | string | 公会 |
| data.comment | - | string | 签名 |
| data.level | - | integer | 等级 |
| data.db | - | boolean | 是否服务器存档的数据 |
| data.lastHardCampaignClearStageId | - | integer | 推图进度 |
| data.lastNormalCampaignClearStageId | - | integer | 推图进度 |
| data.updateTime | - | integer | 数据更新时间戳-毫秒 |
| data.maxFavorRank | - | integer | 最高好感度 |
| data.echelonType | - | integer | 助战类型,多种类型时为0，否则就是唯一的类型 |
| data.assistInfoList.baRank.key | - | integer | - |
| data.assistInfoList.baRank.value | - | integer | - |
| data.assistInfoList.baRank | - | object | - |
| data.assistInfoList.baGlobalRank.key | - | integer | - |
| data.assistInfoList.baGlobalRank.value | - | integer | - |
| data.assistInfoList.baGlobalRank | - | object | - |
| data.assistInfoList.rankUpdateTime | - | integer | 排名更新时间 |
| data.assistInfoList.type | - | integer | 角色类型 |
| data.assistInfoList.uniqueId | - | integer | 学生id |
| data.assistInfoList.bulletType | - | string | - |
| data.assistInfoList.tacticRole | - | string | - |
| data.assistInfoList.echelonType | - | integer | 助战类型 |
| data.assistInfoList.level | - | integer | 学生等级 |
| data.assistInfoList.slotIndex | - | integer | 排序位置0或1 |
| data.assistInfoList.starGrade | - | integer | 学生星级 |
| data.assistInfoList.favorRank | - | integer | 学生好感度 |
| data.assistInfoList.favorExp | - | integer | 学生好感度经验值 |
| data.assistInfoList.maxFavorExp | - | integer | 当前好感升级所需经验 |
| data.assistInfoList.publicSkillLevel | - | integer | 技能1等级 |
| data.assistInfoList.exSkillLevel | - | integer | 大招等级 |
| data.assistInfoList.passiveSkillLevel | - | integer | 技能2等级 |
| data.assistInfoList.extraPassiveSkillLevel | - | integer | 技能3等级 |
| data.assistInfoList.equipment.empty | - | boolean | - |
| data.assistInfoList.equipment.array | - | boolean | - |
| data.assistInfoList.equipment.null | - | boolean | - |
| data.assistInfoList.equipment.object | - | boolean | - |
| data.assistInfoList.equipment.float | - | boolean | - |
| data.assistInfoList.equipment.number | - | boolean | - |
| data.assistInfoList.equipment.missingNode | - | boolean | - |
| data.assistInfoList.equipment.bigDecimal | - | boolean | - |
| data.assistInfoList.equipment.floatingPointNumber | - | boolean | - |
| data.assistInfoList.equipment.bigInteger | - | boolean | - |
| data.assistInfoList.equipment.nodeType | - | string | - |
| data.assistInfoList.equipment.valueNode | - | boolean | - |
| data.assistInfoList.equipment.container | - | boolean | - |
| data.assistInfoList.equipment.integralNumber | - | boolean | - |
| data.assistInfoList.equipment.string | - | boolean | - |
| data.assistInfoList.equipment.textual | - | boolean | - |
| data.assistInfoList.equipment.long | - | boolean | - |
| data.assistInfoList.equipment.short | - | boolean | - |
| data.assistInfoList.equipment.int | - | boolean | - |
| data.assistInfoList.equipment.double | - | boolean | - |
| data.assistInfoList.equipment.boolean | - | boolean | - |
| data.assistInfoList.equipment.binary | - | boolean | - |
| data.assistInfoList.equipment.pojo | - | boolean | - |
| data.assistInfoList.equipment.embeddedValue | - | boolean | - |
| data.assistInfoList.equipment | - | object | - |
| data.assistInfoList.weapon | - | boolean | 是否有专武 |
| data.assistInfoList.weaponUniqueId | - | integer | 专武id |
| data.assistInfoList.weaponType | - | integer | 专武类型 |
| data.assistInfoList.weaponLevel | - | integer | 专武等级 |
| data.assistInfoList.weaponStarGrade | - | integer | 专武星级 |
| data.assistInfoList.gearInfo.tier | - | integer | - |
| data.assistInfoList.gearInfo | - | object | - |
| data.assistInfoList.potentialStats | - | object | 解放等级 |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 助战查询

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/friends/assist_query

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
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

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| server | 1 | integer | 否 | 服务器1国服，2B服，3日服，4综合，5全球，6港澳台，7韩服，8亚服，9北美服 |
| page | 1 | integer | 否 | 页 |
| size | 10 | integer | 否 | 单页数据量 |
| friend | - | integer | 否 | 好友数量小于等于 |
| assistType | - | integer | 否 | 助战类型0全部，2是总力战 15是考试 |
| sort | - | integer | 否 | 0默认， 1，2好感度的降序，升序，3,4好友数量降序升序 |
| uniqueId | - | integer | 否 | 学生id |
| level | - | integer | 否 | 学生等级，大于等于 |
| starGrade | - | integer | 否 | 学生星级，大于等于 |
| weaponLevel | - | integer | 否 | 专武等级，大于等于 |
| weaponStarGrade | - | integer | 否 | 专武星级，大于等于 |
| publicSkillLevel | - | integer | 否 | 技能1等级，大于等于 |
| exSkillLevel | - | integer | 否 | 大招等级，大于等于 |
| passiveSkillLevel | - | integer | 否 | 技能2等级，大于等于 |
| extraPassiveSkillLevel | - | integer | 否 | 技能3等级，大于等于 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"page": 0,
		"size": 0,
		"totalPages": 0,
		"totalData": 0,
		"records": [
			{
				"key": "",
				"special": 0,
				"server": 0,
				"friendCode": "",
				"friendCount": 0,
				"nickname": "",
				"representCharacterUniqueId": 0,
				"clanName": "",
				"comment": "",
				"level": 0,
				"db": "",
				"lastHardCampaignClearStageId": 0,
				"lastNormalCampaignClearStageId": 0,
				"updateTime": 0,
				"maxFavorRank": 0,
				"echelonType": 0,
				"assistInfoList": [
					{
						"baRank": {
							"key": 0,
							"value": 0
						},
						"baGlobalRank": {
							"key": 0,
							"value": 0
						},
						"rankUpdateTime": 0,
						"type": 0,
						"uniqueId": 0,
						"bulletType": "",
						"tacticRole": "",
						"echelonType": 0,
						"level": 0,
						"slotIndex": 0,
						"starGrade": 0,
						"favorRank": 0,
						"favorExp": 0,
						"maxFavorExp": 0,
						"publicSkillLevel": 0,
						"exSkillLevel": 0,
						"passiveSkillLevel": 0,
						"extraPassiveSkillLevel": 0,
						"equipment": {
							"empty": "",
							"array": "",
							"null": "",
							"object": "",
							"float": "",
							"number": "",
							"missingNode": "",
							"bigDecimal": "",
							"floatingPointNumber": "",
							"bigInteger": "",
							"nodeType": "",
							"valueNode": "",
							"container": "",
							"integralNumber": "",
							"string": "",
							"textual": "",
							"long": "",
							"short": "",
							"int": "",
							"double": "",
							"boolean": "",
							"binary": "",
							"pojo": "",
							"embeddedValue": ""
						},
						"weapon": "",
						"weaponUniqueId": 0,
						"weaponType": 0,
						"weaponLevel": 0,
						"weaponStarGrade": 0,
						"gearInfo": {
							"tier": 0
						},
						"potentialStats": {}
					}
				]
			}
		],
		"lastPage": ""
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.page | - | integer | 页 |
| data.size | - | integer | 单页显示数据量 |
| data.totalPages | - | integer | 总页数 |
| data.totalData | - | integer | 总数据量 |
| data.records.key | - | string | 唯一id |
| data.records.special | - | integer | 特殊标记，0默认 |
| data.records.server | - | integer | 服务器信息 |
| data.records.friendCode | - | string | 好友码 |
| data.records.friendCount | - | integer | 好友数量 |
| data.records.nickname | - | string | 用户名 |
| data.records.representCharacterUniqueId | - | integer | 头像 |
| data.records.clanName | - | string | 公会 |
| data.records.comment | - | string | 签名 |
| data.records.level | - | integer | 等级 |
| data.records.db | - | boolean | 是否服务器存档的数据 |
| data.records.lastHardCampaignClearStageId | - | integer | 推图进度 |
| data.records.lastNormalCampaignClearStageId | - | integer | 推图进度 |
| data.records.updateTime | - | integer | 数据更新时间戳-毫秒 |
| data.records.maxFavorRank | - | integer | 最高好感度 |
| data.records.echelonType | - | integer | 助战类型,多种类型时为0，否则就是唯一的类型 |
| data.records.assistInfoList.baRank.key | - | integer | - |
| data.records.assistInfoList.baRank.value | - | integer | - |
| data.records.assistInfoList.baRank | - | object | - |
| data.records.assistInfoList.baGlobalRank.key | - | integer | - |
| data.records.assistInfoList.baGlobalRank.value | - | integer | - |
| data.records.assistInfoList.baGlobalRank | - | object | - |
| data.records.assistInfoList.rankUpdateTime | - | integer | 排名更新时间 |
| data.records.assistInfoList.type | - | integer | 角色类型 |
| data.records.assistInfoList.uniqueId | - | integer | 学生id |
| data.records.assistInfoList.bulletType | - | string | - |
| data.records.assistInfoList.tacticRole | - | string | - |
| data.records.assistInfoList.echelonType | - | integer | 助战类型 |
| data.records.assistInfoList.level | - | integer | 学生等级 |
| data.records.assistInfoList.slotIndex | - | integer | 排序位置0或1 |
| data.records.assistInfoList.starGrade | - | integer | 学生星级 |
| data.records.assistInfoList.favorRank | - | integer | 学生好感度 |
| data.records.assistInfoList.favorExp | - | integer | 学生好感度经验值 |
| data.records.assistInfoList.maxFavorExp | - | integer | 当前好感升级所需经验 |
| data.records.assistInfoList.publicSkillLevel | - | integer | 技能1等级 |
| data.records.assistInfoList.exSkillLevel | - | integer | 大招等级 |
| data.records.assistInfoList.passiveSkillLevel | - | integer | 技能2等级 |
| data.records.assistInfoList.extraPassiveSkillLevel | - | integer | 技能3等级 |
| data.records.assistInfoList.equipment.empty | - | boolean | - |
| data.records.assistInfoList.equipment.array | - | boolean | - |
| data.records.assistInfoList.equipment.null | - | boolean | - |
| data.records.assistInfoList.equipment.object | - | boolean | - |
| data.records.assistInfoList.equipment.float | - | boolean | - |
| data.records.assistInfoList.equipment.number | - | boolean | - |
| data.records.assistInfoList.equipment.missingNode | - | boolean | - |
| data.records.assistInfoList.equipment.bigDecimal | - | boolean | - |
| data.records.assistInfoList.equipment.floatingPointNumber | - | boolean | - |
| data.records.assistInfoList.equipment.bigInteger | - | boolean | - |
| data.records.assistInfoList.equipment.nodeType | - | string | - |
| data.records.assistInfoList.equipment.valueNode | - | boolean | - |
| data.records.assistInfoList.equipment.container | - | boolean | - |
| data.records.assistInfoList.equipment.integralNumber | - | boolean | - |
| data.records.assistInfoList.equipment.string | - | boolean | - |
| data.records.assistInfoList.equipment.textual | - | boolean | - |
| data.records.assistInfoList.equipment.long | - | boolean | - |
| data.records.assistInfoList.equipment.short | - | boolean | - |
| data.records.assistInfoList.equipment.int | - | boolean | - |
| data.records.assistInfoList.equipment.double | - | boolean | - |
| data.records.assistInfoList.equipment.boolean | - | boolean | - |
| data.records.assistInfoList.equipment.binary | - | boolean | - |
| data.records.assistInfoList.equipment.pojo | - | boolean | - |
| data.records.assistInfoList.equipment.embeddedValue | - | boolean | - |
| data.records.assistInfoList.equipment | - | object | - |
| data.records.assistInfoList.weapon | - | boolean | 是否有专武 |
| data.records.assistInfoList.weaponUniqueId | - | integer | 专武id |
| data.records.assistInfoList.weaponType | - | integer | 专武类型 |
| data.records.assistInfoList.weaponLevel | - | integer | 专武等级 |
| data.records.assistInfoList.weaponStarGrade | - | integer | 专武星级 |
| data.records.assistInfoList.gearInfo.tier | - | integer | - |
| data.records.assistInfoList.gearInfo | - | object | - |
| data.records.assistInfoList.potentialStats | - | object | 解放等级 |
| data.lastPage | - | boolean | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 账号登陆

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 注销

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/auth/sso/logout

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"empty": "",
	"array": "",
	"null": "",
	"object": "",
	"float": "",
	"number": "",
	"missingNode": "",
	"bigDecimal": "",
	"floatingPointNumber": "",
	"bigInteger": "",
	"nodeType": "",
	"valueNode": "",
	"container": "",
	"integralNumber": "",
	"string": "",
	"textual": "",
	"long": "",
	"short": "",
	"int": "",
	"double": "",
	"boolean": "",
	"binary": "",
	"pojo": "",
	"embeddedValue": ""
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| empty | - | boolean | 否 | - |
| array | - | boolean | 否 | - |
| null | - | boolean | 否 | - |
| object | - | boolean | 否 | - |
| float | - | boolean | 否 | - |
| number | - | boolean | 否 | - |
| missingNode | - | boolean | 否 | - |
| bigDecimal | - | boolean | 否 | - |
| floatingPointNumber | - | boolean | 否 | - |
| bigInteger | - | boolean | 否 | - |
| nodeType | - | string | 否 | - |
| valueNode | - | boolean | 否 | - |
| container | - | boolean | 否 | - |
| integralNumber | - | boolean | 否 | - |
| string | - | boolean | 否 | - |
| textual | - | boolean | 否 | - |
| long | - | boolean | 否 | - |
| short | - | boolean | 否 | - |
| int | - | boolean | 否 | - |
| double | - | boolean | 否 | - |
| boolean | - | boolean | 否 | - |
| binary | - | boolean | 否 | - |
| pojo | - | boolean | 否 | - |
| embeddedValue | - | boolean | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": "",
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data | - | string | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 登陆

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-08-27 18:47:23

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/auth/sso/login

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"email": "",
	"password": ""
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| email | - | string | 否 | 邮箱 |
| password | - | string | 否 | 密码 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": "",
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data | - | string | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 作业管理-竞技场

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-09-11 04:48:25

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 赛季

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-09-11 04:48:25

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/job/jjc/season

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"empty": "",
	"array": "",
	"null": "",
	"object": "",
	"float": "",
	"number": "",
	"missingNode": "",
	"bigDecimal": "",
	"floatingPointNumber": "",
	"bigInteger": "",
	"nodeType": "",
	"valueNode": "",
	"container": "",
	"integralNumber": "",
	"string": "",
	"textual": "",
	"long": "",
	"short": "",
	"int": "",
	"double": "",
	"boolean": "",
	"binary": "",
	"pojo": "",
	"embeddedValue": ""
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| empty | - | boolean | 否 | - |
| array | - | boolean | 否 | - |
| null | - | boolean | 否 | - |
| object | - | boolean | 否 | - |
| float | - | boolean | 否 | - |
| number | - | boolean | 否 | - |
| missingNode | - | boolean | 否 | - |
| bigDecimal | - | boolean | 否 | - |
| floatingPointNumber | - | boolean | 否 | - |
| bigInteger | - | boolean | 否 | - |
| nodeType | - | string | 否 | - |
| valueNode | - | boolean | 否 | - |
| container | - | boolean | 否 | - |
| integralNumber | - | boolean | 否 | - |
| string | - | boolean | 否 | - |
| textual | - | boolean | 否 | - |
| long | - | boolean | 否 | - |
| short | - | boolean | 否 | - |
| int | - | boolean | 否 | - |
| double | - | boolean | 否 | - |
| boolean | - | boolean | 否 | - |
| binary | - | boolean | 否 | - |
| pojo | - | boolean | 否 | - |
| embeddedValue | - | boolean | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": [
		{
			"season": "",
			"map": ""
		}
	],
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.season | - | string | 赛季名称 |
| data.map | - | string | 地形 |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 添加作业

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-09-12 09:48:41

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 已完成

**接口URL**

> /api/job/jjc/add

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
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

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| season | S30 | string | 否 | 赛季 |
| title | 测试标题 | string | 是 | 标题 |
| remark | - | string | 否 | 简介 |
| attack.studentId | 10000 | integer | 否 | 学生id |
| attack.starGrade | - | integer | 否 | 星级0-N |
| attack.hasWeapon | - | integer | 否 | 有无专武 0没有，否则是星级 |
| attack.slotIndex | 1 | integer | 否 | 站位信息 |
| attack.squadType | Main | string | 否 | 弃用 |
| defend.studentId | 10000 | integer | 否 | 学生id |
| defend.starGrade | - | integer | 否 | 星级0-N |
| defend.hasWeapon | - | integer | 否 | 有无专武 0没有，否则是星级 |
| defend.slotIndex | 1 | integer | 否 | 站位信息 |
| defend.squadType | Main | string | 否 | 弃用 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": "",
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data | - | string | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 查询作业

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-09-12 10:49:26

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> /api/job/jjc/query

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
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

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| season | S30 | string | 是 | 赛季 |
| queryType | - | integer | 否 | 查询类型0 点赞,1时间倒序 |
| matchType | - | integer | 否 | 匹配类型 0普通，1精确 |
| list.studentId | 10000 | integer | 否 | 学生id |
| list.slotIndex | 1 | integer | 否 | 站位信息 |
| page | 1 | integer | 否 | 页 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"page": 0,
		"size": 0,
		"totalPages": 0,
		"totalData": 0,
		"records": [
			{
				"jobId": 0,
				"title": "",
				"authorName": "",
				"remark": "",
				"attack": [
					{
						"studentId": 0,
						"starGrade": 0,
						"hasWeapon": 0,
						"slotIndex": 0,
						"squadType": 0,
						"bulletType": ""
					}
				],
				"defend": [
					{
						"studentId": 0,
						"starGrade": 0,
						"hasWeapon": 0,
						"slotIndex": 0,
						"squadType": 0,
						"bulletType": ""
					}
				],
				"status": {
					"userLikeStatus": 0,
					"like": 0,
					"negative": 0,
					"views": 0
				},
				"comments": {
					"id": 0,
					"user": {
						"id": 0,
						"nickname": "",
						"avatar": ""
					},
					"content": "",
					"giveLike": {
						"like": 0,
						"click": 0,
						"userLiked": 0
					},
					"updateTime": 0,
					"children": {
						"page": 0,
						"size": 0,
						"totalPages": 0,
						"totalData": 0,
						"records": [
							""
						],
						"lastPage": ""
					}
				},
				"updateTime": 0,
				"authDelete": ""
			}
		],
		"lastPage": ""
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.page | - | integer | 页 |
| data.size | - | integer | 单页显示数据量 |
| data.totalPages | - | integer | 总页数 |
| data.totalData | - | integer | 总数据量 |
| data.records.jobId | - | integer | 作业id |
| data.records.title | - | string | 标题 |
| data.records.authorName | - | string | 作者 |
| data.records.remark | - | string | 简介 |
| data.records.attack.studentId | - | integer | 学生id |
| data.records.attack.starGrade | - | integer | 星级0-N |
| data.records.attack.hasWeapon | - | integer | 有无专武 0没有，否则是星级 |
| data.records.attack.slotIndex | - | integer | 站位信息 |
| data.records.attack.squadType | - | integer | 1前排，2后排 |
| data.records.attack.bulletType | - | string | 类型 |
| data.records.defend.studentId | - | integer | 学生id |
| data.records.defend.starGrade | - | integer | 星级0-N |
| data.records.defend.hasWeapon | - | integer | 有无专武 0没有，否则是星级 |
| data.records.defend.slotIndex | - | integer | 站位信息 |
| data.records.defend.squadType | - | integer | 1前排，2后排 |
| data.records.defend.bulletType | - | string | 类型 |
| data.records.status.userLikeStatus | - | integer | 用户的点赞状态，0无状态，1点赞，2点踩 |
| data.records.status.like | - | integer | 点赞人数 |
| data.records.status.negative | - | integer | 点踩人数 |
| data.records.status.views | - | integer | 浏览量 |
| data.records.status | - | object | - |
| data.records.comments.id | - | integer | 评论id |
| data.records.comments.user.id | - | integer | 用户id |
| data.records.comments.user.nickname | - | string | 用户名称 |
| data.records.comments.user.avatar | - | string | 用户头像 |
| data.records.comments.user | - | object | - |
| data.records.comments.content | - | string | 评论内容,带有@信息或者是回复某个用户信息时的特殊格式如下
暂时未设置 |
| data.records.comments.giveLike.like | - | integer | 点赞 |
| data.records.comments.giveLike.click | - | integer | 点踩 |
| data.records.comments.giveLike.userLiked | - | integer | 用户是否点赞 |
| data.records.comments.giveLike | - | object | - |
| data.records.comments.updateTime | - | integer | 评论时间-UTC+8 |
| data.records.comments.children.page | - | integer | 页 |
| data.records.comments.children.size | - | integer | 单页显示数据量 |
| data.records.comments.children.totalPages | - | integer | 总页数 |
| data.records.comments.children.totalData | - | integer | 总数据量 |
| data.records.comments.children.records.0 | - | array | 数据 |
| data.records.comments.children.lastPage | - | boolean | - |
| data.records.comments.children | - | object | - |
| data.records.comments | - | object | - |
| data.records.updateTime | - | integer | - |
| data.records.authDelete | - | boolean | 是否有删除权限 |
| data.lastPage | - | boolean | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 点赞接口

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-09-12 17:50:57

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> /api/job/jjc/like

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"jobId": 0,
	"status": 1
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobId | - | integer | 否 | 作业或评论id |
| status | 1 | integer | 否 | 0取消点赞，1点赞，2点踩 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": "",
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data | - | string | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 查询作业评论

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-09-20 20:46:08

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> /api/job/jjc/query_comments

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"jobId": 1,
	"type": 0,
	"commentId": 0,
	"page": 1
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobId | 1 | integer | 否 | 作业id |
| type | - | integer | 否 | 查询类型0点赞倒序，1时间到序，2时间正序 |
| commentId | - | integer | 否 | 评论id，默认0，如果按照评论查询子评论时 type类型失效，默认按照时间正序排序 |
| page | 1 | integer | 否 | 第几页 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"page": 0,
		"size": 0,
		"totalPages": 0,
		"totalData": 0,
		"records": [
			""
		],
		"lastPage": ""
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.page | - | integer | 页 |
| data.size | - | integer | 单页显示数据量 |
| data.totalPages | - | integer | 总页数 |
| data.totalData | - | integer | 总数据量 |
| data.records.0 | - | array | 数据 |
| data.lastPage | - | boolean | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 添加评论

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-09-21 04:50:26

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> /api/job/jjc/add_comments

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"jobId": 1,
	"commentId": 0,
	"content": ""
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobId | 1 | integer | 否 | 作业id |
| commentId | - | integer | 否 | 回复的评论id，如果是在作业下面评论则为0 |
| content | - | string | 否 | 评论内容
暂时不支持图片 |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": {
		"id": 0,
		"user": {
			"id": 0,
			"nickname": "",
			"avatar": ""
		},
		"content": "",
		"giveLike": {
			"like": 0,
			"click": 0,
			"userLiked": 0
		},
		"updateTime": 0,
		"children": {
			"page": 0,
			"size": 0,
			"totalPages": 0,
			"totalData": 0,
			"records": [
				""
			],
			"lastPage": ""
		}
	},
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data.id | - | integer | 评论id |
| data.user.id | - | integer | 用户id |
| data.user.nickname | - | string | 用户名称 |
| data.user.avatar | - | string | 用户头像 |
| data.user | - | object | - |
| data.content | - | string | 评论内容,带有@信息或者是回复某个用户信息时的特殊格式如下
暂时未设置 |
| data.giveLike.like | - | integer | 点赞 |
| data.giveLike.click | - | integer | 点踩 |
| data.giveLike.userLiked | - | integer | 用户是否点赞 |
| data.giveLike | - | object | - |
| data.updateTime | - | integer | 评论时间-UTC+8 |
| data.children.page | - | integer | 页 |
| data.children.size | - | integer | 单页显示数据量 |
| data.children.totalPages | - | integer | 总页数 |
| data.children.totalData | - | integer | 总数据量 |
| data.children.records.0 | - | array | 数据 |
| data.children.lastPage | - | boolean | - |
| data.children | - | object | - |
| data | - | object | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 删除作业

> 创建人: 西行寺雨季

> 更新人: 西行寺雨季

> 创建时间: 2024-09-28 14:59:25

> 更新时间: 2026-03-08 20:59:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> /api/job/jjc/delete_comments

| 环境  | URL |
| --- | --- |
| API | https://api.arona.icu |

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"jobId": 1
}
```

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobId | 1 | integer | 否 | 作业id或评论id |

**认证方式**

> 继承父级

**响应示例**

* OK(200)

```javascript
{
	"code": 0,
	"crypt": "",
	"message": "",
	"data": "",
	"traceId": "",
	"flowMillisecond": 0
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| code | - | integer | - |
| crypt | - | boolean | - |
| message | - | string | - |
| data | - | string | - |
| traceId | - | string | - |
| flowMillisecond | - | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**
