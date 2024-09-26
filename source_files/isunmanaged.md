










 


IsUnmanaged







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isunmanaged.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Unmanaged Approach](unmanaged_approach.htm) &gt;
IsUnmanaged | [Previous page](ignoreoverfill.htm)
[Return to chapter overview](unmanaged_approach.htm)










Definition
----------


Determines if the strategy will be using Unmanaged order methods. 


 




|  |
| --- |
| Note: Unmanaged order methods and [Managed order methods](managed_approach.htm) CANNOT be used interchangeably.  When IsUnmanaged is set to true, calling managed order methods such as EnterLong(), SetStopLoss(), etc, will generate an error which will be displayed on the [Log tab](log_tab2.htm) of the Control Center. |



 


 


Property Value
--------------


This property returns true if the strategy will use Unmanaged order methods; otherwise, false. Default is set to false. 


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


IsUnmanaged


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Use Unmanaged order methods
         IsUnmanaged = true;
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
 
 
 



