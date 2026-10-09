# DSP Agent

一个尝试让 AI Agent 自主游玩《戴森球计划》的实验性项目。

项目希望让 Agent 通过结构化游戏状态完成观察、规划、执行和验证，而不是依赖固定的鼠标键盘脚本。

> 当前状态：Phase 1 原型验证完成；Phase 2 Agent 核心开发进行中，当前已完成同步 Mock Agent 的最小数据模型。

## 项目目标

逐步实现一个能够：

1. 读取游戏状态。
2. 根据目标制定行动计划。
3. 通过受控接口执行操作。
4. 验证执行结果并处理失败。
5. 完成资源采集、科技研究和生产线建设。

## 系统架构

```text
Agent
  ↓
Spherewright MCP
  ↓
Spherewright BepInEx Plugin
  ↓
Dyson Sphere Program
```

当前使用 Codex 验证 MCP 工具链。后续将在仓库中实现独立的 Agent 层，包括状态模型、规划器、执行器和评估模块。

## 当前进度

### Phase 1：基础链路验证

- [x] 建立独立 Mod 测试环境
- [x] 连接 Spherewright MCP
- [x] 创建 Agent 专用测试世界
- [x] 读取玩家和世界状态
- [x] 完成一次 `observe → prepare → commit → verify` 闭环
- [x] 验证保存与重启恢复

详细环境、兼容性和测试证据见：

- [第一阶段环境与验证记录](./环境记录.md)

### Phase 2：Agent 核心

目标是实现一个独立、可靠、可测试的 Python Agent，完成：

```text
观察
→ 规划
→ 安全执行
→ 等待终态
→ 状态回读
→ 结果验证
```

#### 里程碑一：同步 Mock Agent

- [x] 建立 `dsp_agent` Python 包
- [x] 定义 `WorldState`
- [x] 定义 `Goal`
- [x] 定义 `Intent` 和 `IntentType`
- [x] 添加状态和目标的基础合法性检查
- [x] 编写数据模型手动验证程序
- [ ] 实现规则 Planner
- [ ] 实现 Mock Executor
- [ ] 实现同步 Agent 主循环

#### 里程碑二：数据和自动化测试

- [ ] 添加 JSON 状态读取
- [ ] 建立 Python 虚拟环境和依赖管理
- [ ] 添加 pytest 自动化测试
- [ ] 测试 Planner、Executor 和停止条件

#### 里程碑三：异步 Mock Agent

- [ ] 实现异步动作执行
- [ ] 添加超时、取消和动作轮询
- [ ] 验证不确定结果不会导致重复动作

#### 里程碑四：Spherewright 只读连接

- [ ] 封装 MCP 客户端
- [ ] 读取 session、player 和 resource 状态
- [ ] 将 Spherewright 返回值映射为统一状态模型

#### 里程碑五：Safe Executor

- [ ] 实现 `fresh read → prepare → commit → terminal → readback`
- [ ] 实现幂等键管理
- [ ] 处理 stale state、outcome unknown 和 quarantine
- [ ] 添加结构化日志和敏感信息脱敏

#### 里程碑六：真实游戏验收

- [ ] 自主获取至少一个新的铜矿
- [ ] 验证背包与资源节点变化
- [ ] 正常保存并验证保存结果
- [ ] 目标完成后立即停止

详细阶段目标、学习过程和验证证据见：

- [第二阶段环境与实现记录](./环境记录.md#第二阶段agent-核心开发)

### Phase 3：早期游戏任务

- [ ] 自动采集基础资源
- [ ] 自动手工制造
- [ ] 自动选择初始科技
- [ ] 建造并验证第一条生产线

## 当前局限

当前仓库已有同步 Mock Agent 的最小数据模型，但尚未实现 Planner、Executor、Agent 主循环和 Spherewright MCP 客户端，因此仍属于技术原型，而不是完整的自主游戏 Agent。

当前数据模型只用于离线学习和验证，尚未映射完整的 Spherewright 状态，也没有执行第二阶段的真实游戏写操作。

当前测试也只能证明已测试接口可用，不能证明所有 Spherewright 功能都与当前游戏版本兼容。

## 仓库结构

```text
.
├── .gitignore
├── README.md
├── dsp_agent/
│   ├── __init__.py
│   ├── demo_models.py
│   └── models.py
└── 环境记录.md
```

## 项目性质

本项目是个人学习和技术研究项目，与《戴森球计划》开发商及 Spherewright 作者无官方关联。
