










 


Description







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?description.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Description | [Previous page](clone.htm)
[Return to chapter overview](common.htm)










Definition
----------


Text which is used on the UI's information box to be displayed to a user when configuration a NinjaScript object.


 


Method Return Value
-------------------


A string value representing text used to describe the object.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


Syntax
------


Description


 


 


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
}    |






 
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
 
 
 



