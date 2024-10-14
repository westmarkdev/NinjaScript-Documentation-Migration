










 


PlaySound()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?playsound.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
PlaySound() | [Previous page](log.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Plays a .wav file while running on real-time data. 


 




|  |
| --- |
| Notes:  
1. This method will only execute once the [State](state.htm) has reached State.Realtime.  Calls to this method during State.Historical will be ignored (in contrast to the implementation for [AddOns](alert_and_debug_concepts.htm))2.The default behavior is to play the .wav file in an asynchronous manner, which can result in calls to PlaySound() to play over one another.  Sound files can optionally be configured to execute in a synchronous manner by enabling the Tools &gt; Options &gt; Sounds &gt; "Play consecutively" property  |



 


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


PlaySound(string fileName)


 




|  |
| --- |
| Warning:  The underlying framework used to play the sound requires the audio file to be in PCM .wav format.  Using another file format such as will generate an error at runtime.   |



 


 


Parameters
----------




|  |  |
| --- | --- |
| fileName | The absolute file path of the .wav file to play |



 


 




|  |
| --- |
| Tip: You can obtain the default NinjaTrader installation directory to access the sounds folder by using NinjaTrader.Core.Globals.InstallDir property.  Please see the example below for usage. |



 


 


Examples
--------




| ns |
| --- |
| // Plays the wav file mySound.wav
PlaySound(@"C:\mySound.wav");
 
// Plays the default Alert1 sound that comes packaged with NinjaTrader
PlaySound(NinjaTrader.Core.Globals.InstallDir + @"\sounds\Alert1.wav"); |






 
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
 
 
 



