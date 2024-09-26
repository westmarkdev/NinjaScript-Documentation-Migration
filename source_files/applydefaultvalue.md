










 


ApplyDefaultValue







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?applydefaultvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
ApplyDefaultValue | [Previous page](applydefaultbaseperiodvalue.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Sets the default [BarsPeriod](barsperiod.htm) values used for a custom Bar Type. 


 


Method Return Value
-------------------


This method does not return a value.


 


Parameters
----------




|  |  |
| --- | --- |
| period | The [BarsPeriod](barsperiod.htm) chosen by the user when utilizing this Bars type |





Syntax
------


You must override the method in your Bars Type with the following syntax:


 


public override void ApplyDefaultValue(BarsPeriod period)  

{  

   

}


 


Examples
--------




| ns |
| --- |
| public override void ApplyDefaultValue(BarsPeriod period)
{
 period.BarsPeriodTypeName = "MyBarType";
 period.Value = 1;
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
 
 
 



