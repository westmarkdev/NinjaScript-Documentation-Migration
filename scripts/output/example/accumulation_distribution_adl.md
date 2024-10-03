---
title: accumulation_distribution_adl
path: accumulation_distribution_adl
created: Thursday, October 3rd 2024, 11:50:19 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Description

There are many indicators available to measure volume and the flow of money for a particular stock, index, or security. One of the most popular volume indicators over the years has been the Accumulation/Distribution Line. The basic premise behind volume indicators, including the Accumulation/Distribution Line, is that volume precedes price. Volume reflects the amount of shares traded in a particular stock, and is a direct reflection of the money flowing into and out of a stock. Many times before a stock advances, there will be a period of increased volume just prior to the move. Most volume or money flow indicators are designed to identify early increases in positive or negative volume flow to gain an edge before the price moves. (Note: the terms "money flow" and "volume flow" are essentially interchangeable.) 

## Syntax

```csharp
ADL()  
ADL(ISeries<double> input)  
```

Returns default value:

```csharp
ADL()[int barsAgo]  
ADL(ISeries<double> input)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

| Parameter | Description |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator.htm)) |

## Example

```csharp
// Evaluates if ADL is rising
bool isRising = IsRising(ADL());
Print("Is ADL rising? " + isRising);
```

## Source Code

You can view this indicator method source code by selecting the menu `New > NinjaScript Editor > Indicators` within the NinjaTrader Control Center window.
