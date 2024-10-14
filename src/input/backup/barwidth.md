










 


BarWidth







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barwidth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
BarWidth | [Previous page](chart_style.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


The painted width of a ChartStyle bar.  This value will updated as the ChartControl is resized.


 


Property Value
--------------


A double value representing the current width the chart bars


 


Syntax
------


BarWidth


 


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name             = "Example ChartStyle";         
     ChartStyleType   = (ChartStyleType) 52;
     BarWidth         = 1;
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
 
 
 



