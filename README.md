# GZDoom loader with Discord presence
<img src="img/gzdoom.png" style="height: 100px; margin-right: 10px" href="zdoom.org"/>
<img src="img/discord.png" style="height: 100px" href="discord.com" />

## Set Up
To set up the loader, copy the files from the `files/` directory and place them inside the root directory of your **GZDoom** folder. To download GZDoom, visit their official web page (https://zdoom.org/downloads).

### Discord Application
To display a Discord Presence, we need to create a **Discord Application**. First of all, log in to your Discord account in [Discord Developer Portal](https://discord.com/developers/).

Create a new application and name it **GZDoom**. After this, navigate to the **Rich Presence** tab, and upload the [gzdoom.png](https://github.com/Fonta22/GZDoom-Loader/blob/main/img/gzdoom.png) image, stored inside the `img/` directory. In your application, you need to name it **"circle_gzdoom"**.

![asset](https://user-images.githubusercontent.com/61181201/200796565-99da758f-dd26-41e2-9e82-709a4a171123.png)

Also use this image as **App Icon** and **Cover Image**.

### .env
When you have created your [Discord Application](#discord-application), edit the `.env` file, and insert your **Discord Application ID**.

```
APP_ID=<Discord Application ID>
```

To get it, visit the **General Information** tab, and copy it.

![image](https://user-images.githubusercontent.com/61181201/200798354-04cd3165-1c72-4a62-935d-4abb77f3fff0.png)

## Running GZDoom
To run GZDoom with the Discord Presence, open a command prompt in the GZDoom directory, and run `gzdoom.bat`, and select which **WAD** you want to load using command line arguments.

The available WADs are:
- [DOOM.WAD](https://github.com/Fonta22/GZDoom-Loader/blob/main/files/WAD/DOOM.WAD)
- [DOOM2.WAD](https://github.com/Fonta22/GZDoom-Loader/blob/main/files/WAD/DOOM2.WAD)
- [HERETIC.WAD](https://github.com/Fonta22/GZDoom-Loader/blob/main/files/WAD/HERETIC.WAD)
- [HEXEN.WAD](https://github.com/Fonta22/GZDoom-Loader/blob/main/files/WAD/HEXEN.WAD)

You can see them inside the [`WAD/` folder](https://github.com/Fonta22/GZDoom-Loader/tree/main/files/WAD).

> All of these files were taken from the [Internet Archive](https://archive.org/).

Example to run **Doom II**
```
> gzdoom.bat DOOM2
```

## Final Result
When you run GZDoom using the loader, the presence shown in Discord will look like this:

![image](https://user-images.githubusercontent.com/61181201/200800026-61ddc896-c862-476e-8e78-19c09d94927f.png)