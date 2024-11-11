---
title: Halting a Strategy Once User Defined Conditions Are Met
pathName: halting_a_strategy_once_user_defined_conditions_are_met
parent: reference_samples
section: guides
status: imported
---

For error-handling, money-management or any other reason you may want to halt your strategy from processing its core program logic. Before you halt your strategy, it is best to close all positions and cancel all active orders to prevent the risk of having an unmanaged position in the market. We have provided two reference samples for these topics.

## Key concepts in the SampleHaltBasicStrategy example

* Using **PnL** statistics to determine when to halt processing of the strategy
* Cancelling active orders
* Closing active positions

## Key concepts in the SampleHaltAdvancedStrategy example

* Using a custom method to halt processing on all event-driven methods
* Advanced order handling in error situations with the **OnOrderUpdate()** method

* This is intended for strategies driven exclusively by the **OnBarUpdate()** method.

** This sample's intended audience is for advanced programmers who have programmed strategies that take advantage of event-driven methods such as, but not limited to, **OnMarketData()** or **OnOrderUpdate()** in addition to the **OnBarUpdate()** method.

## Important related documentation

* [CancelOrder()](cancel)
* [Order](order)
* [SystemPerformance](systemperformance)
* [AllTrades](alltrades)
* [TradesPerformance](tradesperformance)
* [OnMarketData()](onmarketdata)
* [OnOrderUpdate()](onorderupdate)

* This reference sample uses the **.AllTrades** property. This property will include all historical virtual trades as well as real-time trades. If you wish to only make calculations based on real-time trades you can use the **.RealtimeTrades** property.

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file

[SampleHaltAdvancedStrategy_NT8.zip](samples/SampleHaltAdvancedStrategy_NT8.zip)

[SampleHaltBasicStrategy_NT8.zip](samples/SampleHaltBasicStrategy_NT8.zip)
