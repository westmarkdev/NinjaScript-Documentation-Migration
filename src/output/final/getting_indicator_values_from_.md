---
title: "Getting indicator values from a specified time"
pathName: /docs/desktop/getting_indicator_values_from_a_specified_time
---

Sometimes, you may want to access a value from a historical point in time, but have not kept track of the value to make this readily available. With NinjaScript, it is possible to pick a bar based on time to access that value. `GetBar()` returns the number of bars ago that holds the same timestamp of the time you request. This sample demonstrates how to get an indicator value from 9:30AM of the previous trading day.

## Key concepts in this example

- Obtaining a Simple Moving Average value from a specific time by referencing the bar number for that time.

## Important related documentation

- [GetBar()](/docs/desktop/getbar)
- [Draw.Line()](/docs/desktop/draw_line)
- [Time](/docs/desktop/iseries_time)
- [Sessions](/docs/desktop/tradinghours_sessions)
- [DateTime](https://learn.microsoft.com/en-us/dotnet/api/system.datetime?view=netframework-4.8)

## Import instructions

1. Download the file contained in this Help Guide topic to your PC desktop.
2. From the Control Center window, select the menu Tools > Import > NinjaScript.
3. Select the downloaded file.

[SampleGetBar_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleGetBar_NT8.zip) 

