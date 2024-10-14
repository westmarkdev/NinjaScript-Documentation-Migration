










 


MergePolicy







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barsrequest_mergepolicy.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [BarsRequest](barsrequest.htm) &gt;
MergePolicy | [Previous page](request.htm)
[Return to chapter overview](barsrequest.htm)










Definition
----------


Determines the merge policy of the bars request.


 




|  |
| --- |
| Notes:
•This property is ONLY applicable to Futures contracts•General information regrading merge policies can be found from the [Market Data Configuration](merge_policy.htm) section•For an Instruments configured merge policy, please see the [MasterInstrument.MergePolicy](merge_policy.htm) property |



 


 


Property Value
--------------


Represents the MergePolicy used for the bars request.


 


Possible values are:


 




|  |  |
| --- | --- |
| DoNotMerge | No merge policy is applied |
| MergeBackAdjusted | Merge policy is applied between contracts along with rollover offsets |
| MergeNonBackAdjusted | Merge policy is applied between contracts without offsets |
| UseGlobalSettings | Uses the value configured from Tools -&gt; Options -&gt; Market Data |
| UseDefault | Uses the default values configured for the [MasterInstrument](masterinstrument.htm) |



 


 


Syntax
------


MergePolicy



Example
-------




| ns |
| --- |
| // request the last 365 1 day bars
BarsRequest useGlobalRequest = new BarsRequest(Instrument.GetInstrument("ES 09-16"), 365);
useGlobalRequest.BarsPeriod = new BarsPeriod { BarsPeriodType = BarsPeriodType.Day, Value = 1 };
 
// use the merge policy the user has configured as their global setting
useGlobalRequest.MergePolicy = MergePolicy.UseGlobalSettings;
useGlobalRequest.Request(new Action<barsrequest, errorcode,="" string="">((barsRequest, errorCode, errorMessage) =&gt;{
 
   Print("bars returned=" + barsRequest.Bars.Count);
 
}));
 
// dispose of the bars request if we are done with it
useGlobalRequest.Dispose(); |






 
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
 
 
 



</barsrequest,>