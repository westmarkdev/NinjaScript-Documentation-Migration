










 


Alert, Debug, Share







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?alert__debugging_and_sharing.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Alert, Debug, Share | [Previous page](currentbars.htm)
[Return to chapter overview](common.htm)










The following section documents properties and methods used to trigger alerts from a NinjaScript object, send debug messages to the NinjaScript Output Window, or utilize Share Services to send emails or post to social-media networks. 


 




|  |  |
| --- | --- |
| [Alert()](alert.htm) | Generates a visual/audible alert for the [Alerts Log](alerts_log.htm) window |
| [ClearOutputWindow()](clearoutputwindow.htm) | Clears all data from the NinjaTrader [Output Window](output.htm) |
| [Log()](log.htm) | Generates a NinjaScript category log event record which is output to the [Log](log_tab2.htm) tab of the NinjaTrader Control Center / Account Data windows |
| [PlaySound()](playsound.htm) | Plays a .wav file while running on real-time data |
| [Print()](print.htm) | Converts object data to a string format and appends the specified value as text to the NinjaScript [Output window](output.htm) |
| [PrintTo](printto.htm) | Determines either tab of NinjaScript [Output window](output.htm) the [Print()](print.htm) and [ClearOutputWindow()](clearoutputwindow.htm) method targets |
| [RearmAlert()](rearmalert.htm) | Rearms an alert created via the [Alert()](alert.htm) method |
| [SendMail()](sendmail.htm) | Sends an email message through the default email sharing service.  |
| [Share()](share.htm) | Sends a message or screen shot to a social network or Share Service.   |






 
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
 
 
 



