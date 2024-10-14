










 


Debugging your NinjaScript Code







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?debugging_your_ninjascript_cod.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Tips](tips.htm) &gt;
Debugging your NinjaScript Code | [Previous page](creating_user_defined_input_pa.htm)
[Return to chapter overview](tips.htm)










Debugging can be a frustrating and time-consuming task. In order to make the most of your time, it is best to proceed in a methodical manner. The first step you should do is to strip your code down into simple code segments. You want to start your debugging at a point where you know the code works as expected. From there you can then add more layers of complexity. With each additional layer, you want to ensure it works as expected before adding more layers.


 


To begin the process of stripping down your code you can either make a new temporary NinjaScript and copy over only the key relevant code segments or you can comment out segments that are not vital to the test.


 


To comment out code segments you can either press the "Comment selection" button on the top toolbar in the NinjaScript editor or type "//" in front of the line. To mass comment code segments, you can use your mouse cursor and select multiple lines and press the "Comment selection" button as well. To uncomment code, remove the "//" or select the line and press the "Uncomment selection" button.




| ns |
| --- |
| double limitPrice = 0; //You can comment after working code
// double stopPrice = 0;
// you can also comment out whole lines to prevent it from being used by using // |



 


Commenting code segments is also useful if you wanted to just temporarily check if your code compiles. When your NinjaScript editor pops up with errors you can click on the error message and it will bring you to the erroneous line. After you comment out the erroneous lines you should be able to compile.


 


The most common method you can use to ensure your code works as expected is through the use of the Print() command. The Print command will print the supplied value to the New -&gt; NinjaScript Output window.


 


Example:




| ns |
| --- |
| if (Close[0] &gt; Open[0])
{
     Print("Code has entered If statement. Close: " + Close[0] + " Open: " + Open[0]);
     // Do something
} |



 


Placing Print() commands throughout your code logic allows you to trace where you are exactly. You can see where your code goes and where it does not go by viewing the output from the Output Window. Coupled with reading the error log from the Log tab in the Control Center, you can pinpoint where your code is crashing or locking up and make changes accordingly.


 


Debugging orders can be a bit harder though because you cannot discern the behavior state of your orders through the Print() command easily. In addition to Print(), you can use [TraceOrders](traceorders.htm) to help you decipher what is happening under the hood for orders. [TraceOrders](traceorders.htm) will print information into the Output Window that will contain details about your orders.




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         TraceOrders = true;
     }
} |



 


When debugging stop or limit orders it can also be extremely useful to draw dots along your chart of the actual stop/limit prices. This way you can visually see where your orders are at and if they should have been filled or not. [Draw.Dot](draw_dot.htm)




| ns |
| --- |
| Draw.Dot(this, "tag1", true, 0, Low[0] - TickSize, Brushes.Red); |



 


Sometimes your code will compile and run fine, but it will produce inaccurate results. To check for accuracy, you can use Print() along with the Data Box to compare values. If you are doing a complex mathematical calculation, you can print the value at every step to ensure the calculations are as expected.


 


External references can also be very useful when debugging. They are great for gaining insight into syntax and usage of various methods. Searching Google or MSDN can provide useful examples and code snippets you can adapt to use with your own code.


 


Some useful resources:


[NinjaScript Debugging](http://www.ninjatrader.com/support/forum/showthread.php?p=23415#post23415)


[CSharp Essentials](http://www.techotopia.com/index.php/C_Sharp_Essentials)


[C# Station](https://csharp-station.com/)


[Microsoft Developer Network](http://msdn2.microsoft.com/en-us/library/aa139615.aspx)


[The Code Project](http://www.codeproject.com/)





 
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
 
 
 



