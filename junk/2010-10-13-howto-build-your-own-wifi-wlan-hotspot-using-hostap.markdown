Title: HowTo: Build your own Wifi WLAN hotspot using hostap
Author: Victor
Date: 2010-10-13
Tags: howto, networking, security, wlan, linux, admin
Category: blog

This time I'm going to show you how to build your own wi-fi hotspot in less than 10 minutes. There is no need of sophisticated software like FreeRadius or Chilispot. Using common tools you'll be able to set up your WLAN AP (Access Point) and allow others to connect to it. Therefore we'll be using our own DHCP server to manage the clients and their IP addresses. In this tutorial I'll be using **BlackTiny** again since mobility was the main reason for writing this: There were a lot of situations where I wanted to share my Internet connectivity but I couldn't do that due to misconfigurations and false network settings. I'd like to share my experience with you and help you easily configure your AP.

## Before we start ...

Some technical info

*   *General*: Linux debian **2.6.32-5-amd64** #1 SMP x86_64 GNU/Linux
*   *Linux distro*: Debian **Squeeze/Sid**
*   *hostapd version*: 0.6.10-2
*   *hostap-utils version*: 0.4.7-1
*   *DHCP server version*: 4.1.1-P1-9

Make sure ...

*   your card supports [promiscous mode][2]
*   proper card kernel module is up and running (**ath5k** in my case)
*   [mac80211][3] is up and running (check using *lsmod*)
*   you have **hostapd** installed
*   a **DHCP** server is running on your system (see below)



## Go "Up in the air" / configure hostapd

~~~.shell
# hostapd -h
hostapd v0.6.10
User space daemon for IEEE 802.11 AP management,
IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator
Copyright (c) 2002-2009, Jouni Malinen <j@w1.fi> and contributors

usage: hostapd [-hdBKtv] [-P <PID file>] <configuration file(s)>

options:
   -h   show this usage
   -d   show more debug messages (-dd for even more)
   -B   run daemon in the background
   -P   PID file
   -K   include key data in debug messages
   -t   include timestamps in some debug messages
   -v   show hostapd version
~~~

So we'll need a configuration. Mine was located at `/etc/hostapd/hostapd.conf`. You should now open it using your editor (vim still rocks! ^^) and read it. Don't try to skim over it. You'll end up in misconfiguring hostapd and getting crazy error messages. So these are the main important settings:

~~~.shell
# Which interface should be used
interface=wlan1

# Driver interface type (hostap/wired/madwifi/prism54/test/none/nl80211/bsd);
# default: hostap). nl80211 is used with all Linux mac80211 drivers.
# Use driver=none if building hostapd as a standalone RADIUS server that does
# not control any wireless/wired driver.
driver=nl80211

# SSID to be used in IEEE 802.11 management frames
ssid=TestHOSTAP

# Operation mode (a = IEEE 802.11a, b = IEEE 802.11b, g = IEEE 802.11g,
# Default: IEEE 802.11b
hw_mode=b

# Channel number (IEEE 802.11)
# (default: 0, i.e., not set)
# Please note that some drivers (e.g., madwifi) do not use this value from
# hostapd and the channel will need to be configuration separately with
# iwconfig.
channel=11

# IEEE 802.11 specifies two authentication algorithms. hostapd can be
# configured to allow both of these or only one. Open system authentication
# should be used with IEEE 802.1X.
# Bit fields of allowed authentication algorithms:
# bit 0 = Open System Authentication
# bit 1 = Shared Key Authentication (requires WEP)
auth_algs=3

# The own IP address of the access point (used as NAS-IP-Address)
own_ip_addr=127.0.0.1
~~~

You won't need any authentication settings since this is supposed to be a free hotspot.

Now let's try our configuration:

~~~.shell
# hostapd -d /etc/hostapd/hostapd.conf 
Configuration file: /etc/hostapd/hostapd.conf
ctrl_interface_group=0
Opening raw packet socket for ifindex 4199392
BSS count 1, BSSID mask ff:ff:ff:ff:ff:ff (0 bits)
SIOCGIWRANGE: WE(compiled)=22 WE(source)=21 enc_capa=0xf
nl80211: Added 802.11b mode based on 802.11g information
RATE[0] rate=10 flags=0x2
RATE[1] rate=20 flags=0x6
RATE[2] rate=55 flags=0x4
RATE[3] rate=110 flags=0x4
Passive scanning not supported
Mode: IEEE 802.11b  Channel: 11  Frequency: 2462 MHz
Flushing old station entries
Deauthenticate all stations
Using interface wlan1 with hwaddr 00:11:22:33:44:55 and ssid 'TestHOSTAP''
wlan1: Setup of interface done.
MGMT (TX callback) ACK
  MGMT (TX callback) ACK
mgmt::proberesp cb
MGMT (TX callback) ACK
mgmt::proberesp cb
~~~

It's working! Let's go to the next step.

## Configure network stuff

First let's have a look at some debug messages.

 [2]: http://en.wikipedia.org/wiki/Promiscuous_mode
 [3]: http://wireless.kernel.org/en/developers/Documentation/mac80211
