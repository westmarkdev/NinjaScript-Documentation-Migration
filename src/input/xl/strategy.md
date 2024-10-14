










 


Strategy







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?strategy.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Strategy | [Previous page](signature.htm)
[Return to chapter overview](language_reference_wip.htm)










The methods and properties covered in this section are unique to custom strategy development.


 


In this section
---------------




|  |  |
| --- | --- |
| [Account](strategy_account.htm) | Represents the real-world or simulation Account configured for the strategy. |
| [AddChartIndicator()](addchartindicator.htm) | Adds an indicator to the strategy only for the purpose of displaying it on a chart. |
| [AddPerformanceMetric()](addperformancemetric.htm) | Adds an instance of custom [Performance Metric](performancemetrics.htm) to a strategy used in strategy calculations. |
| [ATM Strategy Methods](atm_strategy_methods.htm) | Adds ATM strategies to manage your position |
| [BarsRequiredToTrade](barsrequiredtotrade.htm) | The number of historical bars required before the strategy starts processing order methods called in the [OnBarUpdate()](onbarupdate.htm) method. |
| [BarsSinceEntryExecution()](barssinceentryexecution.htm) | Returns the number of bars that have elapsed since the last specified entry. |
| [BarsSinceExitExecution()](barssinceexitexecution.htm) | Returns the number of bars that have elapsed since the last specified exit. |
| [ChartIndicators](chartindicators.htm) | Contains a collection of Indicators which have been added to the strategy instance using [AddChartIndicator()](addchartindicator.htm). |
| [CloseStrategy()](closestrategy.htm) | Cancels all working orders, closes any existing positions, and finally disables the strategy. |
| [ConnectionLossHandling](connectionlosshandling.htm) | Sets the manner in which your strategy will behave when a connection loss is detected. |
| [DaysToLoad](daystoload.htm) | Determines the number of trading days which will be configured when loading the strategy from the Strategies Grid. |
| [DefaultQuantity](defaultquantity.htm) | An order size variable that can be set either programmatically or overriden via the Strategy that determines the quantity of an entry order. |
| [DisconnectDelaySeconds](disconnectdelayseconds.htm) | Determines the amount of time a disconnect would have to last before [connection loss handling](connectionlosshandling.htm) takes action. |
| [EntriesPerDirection](entriesperdirection.htm) | Determines the maximum number of entries allowed per direction while a position is active based on the [EntryHandling](entryhandling.htm) property. |
| [EntryHandling](entryhandling.htm) | Sets the manner in how entry orders will handle. |
| [Execution](execution.htm) | Represents a read only interface that exposes information regarding an execution (filled order) resulting from an order and is passed as a parameter in the [OnExecutionUpdate()](onexecutionupdate.htm) method. |
| [ExitOnSessionCloseSeconds](exitonsessioncloseseconds.htm) | The number of seconds before the actual session end time that the "[IsExitOnSessionCloseStrategy](isexitonsessionclosestrategy.htm)" function will trigger. |
| [IncludeCommission](includecommission.htm) | Determines if the strategy performance results will include commission on a historical backtest. |
| [IncludeTradeHistoryInBacktest](includetradehistoryinbacktest.htm) | Determines if the strategy will save orders, trades, and execution history. |
| [IsAdoptAccountPositionAware](isadoptaccountpositionaware.htm) | Determines if the strategy is programmed in a manner capable of handling  real-world account positions. |
| [IsExitOnSessionCloseStrategy](isexitonsessionclosestrategy.htm) | Determines if the strategy will cancel all strategy generated orders and close all open strategy positions at the close of the session. |
| [IsFillLimitOnTouch](isfilllimitontouch.htm) | Determines if the strategy will use a more liberal fill algorithm for back-testing purposes only. |
| [IsInstantiatedOnEachOptimizationIteration](isinstantiatedoneachoptimizationiteration.htm) | Determines if the strategy should be re-instantiated (re-created) after each optimization run when using the [Strategy Analyzer Optimizer](optimize_a_strategy.htm). |
| [IsInStrategyAnalyzer](isinstrategyanalyer.htm) | Determines if the current NinjaScript Strategy is run from a Strategy Analyzer chart. |
| [IsTradingHoursBreakLineVisible](istradinghoursbreaklinevisible.htm) | Plots trading hours break lines on the indicator panel. |
| [IsWaitUntilFlat](iswaituntilflat.htm) | Indicates the strategy is currently waiting until a flat position is detected before submitting live orders. |
| [NumberRestartAttempts](numberrestartattempts.htm) | Determines the maximum number of restart attempts allowed within the last x minutes defined in [RestartsWithinMinutes](restartswithinminutes.htm) when the strategy experiences a connection loss. |
| [OnAccountItemUpdate()](onaccountitemupdate.htm) | An event driven method used for strategies which is called for each AccountItem update for the account on which the strategy is running. |
| [OnExecutionUpdate()](onexecutionupdate.htm) | An event driven method which is called on an incoming execution of an order managed by a strategy. |
| [OnOrderTrace()](onordertrace.htm) | An event driven method used for strategies which will allow you to customize the output of [TraceOrders](traceorders.htm).   |
| [OnOrderUpdate()](onorderupdate.htm) | An event driven method which is called each time an order managed by a strategy changes state. |
| [OnPositionUpdate()](onpositionupdate.htm) | An event driven method which is called each time the position of a strategy changes state. |
| [OptimizationPeriod](order.htm) | Reserved for [Walk-Forward Optimization](walk_forward_optimize_a_strate.htm), this property determines the number of days used for the "in sample" backtest period for a given strategy.  See also [TestPeriod](testperiod.htm). |
| [Order](order.htm) | Represents a read only interface that exposes information regarding an order. |
| [Order Methods](order_methods.htm) | NinjaScript provides several approaches you can use for order placement within your NinjaScript strategy. |
| [OrderFillResolution](orderfillresolution.htm) | Determines how strategy orders are filled during historical states.  |
| [OrderFillResolutionType](orderfillresolutiontype.htm) | Determines the bars type which will be used for historical fill processing. |
| [OrderFillResolutionValue](orderfillresolutionvalue.htm) | Determines the bars period interval value which will be used for historical fill processing. |
| [PerformanceMetrics](strategy_performancemetrics.htm) | Holds an array of [PerformanceMetrics](performancemetrics.htm) objects that represent custom metrics that can be used for strategy calcuations. |
| [Plots](strategy_plots.htm) | A collection holding all of the Plot objects that define their visualization characteristics. |
| [Position](position.htm) | Represents position related information that pertains to an instance of a strategy. |
| [PositionAccount](positionaccount.htm) | Represents position related information that pertains to real-world account (live or simulation).   |
| [Positions](positions.htm) | Holds an array of [Position](position.htm) objects that represent positions managed by the strategy. |
| [PositionsAccount](positionsaccount.htm) | Holds an array of [PositionAccount](positionaccount.htm) objects that represent positions managed by the strategy's account. |
| [RealtimeErrorHandling](realtimeerrorhandling.htm) | Defines the behavior of a strategy when a strategy generated order is returned from the broker's server in a "Rejected" state. |
| [RestartsWithinMinutes](restartswithinminutes.htm) | Determines within how many minutes the strategy will attempt to restart. |
| [SetOrderQuantity](setorderquantity.htm) | Determines how order sizes are calculated for a given strategy. |
| [Slippage](slippage.htm) | Sets the amount of slippage in ticks per execution used in performance calculations during backtests. |
| [StartBehavior](startbehavior.htm) | Sets the start behavior of the strategy. See [Syncing Account Positions](syncing_account_positions.htm) for more information. |
| [StopTargetHandling](stoptargethandling.htm) | Determines how stop and target orders are submitted during an entry order execution.  |
| [StrategyBaseConverter](strategybaseconverter.htm) | A custom TypeConverter class handling the designed behavior of an strategy's property descriptor collection.  |
| [SystemPerformance](systemperformance.htm) | The SystemPerformance object holds all trades and trade performance data generated by a strategy. |
| [TestPeriod](testperiod.htm) | Reserved for [Walk-Forward Optimization](walk_forward_optimize_a_strate.htm), this property determines the number of days used for the "out of sample" backtest period for a given strategy. |
| [TimeInForce](timeinforce.htm) | Sets the time in force property for all orders generated by a strategy. |
| [TraceOrders](traceorders.htm) | Determines if OnOrderTrace() would be called for a given strategy. |
| [Trade](trade.htm) | A Trade is a completed buy/sell or sell/buy transaction. It consists of an entry and exit execution.  |
| [TradeCollection](tradecollection.htm) | A collection of [Trade](trade.htm) objects. |
| [TradesPerformanceValues](tradesperformancevalues.htm) | Performance values of a [collection](tradecollection.htm) of [Trade](trade.htm) objects. |
| [WaitForOcoClosingBracket](waitforococlosingbracket.htm) | Determines if the strategy will submit both legs of an OCO bracket before submitting the pair to the broker. |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



