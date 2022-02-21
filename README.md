# i3status-uptime

Simple python3 script that reads, formats and returns the uptime of your system so that i3status can read and display it.

Since it would be worthless to run a dedicated daemon to do this, the script execution has to be programmed in Cron. This way, we don't even need systemd.

The task will be ran every minute, and its output should be saved into a file that we will then read to display its contents in i3status.

The cron entry should look similar to this:

`* * * * * python3 /home/user/whatever/uptime.py > /home/user/uptime`

In our i3status config file, we will need to add an element to our bar:

`order += "read_file uptime"`

And declare it down below:

```
read_file uptime {
	path = "/home/user/uptime"
	format = "UP %content"
}
```

In this case, "UP" is simply a prefix that I have set for my own use. The result is the following:

![image](https://user-images.githubusercontent.com/82534925/154975938-386bc191-3c85-442c-9e1b-8a16edd02f91.png)
