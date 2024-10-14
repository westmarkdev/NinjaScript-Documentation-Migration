










 


ClearOutputWindow()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?clearoutputwindow.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
ClearOutputWindow() | [Previous page](alert.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Clears all data from the NinjaTrader [Output Window](output.htm).  


 




|  |
| --- |
| Note:  The ClearOutputWindow() method only targets the Output tab most recently determined by set [PrintTo](printto.htm) property. |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


ClearOutputWindow()


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{      
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";   
     Description = @"An indicator used to demonstrate various NinjaScript methods and properties";            
   }
   else if (State == State.Configure)
   {            
     AddDataSeries(BarsPeriodType.Minute, 5);            
   }   
   
   else if(State == State.DataLoaded)
   {
     //clear the output window as soon as the bars data is loaded
     ClearOutputWindow();         
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
 
 
 



