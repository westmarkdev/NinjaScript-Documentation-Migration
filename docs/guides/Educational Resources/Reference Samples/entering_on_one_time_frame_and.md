---
title: Entering on one time frame and exiting on another
pathName: entering_on_one_time_frame_and_exiting_on_another
parent: reference_samples
section: guides
status: imported
---

You can submit orders to different bars objects. This allows you the flexibility of submitting orders to different timeframes. You can watch for trade conditions across different time frames and place orders on whichever one you want. This is useful for strategies that require more finesse in the exit than the entry. You can now enter trades on longer time frames and then monitor and exit your trade on a more granular time frame.

## Key concepts in this example

* Comparing values across multiple time frames
* Submitting orders to a non-primary bar object

## Important related documentation

* [BarsArray](barsarray)
* [BarsInProgress](barsinprogress)
* [AddDataSeries()](adddataseries)
* [BarsSinceExitExecution()](barssinceexitexecution)
* [BarsRequiredToTrade()](barsrequiredtotrade)
* [EnterLongLimit()](enterlonglimit)

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file

[SampleMultiTimeFrameOrders_NT8.zip](samples/SampleMultiTimeFrameOrders_NT8.zip)
