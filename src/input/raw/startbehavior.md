










 


StartBehavior







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?startbehavior.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
StartBehavior | [Previous page](slippage.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Sets the start behavior of the strategy. See [Syncing Account Positions](syncing_account_positions.htm) for more information.


 




|  |
| --- |
| Note:  In order to use AdoptAccountPosition you will need to first set [IsAdoptAccountPositionAware](isadoptaccountpositionaware.htm) to true. Please be sure that your strategy is specifically programmed in a manner that can accommodate account positions before using this mode. |



 


Property Value
--------------


An enum value that determines how the strategy behaves; Default value is set to StartBehavior.WaitUntilFlat.  Possible values are:





|  |
| --- |
| StartBehavior.AdoptAccountPosition |
| StartBehavior.ImmediatelySubmit |
| StartBehavior.ImmediatelySubmitSynchronizeAccount |
| StartBehavior.WaitUntilFlat |
| StartBehavior.WaitUntilFlatSynchronizeAccount |



 


Syntax
------


StartBehavior


 


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         StartBehavior = StartBehavior.WaitUntilFlat;
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
 
 
 



