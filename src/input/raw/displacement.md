










 


Displacement







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?displacement.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt; [AddPlot()](addplot.htm) &gt;
Displacement | [Previous page](areplotsconfigurable.htm)
[Return to chapter overview](addplot.htm)










Definition
----------


An offset value that shifts the visually displayed value of an indicator.


 


Property Value
--------------


An int value that represents the number of bars ago to offset with.


 


Syntax
------


Displacement



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         Displacement = 2; // Plots the indicator value from 2 bars ago on the current bar     
         AddPlot(Brushes.Orange, "SMA");
     }
} |






 
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
 
 
 



