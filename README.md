# :star2: PWNAGOTCHI v2.8.9 - Custom Faces Mod (⌐■_■)
Project for those who are tired of the same old string faces.
This mod allows you to use custom images as pwnagotchi Faces, with transparency feature (.png) and themed plugins.


https://github.com/jayofelony/pwnagotchi/releases/tag/v2.8.9  -- This dude is the Pwnagotchi master. Best build on the web. Get it from him! Load my config.toml file after first boot using Filezilla.


This is the current most popular collection of custom faces I could find. Pull the Pwnagotchi faces off this directory to get started. 


> **Important**
> The following steps were performed on a `Windows` computer using `Powershell` as SSH client, `FileZilla` as FTP client and the pwnagotchi with a `Waveshare 2.13 V4 e-ink display` running on a `RPI0W`.
>> If you will use it in another fork or hardware, please be aware that you might need to adapt what is shown here

> **Note**
> If the folder doesn't specify which screen it was tested on, assume the sprites are for the `waveshare_v4` and similar sizes

> **Note**
> Anyone can contribute by making a pull request.
>> Don't limit yourself to just this article, feel free to create your own themes!

> **Note**
> This tutorial requires a minimum level of knowledge.

> **Note**
> If pwnagotchi updates automatically, most mods must be applied again.


## :heavy_exclamation_mark::heavy_exclamation_mark:  Disclaimer
> **Warning**
>From **Modernknight101**: Heed all warnings from previous authors as this is an update.
>The content here is free for use, but it doesn't mean you can use it however you want. No author or contributor assumes responsibility for the misuse of this device, project, or any component herein. The project and modifications were **developed solely for educational purposes**.
> Any files, plugins or modifications of this project or original project found here should **not be sold**. In the case of use in open projects, videos or any form of dissemination, please remember to give credit to the repository ♥

> **Warning**
> Certain content may be protected by copyright, use with caution.


## :bookmark_tabs: Get Started

First, with the pwnagotchi connected to a computer in `MANU` mode, establish a FTP connection via Filezilla as well as initiate a SSH connection via Powershell.

