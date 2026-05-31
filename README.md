<div align="center">

# COBALT
Qt application that can be used to convert windows cursor such as .cur and .ani into xcursor using win2xcur.

</div>

Feel free to download some of the cursors that has been converted on my [pling](https://www.pling.com/u/pxryzl/) account

Win2xcur creator [Github](https://github.com/quantum5/win2xcur) page.

> [!WARNING]
> **Some part of the coding and debugging is done with AI assistant, especially with the conversion script. Be assured that this whole project isn't just a vibe coded and just be done with it, I personally review and check the code myself and test the software multiple times but I understand the AI hatred, so for those kind of people this might not be for you.**

## Dependencies
You need to install pyside6

### Arch Linux
```sh
pacman -S pyside6
```
## Win2xcur
>[!NOTE]
> **I include the win2xcur and win2xcurtheme python file in the vendor directory but I recommend that you just install it yourself.**

### Pipx
```sh
pipx install win2xcur
```

### AUR
```sh
yay -S win2xcur
```

## Automatic Convert
> [!WARNING]
> **This will automatically convert a directory containing the cursor files without needing to manually pick the cursor but the cursor file name needed to be similar or at least close to the default windows cursor name.**

Example of windows cursor name
  ```txt
  Alt,Busy,Cross,Default,Dgn1,Dgn2,Hand,Help,Horizontal,Link,Move,Text,Unavailable,Vertical,Work
  ```
As long as the name is similar or an alias to the cursor then it would still get converted. Such as,
```txt
Default = Pointer, Normal
Cross = Precision
Dgn1 = Diagonal1
Dgn2 = Diagonal2
Hand = Handwriting
```
Cursor file such as `Location/Pin` or `Person/People` won't be needed

## Issues
### .cur file didn't get converted
Sometimes there would be an issue where .cur file wouldn't get converted and it's usually because the file is another type of file (e.g `.png,.jpg,.ico`) that has been renamed to .cur

To check the .cur file use the file command
```sh
file Example.cur
```
A .cur would give out this message
```sh
Example.cur: MS Windows cursor resource - 1 icon, 32x32, hotspot @16x4
```
Meanwhile other file such as .ico would show this instead
```sh
Example.cur: MS Windows icon resource - 1 icon, -128x-128, 62 planes, 22 bits/pixel
```
