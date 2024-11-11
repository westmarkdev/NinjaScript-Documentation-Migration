---
title: Darvas
pathName: darvas
parent: system_indicator_methods
section: references
status: check
---

## Description

A trading strategy that was developed in 1956 by former ballroom dancer Nicolas Darvas. Darvas' trading technique involved buying into stocks that were trading at new 52-week highs with correspondingly high volumes.

... Courtesy of [Investopedia](investopedia)

## Syntax

**Darvas()**

**Darvas(ISeries`<double>` input)**

### Returns the upper value

**Darvas().Upper[int barsAgo]**

**Darvas(ISeries`<double>` input).Upper[int barsAgo]**

### Returns the lower value

**Darvas().Lower[int barsAgo]**

**Darvas(ISeries`<double>` input).Lower[int barsAgo]**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* input
* Indicator source data ([?](valid_input_data_for_indicator.md))
{% /table %}

## Examples

```csharp
// Prints the current upper Darvas value
double value = Darvas().Upper[0];
Print("The current upper Darvas value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