```console/powershell
Login: ssh pi@10.0.0.2
pi@pwnagotchi:~ $ sudo su
root@pwnagotchi:/home/pi#
root@pwnagotchi:/home/pi# whoami
root
```
Navigate to root directory:
```console
root@pwnagotchi:/home/pi# cd /
```
Let's create two folders, one for backing up the files and another one to receive the custom faces:
```console
root@pwnagotchi:/# mkdir files-backup
root@pwnagotchi:/# mkdir custom-faces
```
Stop the pwnagotchi service
```console
root@pwnagotchi:/: systemctl stop pwnagotchi
```
Here are the following files:
```console
root@pwnagotchi:/usr/local/lib/python3.7/dist-packages/pwnagotchi/ui# ls
components.py  faces.py       view.py
display.py     fonts.py  __init__.py  state.py     
```
Now backup the files in the above folder using filezilla to the /files-backup/ folder
```
Ok, once that's done, replace the .py files from the ui folder with the ones from this directory.

## :page_with_curl: Configuration
From here, we will able configure the images for our custom Faces. So lets do that!

Prepare the files, there are a total of `25`. I use images of size `128x45`. To make it easier, name the files according to the facial expression or emotion:
> **_Default .png file names:_**  

~~~
LOOK_R, LOOK_L, LOOK_R_HAPPY, LOOK_L_HAPPY, SLEEP, SLEEP2, AWAKE, BORED, INTENSE, COOL, HAPPY, GRATEFUL, EXCITED, MOTIVATED, DEMOTIVATED, LONELY, SAD, ANGRY, FRIEND, BROKEN, DEBUG, UPLOAD, UPLOAD1, UPLOAD2, ICON, POSITION_X, POSITION_Y
~~~

Stop the pwnagotchi service, if its not:
```console
root@pwnagotchi:/# systemctl stop pwnagotchi
```

### :flower_playing_cards: Upload Images
Use `FileZilla` or any other method you know to upload your images to the `/custom-faces/` folder that was created earlier.


Open the pwnagotchi's configuration file:
```console
root@pwnagotchi:/# nano /etc/pwnagotchi/config.toml
```
Locate this code snippet:
```python
...
ui.faces.look_r = "( ⚆_⚆)"
ui.faces.look_l = "(☉_☉ )"
ui.faces.look_r_happy = "( ◕‿◕)"
ui.faces.look_l_happy = "(◕‿◕ )"
ui.faces.sleep = "(⇀‿‿↼)"
ui.faces.sleep2 = "(≖‿‿≖)"
ui.faces.awake = "(◕‿‿◕)"
ui.faces.bored = "(-__-)"
ui.faces.intense = "(°▃▃°)"
ui.faces.cool = "(⌐■_■)"
ui.faces.happy = "(•‿‿•)"
ui.faces.excited = "(ᵔ◡◡ᵔ)"
ui.faces.grateful = "(^‿‿^)"
ui.faces.motivated = "(☼‿‿☼)"
ui.faces.demotivated = "(≖__≖)"
ui.faces.smart = "(✜‿‿✜)"
ui.faces.lonely = "(ب__ب)"
ui.faces.sad = "(╥☁╥ )"
ui.faces.angry = "(-_-')"
ui.faces.friend = "(♥‿‿♥)"
ui.faces.broken = "(☓‿‿☓)"
ui.faces.debug = "(#__#)"
ui.faces.upload = "(1__0)"
ui.faces.upload1 = "(1__1)"
ui.faces.upload2 = "(0__1)"
...
```

This snippet will be responsible for enabling our customization. If it doesn't exist, you can add it.

Add the new entries pointing to the folder where the images were placed, set the position where the custom Face will be displayed and set the activation flag to `True`.

```python
...
ui.faces.look_r = "/custom-faces/LOOK_R.png"
ui.faces.look_l = "/custom-faces/LOOK_L.png"
ui.faces.look_r_happy = "/custom-faces/LOOK_R_HAPPY.png"
ui.faces.look_l_happy = "/custom-faces/LOOK_L_HAPPY.png"
ui.faces.sleep = "/custom-faces/SLEEP.png"
ui.faces.sleep2 = "/custom-faces/SLEEP2.png"
ui.faces.awake = "/custom-faces/AWAKE.png"
ui.faces.bored = "/custom-faces/BORED.png"
ui.faces.intense = "/custom-faces/INTENSE.png"
ui.faces.cool = "/custom-faces/COOL.png"
ui.faces.happy = "/custom-faces/HAPPY.png"
ui.faces.excited = "/custom-faces/EXCITED.png"
ui.faces.grateful = "/custom-faces/GRATEFUL.png"
ui.faces.motivated = "/custom-faces/MOTIVATED.png"
ui.faces.demotivated = "/custom-faces/DEMOTIVATED.png"
ui.faces.smart = "/custom-faces/SMART.png"
ui.faces.lonely = "/custom-faces/LONELY.png"
ui.faces.sad = "/custom-faces/SAD.png"
ui.faces.angry = "/custom-faces/ANGRY.png"
ui.faces.friend = "/custom-faces/FRIEND.png"
ui.faces.broken = "/custom-faces/BROKEN.png"
ui.faces.debug = "/custom-faces/DEBUG.png"
ui.faces.upload = "/custom-faces/UPLOAD.png"
ui.faces.upload1 = "/custom-faces/UPLOAD1.png"
ui.faces.upload2 = "/custom-faces/UPLOAD2.png"
ui.faces.png = true
ui.faces.position_x = 0
ui.faces.position_y = 34
...
```

> **Note**
> **_1:_** Check if your installed plugins modify the 'faces'. If there are any, replace them with the equivalent custom image address. If you don't do this, the pwnagotchi may crash. The code looks like this: `ui.set('face', "(◕‿‿◕)")` or `view.set('face', "(◕‿‿◕)")`

> **Note**
> **_2:_** I recommend that you always use the same path (`/custom-faces/` folder) for your customization. That way, it becomes easier as you only need to replace the files!

CTRL + O to save, CTRL + X to close file.

Restart your device
```console
root@pwnagotchi:/# systemctl restart pwnagotchi
```

Enjoy!

## :writing_hand: How to Contribute?
> This is an entirely open project that accepts contributions via pull requests, your name will be placed as an author. If you have any questions, please open an issue.
1. Create a fork of this repository
2. Create your theme following the pattern of the ones already posted
3. Commit your changes in English
4. Include a brief summary of what was added
5. Submit your pull request


## :pill: Troubleshooting
- Check the log file, read and interpret:
```console
root@pwnagotchi:/# tail -f /var/log/pwnagotchi.log
```
- The logs may not be enough, so use:
```console
pi@pwnagotchi:~ $ sudo su
root@pwnagotchi:/home/pi# systemctl stop pwnagotchi
root@pwnagotchi:/home/pi# pwnagotchi
```
> With this command you directly run the pwnagotchi services and this way you can see what happens at run time, showing errors what does not appear in the log

- Restore the backup files that we placed in `/files-backup/` and try again

- If you don't have permission, try `chmod 777`

- Make sure that **all entries related to the plugins** are indeed in the `config.toml` file

## :star: Discover another projects
- [Fancygotchi](https://github.com/V0r-T3x/fancygotchi) by [V0r-T3x](https://github.com/V0r-T3x)


## :tophat: Thank You ♥
## :sparkling_heart: Support Me 
> If you like my work and want to support me, plz consider

https://www.paypal.me/Modernknight101

or buy a copy or my sci-fi book, available on Amazon

https://a.co/d/hx5OLOO  Gods Among Us: Alienthology
