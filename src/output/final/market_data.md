---
title: "Analytical"
pathName: /docs/desktop/market_data
---

NinjaScript provides a number of methods and properties useful for analyzing and identifying specific conditions within [Series&lt;t&gt;](/docs/desktop/seriest) collections. Some of these methods test a condition and return true or false, while others return an int-based bar index or other numerical value. A list of analytical methods can be found below:

## Methods and Properties

|  |  |
| --- | --- |
| [CountIf()](/docs/desktop/countif) | Counts the number of occurrences of the test condition |
| [CrossAbove()](/docs/desktop/crossabove) | Evaluates a cross above condition |
| [CrossBelow()](/docs/desktop/crossbelow) | Evaluates a cross below condition |
| [GetCurrentAsk()](/docs/desktop/getcurrentask) | Returns the current Ask price |
| [GetCurrentAskVolume()](/docs/desktop/getcurrentaskvolume) | Returns the current Ask volume |
| [GetCurrentBid()](/docs/desktop/getcurrentbid) | Returns the current Bid price |
| [GetCurrentBidVolume()](/docs/desktop/getcurrentbidvolume) | Returns the current Bid volume |
| [GetMedian()](/docs/desktop/getmedian) | Returns the median value of the specified series |
| [HighestBar()](/docs/desktop/highestbar) | Returns the number of bars ago the highest price value occurred |
| [IsFalling()](/docs/desktop/falling) | Evaluates a falling condition |
| [IsRising()](/docs/desktop/rising) | Evaluates a rising condition |
| [Least Recent Occurrence (LRO)](/docs/desktop/least_recent_occurence_lro) | Returns the number of bars ago that the least recent occurrence of a test condition evaluated to true |
| [LowestBar()](/docs/desktop/lowestbar) | Returns the number of bars ago the lowest price value occurred |
| [Most Recent Occurrence (MRO)](/docs/desktop/most_recent_occurence_mro) | Returns the number of bars ago that the most recent occurrence of a test condition evaluated to true |
| [Slope()](/docs/desktop/slope) | Returns a measurement of the steepness of a price series measured by the change over time |
| [TickSize](/docs/desktop/ticksize) | The value of 1 tick for the corresponding instrument |
| [ToDay()](/docs/desktop/today) | Calculates an integer value representing a date |
| [ToTime()](/docs/desktop/totime) | Calculates an integer value representing a time |
