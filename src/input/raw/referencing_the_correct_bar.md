










 


Referencing the correct bar







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?referencing_the_correct_bar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Tips](tips.htm) &gt;
Referencing the correct bar | [Previous page](parameter_sequencing.htm)
[Return to chapter overview](tips.htm)










When coding an indicator or strategy it is important to be able to access the intended bars for correct calculations. In NinjaScript we are able to access the bars we want through proper use of the bar's indexing.


 


The bar's indexing is setup in a reverse chronological order. This means "0" refers to the most recent bar, "1" refers to the previous bar, "2" refers to the bar before that one, etc.


 


For example, if we wanted to subtract the high and low of 10 bars ago from each other we would do this:




| ns |
| --- |
| double value = High[10] - Low[10]; |



 


Now that we know how the indexing works there are several properties and methods at our disposal that can help us access important keystone bars. The more important ones are [CurrentBar](currentbar.htm) and [BarsSinceNewTradingDay](barssincenewtradingday.htm).


 


CurrentBar
----------


CurrentBar returns an int representing the number of bars existing on the chart. This property is most useful when you want to run calculations from the very beginning of the chart.


 


For example, if you wanted to find the average high value of the first 10 bars on the chart you could do this:




| ns |
| --- |
| double highValue = 0;
int x = CurrentBar;
while (x &gt; CurrentBar - 10)
{
    highValue += High[x];
    x--;
}
Print("The average high value: " + highValue/10); |



 




|  |
| --- |
| Note: A common mistake in using CurrentBar is using it in the index to access the most recent bar. In this situation, instead of doing something like Close[CurrentBar] you will want to do Close[0]. |



 


BarsSinceNewTradingDay
----------------------


BarsSinceNewTradingDay is another property that can help you find the first bar of the current trading day. The difference between BarsSinceNewTradingDay and CurrentBar is that BarsSinceNewTradingDay resets its count whenever a new session begins. This means if you use it in an index it will only get you to the beginning of the current session and not any previous sessions.


 


For example, if you wanted to find the open of the current session you could do this:




| ns |
| --- |
| double openValue = Open[Bars.BarsSinceNewTradingDay]; |



 


The example used in the discussion about CurrentBar can also be done with Bars.BarsSinceNewTradingDay if you wanted to calculate values based on the current session instead of the start of the chart too.


 




|  |
| --- |
| Note: If you wish to access values older than 256 bars ago you will need to ensure the [MaximumBarsLookBack](maximumbarslookback.htm)is set to .Infinite. |



 


Other Properties and Methods
----------------------------


There are also a number of other properties and methods that can be useful in helping you locate the correct bars index to reference. Please take a look at these in the help guide: 


[BarsSinceEntryExecution()](barssinceentryexecution.htm)


[BarsSinceExitExecution()](barssinceexitexecution.htm)


[GetBar()](getbar.htm)


[GetDayBar()](getdaybar.htm)


[HighestBar()](highestbar.htm)


[LowestBar()](lowestbar.htm)


[LRO()](least_recent_occurence_lro.htm)


[MRO()](most_recent_occurence_mro.htm)





 
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
 
 
 



