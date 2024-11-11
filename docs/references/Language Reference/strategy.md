---
title: Strategy
pathName: strategy
parent: language_reference
order: 14
status: imported
section: references
---

The methods and properties covered in this section are unique to custom strategy development.

## In this section

{% table %}

* [Strategy Account](strategy_account)
* Represents the real-world or simulation Account configured for the strategy.

---

* [AddChartIndicator()](addchartindicator)
* Adds an indicator to the strategy only for the purpose of displaying it on a chart.

---

* [AddPerformanceMetric()](addperformancemetric)
* Adds an instance of custom **Performance Metric** to a strategy used in strategy calculations.

---

* [ATM Strategy Methods](atm_strategy_methods)
* Adds ATM strategies to manage your position

---

* [BarsRequiredToTrade](barsrequiredtotrade)
* The number of historical bars required before the strategy starts processing order methods called in the **OnBarUpdate()** method.

---

* [BarsSinceEntryExecution()](barssinceentryexecution)
* Returns the number of bars that have elapsed since the last specified entry.

---

* [BarsSinceExitExecution()](barssinceexitexecution)
* Returns the number of bars that have elapsed since the last specified exit.

---

* [ChartIndicators](chartindicators)
* Contains a collection of Indicators which have been added to the strategy instance using **AddChartIndicator()**.

---

* [CloseStrategy()](closestrategy)
* Cancels all working orders, closes any existing positions, and finally disables the strategy.

---

* [ConnectionLossHandling](connectionlosshandling)
* Sets the manner in which your strategy will behave when a connection loss is detected.

---

* [DaysToLoad](daystoload)
* Determines the number of trading days which will be configured when loading the strategy from the Strategies Grid.

---

* [DefaultQuantity](defaultquantity)
* An order size variable that can be set either programmatically or overridden via the Strategy that determines the quantity of an entry order.

---

* [DisconnectDelaySeconds](disconnectdelayseconds)
* Determines the amount of time a disconnect would have to last before **connection loss handling** takes action.

---

* [EntriesPerDirection](entriesperdirection)
* Determines the maximum number of entries allowed per direction while a position is active based on the **EntryHandling** property.

---

* [EntryHandling](entryhandling)
* Sets the manner in how entry orders will handle.

---

* [Execution](execution)
* Represents a read-only interface that exposes information regarding an execution (filled order) resulting from an order and is passed as a parameter in the **OnExecutionUpdate()** method.

---

* [ExitOnSessionCloseSeconds](exitonsessioncloseseconds)
* The number of seconds before the actual session end time that the "**IsExitOnSessionCloseStrategy**" function will trigger.

---

* [IncludeCommission](includecommission)
* Determines if the strategy performance results will include commission on a historical backtest.

---

* [IncludeTradeHistoryInBacktest](includetradehistoryinbacktest)
* Determines if the strategy will save orders, trades, and execution history.

---

* [IsAdoptAccountPositionAware](isadoptaccountpositionaware)
* Determines if the strategy is programmed in a manner capable of handling real-world account positions.

---

* [IsExitOnSessionCloseStrategy](isexitonsessionclosestrategy)
* Determines if the strategy will cancel all strategy-generated orders and close all open strategy positions at the close of the session.

---

* [IsFillLimitOnTouch](isfilllimitontouch)
* Determines if the strategy will use a more liberal fill algorithm for back-testing purposes only.

---

* [IsInstantiatedOnEachOptimizationIteration](isinstantiatedoneachoptimizationiteration)
* Determines if the strategy should be re-instantiated (re-created) after each optimization run when using the **Strategy Analyzer Optimizer**.

---

* [IsInStrategyAnalyzer](isinstrategyanalyer)
* Determines if the current **NinjaScript Strategy** is run from a Strategy Analyzer chart.

---

* [IsTradingHoursBreakLineVisible](istradinghoursbreaklinevisible)
* Plots trading hours break lines on the indicator panel.

---

* [IsWaitUntilFlat](iswaituntilflat)
* Indicates the strategy is currently waiting until a flat position is detected before submitting live orders.

---

* [NumberRestartAttempts](numberrestartattempts)
* Determines the maximum number of restart attempts allowed within the last x minutes defined in **RestartsWithinMinutes** when the strategy experiences a connection loss.

