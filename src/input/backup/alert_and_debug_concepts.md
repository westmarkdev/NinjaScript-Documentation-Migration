










 


Alert and Debug Concepts







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?alert_and_debug_concepts.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
Alert and Debug Concepts | [Previous page](nttabpage_save.htm)
[Return to chapter overview](add_on.htm)










In most scenarios you can use the NinjaScript provided methods for triggering alerts and debugging functionality. However, when building your own custom objects, you may find yourself wanting to use this functionality outside the NinjaScript scope (e.g. when building a [NTTabPage](nttabpage_class.htm) for Add Ons).


 


Using the NinjaScript Output
----------------------------


Instead of [Print()](print.htm), use Output.Process() to write a message.


Instead of [ClearOutputWindow()](clearoutputwindow.htm), use Output.Reset() to clear the output window.


 


Example
-------




|  |
| --- |
| ns |
|  
// Instead of Print()
NinjaTrader.Code.Output.Process("my message", PrintTo.OutputTab1);
 
// Instead of ClearOutputWindow()
NinjaTrader.Code.Output.Reset() |



 


 


Using Alerts
------------


Instead of [Alert()](alert.htm), use [NinjaTrader.NinjaScript.Alert.AlertCallback()](alertcallback.htm) for sending an alert.


Instead of [ResetAlert()](rearmalert.htm), use [NinjaTrader.NinjaScript.Alert.RearmAlert()](alert.htm)


 


Example
-------




|  |
| --- |
| ns |
| // Instead of Alert()
NinjaTrader.NinjaScript.Alert.AlertCallback(NinjaTrader.Cbi.Instrument.GetInstrument("MSFT"), this, "someId", NinjaTrader.Core.Globals.Now, Priority.High, "message", null, Brushes.Blue, Brushes.White, 0);
 
// Instead of ResetAlert()
NinjaTrader.NinjaScript.Alert.ResetAlert("someId"); |



 


 


Miscellaneous
-------------


Instead of [Log()](log.htm), use NinjaScript.Log() to send a message to the NinjaTrader logs.


Instead of [PlaySound()](playsound.htm), use Globals.PlaySound() to play a sound.


Instead of [SendMail()](sendmail.htm), use Globals.SendMail() to send a mail.


 




|  |
| --- |
| Tip: Both the Globals.PlaySound() and .SendMail() above could be used in a regular NinjaScript objects as well, however this is not recommended practice since those would not ignore the calls outside State.Realtime which could yield unexpected results. |



 


 


Examples
--------




|  |
| --- |
| ns |
| // Instead of Log()
NinjaScript.Log("My log message", LogLevel.Error);
 
// Instead of PlaySound()
NinjaTrader.Core.Globals.PlaySound(@"C:\mySound.wav");
 
// Instead of SendMail()
NinjaTrader.Core.Globals.SendMail("customers@email.com", "cc\_these\_people@email.com", "Subject", "Mail body", null); |



 


 


Error Codes in Log Files
------------------------


The ErrorCode enumeration can be found in NinjaTrader logs from time to time when an error occurs, and these can provide further clues into the cause of unexpected behavior during your debugging. These error codes are not necessarily related to your code, but they can provide an indication of an issue to address outside of the scope of your code, saving you time in trying to find the source of errors in your code. Below is a list of ErrorCode enum values and their meanings:


 




|  |  |
| --- | --- |
| NoError | No errors were thrown |
| LogOnFailed | Failed to log on due to invalid credentials |
| OrderRejected | Broker rejected the current order |
| UnableToCancelOrder | Order cannot be canceled now, but may be successfully canceled later |
| UnableToChangeOrder | Either the exchange or broker does not support order updates for the instrument in question, or the order has not yet been submitted |
| UserAbort | The operation was aborted by the user |
| Panic | An unspecified error was thrown |






 
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
 
 
 



