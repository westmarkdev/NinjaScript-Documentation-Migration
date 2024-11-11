---
title: Alert, Debug, Share
pathName: alert_debug_share
parent: common
section: references
status: review
---

The following section documents properties and methods used to trigger alerts from a NinjaScript object, send debug messages to the NinjaScript Output Window, or utilize Share Services to send emails or post to social-media networks.

{% table %}

* Method
* Description

---

* [Alert()](alert)
* Generates a visual/audible alert for the [Alerts Log](alerts_log) window

---

* [ClearOutputWindow()](clearoutputwindow)
* Clears all data from the NinjaTrader [Output Window](output)

---

* [Log()](log)
* Generates a NinjaScript category log event record which is output to the [Log](log_tab2) tab of the NinjaTrader Control Center / Account Data windows

---

* [PlaySound()](playsound)
* Plays a .wav file while running on real-time data

---

* [Print()](print)
* Converts object data to a string format and appends the specified value as text to the NinjaScript [Output window](output)

---

* [PrintTo](printto)
* Determines either tab of NinjaScript [Output window](output) the [Print()](print) and [ClearOutputWindow()](clearoutputwindow) method targets

---

* [RearmAlert()](rearmalert)
* Rearms an alert created via the [Alert()](alert) method

---

* [SendMail()](sendmail)
* Sends an email message through the default email sharing service.

---

* [Share()](share)
* Sends a message or screen shot to a social network or Share Service.
{% /table %}