---

* [OnAccountItemUpdate()](onaccountitemupdate)
* An event-driven method used for strategies which is called for each AccountItem update for the account on which the strategy is running.

---

* [OnExecutionUpdate()](onexecutionupdate)
* An event-driven method which is called on an incoming execution of an order managed by a strategy.

---

* [OnOrderTrace()](onordertrace)
* An event-driven method used for strategies which will allow you to customize the output of **TraceOrders**.

---

* [OnOrderUpdate()](onorderupdate)
* An event-driven method which is called each time an order managed by a strategy changes state.

---

* [OnPositionUpdate()](onpositionupdate)
* An event-driven method which is called each time the position of a strategy changes state.

---

* [OptimizationPeriod](optimizationperiod)
* Reserved for **Walk-Forward Optimization**, this property determines the number of days used for the "in sample" backtest period for a given strategy. See also **TestPeriod**.

---

* [Order](order)
* Represents a read-only interface that exposes information regarding an order.

---

* [Order Methods](order_methods)
* **NinjaScript** provides several approaches you can use for order placement within your **NinjaScript strategy**.

---

* [OrderFillResolution](orderfillresolution)
* Determines how strategy orders are filled during historical states.

---

* [OrderFillResolutionType](orderfillresolutiontype)
* Determines the bars type which will be used for historical fill processing.

---

* [OrderFillResolutionValue](orderfillresolutionvalue)
* Determines the bars period interval value which will be used for historical fill processing.

---

* [PerformanceMetrics](performancemetrics)
* Holds an array of **PerformanceMetrics** objects that represent custom metrics that can be used for strategy calculations.

---

* [Plots](strategy_plots)
* A collection holding all of the Plot objects that define their visualization characteristics.

---

* [Position](position)
* Represents position-related information that pertains to an instance of a strategy.

---

* [PositionAccount](positionaccount)
* Represents position-related information that pertains to real-world account (live or simulation).

---

* [Positions](positions)
* Holds an array of **Position** objects that represent positions managed by the strategy.

---

* [PositionsAccount](positionsaccount)
* Holds an array of **PositionAccount** objects that represent positions managed by the strategy's account.

---

* [RealtimeErrorHandling](realtimeerrorhandling)
* Defines the behavior of a strategy when a strategy-generated order is returned from the broker's server in a "Rejected" state.

---

* [RestartsWithinMinutes](restartswithinminutes)
* Determines within how many minutes the strategy will attempt to restart.

---

* [SetOrderQuantity](setorderquantity)
* Determines how order sizes are calculated for a given strategy.

---

* [Slippage](slippage)
* Sets the amount of slippage in ticks per execution used in performance calculations during backtests.

---

* [StartBehavior](startbehavior)
* Sets the start behavior of the strategy. See **Syncing Account Positions** for more information.

---

* [StopTargetHandling](stoptargethandling)
* Determines how stop and target orders are submitted during an entry order execution.

---

* [StrategyBaseConverter](strategybaseconverter)
* A custom **TypeConverter** class handling the designed behavior of a strategy's property descriptor collection.

---

* [SystemPerformance](systemperformance)
* The **SystemPerformance** object holds all trades and trade performance data generated by a strategy.

---

* [TestPeriod](testperiod)
* Reserved for **Walk-Forward Optimization**, this property determines the number of days used for the "out of sample" backtest period for a given strategy.

---

* [TimeInForce](timeinforce)
* Sets the time in force property for all orders generated by a strategy.

---

* [TraceOrders](traceorders)
* Determines if **OnOrderTrace()** would be called for a given strategy.

---

* [Trade](trade)
* A Trade is a completed buy/sell or sell/buy transaction. It consists of an entry and exit execution.

---

* [TradeCollection](tradecollection)
* A collection of **Trade** objects.

---

* [TradesPerformanceValues](tradesperformancevalues)
* Performance values of a **collection** of **Trade** objects.

---

* [WaitForOcoClosingBracket](waitforococlosingbracket)
* Determines if the strategy will submit both legs of an OCO bracket before submitting the pair to the broker.
{% /table %}
