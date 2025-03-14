

# 英雄联盟BP与游戏思路推荐系统

## 项目简介

本项目是一个基于大型语言模型的英雄联盟辅助工具，旨在为玩家提供实时的英雄选择（Ban/Pick）建议和游戏策略推荐。通过连接英雄联盟客户端API，获取当前对局信息，结合大模型分析能力，为玩家提供个性化的游戏建议。

## 主要功能

- **实时BP推荐**：根据当前队伍阵容和对手选择，推荐最佳的英雄选择
- **对线策略**：针对特定对线组合提供详细的对线思路和技巧
- **团队配合**：分析团队阵容优势和劣势，提供团队配合建议
- **游戏节奏**：根据阵容特点推荐合适的游戏节奏和关键时间点
- **装备推荐**：基于对局情况提供动态的装备构建建议

## 技术架构

- **前端界面**：基于PyQt5构建的桌面应用程序
- **客户端连接**：通过League Client API获取游戏数据
- **数据分析**：使用大型语言模型分析游戏数据并生成建议
- **数据存储**：本地缓存历史数据，支持离线模式

## 安装指南

### 系统要求
- Python 3.8+
- 英雄联盟客户端
- Windows 10/11 (其他系统可能需要额外配置)

### 安装步骤

1. 克隆仓库到本地
```bash
git clone https://gitee.com/dmy-wang/hextech.git
cd hextech
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行程序
```bash
python main.py
```

## 使用说明

1. 启动英雄联盟客户端并登录
2. 运行本程序
3. 进入英雄选择界面后，程序将自动连接并分析当前对局
4. 查看推荐的BP选择和游戏策略
5. 在游戏中可随时查看针对性建议

## 功能截图

![BP推荐界面](screenshots/bp_recommendation.png)
![对线策略](screenshots/lane_strategy.png)
![团队配合](screenshots/team_synergy.png)

## 开发计划

- [ ] 添加更多英雄数据和对局分析
- [ ] 支持多语言界面
- [ ] 集成游戏内覆盖显示功能
- [ ] 添加历史数据分析和个人表现评估
- [ ] 支持自定义策略偏好设置

## 技术细节

本项目利用大型语言模型的强大分析能力，结合英雄联盟的游戏机制和当前版本数据，为玩家提供个性化的游戏建议。系统通过以下步骤工作：

1. 连接英雄联盟客户端API获取实时数据
2. 分析当前选择阶段和已选/禁用英雄
3. 结合版本强势英雄数据和玩家历史数据
4. 通过大模型生成针对性建议
5. 实时更新并展示给用户

## 贡献指南

欢迎贡献代码、提出问题或建议！请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请参见 [LICENSE](LICENSE) 文件

## 联系方式

- 项目维护者：[您的名字](mailto:your.email@example.com)
- 项目主页：[GitHub仓库地址](https://github.com/yourusername/lol-assistant)

---

**免责声明**：本项目不隶属于Riot Games，不代表或反映Riot Games或任何官方参与英雄联盟的人的观点或意见。英雄联盟和Riot Games是Riot Games, Inc.的商标或注册商标。
