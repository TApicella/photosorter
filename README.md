# photosorter
A program for easily organizing and sorting photographs

I'm an amateur photographer, and I often generate over 500 photos a month. I find sorting through directories full of photos tedious, particularly when there are often very similar photos in a row with slight variation in angle and zoom. I wanted to create a way to make the process of sorting through photos more enjoyable, so over the course of a few afternoons (probably about 5-6 hours time total), I wrote up this GUI. 

The first screen allows you to pick source and destination directories for your photos. 


![alt tag](https://raw.githubusercontent.com/TApicella/photosorter/master/screenshots/photosorter-interface-select.png)


If you have a config.txt file in the photosorter directory, you can specify a starting directory to make selection easier. 

Once your directories are chosen, a list of all of the photos is generated and randomized. A file is created called processed.txt that saves the filenames of photos you've already moved/copied so that they won't be included in the sorting list. 

The next screen displays a resized version of your photo for previewing purposes, and allows you to move or copy it to one of your destination directories by double clicking the name. Clicking the photo simply skips the photo. The top bar displays the filename and a count of how many photos you've looked at, so you can set a goal number and sort until you've reached your goal.

Adding a comment in the comments field prior to sorting will add an entry in a comments.txt file in the destination directory, so you can make a note to yourself such as "crop out left side" or "make this black and white." 


![alt tag](https://raw.githubusercontent.com/TApicella/photosorter/master/screenshots/photosorter-interface-view.png)


There are many improvements that can be made, such as advanced configuration options, a more attractive interface, more options such as resizing and cropping the photo in the preview window, but as a personal tool this has worked exceptionally well for me, and I wanted to open source it in case it can help anyone else as well. 
