










 


State







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?state.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnStateChange()](onstatechange.htm) &gt;
State | [Previous page](setstate.htm)
[Return to chapter overview](onstatechange.htm)










Definition
----------


Represents the current progression of the object as it advances from setup, processing data, to termination.  These states can be used for setting up or declaring various resources and properties. 


 




|  |
| --- |
| Note:  More detailed explanation of various states along with examples can be found in the [OnStateChange()](onstatechange.htm) method section of this help guide.  You can also attempt to set a new State using the [SetState()](setstate.htm) method. |



 



Property Value
--------------


An enum value representing the current state of the object.  Possible values are:




|  |  |
| --- | --- |
| SetDefaults | Default values are set (pushed to UI). |
| Configure | User the presses the OK or Apply button. |
| Active | Object is configured and is ready to receive instructions |
| DataLoaded | All data series have been loaded |
| Historical | Begins to process historical data |
| Transition | Finished processing historical data |
| Realtime | Begins to process realtime data. |
| Terminated | Begins to shut down |



 


Syntax
------


State


 


 



Examples
--------




| ns Understanding the sequence of States |
| --- |
| protected override void OnStateChange()
{         
   Print(DateTime.Now + ": Current State is State."+State);
} |



 


 




|  |
| --- |
| ns Using State to only process real-time data |
| protected override void OnBarUpdate()
{
   // only process real-time OnBarUpdate events
   if (State == State.Historical)
     return;
      
   //rest of logic           
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
 
 
 



