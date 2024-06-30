# quantum-trader

## 量化交易策略系统

`quantum-trader` 是一个基于 `freqtrade` 框架的量化交易策略集。致力于为用户提供灵活、高效和可定制的量化交易解决方案。

### 主要特点

- **基于freqtrade**：`quantum-trader` 主要应用在 `freqtrade` 框架中，`freqtrade` 是一个强大且完善的量化交易框架，与 `quantum-trader` 结合可以更好、快速的扩展交易环境。
- **持续更新**：我们的交易策略正在不断地更新和优化，以适应市场的变化和捕捉新的交易机会。
- **丰富的指标库**：`quantumtrader_ta` 是 `quantum-trader` 的核心指标库，提供了多种常用的技术分析指标，帮助用户更准确地分析市场走势和交易信号。我们主要引用`ta-lib`、`pandas_ta`等大众所知的指标库，同时再根据市场上的一些成熟、创新指标做出整合和优化

### 关于quantumtrader_ta指标库

`quantumtrader_ta` 是 `quantum-trader` 的相关指标库，它包含了丰富的技术分析指标，包括但不限于移动平均线、相对强弱指数（RSI）、随机指标（Stochastic Oscillator）等。这些指标可以帮助用户更全面地分析市场，并构建有效的交易策略。

目前，`quantumtrader_ta` 指标库还在不断更新中，我们将持续添加新的指标和优化现有指标，以满足用户的不断增长的需求。

### 如何使用

1. **安装依赖**：确保您已经安装了 `freqtrade` 框架和相关的依赖项。
2. **下载与配置**：从gitee或其他分发渠道下载 `quantum-trader` 的源代码，并根据需要进行配置和扩展。
3. **编写策略**：利用 `quantumtrader_ta` 指标库中的指标，编写自己的交易策略。
4. **回测与交易**：使用 `freqtrade` 提供的回测功能验证策略的有效性，并进行实时交易。

### 贡献与反馈

我们非常欢迎社区成员对 `quantum-trader` 的贡献和反馈。如果您有任何建议、问题或改进意见，请通过GitHub的issue跟踪系统提交，或者通过其他渠道与我们取得联系。

### 许可证

`quantum-trader` 使用 [MIT 许可证](LICENSE)。这意味着您可以自由地使用、修改和分发 `quantum-trader`，但需要遵守许可证中的条款和条件。

感谢您对 `quantum-trader` 的关注和支持！我们期待与您一起构建更强大的量化交易策略系统。