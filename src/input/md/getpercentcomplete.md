










 


GetPercentComplete()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getpercentcomplete.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Bars Type](bars_type.htm) &gt;
GetPercentComplete() | [Previous page](getinitiallookbackdays.htm)
[Return to chapter overview](bars_type.htm)










Definition
----------


Determines the value your BarsType would return for [Bars.PercentComplete](percentcomplete.htm)


 


Method Return Value
-------------------


This method returns a double value.



Method Parameters
-----------------




|  |  |
| --- | --- |
| bars | The [bars](bars.htm) object chosen by the user when utilizing this Bars type |
| now | The DateTime value to measure |



 


 


Syntax
You must override the method in your Bars Type with the following syntax.
--------------------------------------------------------------------------------


 


public override double GetPercentComplete(Bars bars, DateTime now)  

{  

   

}



Examples
--------




| ns |
| --- |
| public override double GetPercentComplete(Bars bars, DateTime now)
{
     // Calculate the percent complete for our monthly bars
     if (now.Date &lt;= bars.LastBarTime.Date)
     {
         int month = now.Month;
         int daysInMonth = (month == 2) ? (DateTime.IsLeapYear(now.Year) ? 29 : 28) : 
               (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 ? 31 : 30);
         return (daysInMonth - (barsSeries.LastBarTime.Date.AddDays(1).Subtract(now).TotalDays / barsSeries.BarsPeriod.Value)) /
               daysInMonth; // an estimate
     }
     return 1;
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
 
 
 



