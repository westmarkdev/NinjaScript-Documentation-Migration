










 


Analytical







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?market_data.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Analytical | [Previous page](share.htm)
[Return to chapter overview](common.htm)










NinjaScript provides a number of methods and properties useful for analyzing and identifying specific conditions within [Series<t>](seriest.htm) collections. Some of these methods test a condition and return true or false, while others return an int-based bar index or other numerical value. A list of analytical methods can be found below:


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [CountIf()](countif.htm) | Counts the number of occurrences of the test condition |
| [CrossAbove()](crossabove.htm) | Evaluates a cross above condition |
| [CrossBelow()](crossbelow.htm) | Evaluates a cross below condition |
| [GetCurrentAsk()](getcurrentask.htm) | Returns the current Ask price |
| [GetCurrentAskVolume()](getcurrentaskvolume.htm) | Returns the current Ask volume |
| [GetCurrentBid()](getcurrentbid.htm) | Returns the current Bid price |
| [GetCurrentBidVolume()](getcurrentbidvolume.htm) | Returns the current Bid volume |
| [GetMedian()](getmedian.htm) | Returns the median value of the specified series |
| [HighestBar()](highestbar.htm) | Returns the number of bars ago the highest price value occurred |
| [IsFalling()](falling.htm) | Evaluates a falling condition |
| [IsRising()](rising.htm) | Evaluates a rising condition |
| [Least Recent Occurrence (LRO)](least_recent_occurence_lro.htm) | Returns the number of bars ago that the least recent occurrence of a test condition evaluated to true |
| [LowestBar()](lowestbar.htm) | Returns the number of bars ago the lowest price value occurred |
| [Most Recent Occurrence (MRO)](most_recent_occurence_mro.htm) | Returns the number of bars ago that the most recent occurrence of a  test condition evaluated to true |
| [Slope()](slope.htm) | Returns a measurement of the steepness of a price series measured by the change over time |
| [TickSize](ticksize.htm) | The value of 1 tick for the corresponding instrument |
| [ToDay()](today.htm) | Calculates an integer value representing a date |
| [ToTime()](totime.htm) | Calculates an integer value representing a time |






 
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
 
 
 



</t>