---
section: guides
title: Scaling out of a position
pathName: scaling_out_of_a_position
parent: reference_samples
status: imported
---

A common technique used by discretionary traders is scaling in and scaling out of a position. To scale out of a position refers to closing a portion of your position when you hit a profit target and then raising your stop to close your remaining portion later.

## Key concepts in this example

* Submitting Profit Target orders
* Submitting Trailing Stop orders
* Closing half of your position at a time

## Important related documentation

* [MarketPosition](position_marketposition)
* [SetProfitTarget()](setprofittarget)
* [SetTrailStop()](settrailstop)
* [EntriesPerDirection*](entriesperdirection)
* [EntryHandling*](entryhandling)
* [SetStopLoss()](setstoploss)

* Entry handling properties can be either programmatically set or set through the Strategy dialog window

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file

[SampleScaleOut_NT8.zip](samples/SampleScaleOut_NT8.zip)

```
