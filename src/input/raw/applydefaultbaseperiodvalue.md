










 


ApplyDefaultBasePeriodValue()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?applydefaultbaseperiodvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
ApplyDefaultBasePeriodValue() | [Previous page](addbar.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Sets the default base values used for the [BarsPeriod](barsperiod.htm) selected by the user (e.g., the default PeriodValue, DaysToLoad, etc.) for your custom Bar Type.


 


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


 


public override void ApplyDefaultBasePeriodValue(BarsPeriod period)


{


 


}


 



Examples
--------




| ns |
| --- |
| public override void ApplyDefaultBasePeriodValue(BarsPeriod period)
{
   //sets the default Minute bars period value to 1, and days to load to 5
if (period.BaseBarsPeriodType == BarsPeriodType.Minute)
{
   period.BaseBarsPeriodValue = 1;
   DaysToLoad = 5;
}
   //sets the default Tick bars period value to 150, and days to load to 3
else if (period.BaseBarsPeriodType == BarsPeriodType.Tick)
{
 period.BaseBarsPeriodValue = 150;
 DaysToLoad = 3;
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
 
 
 



